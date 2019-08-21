FROM python:latest
ENV PYTHONUNBUFFERED 1
ENV C_FORCE_ROOT true
RUN mkdir /src
RUN mkdir /static
WORKDIR /src
ADD ./src /src
ADD ./requirements.txt /src/requirements.txt
RUN pip install -r requirements.txt
CMD python manage.py collectstatic --no-input && python manage.py migrate && python manage.py shell -c "from django.contrib.auth.models import User;  User.objects.filter(email='admin@example.com', is_superuser=True).delete();  User.objects.create_superuser('${MYUSER}', 'admin@example.com', '${MYPASS}'); " && gunicorn mychecker.wsgi -b 0.0.0.0:9000  && python manage.py run_huey 