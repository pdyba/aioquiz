---
title: 'Flask: Forms'
---

Configuration
=============

To handle our web forms we are going to use the Flask-WTF extension,
which in turn wraps the WTForms project in a way that integrates nicely
with Flask apps.

Many Flask extensions require some amount of configuration, so we are
going to setup a configuration file inside our root app folder so that
it is easily accessible if it needs to be edited. Here is what we will
start with (file config.py):

```python
WTF_CSRF_ENABLED = True
SECRET_KEY = 'you-will-never-guess'

SECRET_KEY = 'you-will-never-guess'

```

Pretty simple, it's just two settings that our Flask-WTF extension
needs. The WTF_CSRF_ENABLED setting activates the cross-site request
forgery prevention (note that this setting is enabled by default in
current versions of Flask-WTF). In most cases you want to have this
option enabled as it makes your app more secure.

The SECRET_KEY setting is only needed when CSRF is enabled, and is used
to create a cryptographic token that is used to validate a form. When
you write your own apps make sure to set the secret key to something
that is difficult to guess.

Now that we have our config file we need to tell Flask to read it and
use it. We can do this right after the Flask app object is created, as
follows (file app/main.py):

from flask import Flask

```python
app = Flask(__name__)
app.config.from_object('config')

app.config.from_object('config')

```

The user login form
===================

Web forms are represented in Flask-WTF as classes, subclassed from base
class Form. A form subclass simply defines the fields of the form as
class variables.

Now we will create a login form that users will use to identify with the
system. The login mechanism that we will support in our app is the
standard username/password type.

Let's write our first form:

```python
from wtforms import Form
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired

class LoginForm(Form):
username = StringField(
    "description",
)
password = PasswordField(
    "password",
)

)

```

I believe the class is pretty much self-explanatory. We imported the
Form class, and the two form field classes that we need, StringField and
BooleanField.

The DataRequired import is a validator, a function that can be attached
to a field to perform validation on the data submitted by the user. The
DataRequired validator simply checks that the field is not submitted
empty. There are many more validators included with Flask-WTF, we will
use some more in the future.

Form templates
==============

We will also need a template that contains the HTML that produces the
form. The good news is that the LoginForm class that we just created
knows how to render form fields as HTML, so we just need to concentrate
on the layout. Here is our login template (file
app/templates/login.html):

```html
<!-- extend from base layout -->
{% extends "base.html" %}

{% block content %}
  <h1>Sign In</h1>
  <form action="" method="post" name="login">
      {{ form.hidden_tag() }}
      <p>
          Please enter your Login:<br>
          {{ form.username }}<br>
          and Password:<br>
          {{ form.password }}<br>
      </p>
      <p><input type="submit" value="Sign In"></p>
  </form>
{% endblock %}

{% endblock %}

```

Note that in this template we are reusing the base.html template through the extends template inheritance statement.

:   We will actually do this with all our templates, to ensure a
consistent layout across all pages.

There are a few interesting differences between a regular HTML form and
our template. This template expects a form object instantiated from the
form class we just defined stored in a template argument named form. We
will take care of sending this template argument to the template next,
when we write the view function that renders this template.

The form.hidden_tag() template argument will get replaced with a hidden
field that implements the CSRF prevention that we enabled in the
configuration. This field needs to be in all your forms if you have CSRF
enabled. The good news is that Flask-WTF handles it for us, we just need
to make sure it is included in the form.

The actual fields of our form are rendered by the field objects, we just
need to refer to a {{form.field_name}} template argument in the place
where each field should be inserted. Some fields can take arguments.
Since we have not defined the submit button in the form class we have to
define it as a regular field. The submit field does not carry any data
so it doesn't need to be defined in the form class.

Form views
==========

The final step before we can see our form is to code a view function
that renders the template.

This is actually quite simple since we just need to pass a form object
to the template. Here is our new view function:

```python
@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm(request.form)
    return render_template('login.html', form=form)

    return render_template('login.html', form=form)

```

So basically, we have imported our LoginForm class, instantiated an
object from it, and sent it down to the template. This is all that is
required to get form fields rendered.

Let's ignore for now the flash and redirect imports. We'll use them a
bit later.

The only other thing that is new here is the methods argument in the route decorator.

:   This tells Flask that this view function accepts GET and POST
requests. Without this the view will only accept GET requests. We
will want to receive the POST requests, these are the ones that will
bring in the form data entered by the user.

At this point you can try the app and see the form in your web browser.
After you start the application you will want to open
<http://localhost:5000/login> in your web browser, as this is the route
we have associated with the login view function.

We have not coded the part that accepts data yet, so pressing the submit
button will not have any effect at this time.

Receiving form data
===================

Another area where Flask-WTF makes our job really easy is in the handling of the submitted form data.

:   Here is an updated version of our login view function that validates
and stores the form data:

```python
@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm(request.form)
    if request.method == 'POST' and form.validate():
        user = User.query.filter_by(
            username=request.form['username']).first()
        if user is not None and bcrypt.check_password_hash(
                user.password, request.form['password']
        ):
            login_user(user)
            flash('Hi {}{} ! You were logged in. Go Crazy.'.format(
                user.username[0].upper(), user.username[1:]
            ))
            return redirect(url_for('overview'))
        else:
            flash('Invalid username or password.')
    return render_template('login.html', form=form)

    return render_template('login.html', form=form)

```

The validate_on_submit method does all the form processing work. If
you call it when the form is being presented to the user (i.e. before
the user got a chance to enter data on it) then it will return False, so
in that case you know that you have to render the template.

When validate_on_submit is called as part of a form submission
request, it will gather all the data, run all the validators attached to
fields, and if everything is all right it will return True, indicating
that the data is valid and can be processed. This is your indication
that this data is safe to incorporate into the application.

If at least one field fails validation then the function will return
False and that will cause the form to be rendered back to the user, and
this will give the user a chance to correct any mistakes. We will see
later how to show an error message when validation fails.

When validate_on_submit returns True our login view function calls two
new functions, imported from Flask. The flash function is a quick way to
show a message on the next page presented to the user. In this case we
will use it for debugging, since we don't have all the infrastructure
necessary to log in users yet, we will instead just display a message
that shows the submitted data. The flash function is also extremely
useful on production servers to provide feedback to the user regarding
an action.

The flashed messages will not appear automatically in our page, our
templates need to display the messages in a way that works for the site
layout. We will add these messages to the base template, so that all our
templates inherit this functionality. This is the updated base template
(file app/templates/_base.html):

```html
<html>
  <head>
    {% if title %}
    <title>{{ title }} - App</title>
    {% else %}
    <title>App</title>
    {% endif %}
  </head>
  <body>
    <div>Microblog: <a href="/index">Home</a></div>
    <hr>
    {% with messages = get_flashed_messages() %}
      {% if messages %}
        <ul>
        {% for message in messages %}
            <li>{{ message }} </li>
        {% endfor %}
        </ul>
      {% endif %}
    {% endwith %}
    {% block content %}{% endblock %}
  </body>
</html>

</html>

```

The technique to display the flashed message is hopefully
self-explanatory. One interesting property of flash messages is that
once they are requested through the get_flashed_messages function they
are removed from the message list, so these messages appear in the first
page requested by the user after the flash function is called, and then
they disappear.

The other new function we used in our login view is redirect. This
function tells the client web browser to navigate to a different page
instead of the one requested. In our view function we use it to redirect
to the index page we developed in previous chapters. Note that flashed
messages will display even if a view function ends in a redirect.

This is a great time to start the app and test how the form works. Make sure you

:   try submitting the form with the username field empty, to see how
the DataRequired validator halts the submission process.

Improving field validation
==========================

With the app in its current state, forms that are submitted with invalid
data will not be accepted. Instead, the form will be presented back to
the user to correct. This is exactly what we want.

```python
from wtforms import Form
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired

class LoginForm(Form):
username = StringField(
    "description",
    validators=[validators.DataRequired('Please enter your name.')],
)
password = PasswordField(
    "password",
    validators=[validators.DataRequired('Please enter your password.')],
)

)

```

What we are missing is an indication to the user of what is wrong with
the form. Luckily, Flask-WTF also makes this an easy task.

When a field fails validation Flask-WTF adds a descriptive error message
to the form object. These messages are available to the template, so we
just need to add a bit of logic that renders them.

Here is our login template with field validation messages (file
app/templates/login.html):

```html
<!-- extend base layout -->
{% extends "base.html" %}

{% block content %}
  <h1>Sign In</h1>
            {% for error in form.errors %}
            <span style="color: red;">[{{ error }}]</span>
          {% endfor %}<br>
  <form action="" method="post" name="login">
      {{ form.hidden_tag() }}
      <p>
          Please enter your Login:<br>
          {{ form.username }}<br>
          and Password:<br>
          {{ form.password }}<br>
      </p>
      <p><input type="submit" value="Sign In"></p>
  </form>
{% endblock %}

{% endblock %}

```

The only change we've made is to add a for loop that renders any
messages added by the validators below the field. As a general rule, any
fields that have validators attached will have errors added under
form.field_name.errors. In our case we use form.errors. We display
these messages in a red style to call the user's attention.
