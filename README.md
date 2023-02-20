# BackendAPI

This is the django-rest repo that hosts our backend :)

## Environment variables/secrets

For this you will need a working nodejs installation. Someone should have sent you the `.env.pass` file then run

```bash
    npm install -g senv 
    ./env-decrypt.sh 
```

If you change anything remember to run `./env-encrypt.sh`

## Installation for local development:

Dependencies (Assuming you are running a linux distro with apt)

```bash
  sudo apt install python3 libmysqlclient-dev
  pip install pipenv
  cd artApi/
  pipenv shell
  pipenv install
```

Next you'll need to start the local mysql container

```bash
  docker-compose up --build mysql
```

Then go in the main folder and start the server

```bash
  cd artApi
  python manage.py runserver
```

## For running containers:

Make sure to have docker installed and to be in the root directory

```bash
  docker-compose up
```

Always check with docker-desktop if everything is running correctly

### Adding dependencies

Install depndencies with pipenv. Restart the container and you should have everything running correcctly.

## Django commands

* `python manage.py runserver`
* `python manage.py makemigrations`
* `python manage.py migrate`
* `python manage.py collectstatic`

## Running il local network
- To run this project on a local network, you will need to add the following environment variables to your .env file.
- Set private network

`APP_ALLOWED_HOSTS` = Your Local Ip

```bash
    docker-compose build
    docker-compose up
```

- visit host_ip
