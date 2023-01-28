#!/bin/bash

# Install dependencies at runtime
pipenv install

# Apply database migrations
echo "Apply database migrations"
pipenv run manage.py migrate

# SuperUser
if [ -n "$DJANGO_SUPERUSER_USERNAME" ] && [ -n "$DJANGO_SUPERUSER_PASSWORD" ] ;
then
    pipenv run manage.py createsuperuser --no-input
fi

# Collect static files
echo "Collect static files"
pipenv run manage.py collectstatic --noinput


# Start server
echo "Starting server"
pipenv run manage.py runserver 0.0.0.0:8000
