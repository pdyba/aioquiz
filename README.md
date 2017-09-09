# aioquiz

AioQuiz is stand alone opensource platform for Lesson and quiz execution.

It is written in Python using asynchronous framework Sanic, PostgresSQL and AngularJS

## Requirements

* Python 3.5+
* PostgresSQL

python3.5 -m pip install -r requirements


## bootstrap DB

1. Edit bottom of bootstrap.py
2. Edit admin adding function ;)
3. python3.5 bootstrap.py


## build front

###### install node modules
`npm install`

###### build bundle.js
`./build_front.sh`
###### update bundle hash in static/index.html

