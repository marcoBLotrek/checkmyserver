from huey import crontab
from huey.contrib.djhuey import periodic_task, task
from panel.actions import *
import os, re, smtplib, json

@periodic_task(crontab(minute='*/1'))
def every_mins():
    print('Every  minute check all severs')
    checkservers()
    webhook_url = 'https://hooks.slack.com/services/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'
    slack_data = {'text': 'il cron gira'}