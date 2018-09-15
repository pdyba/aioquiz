# AioQuiz

AioQuiz is stand alone opensource application for conducting, managing and monitoring the course of programming workshops.

It is written in Python using asynchronous framework Sanic, PostgresSQL and AngularJS

## Requirements
* `apt-get install python3-dev gcc`
* Python 3.5+
* PostgresSQL (instructions below)
* `python3.5 -m pip install -r requirements`


## install and bootstrap PostgresSQL

```bash
apt-get update
sudo apt-get install postgresql postgresql-contrib
sudo adduser aioquiz
sudo -u postgres createuser --interactive
sudo -u postgres createdb aioquizdb
sudo -u postgres psql
alter user aioquiz with encrypted password '<password>';
grant all privileges on database aioquizdb to aioquiz;
```

### using Docker

```bash
docker run --name aioquiz-postgres -e POSTGRES_USER=aiopg -e POSTGRES_PASSWORD=aiopg -e POSTGRES_DB=postgres -p 5432:5432 -d postgres
```

## bootstrap DB

1. Create config_dev or config_prod in config dir basing on config/template.py
2. Edit bottom of bootstrap.py
3. Edit admin adding function in bootstrap.py
4. `python3.5 bootstrap.py` You may need to run it more than once.


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


## backuping DB

### CRON configure 
Add config_scripts/aioquiz_backup.sh to /usr/local/bin/aioquiz_backup.sh
Add config_scripts/logrotate_aioquizdb.conf to /etc/logrotate.d/aioquizdb.conf
`16 10 * * * /usr/local/bin/aioquiz_backup.sh 2>&1 >> /var/log/aioquiz_backup.log`

### Restoring
sudo -u postgres psql aioquizdb < infile
