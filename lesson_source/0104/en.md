---
title: 'Flask: SQL Alchemy - ORM'
---

Databases in Flask
==================

We will use the Flask-SQLAlchemy extension to manage our application.
This extension provides a wrapper for the SQLAlchemy project, which is
an Object Relational Mapper or ORM.

ORMs allow database applications to work with objects instead of tables
and SQL. The operations performed on the objects are translated into
database commands transparently by the ORM. Knowing SQL can be very
helpful when working with ORMs, but we will not be learning SQL in this
tutorial, we will let Flask-SQLAlchemy speak SQL for us.

Migrations
==========

Typically you end up having to delete the old database and create a new
one each time you need to make updates, losing all the data. And if the
data cannot be recreated easily you may be forced to write export and
import scripts yourself.

Luckily, we have a much better option.

We are going to use SQLAlchemy-migrate to keep track of database updates
for us. It adds a bit of work to get a database started, but that is a
small price to pay for never having to worry about manual database
migrations.

Configuration
=============

For our little application we will use a sqlite database. The sqlite
databases are the most convenient choice for small applications, as each
database is stored in a single file and there is no need to start a
database server.

We have a couple of new configuration items to add to our config file
(file config.py):

```python3
import os
basedir = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')
The SQLALCHEMY_DATABASE_URI is required by the Flask-SQLAlchemy extension. This is the path of our database file.

The SQLALCHEMY_DATABASE_URI is required by the Flask-SQLAlchemy extension. This is the path of our database file.

```

The SQLALCHEMY_MIGRATE_REPO is the folder where we will store the
SQLAlchemy-migrate data files.

Finally, when we initialize our app we also need to initialize our
database. Here is our updated package init file (file app/main.py):

```python3
from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)

Note the two changes we have made to our init script. We are now creating a db object that will be our database, and we are also importing a new module called models. We will write this module next.

Note the two changes we have made to our init script. We are now creating a db object that will be our database, and we are also importing a new module called models. We will write this module next.

```

The database model
==================

The data that we will store in our database will be represented by a
collection of classes that are referred to as the database models. The
ORM layer will do the translations required to map objects created from
these classes into rows in the proper database table. The id field is
usually in all models, and is used as the primary key. Each user in the
database will be assigned a unique id value, stored in this field.
Luckily this is done automatically for us, we just need to provide the
id field. The nickname and email fields are defined as strings (or
VARCHAR in database jargon), and their maximum lengths are specified so
that the database can optimize space usage.

```python3
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nickname = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)

    email = db.Column(db.String(120), index=True, unique=True)

```

The User class that we just created contains several fields, defined as
class variables. Fields are created as instances of the db.Column class,
which takes the field type as an argument, plus other optional arguments
that allow us, for example, to indicate which fields are unique and
indexed.

Creating the database
=====================

With the configuration and model in place we are now ready to create our
database file. The SQLAlchemy-migrate package comes with command line
tools and APIs to create databases in a way that allows easy updates in
the future, so that is what we will use. I find the command line tools a
bit awkward to use, so instead lets write our own set of little Python
scripts that invoke the migration APIs.

Here is a script that creates the database (file db_create.py):

```python3
from migrate.versioning import api
from config import SQLALCHEMY_DATABASE_URI, SQLALCHEMY_MIGRATE_REPO
from app import db
import os.path
db.create_all()
if not os.path.exists(SQLALCHEMY_MIGRATE_REPO):
    api.create(SQLALCHEMY_MIGRATE_REPO, 'database repository')
    api.version_control(SQLALCHEMY_DATABASE_URI, SQLALCHEMY_MIGRATE_REPO)
else:
    api.version_control(SQLALCHEMY_DATABASE_URI, SQLALCHEMY_MIGRATE_REPO, api.version(SQLALCHEMY_MIGRATE_REPO))

    api.version_control(SQLALCHEMY_DATABASE_URI, SQLALCHEMY_MIGRATE_REPO, api.version(SQLALCHEMY_MIGRATE_REPO))

```

Note how this script is completely generic. All the application specific
pathnames are imported from the config file. When you start your own
project you can just copy the script to the new app's directory and it
will work right away.

	>>>  python db_create.py

After you run the command you will have a new app.db file. This is an
empty sqlite database, created from the start to support migrations. You
will also have a db_repository directory with some files inside. This
is the place where SQLAlchemy-migrate stores its data files. Note that
we do not regenerate the repository if it already exists. This will
allow us to recreate the database while leaving the existing repository
if we need to.

Our first migration Now that we have defined our model, we can
incorporate it into our database. We will consider any changes to the
structure of the app database a migration, so this is our first, which
will take us from an empty database to a database that can store users.

To generate a migration I use another little Python helper script (file
db_migrate.py):

```python3
import imp
from migrate.versioning import api
from app import db
from config import SQLALCHEMY_DATABASE_URI, SQLALCHEMY_MIGRATE_REPO
v = api.db_version(SQLALCHEMY_DATABASE_URI, SQLALCHEMY_MIGRATE_REPO)
migration = SQLALCHEMY_MIGRATE_REPO + ('/versions/%03d_migration.py' % (v+1))
tmp_module = imp.new_module('old_model')
old_model = api.create_model(SQLALCHEMY_DATABASE_URI, SQLALCHEMY_MIGRATE_REPO)
exec(old_model, tmp_module.__dict__)
script = api.make_update_script_for_model(SQLALCHEMY_DATABASE_URI, SQLALCHEMY_MIGRATE_REPO, tmp_module.meta, db.metadata)
open(migration, "wt").write(script)
api.upgrade(SQLALCHEMY_DATABASE_URI, SQLALCHEMY_MIGRATE_REPO)
v = api.db_version(SQLALCHEMY_DATABASE_URI, SQLALCHEMY_MIGRATE_REPO)
print('New migration saved as ' + migration)
print('Current database version: ' + str(v))

print('Current database version: ' + str(v))

```

The script looks complicated, but it doesn't really do much. The way
SQLAlchemy-migrate creates a migration is by comparing the structure of
the database (obtained in our case from file app.db) against the
structure of our models (obtained from file app/models.py). The
differences between the two are recorded as a migration script inside
the migration repository. The migration script knows how to apply a
migration or undo it, so it is always possible to upgrade or downgrade a
database format.

While I have never had problems generating migrations automatically with
the above script, I could see that sometimes it would be hard to
determine what changes were made just by comparing the old and the new
format. To make it easy for SQLAlchemy-migrate to determine the changes
I never rename existing fields, I limit my changes to adding or removing
models or fields, or changing types of existing fields. And I always
review the generated migration script to make sure it is right.

It goes without saying that you should never attempt to migrate your
database without having a backup, in case something goes wrong. Also
never run a migration for the first time on a production database,
always make sure the migration works correctly on a development
database.

So let's go ahead and record our migration:

	>>>  db_migrate.py

And the output from the script will be: New migration saved as
db_repository/versions/001_migration.py Current database version: 1
The script shows where the migration script was stored, and also prints
the current database version. The empty database version was version 0,
after we migrated to include users we are at version 1.

Database upgrades and downgrades By now you may be wondering why is it
that important to go through the extra hassle of recording database
migrations.

Imagine that you have your application in your development machine, and
also have a copy deployed to a production server that is online and in
use.

Let's say that for the next release of your app you have to introduce a
change to your models, for example a new table needs to be added.
Without migrations you would need to figure out how to change the format
of your database, both in your development machine and then again in
your server, and this could be a lot of work.

If you have database migration support, then when you are ready to
release the new version of the app to your production server you just
need to record a new migration, copy the migration scripts to your
production server and run a simple script that applies the changes for
you. The database upgrade can be done with this little Python script
(file db_upgrade.py):

```python3
from migrate.versioning import api
from config import SQLALCHEMY_DATABASE_URI
from config import SQLALCHEMY_MIGRATE_REPO
api.upgrade(SQLALCHEMY_DATABASE_URI, SQLALCHEMY_MIGRATE_REPO)
v = api.db_version(SQLALCHEMY_DATABASE_URI, SQLALCHEMY_MIGRATE_REPO)
print('Current database version: ' + str(v))

print('Current database version: ' + str(v))

```

When you run the above script, the database will be upgraded to the
latest revision, by applying the migration scripts stored in the
database repository.

It is not a common need to have to downgrade a database to an old
format, but just in case, SQLAlchemy-migrate supports this as well (file
db_downgrade.py):

```python3
from migrate.versioning import api
from config import SQLALCHEMY_DATABASE_URI
from config import SQLALCHEMY_MIGRATE_REPO
v = api.db_version(SQLALCHEMY_DATABASE_URI, SQLALCHEMY_MIGRATE_REPO)
api.downgrade(SQLALCHEMY_DATABASE_URI, SQLALCHEMY_MIGRATE_REPO, v - 1)
v = api.db_version(SQLALCHEMY_DATABASE_URI, SQLALCHEMY_MIGRATE_REPO)
print('Current database version: ' + str(v))

print('Current database version: ' + str(v))

```

This script will downgrade the database one revision. You can run it
multiple times to downgrade several revisions. There is also Alembic
library for managing migrations.

Database relationships
======================

Relational databases are good at storing relations between data items.
Consider the case of a user writing a blog post. The user will have a
record in the users table, and the post will have a record in the posts
table. The most efficient way to record who wrote a given post is to
link the two related records.

Once a link between a user and a post is established there are two types
of queries that we may need to use. The most trivial one is when you
have a blog post and need to know what user wrote it. A more complex
query is the reverse of this one. If you have a user, you may want to
know all the posts that the user wrote. Flask-SQLAlchemy will help us
with both types of queries.

Our posts table will have the required id, the body of the post and a
timestamp. Not much new there. But the user_id field deserves an
explanation.

We said we wanted to link users to the posts that they write. The way to
do that is by adding a field to the post that contains the id of the
user that wrote it. This id is called a foreign key. Our database design
tool shows foreign keys as a link between the foreign key and the id
field of the table it refers to. This kind of link is called a
one-to-many relationship, one user writes many posts.

Let's modify our models to reflect these changes:

```python3
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nickname = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    posts = db.relationship('Post', backref='author', lazy='dynamic')


class Post(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    body = db.Column(db.String(140))
    timestamp = db.Column(db.DateTime)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

```

We have added the Post class, which will represent blog posts written by
users. The user_id field in the Post class was initialized as a foreign
key, so that Flask-SQLAlchemy knows that this field will link to a user.

Note that we have also added a new field to the User class called posts,
that is constructed as a db.relationship field. This is not an actual
database field, so it isn't in our database diagram. For a one-to-many
relationship a db.relationship field is normally defined on the "one"
side. With this relationship we get a user.posts member that gets us the
list of posts from the user. The first argument to db.relationship
indicates the "many" class of this relationship. The backref argument
defines a field that will be added to the objects of the "many" class
that points back at the "one" object. In our case this means that we can
use post.author to get the User instance that created a post. Don't
worry if these details don't make much sense just yet, we'll see
examples of this at the end of this article.

Let's record another migration with this change. Simply run:

	>>>  python db_migrate.py

And the script will respond:

New migration saved as db_repository/versions/002_migration.py Current
database version: 2 It isn't really necessary to record each little
change to the database model as a separate migration, a migration is
normally only recorded at significant points in the history of the
project. We are doing more migrations than necessary here only to show
how the migration system works.

Play time
=========

We have spent a lot of time defining our database, but we haven't seen
how it works yet. Since our app does not have database code yet let's
make use of our brand new database in the Python interpreter.

This brings our database and models into memory and then let's create a
new user:

	>>>  from app import db, models >>> u =
	>>>  models.User(nickname='john', <email='john@email.com>') >>>
	>>>  db.session.add(u) >>> db.session.commit()

Changes to a database are done in the context of a session. Multiple
changes can be accumulated in a session and once all the changes have
been registered you can issue a single db.session.commit(), which writes
the changes atomically. If at any time while working on a session there
is an error, a call to db.session.rollback() will revert the database to
its state before the session was started. If neither commit nor rollback
are issued then the system by default will roll back the session.
Sessions guarantee that the database will never be left in an
inconsistent state.

Let's add another user:

	>>>  u = models.User(nickname='susan',
	>>>  <email='susan@email.com>') >>> db.session.add(u) >>>
	>>>  db.session.commit() >>>

Now we can query what our users are:

	>>>  users = models.User.query.all() >>> users
	>>>  [<User u'john'>, <User u'susan'>] >>> for u in
	>>>  users: ... print(u.id,u.nickname) ... 1 john 2 susan >>>

For this we have used the query member, which is available in all model
classes. Note how the id member was automatically set for us.

Here is another way to do queries. If we know the id of a user we can
find the data for that user as follows:

	>>>  u = models.User.query.get(1) >>> u <User
	>>>  u'john'>>>

Now let's add a blog post:

	>>>  import datetime >>> u = models.User.query.get(1)
	>>>  p = models.Post(body='my first post!',
	>>>  timestamp=datetime.datetime.utcnow(), author=u) >>>
	>>>  db.session.add(p) >>> db.session.commit()

Here we set our timestamp in UTC time zone. All timestamps stored in our
database will be in UTC. We can have users from all over the world
writing posts and we need to use uniform time units. In a future
tutorial we will see how to show these times to users in their local
timezone.

You may have noticed that we have not set the user_id field of the Post
class. Instead, we are storing a User object inside the author field.
The author field is a virtual field that was added by Flask-SQLAlchemy
to help with relationships, we have defined the name of this field in
the backref argument to db.relationship in our model. With this
information the ORM layer will know how to complete the user_id for us.

To complete this session, let's look at a few more database queries that
we can do:

	>>>  # get all posts from a user >>> u = models.User.query.get(1)
	>>>  u <User u'john'>>> posts = u.posts.all()
	>>>  posts [<Post u'my first post!'>]
>
	>>>  # obtain author of each post >>> for p in posts: ...
	>>>  print(p.id,p.author.nickname,p.body) ...

1 john my first post!

	>>>  # a user that has no posts >>> u = models.User.query.get(2)
	>>>  u <User u'susan'>>> u.posts.all() []
>
	>>>  # get all users in reverse alphabetical order >>>
	>>>  models.User.query.order_by('nickname').all() [<User u'susan'>,
	>>>  <User u'john'>] >>>

The Flask-SQLAlchemy documentation is the best place to learn about the
many options that are available to query the database.

Before we close, let's erase the test users and posts we have created:

	>>>  users = models.User.query.all() >>> for u in
	>>>  users: ... db.session.delete(u) ... >>> posts =
	>>>  models.Post.query.all() >>> for p in posts: ...
	>>>  db.session.delete(p) ... >>> db.session.commit()

Of course we can use that in scripts
