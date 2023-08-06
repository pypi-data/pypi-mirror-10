#ifndef YAYI_COMMON_THREAD_POOL_HPP__
#define YAYI_COMMON_THREAD_POOL_HPP__

//! @file
//! This file contains the thread pool interface
//! @author Raffi Enficiaud


#include <yayiCommon/common_types.hpp>


namespace yayi
{

  /*! Base class for asynchronous job execution
   *
   * This class is meant to be derived in order to add processing logic in the @c IAsyncJob::run method.
   * Once an instance is created, it can be scheduled for processing in the thread pool using the
   * @ref yayi::post_job function.
   *
   * @note
   * The job may be created on the heap, but the caller should ensure that the job is fully terminated
   * before the destructor is called. A call to @c wait_for_completion can be used for that.
   */
  struct YCom_ IAsyncJob
  {
    //! @internal
    //! Opaque state
    void *state;
    
    IAsyncJob();
    virtual ~IAsyncJob();
    
    //! Indicates the job is over
    bool is_complete() const;

    //! Indicates the job is or has been in the processing queue.
    bool is_scheduled() const;

    /*! Waits for the task to complete
     *
     * If the parameter @c nb_microsecond_wait is given and non null, waits at most 
     * that amount of microseconds.
     *
     * @returns true if the task completed, false if
     *  - the task is not scheduled
     *  - the task does not finish in the given time (if any)
     *
     * @post if the function returns true, then IAsyncJob::is_complete evaluates to true.
     *
     */ 
    bool wait_for_completion(size_t nb_microsecond_wait = 0) const;

    //! The concrete code that is executed within a thread.
    //! This function is meant to be called by the thread pool. 
    virtual yaRC run() = 0;

    //! Receives and process a completion notification from a child job.
    //! @note meant to be called in the same thread as the thread running the @ref IAsyncJob::run
    //! call.
    virtual bool notify_completion(IAsyncJob *child);
    
  };



  /*! Represents a group of jobs
   *
   * Represents a group of jobs, that can in turn contain other groups. This view forms a tree
   * of jobs and groups.
   * 
   * A group is completed (@ref IAsyncJob::is_complete evaluates to @c true) when all its jobs are 
   * completed as well. The notifications are sent from the child not to their direct parent node.
   *
   * When a group is posted for scheduling, all the jobs it contains are scheduled as well, the group
   * itself not being a job (the @ref IAsyncJobGroup::run should not be called). There is no ordering 
   * among the jobs contained in a jobs tree.
   *
   * As for jobs, if a group has been posted, it cannot be posted again. This is particularly important 
   * if the group is a subtree of a bigger tree of jobs: if a subtree has been posted, then an error would 
   * occur during the posting of the tree itself.
   */
  struct YCom_ IAsyncJobGroup : public IAsyncJob
  {
    //!@internal
    //! Opaque state
    void* group_state;
    
    IAsyncJobGroup();
    virtual ~IAsyncJobGroup();

    //! Should not be called. Throws an exception.
    virtual yaRC run();

    //! Get notifications from the jobs and groups that are direct child of this node
    //! in the job tree.
    //!
    //! These notifications are sent by a child node to indicate their completion. The current
    //! node is then complete when it received as many notifications as its number of children.
    virtual bool notify_completion(IAsyncJob *child);

    /*! Adds a job to the group.
     *
     * @returns 
     *  - false if the group is already scheduled for processing
     *  - false if the job is already scheduled
     *  - false if the job or group is already owned by another group. This ensures that
     *    the tree is well defined.
     *  - true if successful. 
     *  
     * @post @ref IAsyncJob::is_scheduled "job->is_scheduled" evaluates to true if the function call returned success.
     *
     * @note 
     * If the call succeeds, the ownsership of the job belongs to the group (the group is 
     * responsible for releasing the job when the group is destructed).
     */
    bool add_job(IAsyncJob* job);
  };



  //! Specifies the number of threads in the thread pool
  //! The operation is thread safe
  //! Reducing the number of threads might be blocking the caller, while increasing the number of threads 
  //! should be immediate.
  YCom_ yaRC set_thread_pool_size(int i);

  //! Returns the number of active threads in the thread pool.
  //! @see set_thread_pool_size
  YCom_ std::size_t get_thread_pool_size();
  
  /*! Posts a job or a group of jobs into the thread pool
   *
   * @returns 
   *  - @ref yaRC_ok if the job or the group of jobs has been queued in the processing queue.
   *  - @ref yaRC_E_locked if the job or any job in the group has already been queued before 
   *    the call to @c post_job . Note that in the case of a group of jobs, the group will have
   *    an inconsistent state. The caller should ensure that no job of the group has already been 
   *    posted.
   *  - @ref yaRC_E_bad_size if the pool has no running threads.
   *
   * @post @c IAsyncJob::is_scheduled evaluates to true for all the jobs and the groups contained 
   *       in @c job
   *
   * The processing of the jobs starts as soon as possible.
   */
  YCom_ yaRC post_job(IAsyncJob& job);

  //! Returns the size of the current queue in the processing pool.
  //!
  //! @note the groups are not counted in the returned value.
  YCom_ std::size_t get_thread_pool_queue_size();
  
}

#endif /* YAYI_COMMON_THREAD_POOL_HPP__ */
