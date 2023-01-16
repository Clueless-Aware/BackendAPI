# BackendAPI

## Installation for local development:

Dependencies (Assuming you are running a linux distro with apt)

```bash
  sudo apt install python3 libmysqlclient-dev
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


### Adding dependencies

After you have added dependencies and installed them with pipenv remember to regenerate the `requirements.txt` file
This is needs to be done because docker needs to use a `requirements.txt` file.
