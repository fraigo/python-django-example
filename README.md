# Python/Django Web application example

A Python/Django Base Web application. 


## Python modules: 

* `django`: Full featured Web framework
* `gunicorn`: Python WSGI HTTP Server for UNIX
* `django_heroku`: Heroku module for deployment integration


## Development

### Install python packages

`pip install -r requirements.txt`


### Prepare database

`python manage.py migrate`

`python manage.py createsuperuser`



### Run the web service (Debug mode)

Modify `webapp/settings.py` with `DEBUG = False`

`python manage.py runserver`

### Run the web service (Production mode)

`python manage.py collectstatic`

`python manage.py runserver`


### Access the web service

Go to http://localhost:8000/ for the main site

Go to http://localhost:8000/admin/ for the administrator interface, using your previously created super user.



## Deployment to Heroku

### Install Heroku client

This command line interface (CLI) helps to do some tasks related to Heroku. 

You can install this tool following [the official guide](https://devcenter.heroku.com/articles/heroku-cli#download-and-install). 

The main steps are:

1.- For MacOS, install Homebrew and run
`brew install heroku/brew/heroku`

2.- In Ubuntu/Debian based systems, install SnapCraftand run
`sudo snap install --classic heroku`

3.- For windows, download and execute the installer.

### Register your application in Heroku

1.- Create an account in Heroku.com to login (https://signup.heroku.com/)
2.- After registation, go to https://dashboard.heroku.com/
3.- Create a new application using the button [Add] (https://dashboard.heroku.com/new-app)

### Login to Heroku

You need an accout in Heroku.com to login.

`heroku login [--interactive]`

### Asociate your repository with Heroku

Use the **app name** you previously registered in Heroku

`heroku git:remote -a your-app-name`

### Deploy your application

`git push heroku master`

