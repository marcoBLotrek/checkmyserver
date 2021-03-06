#!/bin/bash

if [ "$1" = "stop" ]; then
    cat huey.pid | xargs kill -9
    rm huey.pid
fi

if [ "$1" = "start" ]; then
    python manage.py run_huey --logfile huey_logs.log &
    echo $! > huey.pid
fi
