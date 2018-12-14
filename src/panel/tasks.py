from huey import crontab
from huey.contrib.djhuey import periodic_task, task
from panel.actions import *

@periodic_task(crontab(minute='*/5'))
def every_mins():
    print('Every  minute check all severs')
    checkservers()