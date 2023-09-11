#!/bin/bash

container_type=${CONTAINER_TYPE-bot};

if [ $container_type = "bot" ]; then
  python manage.py bot
else
  python manage.py migrate --noinput
  python manage.py runserver 0.0.0.0:8000
fi;