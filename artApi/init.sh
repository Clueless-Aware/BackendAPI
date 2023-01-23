#!/bin/bash

# Install dependencies at runtime
pip install -r requirements.txt --no-cache-dir

# Apply database migrations
echo "Apply database migrations"
python manage.py migrate

# SuperUser
if [ -n "$DJANGO_SUPERUSER_USERNAME" ] && [ -n "$DJANGO_SUPERUSER_PASSWORD" ] ;
then
    python manage.py createsuperuser --no-input
fi

# Collect static files
echo "Collect static files"
python manage.py collectstatic --noinput


# Start server
echo "Starting server"
python manage.py runserver 0.0.0.0:8000
