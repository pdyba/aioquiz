---
title: 'Flask: Templates'
---

Why we need templates
=====================

Let's consider how we can expand our little application.

We want the home page of our app to have a heading that welcomes the
logged in user, that's pretty standard for applications of this kind.
Ignore for now the fact that we have no way to log a user in, I'll
present a workaround for this issue in a moment.

An easy option to output a nice and big heading would be to change our
view function to output HTML, maybe something like this:

```python3
@app.route('/')
@app.route('/index')
def index():
    user = {'nickname': 'Martha'}  # fake user
    return '''
<html>
  <head>
    <title>Home Page</title>
  </head>
  <body>
    <h1>Hello, ''' + user['nickname'] + '''</h1>
  </body>
</html>
'''

'''

```

Give the application a try to see how this looks in your browser.

Since we don't have support for users yet I have resorted to using a
placeholder user object, sometimes called fake or mock object. This
allows us to concentrate on certain aspects of our application that
depend on parts of the system that haven't been built yet.

I hope you agree with me that the solution used above to deliver HTML to
the browser is very ugly. Consider how complex the code will become if
you have to return a large and complex HTML page with lots of dynamic
content. And what if you need to change the layout of your web site in a
large app that has dozens of views, each returning HTML directly? This
is clearly not a scalable option.

Templates to the rescue
=======================

If you could keep the logic of your application separate from the layout
or presentation of your web pages things would be much better organized,
don't you think? You could even hire a web designer to create a killer
web site while you code the site's behaviors in Python. Templates help
implement this separation.

Let's write our first template file app/templates/index.html:

```html
<html>
  <head>
    <title>{{ title }} - App</title>
  </head>
  <body>
      <h1>Hello, {{ user.nickname }}!</h1>
  </body>
</html>

</html>

```

As you see above, we just wrote a mostly standard HTML page, with the
only difference that there are some placeholders for the dynamic content
enclosed in {{ ... }} sections.

Now let's see how we use this template from our view function (file
app/views.py):

from flask import render_template

```python3
from flask import render_template

@app.route('/')
@app.route('/index')
def index():
    user = {'nickname': 'Martha'}  # fake user
    return render_template('index.html', title='Home', user=user)

    return render_template('index.html', title='Home', user=user)

```

Try the application at this point to see how the template works. Once
you have the rendered page in your browser you may want to view the
source HTML and compare it against the original template.

To render the template we had to import a new function from the Flask
framework called render_template. This function takes a template
filename and a variable list of template arguments and returns the
rendered template, with all the arguments replaced.

Under the covers, the render_template function invokes the Jinja2
templating engine that is part of the Flask framework. Jinja2
substitutes {{...}} blocks with the corresponding values provided as
template arguments.

Control statements in templates
===============================

The Jinja2 templates also support control statements, given inside
{%...%} blocks. Let's add an if statement to our template (file
app/templates/index.html):

```html
<html>
  <head>
    {% if title %}
    <title>{{ title }} - App</title>
    {% else %}
    <title>Welcome to The App</title>
    {% endif %}
  </head>
  <body>
      <h1>Hello, {{ user['nickname'] }}!</h1>
  </body>
</html>

</html>

```

Now our template is a bit smarter. If the view function forgets to
define a page title then instead of showing an empty title the template
will provide its own title. Feel free to remove the title argument in
the render_template call of our view function to see how the
conditional statement works.

Loops in templates
==================

The logged in user in our App application will probably want to see some
lists, so let's see how we can do that.

Lets thing about a blog in that case.

```python3
from flask import render_template

@app.route('/')
@app.route('/index')
def index():
    user = {'nickname': 'Martha'}  # fake user
    posts = [  # fake array of posts
        {
            'author': {'nickname': 'John'},
            'title': 'Beautiful day in Poznan!',
            'body': 'Very random text about Poznan!'
        },
        {
            'author': {'nickname': 'Susan'},
            'title': 'The Avengers movie was so cool!',
            'body': 'Long random text about the movie!'
        }
    ]
    return render_template("index.html", title='Home', user=user, posts=posts)

    return render_template("index.html", title='Home', user=user, posts=posts)

```

To represent user posts we are using a list, where each element has
author and body fields. When we get to implement a real database we will
preserve these field names, so we can design and test our template using
the fake objects without having to worry about updating it when we move
to a database.

On the template side we have to solve a new problem. The list can have
any number of elements, it will be up to the view function to decide how
many posts need to be presented. The template cannot make any
assumptions about the number of posts, so it needs to be prepared to
render as many posts as the view sends.

So let's see how we do this using a for control structure (file
app/templates/index.html):

```html
<html>
  <head>
    {% if title %}
    <title>{{ title }} - App</title>
    {% else %}
    <title>Welcome to the App</title>
    {% endif %}
  </head>
  <body>
    <h1>Hi, {{ user.nickname }}!</h1>

    {% for post in posts %}
    <div>
    <p>{{ post.author.nickname }} writs article with title: <b>{{ post.title }}</b></p></div>
    {% endfor %}

  </body>
</html>

</html>

```

Simple, right? Give it a try, and be sure to play with adding more
content to the posts array.

Template inheritance
====================

Our web application will need to have a navigation bar at the top of the
page with a few links. Here you will get the link to edit your profile,
to login, logout, etc.

We can add a navigation bar to our index.html template, but as our
application grows we will be needing to implement more pages, and this
navigation bar will have to be copied to all of them. Then you will have
to keep all these identical copies of the navigation bar in sync, and
that could become a lot of work if you have a lot of pages and
templates.

Instead, we can use Jinja2's template inheritance feature, which allows
us to move the parts of the page layout that are common to all templates
and put them in a base template from which all other templates are
derived.

So let's define a base template that includes the navigation bar and
also the bit of title logic we implemented earlier (file
app/templates/_base.html):

```html
<html>
  <head>
    {% if title %}
    <title>{{ title }} - App</title>
    {% else %}
    <title>Welcome to the App</title>
    {% endif %}
  </head>
  <body>
    <div>Microblog: <a href="/index">Home</a></div>
    <hr>

    {% block content %}
    {% endblock %}

  </body>
</html>

</html>

```

In this template we use the block control statement to define the place
where the derived templates can insert themselves. Blocks are given a
unique name, and their content can be replaced or enhanced in derived
templates.

And now what's left is to modify our index.html template to inherit from
_base.html (file app/templates/index.html):

```html
{% extends "_base.html" %}
{% block content %}
    <h1>Hi, {{ user.nickname }}!</h1>
    {% for post in posts %}
    <div><p>{{ post.author.nickname }} says: <b>{{ post.body }}</b></p></div>
    {% endfor %}
{% endblock %}

{% endblock %}

```

Since the _base.html template will now take care of the general page
structure we have removed those elements from this one and left only the
content part. The extends block establishes the inheritance link between
the two templates, so that Jinja2 knows that when it needs to render
index.html it needs to include it inside base.html. The two templates
have matching block statements with name content, and this is how Jinja2
knows how to combine the two into one. When we get to write new
templates we will also create them as extensions to _base.html.
