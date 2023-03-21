# BackendAPI

This is the django-rest repo that hosts our backend :)

For running this locally you just need docker and any DB manager
(DBeaver recommended)

## Environment variables/secrets

For this you will need a working nodejs installation. Someone on the should have sent you the `.env.pass` file then run

```bash
    npm install -g senv 
    ./env-decrypt.sh 
```

Then go in the decrypted `.env` file and add your local ip and localhost if you want
to open the backend to your local network

If you change anything remember to run `./env-encrypt.sh` to modify the file.

## Installation for local development (without containers):

Dependencies (Assuming you are running a linux distro with apt)

```bash
  sudo apt install python3 libmysqlclient-dev
  pip install pipenv
  cd artApi/
  pipenv shell
  pipenv install
```

Next you'll need to start the local mysql and mailhog containers

```bash
  docker-compose up --build mysql
```

Then go in the project folder and start the server

```bash
  cd artApi
  python manage.py runserver
```

## For running containers locally:

Make sure to have docker installed and to be in the root directory

```bash
  docker-compose up
```

Always check with docker-desktop if everything is running correctly.

N.B.: If you are running migrations for the first time you could get an error with migrations history.
To fix this you need to run the following commands in your Mysql bash:

```sql
INSERT INTO django_migrations (app, name, applied)
VALUES ('users', '0001_initial', CURRENT_TIMESTAMP);

UPDATE django_content_type
SET app_label = 'users'
WHERE app_label = 'auth'
  and model = 'user';
```

## Running over HTTPS and a certificate

If you want to do this you will need to start the docker-file in the reverse
proxy directory `./reverseProxy/docker-compose.yaml`

Before running, it hough you will need to create the required docker network
with `docker network create nginx-proxy`

```bash
    cd reverseProxy/
    docker-compose up
```

This container will pick up on any other running containers and act as a reverse proxy
for them. The order doesn't really matter but running the reverseProxy first is recommended.

Now run the docker-compose in the root of the repo:

```bash
    cd ..
    docker-compose -f docker-compose-prod.yaml up --build
```

### Adding dependencies

Install dependencies with pipenv. Restart the container, and you should have everything running correctly.

## Django commands

* `python manage.py runserver`
* `python manage.py makemigrations`
* `python manage.py migrate`
* `python manage.py collectstatic`
