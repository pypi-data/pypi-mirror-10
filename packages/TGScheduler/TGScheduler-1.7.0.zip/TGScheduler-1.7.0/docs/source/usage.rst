Usage
=====

To schedule one task to be run at regular intervals::

    import tgscheduler
    import time


    def task():
        print('Running task')


    print('Init')
    tgscheduler.start_scheduler()

    print('Registering an interval task')
    tgscheduler.add_interval_task(action=task, interval=5, initialdelay=5)

    print('Sleeping')
    while True:
        time.sleep(10)


Another example showing more available calls::

    from tgscheduler import start_scheduler
    from tgscheduler.scheduler import add_interval_task
    from tgscheduler.scheduler add_weekday_task
    from tgscheduler.scheduler add_single_task
    import sys
    import logging
    log = logging.getLogger(__name__)

    def testTask(email=None):
        log.debug("testTask Called")

    def schedule():
        """ start scheduler and setup recurring tasks """

        if "shell" in sys.argv: # disable cron in paster shell mode
            return

        log.info("Starting Scheduler Manager")
        start_scheduler()
        
        # ================ #
        # Add cron tasks here
        
        # Run once a day
        add_weekday_task(action=testTask, weekdays=range(1-8), timeonday=(19, 0))

        # run at intervals
        add_interval_task(action=testTask, taskname="test1", interval=60*60, initialdelay=30)

        # run this once and forgot, useful for long running backgound tasks
        add_single_task(action=testTask, initialdelay=0, args=[request.user.email_address] )

    # Your framework is now supposed to call the "schedule" function.
    schedule()
