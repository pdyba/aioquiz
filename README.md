# AioQuiz

AioQuiz is stand alone opensource application for conducting, managing and monitoring the course of programming workshops.

It is written in Python using asynchronous framework Sanic, PostgresSQL and AngularJS

## Requirements
* `apt-get install python3-dev gcc`
* Python 3.5+
* PostgresSQL (instructions below)
* `python3.5 -m pip install -r requirements`


## install and bootstrap PostgresSQL

apt-get update <br>
sudo apt-get install postgresql postgresql-contrib <br>
adduser aioquiz<br>
sudo -u postgres createuser --interactive<br>
sudo -u postgres createdb aioquizdb<br>

## bootstrap DB

1. Create config_dev or config_prod in config dir basing on config/template.py
2. Edit bottom of bootstrap.py
3. Edit admin adding function in bootstrap.py
4. `python3.5 bootstrap.py`


## build front

###### install node modules
`npm install`

###### build bundle.js
`./build_front.sh`
###### update bundle hash in static/index.html

## run app

`python3.5 aioquiz.py`


## Lets Encrypt Certs:
https://certbot.eff.org/#ubuntuxenial-nginx

    :::bash
    sudo apt-get update
    sudo apt-get install software-properties-common
    sudo add-apt-repository ppa:certbot/certbot
    sudo apt-get update
    sudo apt-get install python-certbot-nginx

`sudo certbot --nginx`

or (no nginx)

`sudo certbot certonly`


Cert refresh for nginx:

`sudo certbot renew --nginx`