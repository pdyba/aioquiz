1.11 SQLAlchemy
=============================================

**SQLAlchemy** - to oprogramowanie do zarządzania bazą danych. Zawiera zestaw narzędzie pozwalający na interakcje z napopularniejszymi bazami danych a także ORM (Object Relational Mapper).
SQLAlchemy jest napisane w Pythonie, jest open source, multiplatformowe i wydane na licencji MIT. 
Najważniejszą cechą jest ORM które pozwala na mapowanie i tworzenie struktury bazy danych na poziomie pythone. 

**ORM** (Mapowanie obiektowo-relacyjne) - sposób odwzorowania obiektowej architektury systemu informatycznego na bazę danych (lub inny element systemu) o relacyjnym charakterze. 

###Instalacja

`pip install sqlalchemy`

W zależności od serwery bazy danych konieczność zainstalowania dodatkowych modułów, na przykład `pip install pymysql`


Uruchomienie developerskiej bazy danych:
`docker run --name pysql -e MYSQL_ROOT_PASSWORD=my-secret-pw -p 3306:3306 -d mysql:5.7`

###SQLAlchemy Core

Core SQLAlchemy zawiera silnik renderujący SQL, integrację DBAPI, integrację transakcji oraz usługi opisu schematu. 
SQLAlchemy używa SQL Expression Language do bezpośredniej interakcji z bazą danych (w odróżnieniu od ORM które działają na wysokim poziomie prezentując warstwę abstrakcji między logiką aplikacji z bazą danych).

Łączenie z bazą:
```python
engine = create_engine("mysql://user:pwd@host/schema", echo = True)
```

Tworzenie tabeli:
```python
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String

engine = create_engine("mysql+pymysql://root:my-secret-pw@127.0.0.1/pysql", echo=True)

meta = MetaData()

students = Table(
   'students', meta,
   Column('id', Integer, primary_key=True),
   Column('name', String(255)),
   Column('lastname', String(255)),
)

meta.create_all(engine)
```

###SQL Expressions:
Wyrażenia służą do wykonywania operacji na baziea danych.

INSERT
```python
ins = students.insert().values(name = 'Karan')
str(ins)
```

'INSERT INTO users (name) VALUES (:name)'

Cały kod na umieszczenie wiersza w bazie danych:
```python
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String

engine = create_engine("mysql+pymysql://root:my-secret-pw@127.0.0.1/pysql", echo=True)

meta = MetaData()

students = Table(
   'students', meta,
   Column('id', Integer, primary_key=True),
   Column('name', String(255)),
   Column('lastname', String(255))
)

ins = students.insert().values(name="Patryk")
conn = engine.connect()
conn.execute(ins)
```
Obiekt meta jest kolekcją zawierającą tabele. 
Tworzymy wyrażenie insert, tworzymy połączenie z bazą a następnie wykonujemy wyrażenie korzystając z połączenia.

SELECT
```python
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String

engine = create_engine("mysql+pymysql://root:my-secret-pw@127.0.0.1/pysql", echo=True)

meta = MetaData()

students = Table(
   'students', meta,
   Column('id', Integer, primary_key=True),
   Column('name', String(255)),
   Column('lastname', String(255))
)

conn = engine.connect()

s = students.select().where(students.c.id > 2)
result = conn.execute(s)

for row in result:
    print(row)
```

UPDATE:
```python
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String

engine = create_engine("mysql+pymysql://root:my-secret-pw@127.0.0.1/pysql", echo=True)

meta = MetaData()

students = Table(
   'students', meta,
   Column('id', Integer, primary_key=True),
   Column('name', String(255)),
   Column('lastname', String(255))
)

conn = engine.connect()
u = students.update().where(students.c.lastname == 'Nowak').values(lastname='Noowak')
conn.execute(u)
```

DELETE
```python
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String

engine = create_engine("mysql+pymysql://root:my-secret-pw@127.0.0.1/pysql", echo=True)

meta = MetaData()

students = Table(
   'students', meta,
   Column('id', Integer, primary_key=True),
   Column('name', String(255)),
   Column('lastname', String(255))
)

conn = engine.connect()
d = students.delete().where(students.c.id == 1)
result = conn.execute(d)
```

Textual SQL
AQLAlchemy pozwala na wykonywanie "czystych" zapytań SQL:
```python
from sqlalchemy import create_engine, text

engine = create_engine("mysql+pymysql://root:my-secret-pw@127.0.0.1/pysql", echo=True)

s = text("SELECT * FROM students where lastname = :last")

conn = engine.connect()
result = conn.execute(s, last='Wieczorek')

for row in result:
    print(row)
```

Przykład stworzenia nowego schematu z użyciem tekstowego zapytania:
```python
from sqlalchemy import create_engine, text

engine = create_engine("mysql+pymysql://root:my-secret-pw@127.0.0.1", echo=True)

s = text('CREATE SCHEMA schema_name')
conn = engine.connect()
conn.execute(s)
```

Przy wykonywaniu takich zapytań należy pamiętać o bindowaniu parametrów (jeśli są) zamiast wklejaniu ich bezpośrednio do zapytania SQL aby uniknąć ataków SQL Injection 

Pełna dokumentacja: https://docs.sqlalchemy.org/en/14/

### ORM

ORM pozwala mapować klasy/obiekty na tabele/wiersze bazy danych

Mapowanie klas:
```python
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine("mysql+pymysql://root:my-secret-pw@127.0.0.1/pysql", echo=True)

Base = declarative_base()


class Customers(Base):
    __tablename__ = 'customers'

    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    address = Column(String(255))
    email = Column(String(100))


Base.metadata.create_all(engine)
```
`declarative_base` zwraca bazową klasę do klas korzystających z ORM.


Tworzenie obiektów
```python
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


engine = create_engine("mysql+pymysql://root:my-secret-pw@127.0.0.1/pysql", echo=True)

Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()


class Customers(Base):
    __tablename__ = 'customers'

    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    address = Column(String(255))
    email = Column(String(100))


customer = Customers(name="Jan", address="Address", email="email@example.com")

session.add(customer)
session.commit()
```

Wyciąganie obiektów
```python
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


engine = create_engine("mysql+pymysql://root:my-secret-pw@127.0.0.1/pysql", echo=True)

Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()


class Customers(Base):
    __tablename__ = 'customers'

    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    address = Column(String(255))
    email = Column(String(100))


result = session.query(Customers).all()

for customer in result:  # type: Customers
    print(f"{customer.name} {customer.address} {customer.email}")
```

Zapytania można filtrować za pomocą funkcji `filter()` na przykład:
```python
result = session.query(Customers).filter(Customers.address == "Address")
```

Wykonanie zapytań może odbyć się za pomocą kliku funkcji:
- `all()` - Zwróci listę wszystkich obiektów spełniających kryteria

- `first()` - Zwróci jeden obiekt spełniający kryteria

- `one()` - Zwróci jeden obiekt spełniający kryteria lub błąd jeśli będzie istniało więcej obiektów spełniających kreteria

Edycja obiektów
```python
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


engine = create_engine("mysql+pymysql://root:my-secret-pw@127.0.0.1/pysql", echo=True)

Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()


class Customers(Base):
    __tablename__ = 'customers'

    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    address = Column(String(255))
    email = Column(String(100))


result = session.query(Customers).first()
result.name = "Marcin"
session.commit()
```

Przy operacjach na obiektach istniejących już w bazie danych nie ma konieczności używania funkcji `session.add()`

Relacje
```
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

engine = create_engine("mysql+pymysql://root:my-secret-pw@127.0.0.1/pysql", echo=True)

Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()


class Customer(Base):
    __tablename__ = 'customers'

    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    address = Column(String(255))
    email = Column(String(100))


class Invoice(Base):
    __tablename__ = 'invoices'

    id = Column(Integer, primary_key=True)
    custid = Column(Integer, ForeignKey('customers.id'))
    invno = Column(Integer)
    amount = Column(Integer)
    customer = relationship("Customer", back_populates="invoices")


Customer.invoices = relationship("Invoice", order_by=Invoice.id, back_populates="customer")
Base.metadata.create_all(engine)
```

Korzystanie z relacji:
```python
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

engine = create_engine("mysql+pymysql://root:my-secret-pw@127.0.0.1/pysql", echo=True)

Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()


class Customer(Base):
    __tablename__ = 'customers'

    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    address = Column(String(255))
    email = Column(String(100))


class Invoice(Base):
    __tablename__ = 'invoices'

    id = Column(Integer, primary_key=True)
    custid = Column(Integer, ForeignKey('customers.id'))
    invno = Column(Integer)
    amount = Column(Integer)
    customer = relationship("Customer", back_populates="invoices")


Customer.invoices = relationship("Invoice", order_by=Invoice.id, back_populates="customer")

c1 = Customer(name="Marcin", address="Address", email="email@example.com")
c1.invoices = [Invoice(invno=10, amount=15000), Invoice(invno=14, amount=3850)]

session.add(c1)
session.commit()
```

SQLAlchemy pozwala realizować relacje `One To Many`, `Many To One`, `One to One`, `Many to Many`

Pełna dokumentacja: https://docs.sqlalchemy.org/en/14/
