# AioQuiz

AioQuiz is stand alone opensource application for conducting, managing and monitoring the course of programming workshops.

It is written in Python using asynchronous framework Sanic, PostgresSQL and AngularJS

## Requirements

* Python 3.5+
* PostgresSQL
* `python3.5 -m pip install -r requirements`


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
