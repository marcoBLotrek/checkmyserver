redis-server --daemonize yes 
echo redis server startato
sh huey.sh stop
sh huey.sh start
echo cron startato 
