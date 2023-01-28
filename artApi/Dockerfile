FROM python:alpine

EXPOSE 8000

# ENV DockerHome=backend
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip install --upgrade pip && \
    pip install pipenv

# Database setup
RUN apk add mariadb-connector-c-dev
RUN apk add mariadb-dev build-base
RUN apk add libffi-dev
RUN apk add --no-cache bash

# Python dependencies
WORKDIR /backend
COPY . /backend
RUN pipenv install

#
RUN pipenv install gunicorn

# Script
RUN chmod +x ./init.sh

ENTRYPOINT ["./init.sh"]
