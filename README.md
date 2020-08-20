# Local Setup

### Prerequisites

You will need `python3` and `pip3` with `virtualenv`. You'll also need some other miscellaneous dependencies (see `requirements.txt`), I think on the latest Ubuntu you'll need to run:

```
sudo apt-get install build-essential python3-dev libgpgme11-dev
sudo apt-get install libbz2-dev libsqlite3-dev
sudo apt-get install python3-pip
sudo pip3 install virtualenv
```

You can also install virtualenv via apt `sudo apt-get install virtualenv`.

Before proceeding, please make sure you have python 3.6.6 installed.

### Clone the repo

```
git clone git@github.com:ravi-ojha/ibc-django.git
```

### Create a virtual environment

Before this, check the version of python is invoked when running `python3` is `3.6.6`

```
cd ibc-django
virtualenv -p python3 venv
source venv/bin/activate
```

Note on Ubuntu you may need to use `virtualenv -p python3.6m venv` instead.

### Install repo requirements

```
pip3 install -r requirements.txt
```

### Migrate local db

```
./manage.py migrate
```

### Create users

```
./manage.py createsuperuser
```

Provide any email/user/password. Remember that.

### Launch shell

```
./manage.py shell
```

If that worked, exit and launch server

### Launch server

```
./manage.py runserver
```

# Prod deployment

SSH into the server. `cd` to repo and enable virtual env. Bash alias is `work-on-ibc-django`

If there are any static file changes, run `./manage.py collectstatic`

```
sudo service nginx restart
sudo systemctl restart gunicorn
```

nginx restart is only required in case of static file updates.

Check the gunicorn status by `sudo systemctl status gunicorn`

If there are django model changes, please read about django migrations before running any migration commands in prod.
