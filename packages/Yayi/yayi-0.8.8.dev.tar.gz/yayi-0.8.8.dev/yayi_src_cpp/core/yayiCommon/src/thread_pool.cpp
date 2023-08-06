//! @file
//! This file contains the thread pool interface
//! @author Raffi Enficiaud


#include <yayiCommon/common_types.hpp>
#include <yayiCommon/include/thread_pool.hpp>
#include <yayiCommon/common_errors.hpp>


#include <boost/asio/io_service.hpp>
#include <boost/bind.hpp>
#include <boost/thread/thread.hpp>
#include <boost/thread/recursive_mutex.hpp>
#include <map>


namespace yayi
{

  struct opaque_state_impl
  {
    bool is_scheduled;
    bool is_finished;
    yaRC return_code;
    IAsyncJob *owned_by;
    
    typedef boost::recursive_timed_mutex mutex_t;
    mutable mutex_t internal_mutex;
    boost::condition_variable_any condition_;
    
    opaque_state_impl() :
      is_scheduled(false),
      is_finished(false),
      return_code(yaRC_E_unknown),
      owned_by(0)
    {}
  };
  
  IAsyncJob::IAsyncJob() : state(0)
  {
    state = new opaque_state_impl;
  }
  
  IAsyncJob::~IAsyncJob()
  {
    opaque_state_impl* internal_state = static_cast<opaque_state_impl*>(state);
    if(internal_state->is_scheduled && !internal_state->is_finished)
    {
      errors::yayi_error_stream() 
        << "[YAYI][ERROR][multithreading] some scheduled tasks are being destroyed before "
        << "their completion. This indicates an error."
        << std::endl;
    }

#ifndef NDEBUG
    if(internal_state->owned_by && (dynamic_cast<IAsyncJobGroup*>(internal_state->owned_by) == 0))
    {
      errors::yayi_error_stream() 
        << "[YAYI][ERROR][multithreading] job owned by something else than a group."
        << std::endl;
    }
#endif

    delete internal_state;
  }
    
  bool IAsyncJob::is_complete() const
  {
    return static_cast<opaque_state_impl*>(state)->is_finished;
  }

  bool IAsyncJob::is_scheduled() const
  {
    return static_cast<opaque_state_impl*>(state)->is_scheduled;
  }
  
  struct predicate_finished
  {
    const volatile bool &var;
    predicate_finished(const volatile bool &var_) : var(var_){}
    
    bool operator()() const
    {
      return var;
    }
  };
  
  bool IAsyncJob::wait_for_completion(size_t nb_microsecond_wait) const
  {
    opaque_state_impl* internal_state = static_cast<opaque_state_impl*>(state);
    boost::unique_lock<opaque_state_impl::mutex_t> ulock(internal_state->internal_mutex);
    if(!internal_state->is_scheduled)
      return false;

    if(internal_state->is_finished)
      return true;
    
    if(nb_microsecond_wait == 0)
    {
      internal_state->condition_.wait(
        ulock, 
        predicate_finished(internal_state->is_finished));
        
      return true;
    }
    else
    {
      bool status = internal_state->condition_.wait_for(
        ulock, 
        boost::chrono::microseconds(nb_microsecond_wait),
        predicate_finished(internal_state->is_finished));
        
      return status;
    }
  }

  bool IAsyncJob::notify_completion(IAsyncJob *child)
  {
    if(!child)
      return false;

    opaque_state_impl* internal_state = static_cast<opaque_state_impl*>(state);
    boost::unique_lock<opaque_state_impl::mutex_t> ulock(internal_state->internal_mutex);

    opaque_state_impl* child_internal_state = static_cast<opaque_state_impl*>(child->state);
    //boost::unique_lock<opaque_state_impl::mutex_t> ulock(internal_state->internal_mutex);

    if(child_internal_state->owned_by != this)
      return false;

    // notify the direct watchers 
    internal_state->condition_.notify_all();
    return true;

  }


  struct opaque_group_state_impl
  {
    typedef std::list<IAsyncJob*> container_t;
    container_t list_jobs_queued;
    container_t list_jobs_finished;

    opaque_group_state_impl()
    {}
  };

    
  IAsyncJobGroup::IAsyncJobGroup() : group_state(0)
  {
    group_state = new opaque_group_state_impl();
  }

  IAsyncJobGroup::~IAsyncJobGroup()
  {
    opaque_group_state_impl *g_state = static_cast<opaque_group_state_impl*>(group_state);

    if(this->is_scheduled() && !this->is_complete())
    {
      errors::yayi_error_stream() 
        << "[YAYI][ERROR][multithreading] job group being deleted before its "
        << "completion. This indicates an error."
        << std::endl;
    }

    for(opaque_group_state_impl::container_t::iterator it(g_state->list_jobs_finished.begin()), ite(g_state->list_jobs_finished.end());
        it != ite;
        ++it)
    {
      delete *it;
      *it = 0;
    }

    for(opaque_group_state_impl::container_t::iterator it(g_state->list_jobs_queued.begin()), ite(g_state->list_jobs_queued.end());
        it != ite;
        ++it)
    {
      delete *it;
      *it = 0;
    }

    delete g_state;
  }

  bool IAsyncJobGroup::add_job(IAsyncJob* job)
  {
    if(!job)
      return false;

    // lock the group
    opaque_state_impl* group_internal_state = static_cast<opaque_state_impl*>(state);
    boost::unique_lock<opaque_state_impl::mutex_t> ulock_group(group_internal_state->internal_mutex);
    if(this->is_scheduled())
      return false;

    // lock the job
    opaque_state_impl* job_internal_job_state = static_cast<opaque_state_impl*>(job->state);
    boost::unique_lock<opaque_state_impl::mutex_t> ulock_job(job_internal_job_state->internal_mutex);
      
    if(job->is_scheduled())
      return false;

    // cannot belong to more than one group
    if(job_internal_job_state->owned_by)
      return false;

    opaque_group_state_impl *g_state = static_cast<opaque_group_state_impl*>(group_state);
    g_state->list_jobs_queued.push_back(job);

    job_internal_job_state->owned_by = this;

    return true;
  }

  bool IAsyncJobGroup::notify_completion(IAsyncJob *child)
  {
    if(!child)
      return false;

    opaque_state_impl* group_internal_job_state = static_cast<opaque_state_impl*>(state);
    boost::unique_lock<opaque_state_impl::mutex_t> ulock(group_internal_job_state->internal_mutex);

    opaque_state_impl* child_internal_state = static_cast<opaque_state_impl*>(child->state);

    if(child_internal_state->owned_by != this)
      return false;

    opaque_group_state_impl *g_state = static_cast<opaque_group_state_impl*>(this->group_state);
      
    {
      opaque_group_state_impl::container_t& list_jobs_queued = g_state->list_jobs_queued;
      opaque_group_state_impl::container_t::iterator it = std::find(list_jobs_queued.begin(), list_jobs_queued.end(), child);
      assert(it != list_jobs_queued.end());
      list_jobs_queued.erase(it);
      g_state->list_jobs_finished.push_back(child);
      
      if(list_jobs_queued.empty())
      {
        group_internal_job_state->is_finished = true;
        group_internal_job_state->condition_.notify_all();
        if(group_internal_job_state->owned_by)
        {
          group_internal_job_state->owned_by->notify_completion(this);
        }
      }
    }
    return true;
  }

    
  yaRC IAsyncJobGroup::run()
  {
    throw std::runtime_error("Should not be called directly");
  }

    


  namespace thread_internal
  {



    struct thread_pool_manager
    {
      boost::asio::io_service ioService;
      // the order is important here, work should appear after ioService
      boost::asio::io_service::work work;
      boost::thread_group threadpool;


      int nb_threads_current;
      std::map<boost::thread::id, boost::thread*> threads_map;
      boost::condition_variable_any condition_;

      // Mutex for protected operations
      typedef boost::recursive_mutex mutex_t;
      mutable mutex_t internal_mutex;

      // number of jobs
      std::size_t current_nb_jobs;

      thread_pool_manager() : work(ioService), nb_threads_current(0), current_nb_jobs(0)
      {
      }
      
      // Releases the thread pool and wait for completion
      ~thread_pool_manager()
      {
        ioService.stop();
        threadpool.join_all();
      }      

      // internal
      // this function kills threads. This is used to reduce the number of active threads
      // in the pool.
      void peek_free_thread_id(int& counter, boost::thread::id& out_id)
      {
        boost::unique_lock<mutex_t> lock(internal_mutex);

        out_id = boost::this_thread::get_id();
        counter++;
        condition_.notify_one();

        // this call kills the thread from within, without propagating the exception.
        throw boost::thread_interrupted();
      }

      yaRC set_pool_size(int nb_threads)
      {
        boost::unique_lock<mutex_t> lock(internal_mutex);


        if(nb_threads >= nb_threads_current)
        {
          // increase the number of threads
          for(int i = 0; i < nb_threads - nb_threads_current; i++)
          {
            boost::thread* new_thread = threadpool.create_thread(boost::bind(&boost::asio::io_service::run, &ioService));
            threads_map[new_thread->get_id()] = new_thread;
          }
          nb_threads_current = nb_threads;
        }
        else
        {
          int nb_updates(0);

          std::vector<boost::thread::id> removed_threads(nb_threads_current - nb_threads);
          for(int i = 0; i < nb_threads_current - nb_threads; i++)
          {
            ioService.post(boost::bind(&thread_pool_manager::peek_free_thread_id, this, boost::ref(nb_updates), boost::ref(removed_threads[i])));
          }

          // we wait for nb_threads_current - nb_threads removals

          while (nb_updates < nb_threads_current - nb_threads)
          {
            // when entering wait, the lock is unlocked and made available to other threads.
            // when awakened, the lock is locked before wait returns. 
            condition_.wait(lock);
          }

          // removing the freed threads
          for(int i = 0; i < nb_threads_current - nb_threads; i++)
          {
            boost::thread* removed_thread = threads_map[removed_threads[i]];
            if(removed_thread)
            {
              threadpool.remove_thread(removed_thread);
              delete removed_thread;
            }
            threads_map.erase(removed_threads[i]);
          }

          // update the number of current threads
          nb_threads_current = nb_threads;

        }
        return yaRC_ok;
      }

      // Size of the current thread pool
      std::size_t size() const
      {
        return threadpool.size();
      }

      // a simple wrapper for doing all the necessary signaling
      // and state change of the job
      struct job_wrapper
      {
        IAsyncJob* job;
        thread_pool_manager *manager;
        job_wrapper(IAsyncJob* job_, thread_pool_manager *manager_) : 
          job(job_), manager(manager_)
        {}
        
        void operator()()
        {
          assert(job);
          opaque_state_impl *opaque = static_cast<opaque_state_impl*>(job->state);
          opaque->return_code = job->run();
          opaque->is_finished = true;
          
          // try to do that without locking
          {
            boost::unique_lock<mutex_t> lock(manager->internal_mutex);
            manager->current_nb_jobs--;
          }


          // signals the completion
          {
            // prevents the job from mutating during the chain of notifications
            boost::unique_lock<opaque_state_impl::mutex_t> lock(opaque->internal_mutex);

            // signals all waiting threads
            opaque->condition_.notify_all();

            // signals the hierarchy
            if(opaque->owned_by)
            {
              // if this is owned, then it should not be possible to delete the job
              // directly. Rather the owner has this responsibility
              opaque->owned_by->notify_completion(job);
            }
          }
          // we cannot do any other operation starting this point.
        }
      };

      yaRC post_job(IAsyncJob *job)
      {
        if(!job)
          return yaRC_E_null_pointer;
        
        boost::unique_lock<mutex_t> lock(internal_mutex);
        
        // cannot treat
        if(size() == 0)
        {
          return yaRC_E_bad_size;
        }
        
        // only this .cpp has access to the definition of the opaque pointer
        opaque_state_impl *opaque = static_cast<opaque_state_impl*>(job->state);
        
        if(opaque->is_scheduled)
        {
          return yaRC_E_locked;
        }
        // taking ownership of the scheduling
        opaque->is_scheduled = true;

        IAsyncJobGroup* job_group = dynamic_cast<IAsyncJobGroup*>(job);
        if(job_group)
        {
          // we enqueue the elements of the group directly.

          opaque_group_state_impl* g_state = static_cast<opaque_group_state_impl*>(job_group->group_state);

          for(opaque_group_state_impl::container_t::iterator it(g_state->list_jobs_queued.begin()), ite(g_state->list_jobs_queued.end());
              it != ite;
              ++it)
          {
            yaRC res_post = post_job(*it);
            if(res_post != yaRC_ok)
            {
              // the group is in an inconsistent state. It cannot be posted anymore 
              // as the scheduled flag is on.
              return res_post;
            }
            // we do not increment the queue size for a group as its run method is never called
            // directly.
          }
        }
        else
        {
          ioService.post(job_wrapper(job, this));
          // increments the number of jobs currently in the queue
          current_nb_jobs++;
        }


        return yaRC_ok;
      }

      std::size_t get_queue_size() const
      {
        boost::unique_lock<mutex_t> lock(internal_mutex);
        return current_nb_jobs;
      }
    };


    thread_pool_manager manager;

  }


  yaRC set_thread_pool_size(int i)
  {
    // we should wait until the active processes finish
    return thread_internal::manager.set_pool_size(i);
  }

  std::size_t get_thread_pool_size()
  {
    return thread_internal::manager.size();
  }

  std::size_t get_thread_pool_queue_size()
  {
    return thread_internal::manager.get_queue_size();
  }
  
  yaRC post_job(IAsyncJob& job)
  {
    return thread_internal::manager.post_job(&job);
  }
  
}
