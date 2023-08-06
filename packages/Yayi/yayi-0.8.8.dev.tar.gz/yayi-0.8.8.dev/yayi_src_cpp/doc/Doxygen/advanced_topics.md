Advanced topics   {#advanced}
===============
[TOC]




Multithreading    {#multithreading}
==============

A bunch of algorithm in image processing can be executed using several processing cores, either on a CPU or a GPU.

Implementation in Yayi
----------------------

Yayi implements a thread pool and defines [jobs](@ref yayi::IAsyncJob). Jobs can be grouped together into
[group](@ref yayi::IAsyncJobGroup). 

Groups may be organised hierarchily, exactly as jobs may belong to a group. 

![Jobs and groups](jobs_and_groups.svg)

Jobs and groups can be polled in order to know if they had complete, using 
- at any time using @ref yayi::IAsyncJob::is_complete
- a timed barrier such as @ref yayi::IAsyncJob::wait_for_completion. This method returns @c false if the job has not 
  completed for a given amount of time, or just wait for the completion

Thread pool {#threadpool}
-----------

A thread pool maintains several threads of *workers*. Each worker process a *job* and each job can be ran only once by
a worker. These workers are running in parallel and define the *pool* of threads/workers.

There is only one thread pool during the lifetime of Yayi. This one can be sized in the number of concurrent thread that
are running, with @ref yayi::set_thread_pool_size. The number of threads can be increased and decreased at any time. The 
increase/decrease will occur as soon as possible (the decrease will happen when a processing thread will be available).

Jobs {#jobs}
----
@ref yayi::IAsyncJob "Jobs" are unit of execution that can be executed in parallel with other jobs in the thread pool. 

In order to define a job, an object deriving from @ref yayi::IAsyncJob should be created, where the method
@ref yayi::IAsyncJob::run is implemented. This method will contain all the logic of the algorithm running in 
multiple processing cores.

A trivial job would be defined as below:

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~{.cpp}
#include <yayiCommon/include/thread_pool.hpp>
#include <boost/thread.hpp>

//! An example of job definition: each run increments the
//! shared counter.
struct test_job : yayi::IAsyncJob
{
  static int nb_instances;
  static boost::mutex mutex_;
 
  
  test_job()
  { }

  ~test_job()
  { }

  //! The method to implement 
  yayi::yaRC run()
  {
    // ensures that only one instance has read access
    // to this shared ressource

    boost::lock_guard<boost::mutex> lck(mutex_);
    nb_instances++;
    return yayi::yaRC_ok;
  }
};
int test_job::nb_instances = 0;
boost::mutex test_job::mutex_ = boost::mutex();
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

In the previous example, the @c run function just increments a shared integer without collisions with potential
other concurrent access to this variable. 

Groups {#groups}
------

@ref yayi::IAsyncJobGroup "Groups" are a way to organize the jobs. They represent several jobs and they can contain other groups as
well. Groups and jobs define a tree. 
Groups are useful if one needs to know the level of completion of a particular subset of the jobs. 

A simple example using the previously defined @c test_job, would be
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~{.cpp}
#include <yayiCommon/include/thread_pool.hpp>
#include <cassert>

void define_simple_group_of_jobs()
{
  IAsyncJobGroup group;
  std::vector<test_job *> v_jobs(10, (test_job *)0);
  for(size_t i = 0; i < v_jobs.size(); i++)
  {
    v_jobs[i] = new test_job;
  }

  // adds the defined jobs to the group
  for(size_t i = 0; i < v_jobs.size(); i++)
  {
    group.add_job(v_jobs[i]);
  }

  assert(post_job(group) == yaRC_ok);
  assert(group.is_scheduled());

  // waits indefinitely for the completion of all the jobs
  // under the tree of jobs rooted at "group"
  bool ret = group.wait_for_completion();
  assert(ret);

  assert(group.is_complete());

  // it is safe to delete "group" here as every jobs have completed.
  // it should be ensured that there is no running threads before 
  // the owner of the jobs gets deleted.
}
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



Posting jobs in the thread pool {#posting}
-------------------------------

A job can then be queued for parallel execution with the function @ref yayi::post_job. 

A group can be posted as well. In that case, all the jobs contained in the 
group will be posted instead, as the group itself does not convey any job but rather an organization of the jobs.
Instead the group can be polled to know if every jobs under the subtree rooted at the group have completed.

All jobs in a group hierarchy will be posted with no hierarchy/priority among them: all jobs in the tree
are supposed to be executed in parallel. 

Once a job is posted, it is flagged as *scheduled* (@ref yayi::IAsyncJob::is_scheduled evaluates to @c true) and 
cannot be posted again. 

