#!/bin/env/python

import datetime
from autosubmit.job.job import Job
from typing import List, Union, Dict

_COMPLETED_RETRIAL = 1
_FAILED_RETRIAL = 0


def timedelta2hours(deltatime):
    return deltatime.days * 24 + deltatime.seconds / 3600.0


class JobStat(object):
    def __init__(self, name, processors, wallclock):
      # type: (str, int, float) -> None
      self._name = name
      self._processors = processors
      self._wallclock = wallclock
      self.submit_time = None # type: datetime.timedelta
      self.start_time = None # type: datetime.timedelta        
      self.finish_time = None # type: datetime.timedelta
      self.completed_queue_time = datetime.timedelta()
      self.completed_run_time = datetime.timedelta()
      self.failed_queue_time = datetime.timedelta()
      self.failed_run_time = datetime.timedelta()
      self.retrial_count = 0
      self.completed_retrial_count = 0
      self.failed_retrial_count = 0

    def inc_retrial_count(self):
        self.retrial_count += 1

    def inc_completed_retrial_count(self):
        self.completed_retrial_count += 1

    def inc_failed_retrial_count(self):
        self.failed_retrial_count += 1

    @property
    def cpu_consumption(self):
        return timedelta2hours(self._processors * self.completed_run_time) + timedelta2hours(self._processors * self.failed_run_time)

    @property
    def failed_cpu_consumption(self):
        return timedelta2hours(self._processors * self.failed_run_time)

    @property
    def real_consumption(self):
        return timedelta2hours(self.failed_run_time + self.completed_run_time)

    @property
    def expected_real_consumption(self):
        return self._wallclock

    @property
    def expected_cpu_consumption(self):
        return self._wallclock * self._processors

    def get_as_dict(self):
        return {
            "name": self._name,
            "processors": self._processors,
            "wallclock": self._wallclock,
            "completedQueueTime": timedelta2hours(self.completed_queue_time),
            "completedRunTime": timedelta2hours(self.completed_run_time),
            "failedQueueTime": timedelta2hours(self.failed_queue_time),
            "failedRunTime": timedelta2hours(self.failed_run_time),
            "cpuConsumption": self.cpu_consumption,
            "failedCpuConsumption": self.failed_cpu_consumption,
            "expectedCpuConsumption": self.expected_cpu_consumption,
            "realConsumption": self.real_consumption,
            "failedRealConsumption": timedelta2hours(self.failed_run_time),
            "expectedConsumption": self.expected_real_consumption,
            "retrialCount": self.retrial_count,
            "submittedCount": self.retrial_count,
            "completedCount": self.completed_retrial_count,
            "failedCount": self.failed_retrial_count
        }


class Statistics(object):

    def __init__(self, jobs, start, end, queue_time_fix):
        # type: (List[Job], str, str, Dict[str, int]) -> None
        """
        """
        self._jobs = jobs 
        self._start = start
        self._end = end
        self._queue_time_fixes = queue_time_fix
        self._name_to_jobStat_dict = dict()
        self.jobs_stat = [] # type: List[JobStat]
        # Old format
        self.max_time = 0.0 # type: float
        self.max_fail = 0 # type: int
        self.start_times = [] # type: List[Union[datetime.timedelta, None]]
        self.end_times = [] # type: List[Union[datetime.timedelta, None]]
        self.queued = [] # type: List[datetime.timedelta]
        self.run = [] # type: List[datetime.timedelta]
        self.failed_jobs = [] # type: List[int]
        self.fail_queued = [] # type: List[datetime.timedelta]
        self.fail_run = [] # type: List[datetime.timedelta]
        self.wallclocks = [] # type: List[float]
        self.threshold = 0.0 # type: float
        self.totals = [" Description text \n", "Line 1"]
            
    def calculate_statistics(self):
      # type: () -> List[JobStat]
      for index, job in enumerate(self._jobs):
          retrials = job.get_last_retrials()          
          for retrial in retrials:
              # print(retrial)
              job_stat = self._name_to_jobStat_dict.setdefault(
                  job.name, JobStat(job.name, job.total_processors, job.total_wallclock))
              job_stat.inc_retrial_count()
              if Job.is_a_completed_retrial(retrial):
                  job_stat.inc_completed_retrial_count()
                  job_stat.submit_time = retrial[0]
                  job_stat.start_time = retrial[1]
                  job_stat.finish_time = retrial[2]
                  adjusted_queue = max(job_stat.start_time - job_stat.submit_time, datetime.timedelta(
                  )) - datetime.timedelta(seconds=self._queue_time_fixes.get(job.name, 0))
                  job_stat.completed_queue_time += max(
                      adjusted_queue, datetime.timedelta())
                  job_stat.completed_run_time += max(
                      job_stat.finish_time - job_stat.start_time, datetime.timedelta())
              else:
                  job_stat.inc_failed_retrial_count()
                  job_stat.submit_time = retrial[0] if len(retrial) >= 1 and type(retrial[0]) == datetime.datetime else None
                  job_stat.start_time = retrial[1] if len(retrial) >= 2 and type(retrial[1]) == datetime.datetime else None
                  job_stat.finish_time = retrial[2] if len(retrial) >= 3 and type(retrial[2]) == datetime.datetime else None
                  if job_stat.finish_time and job_stat.start_time:
                      job_stat.failed_run_time += max(job_stat.finish_time - job_stat.start_time,
                                                      datetime.timedelta())
                  if job_stat.start_time and job_stat.submit_time:
                      adjusted_failed_queue = max(
                          job_stat.start_time - job_stat.submit_time, datetime.timedelta()) - datetime.timedelta(seconds=self._queue_time_fixes.get(job.name, 0))
                      job_stat.failed_queue_time += max(adjusted_failed_queue, datetime.timedelta())
      self.jobs_stat = list(self._name_to_jobStat_dict.values())
      return self.jobs_stat

    def get_statistics(self):
        job_stat_list = self.calculate_statistics()
        return {
            "Period": {"From": str(self._start), "To": str(self._end)},
            "JobStatistics": [job.get_as_dict() for job in job_stat_list]
        }
    
    def make_old_format(self):
      # type: () -> None
      """ Makes old format """
      self.start_times = [job.start_time for job in self.jobs_stat]
      self.end_times = [job.finish_time for job in self.jobs_stat]
      self.queued = [timedelta2hours(job.completed_queue_time) for job in self.jobs_stat]
      self.run = [timedelta2hours(job.completed_run_time) for job in self.jobs_stat]
      self.failed_jobs = [job.failed_retrial_count for job in self.jobs_stat]
      self.max_fail = max(self.failed_jobs)
      self.fail_run = [timedelta2hours(job.failed_run_time) for job in self.jobs_stat]
      self.fail_queued = [timedelta2hours(job.failed_queue_time) for job in self.jobs_stat]
      self.wallclocks = [job.expected_real_consumption for job in self.jobs_stat]
      self.threshold = max(self.wallclocks)
      max_queue = max(self.queued)
      max_run = max(self.run)
      max_fail_queue = max(self.fail_queued)
      max_fail_run = max(self.fail_run)
      self.max_time = max(max_queue, max_run, max_fail_queue, max_fail_run, self.threshold)

    

    
    
