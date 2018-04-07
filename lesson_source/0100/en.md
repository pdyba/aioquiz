---
title: 'Flask: Quick Start'
---

Flask: Instalation and preparaion
=================================

"Hello world" web application with Flask:

from flask import Flask app = Flask(__name__)

```python
@app.route('/')
def hello_world():
    return 'Hello World!'

if __name__ == '__main__':
    app.run()

    app.run()

```

In virtaual env install: Must: .. code-block:: bash

	>>>  \$ pip install flask \$ pip install flask-login \$ pip install
	>>>  flask-wtf

Optional: \$ pip install flask-sqlalchemy

After let's create the basic folder structure for our application:

```bash
$ mkdir app
$ mkdir app/static
$ mkdir app/templates
$ mkdir tmp

$ mkdir tmp

```

The app folder will be where we will put our application package. The
static sub-folder is where we will store static files like images,
javascripts, and cascading style sheets. The templates sub-folder is
obviously where our templates will go.

Let's start by creating a simple init script for our app package (file
app/main.py):

Flask: Hallo world
==================

"Hello world" web application with Flask:

```python
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

if __name__ == '__main__':
    app.run(debug=True)

    app.run(debug=True)

```

The script above simply creates the application object (of class Flask)
and then imports the views module, which we haven't written yet. Do not
confuse app the variable (which gets assigned the Flask instance) with
app the package (from which we import the views module).

If you are wondering why the import statement is at the end and not at
the beginning of the script as it is always done, the reason is to avoid
circular references, because you are going to see that the views module
needs to import the app variable defined in this script. Putting the
import at the end avoids the circular import error.

The views are the handlers that respond to requests from web browsers or
other clients. In Flask handlers are written as Python functions. Each
view function is mapped to one or more request URLs.

This view is actually pretty simple, it just returns a string, to be
displayed on the client's web browser. The two route decorators above
the function create the mappings from URLs / and /index to this
function.

The final step to have a fully working web application is to create a
script that starts up the development web server with our application:

```python
if __name__ == '__main__':
    app.run(debug=True)

    app.run(debug=True)

```

It simply invokes app run method to start the server. Remember that the
app variable holds the Flask instance that we created it above.

To start the app you just run this script. On OS X, Linux and Cygwin you
have to indicate that this is an executable file before you can run it:

	>>>  python main.py

If You are having probles try:

\$ chmod a+x main.py And You can also run it on Linux and MacOS like
that: ./main.py

After the server initializes it will listen on port 5000 waiting for
connections. Now open up your web browser and enter the following URL in
the address field:

<http://localhost:5000> Alternatively you can use the following URL:

<http://localhost:5000/index> Do you see the route mappings in action?
The first URL maps to /, while the second maps to /index. Both routes
are associated with our view function, so they produce the same result.
If you enter any other URL you will get an error, since only these two
have been defined.

When you are done playing with the server you can just hit Ctrl-C to
stop it.
