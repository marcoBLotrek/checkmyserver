from huey import crontab
from huey.contrib.djhuey import periodic_task, task
from panel.actions import *
import os, re, smtplib, json

@periodic_task(crontab(minute='*/1'))
def every_mins():
    print('Every  minute check all severs')
    checkservers()