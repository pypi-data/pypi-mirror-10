#include "main.hpp"

#include <yayiCommon/include/thread_pool.hpp>
#include <boost/thread.hpp>


BOOST_AUTO_TEST_SUITE(thread_pool)

struct pool
{
  pool()
  {
    BOOST_CHECK_EQUAL(yayi::set_thread_pool_size(0), yayi::yaRC_ok);
  }
  ~pool()
  {
    BOOST_CHECK_EQUAL(yayi::set_thread_pool_size(0), yayi::yaRC_ok);
  }
};

BOOST_FIXTURE_TEST_CASE(set_nb_threads, pool)
{
  BOOST_CHECK_EQUAL(yayi::get_thread_pool_size(), 0);
  BOOST_CHECK_EQUAL(yayi::set_thread_pool_size(1), yayi::yaRC_ok);
  BOOST_CHECK_EQUAL(yayi::get_thread_pool_size(), 1);

  BOOST_CHECK_EQUAL(yayi::set_thread_pool_size(2), yayi::yaRC_ok);
  BOOST_CHECK_EQUAL(yayi::get_thread_pool_size(), 2);
  
  BOOST_CHECK_EQUAL(yayi::set_thread_pool_size(1), yayi::yaRC_ok);
  BOOST_CHECK_EQUAL(yayi::get_thread_pool_size(), 1);
  

  BOOST_CHECK_EQUAL(yayi::set_thread_pool_size(0), yayi::yaRC_ok);
  BOOST_CHECK_EQUAL(yayi::get_thread_pool_size(), 0);
}


struct test_job : yayi::IAsyncJob
{
  static int nb_instances;
  int count;

  test_job() : count(0) 
  {
    nb_instances++;
  }

  ~test_job()
  {
    nb_instances--;
  }

  
  yayi::yaRC run()
  {
    count++;
    return yayi::yaRC_ok;
  }
};

int test_job::nb_instances = 0;

struct test_job_wait : test_job
{
  boost::mutex mutex_;
  yayi::yaRC run()
  {
    boost::lock_guard<boost::mutex> lck(mutex_);
    return test_job::run();
  }
};


BOOST_FIXTURE_TEST_CASE(post_job_test, pool)
{
  using namespace yayi;
  test_job job;
  BOOST_CHECK_EQUAL(post_job(job), yaRC_E_bad_size); // pool of size 0 cannot treat
  BOOST_CHECK_EQUAL(yayi::set_thread_pool_size(1), yayi::yaRC_ok);
  BOOST_CHECK_EQUAL(get_thread_pool_queue_size(), 0);
  BOOST_CHECK_EQUAL(post_job(job), yaRC_ok);
  BOOST_CHECK_GE(get_thread_pool_queue_size(), 0);
  BOOST_CHECK_LE(get_thread_pool_queue_size(), 1);

  // simple barrier
  while(get_thread_pool_queue_size() > 0)
  {
    boost::this_thread::sleep_for(boost::chrono::microseconds(1));
  }

  // size 0 is after the count = 1
  BOOST_CHECK(get_thread_pool_queue_size() == 0 && job.count == 1);
  
  BOOST_CHECK_EQUAL(yayi::set_thread_pool_size(0), yayi::yaRC_ok); // wait for completion
  BOOST_CHECK_EQUAL(job.count, 1);
  BOOST_CHECK_EQUAL(get_thread_pool_queue_size(), 0);
}

BOOST_FIXTURE_TEST_CASE(post_job_cannot_post_twice, pool)
{
  using namespace yayi;

  BOOST_CHECK_EQUAL(yayi::set_thread_pool_size(1), yayi::yaRC_ok);
  
  test_job job;
  BOOST_CHECK_EQUAL(post_job(job), yaRC_ok);
  BOOST_CHECK(job.is_scheduled());

  BOOST_CHECK_EQUAL(post_job(job), yaRC_E_locked);
  BOOST_CHECK(job.is_scheduled());
      
  BOOST_CHECK_EQUAL(yayi::set_thread_pool_size(0), yayi::yaRC_ok); // wait for completion
  BOOST_CHECK_EQUAL(get_thread_pool_queue_size(), 0);
}

BOOST_FIXTURE_TEST_CASE(job_wait_for_completion, pool)
{
  using namespace yayi;

  BOOST_CHECK_EQUAL(yayi::set_thread_pool_size(1), yayi::yaRC_ok);
  
  {
    test_job job;
    BOOST_CHECK_EQUAL(post_job(job), yaRC_ok);
    BOOST_CHECK(job.wait_for_completion());
    BOOST_CHECK_EQUAL(job.count, 1);
    BOOST_CHECK(job.is_complete());
    // safe to delete job
  }



  {
    test_job_wait job2;

    {
      // prevent the execution of the code to test that timed wait
      // returns before the run ended
      boost::lock_guard<boost::mutex> lck(job2.mutex_);

      BOOST_CHECK_EQUAL(post_job(job2), yaRC_ok);
      BOOST_CHECK(!job2.wait_for_completion(1));
      BOOST_CHECK_EQUAL(job2.count, 0);
      BOOST_CHECK(!job2.is_complete());
    }

    // no easy way to enter this function before run has started and ensure 
    // that run finishes during that timeframe
    BOOST_CHECK(job2.wait_for_completion(1000));
    BOOST_CHECK_EQUAL(job2.count, 1);
    BOOST_CHECK(job2.is_complete());
    // safe to delete job2
  }

        
  BOOST_CHECK_EQUAL(yayi::set_thread_pool_size(0), yayi::yaRC_ok); // wait for completion
  BOOST_CHECK_EQUAL(get_thread_pool_queue_size(), 0);
}



BOOST_FIXTURE_TEST_CASE(jobgroup_delete_queued_and_finished, pool)
{
  using namespace yayi;

  {
    IAsyncJobGroup group;

    BOOST_CHECK_EQUAL(yayi::set_thread_pool_size(1), yayi::yaRC_ok);
 
    test_job *job = new test_job;
    BOOST_CHECK(group.add_job(job));
    BOOST_CHECK(!group.add_job(job)); // cannot add twice

    // no scheduling, safe to delete
  }

  // properly deleted
  BOOST_CHECK_EQUAL(test_job::nb_instances, 0);
}

BOOST_FIXTURE_TEST_CASE(jobgroup_check_empty_group_status, pool)
{
  using namespace yayi;

  IAsyncJobGroup group;

  BOOST_CHECK(!group.is_scheduled());
  BOOST_CHECK(!group.is_complete());
}



BOOST_FIXTURE_TEST_CASE(jobgroup_cannot_add_twice, pool)
{
  using namespace yayi;

  {
    IAsyncJobGroup group;

    BOOST_CHECK_EQUAL(yayi::set_thread_pool_size(1), yayi::yaRC_ok);
 
    test_job *job = new test_job;
    BOOST_CHECK(group.add_job(job));
    BOOST_CHECK(!group.add_job(job)); // cannot add twice

    // no scheduling, safe to delete
    BOOST_REQUIRE(!group.is_scheduled());
    BOOST_CHECK(!group.is_complete());
  }

  // properly deleted
  BOOST_CHECK_EQUAL(test_job::nb_instances, 0);
}

BOOST_FIXTURE_TEST_CASE(jobgroup_cannot_add_after_scheduling, pool)
{
  using namespace yayi;

  test_job dummy;

  {
    IAsyncJobGroup group;

    BOOST_CHECK_EQUAL(yayi::set_thread_pool_size(1), yayi::yaRC_ok);
  
    test_job *job = new test_job;
    BOOST_CHECK(group.add_job(job));
  
    BOOST_CHECK_EQUAL(post_job(group), yaRC_ok);
  
    BOOST_CHECK(!group.add_job(&dummy));

    BOOST_CHECK_EQUAL(yayi::set_thread_pool_size(0), yayi::yaRC_ok);
  
    BOOST_CHECK_EQUAL(dummy.count, 0);  // not executed
    BOOST_CHECK_EQUAL(job->count, 1);   // executed
  }

  BOOST_CHECK_EQUAL(test_job::nb_instances, 1); // dummy not added
}




BOOST_FIXTURE_TEST_CASE(jobgroup_group_complete, pool)
{
  using namespace yayi;


  BOOST_CHECK_EQUAL(yayi::set_thread_pool_size(1), yayi::yaRC_ok);
  
  {
    IAsyncJobGroup group;
    std::vector<test_job_wait *> v_jobs(10, (test_job_wait *)0);
    for(size_t i = 0; i < v_jobs.size(); i++)
    {
      v_jobs[i] = new test_job_wait;
      v_jobs[i]->mutex_.lock();
    }

    for(size_t i = 0; i < v_jobs.size(); i++)
    {
      BOOST_CHECK(group.add_job(v_jobs[i]));
    }


    BOOST_CHECK_EQUAL(post_job(group), yaRC_ok);
    BOOST_CHECK(group.is_scheduled());

    BOOST_CHECK_EQUAL(get_thread_pool_queue_size(), v_jobs.size());

    // enable the processing
    for(size_t i = 0; i < v_jobs.size(); i++)
    {
      v_jobs[i]->mutex_.unlock();
    }

    BOOST_CHECK(group.wait_for_completion());

    for(size_t i = 0; i < v_jobs.size(); i++)
    {
      BOOST_CHECK_EQUAL(v_jobs[i]->count, 1);
      BOOST_CHECK(v_jobs[i]->is_complete());
    }

    BOOST_CHECK(group.is_complete());
  }
  BOOST_CHECK_EQUAL(test_job::nb_instances, 0);



  // here wait for completion with a duration
  {
    IAsyncJobGroup group;
    std::vector<test_job_wait *> v_jobs(10, (test_job_wait *)0);
    for(size_t i = 0; i < v_jobs.size(); i++)
    {
      v_jobs[i] = new test_job_wait;
      v_jobs[i]->mutex_.lock();
    }

    for(size_t i = 0; i < v_jobs.size(); i++)
    {
      BOOST_CHECK(group.add_job(v_jobs[i]));
    }


    BOOST_CHECK_EQUAL(post_job(group), yaRC_ok);
    BOOST_CHECK(group.is_scheduled());

    BOOST_CHECK_EQUAL(get_thread_pool_queue_size(), v_jobs.size());

    BOOST_CHECK(!group.wait_for_completion(1));

    // enable the processing
    for(size_t i = 0; i < v_jobs.size(); i++)
    {
      v_jobs[i]->mutex_.unlock();
    }

    BOOST_CHECK(group.wait_for_completion(10000)); // 10s, should return faster than that

    for(size_t i = 0; i < v_jobs.size(); i++)
    {
      BOOST_CHECK_EQUAL(v_jobs[i]->count, 1);
      BOOST_CHECK(v_jobs[i]->is_complete());
    }

    BOOST_CHECK(group.is_complete());
  }
  BOOST_CHECK_EQUAL(test_job::nb_instances, 0);


        
  BOOST_CHECK_EQUAL(yayi::set_thread_pool_size(0), yayi::yaRC_ok); // wait for completion
  BOOST_CHECK_EQUAL(get_thread_pool_queue_size(), 0);
}




BOOST_FIXTURE_TEST_CASE(jobgroup_group_nested, pool)
{
  using namespace yayi;


  BOOST_CHECK_EQUAL(yayi::set_thread_pool_size(1), yayi::yaRC_ok);
  
  {
    IAsyncJobGroup *group1 = new IAsyncJobGroup();
    std::vector<test_job_wait *> v_jobs_g1(5, (test_job_wait *)0);
    for(size_t i = 0; i < v_jobs_g1.size(); i++)
    {
      v_jobs_g1[i] = new test_job_wait;
      v_jobs_g1[i]->mutex_.lock();
    }

    for(size_t i = 0; i < v_jobs_g1.size(); i++)
    {
      BOOST_CHECK(group1->add_job(v_jobs_g1[i]));
    }

    IAsyncJobGroup *group2 = new IAsyncJobGroup();
    std::vector<test_job_wait *> v_jobs_g2(5, (test_job_wait *)0);
    for(size_t i = 0; i < v_jobs_g2.size(); i++)
    {
      v_jobs_g2[i] = new test_job_wait;
      v_jobs_g2[i]->mutex_.lock();
    }

    for(size_t i = 0; i < v_jobs_g2.size(); i++)
    {
      BOOST_CHECK(group2->add_job(v_jobs_g2[i]));
    }

    IAsyncJobGroup group;
    BOOST_CHECK(group.add_job(group1));
    BOOST_CHECK(group.add_job(group2));

    BOOST_CHECK(!group1->is_scheduled());
    BOOST_CHECK(!group2->is_scheduled());
    BOOST_CHECK(!group1->is_complete());
    BOOST_CHECK(!group2->is_complete());

    BOOST_CHECK_EQUAL(post_job(group), yaRC_ok);

    BOOST_CHECK(group.is_scheduled());
    BOOST_CHECK(group1->is_scheduled());
    BOOST_CHECK(group2->is_scheduled());
    BOOST_CHECK(!group1->is_complete());
    BOOST_CHECK(!group2->is_complete());

    BOOST_CHECK_EQUAL(get_thread_pool_queue_size(), v_jobs_g1.size() + v_jobs_g2.size());

    // enable the processing
    for(size_t i = 0; i < v_jobs_g1.size(); i++)
    {
      v_jobs_g1[i]->mutex_.unlock();
    }
    for(size_t i = 0; i < v_jobs_g2.size(); i++)
    {
      v_jobs_g2[i]->mutex_.unlock();
    }

    BOOST_CHECK(group.wait_for_completion());

    for(size_t i = 0; i < v_jobs_g1.size(); i++)
    {
      BOOST_CHECK_EQUAL(v_jobs_g1[i]->count, 1);
      BOOST_CHECK(v_jobs_g1[i]->is_complete());
    }
    
    for(size_t i = 0; i < v_jobs_g2.size(); i++)
    {
      BOOST_CHECK_EQUAL(v_jobs_g1[i]->count, 1);
      BOOST_CHECK(v_jobs_g1[i]->is_complete());
    }

    BOOST_CHECK(group.is_complete());
    BOOST_CHECK(group1->is_complete());
    BOOST_CHECK(group2->is_complete());
  }
  BOOST_CHECK_EQUAL(test_job::nb_instances, 0);



  // here wait for completion with a duration
  {
    IAsyncJobGroup *group1 = new IAsyncJobGroup();
    std::vector<test_job_wait *> v_jobs_g1(5, (test_job_wait *)0);
    for(size_t i = 0; i < v_jobs_g1.size(); i++)
    {
      v_jobs_g1[i] = new test_job_wait;
      v_jobs_g1[i]->mutex_.lock();
    }

    for(size_t i = 0; i < v_jobs_g1.size(); i++)
    {
      BOOST_CHECK(group1->add_job(v_jobs_g1[i]));
    }

    IAsyncJobGroup *group2 = new IAsyncJobGroup();
    std::vector<test_job_wait *> v_jobs_g2(5, (test_job_wait *)0);
    for(size_t i = 0; i < v_jobs_g2.size(); i++)
    {
      v_jobs_g2[i] = new test_job_wait;
      v_jobs_g2[i]->mutex_.lock();
    }

    for(size_t i = 0; i < v_jobs_g2.size(); i++)
    {
      BOOST_CHECK(group2->add_job(v_jobs_g2[i]));
    }

    IAsyncJobGroup group;
    BOOST_CHECK(group.add_job(group1));
    BOOST_CHECK(group.add_job(group2));

    BOOST_CHECK(!group1->is_scheduled());
    BOOST_CHECK(!group2->is_scheduled());
    BOOST_CHECK(!group1->is_complete());
    BOOST_CHECK(!group2->is_complete());

    BOOST_CHECK_EQUAL(post_job(group), yaRC_ok);

    BOOST_CHECK(group.is_scheduled());
    BOOST_CHECK(group1->is_scheduled());
    BOOST_CHECK(group2->is_scheduled());
    BOOST_CHECK(!group1->is_complete());
    BOOST_CHECK(!group2->is_complete());

    BOOST_CHECK_EQUAL(get_thread_pool_queue_size(), v_jobs_g1.size() + v_jobs_g2.size());

    BOOST_CHECK(!group.wait_for_completion(1));


    // enable the processing, testing the completion of 
    // individual groups
    for(size_t i = 0; i < v_jobs_g1.size(); i++)
    {
      v_jobs_g1[i]->mutex_.unlock();
    }

    BOOST_CHECK(!group.wait_for_completion(1));
    BOOST_CHECK(group1->wait_for_completion(1000));
    BOOST_CHECK(!group2->wait_for_completion(1));
    BOOST_CHECK(group1->wait_for_completion());

    for(size_t i = 0; i < v_jobs_g2.size(); i++)
    {
      v_jobs_g2[i]->mutex_.unlock();
    }

    BOOST_CHECK(group2->wait_for_completion(1000));
    BOOST_CHECK(group.is_complete()); // might fail

    BOOST_CHECK(group.wait_for_completion(1));

    for(size_t i = 0; i < v_jobs_g1.size(); i++)
    {
      BOOST_CHECK_EQUAL(v_jobs_g1[i]->count, 1);
      BOOST_CHECK(v_jobs_g1[i]->is_complete());
    }
    
    for(size_t i = 0; i < v_jobs_g2.size(); i++)
    {
      BOOST_CHECK_EQUAL(v_jobs_g1[i]->count, 1);
      BOOST_CHECK(v_jobs_g1[i]->is_complete());
    }

    BOOST_CHECK(group.is_complete());
    BOOST_CHECK(group1->is_complete());
    BOOST_CHECK(group2->is_complete());
  }
  BOOST_CHECK_EQUAL(test_job::nb_instances, 0);



  {
    IAsyncJobGroup group;
    std::vector<test_job_wait *> v_jobs(10, (test_job_wait *)0);
    for(size_t i = 0; i < v_jobs.size(); i++)
    {
      v_jobs[i] = new test_job_wait;
      v_jobs[i]->mutex_.lock();
    }

    for(size_t i = 0; i < v_jobs.size(); i++)
    {
      BOOST_CHECK(group.add_job(v_jobs[i]));
    }


    BOOST_CHECK_EQUAL(post_job(group), yaRC_ok);
    BOOST_CHECK(group.is_scheduled());

    BOOST_CHECK_EQUAL(get_thread_pool_queue_size(), v_jobs.size());

    BOOST_CHECK(!group.wait_for_completion(1));

    // enable the processing
    for(size_t i = 0; i < v_jobs.size(); i++)
    {
      v_jobs[i]->mutex_.unlock();
    }

    BOOST_CHECK(group.wait_for_completion(10000)); // 10s, should return faster than that

    for(size_t i = 0; i < v_jobs.size(); i++)
    {
      BOOST_CHECK_EQUAL(v_jobs[i]->count, 1);
      BOOST_CHECK(v_jobs[i]->is_complete());
    }

    BOOST_CHECK(group.is_complete());
  }
  BOOST_CHECK_EQUAL(test_job::nb_instances, 0);


        
  BOOST_CHECK_EQUAL(yayi::set_thread_pool_size(0), yayi::yaRC_ok); // wait for completion
  BOOST_CHECK_EQUAL(get_thread_pool_queue_size(), 0);
}



BOOST_AUTO_TEST_SUITE_END()

