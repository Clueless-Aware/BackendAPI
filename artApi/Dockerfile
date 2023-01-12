FROM --platform=$BUILDPLATFORM python:3.9-alpine AS builder

EXPOSE 8000

ENV DockerHome=backend
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1


RUN pip install --upgrade pip

# Database setup
RUN apk add mariadb-connector-c-dev
RUN apk add mariadb-dev build-base
RUN apk add libffi-dev
RUN apk add --no-cache bash
COPY . ${DockerHome}

# Python dependencies
WORKDIR ${DockerHome}
RUN pip install -r requirements.txt --no-cache-dir

# Script
RUN chmod a+rx ./init.sh

ENTRYPOINT [ "./init.sh" ]
# RUN ./init.sh
