#!/usr/bin/env python
from autosubmitAPIwu.components.jobs.job_factory import Job
from autosubmitAPIwu.components.jobs.joblist_loader import JobListLoader
from autosubmitAPIwu.components.jobs.joblist_helper import JobListHelper

from autosubmitAPIwu.components.representations.graph.edge import Edge, RealEdge
from typing import List, Dict

class GraphRepresentation(object):
  """ Graph Representation of Experiment """
  def __init__(self, expid):
    # type: (str) -> None
    self.expid = expid
    # self.jobs = [] # type: List[Job]
    self.joblist_loader = JobListLoader(expid)
    self.joblist_helper = self.joblist_loader.joblist_helper
    self.jobs = self.joblist_loader.jobs
    self.job_dictionary = self.joblist_loader.job_dictionary
    self.average_post_time = 0.0 # type: float
    self.is_valid_graph_drawing = False # type: bool
    self.edges = [] # List[Edge]
  
  def setup(self):
    self.joblist_loader.load_jobs()
  
  def perform_calculations(self):
    # type: () -> None
    """ Calculate Graph Representation """
    self.joblist_loader.validate_job_list_configuration()
    self.is_valid_graph_drawing = self.joblist_loader.assign_existing_graph_coordinates()
    if not self.is_valid_graph_drawing:
      self.start_level_update()

  def start_level_update(self):
    # type: () -> None
    job_roots = [job for job in self.jobs if len(job.parents_names) == 0]
    for job_root in job_roots:
      job_root.level = 1
      self._level_update(job_root)
  
  def _level_update(self, job):
    # type: (Job) -> None
    for job_name in job.children_names:
      self.job_dictionary[job_name].level = job.level + 1
      self._level_update(self.job_dictionary[job_name])
  
  def add_edges(self):
    for job in self.jobs:
      for child_name in job.children_names:        
        self.edges.append(RealEdge(job.name, child_name, self.joblist_helper.are_these_in_same_package(job.name, child_name)))
        


