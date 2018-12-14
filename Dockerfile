FROM python:latest
ENV PYTHONUNBUFFERED 1
ENV C_FORCE_ROOT true
RUN mkdir /src
RUN mkdir /static
WORKDIR /src
ADD ./src /src
ADD ./requirements.txt /src/requirements.txt
RUN pip install -r requirements.txt
CMD python manage.py collectstatic --no-input
CMD python manage.py migrate
CMD python manage.py shell -c "from django.contrib.auth.models import User; User.objects.create_superuser('admin', 'admin@example.com', 'adminpass')"
CMD gunicorn mychecker.wsgi -b 0.0.0.0:8000 
CMD redis-server --daemonize yes
#CMD cat huey.pid | xargs kill -9
#CMD rm huey.pid
CMD python manage.py run_huey
#CMD sh start.sh