1.12 SQLAlchemy i projekty
===========================

SQL
---

ang. Structured Query Language

* język deklaratywny
* język strukturalny
* język zapytań używany do CRUD -  tworzenia, modyfikowania baz danych oraz do umieszczania i pobierania danych z baz danych.


ORM
---
ang. Object-Relational Mapping ORM
Mapowanie obiektowo-relacyjne – sposób odwzorowania obiektowej architektury systemu informatycznego na bazę danych.

Podstawowym zastosowanniem jest tworzenie systemów opartych o programowanie obiektowe, a gdzie system bazy danych operuje na relacjach.

ORM może negatywnie wpływać na wydajność systemu, niezoptyamlizowane zapytania.

SQLAlchemy
----------

SQLAlchemy to biblioteka ORM, która daje twórcom aplikacji pełną moc i elastyczność SQL.

Zapewnia pełny zestaw dobrze znanych wzorców utrwalania na poziomie przedsiębiorstwa,
zaprojektowanych z myślą o wydajnym dostępie do baz danych, dostosowanym do specyfikacji języka Python.

Tworzenie modelu
----------------

Model - system założeń, pojęć i zależności między nimi pozwalający opisać (modelować) w przybliżony sposób jakiś aspekt rzeczywistości.

```python
from sqlalchemy import Column
from sqlalchemy.types import Integer
from sqlalchemy.types import String
from sqlalchemy.types import Boolean

from main import db

class User(db.Model):
    """
    User model for reviewers.
    """
    __tablename__ = 'user'
    id = Column(Integer, autoincrement=True, primary_key=True)
    active = Column(Boolean, default=True)
    email = Column(String(200), unique=True)
    password = Column(String(200), default='')
    admin = Column(Boolean, default=False)
```

Skrypt, który stworzy nam bazę danych we właściwej bazie danych:

```python
from sqlalchemy import create_engine

from main import db
import models

def db_start():
    create_engine('sqlite:///tmp/test.db', convert_unicode=True)
    db.create_all()
    db.session.commit()

if __name__ == '__main__':
    db_start()


    db_start()
```

Zapisywanie
-----------

Aby nasze zmiany stały się pernamentne musimy wynik naszych działań zapisać po ich naniesieniu.
Ważne: pobierając, nie trzeba tej komendy wykonywać. Przed dodaniem nowego wpisu trzeba będzie dodać też `db.session.add(<klasa>)`

```python
db.session.commit()
```

C - tworzenie
--------------

```python
from views import User

user = User()

user.active = True
user.email = 'piotr@pylove.org'
user.password = 'PiotrMaK0d@'
user.admin = True

db.session.add(user)
db.session.commit()
```

R - Wyciąganie po ID, wyszukiwanie
----------------------------------

```python

user = User.query.filter_by(email='piotr@pylove.org').first()
admins = User.query.filter_by(admin=True).all()
admins = User.query.filter_by(admin=True).order_by(User.email.asc()).all()
admins = User.query.filter_by(admin=True).order_by(User.email.desc()).all()
user_1 = User.query.get(1)
```

U - updatowanie
---------------

```python
user_1 = User.query.get(1)
user_1.password = "KotP@dl!"
db.session.commit()
```

D - Usuwanie
------------

```python
user_1 = Order.query.get(1)
db.session.delete(user_1)
db.session.commit()
```

Przykład main.py
----------------

```python
from os import path

from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy()
db.app = app
db.init_app(app)
lm = LoginManager()
lm.init_app(app)
bcrypt = Bcrypt()

app.static_path = path.join(path.abspath(__file__), 'static')


if __name__ == '__main__':
    from views import *
    app.run(debug=True)
    app.run(debug=True)
```

