# BackendAPI

## Installation for local development:

Dependencies

```bash
  sudo apt install python3
  sudo apt install libmysqlclient-dev
  pip install pipenv
  pipenv shell
  pipenv install
```

Next you'll need to start the local mysql container
```
  docker-compose up --build mysql
```


Then go in the main folder and start the server
```
  cd artApi
  python manage.py runserver
```

## For running containers:

Make sure to have docker installed and to be in the root directory

```
  docker-compose up
```
Always check with docker-desktop if everything is running correctly
