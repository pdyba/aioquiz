1.17 Systemy kolejkowe i bazy danych NOSQL
==========================================

System Kolejkowy - Message Queue
--------------------------------

Zwany też Kolejką komunikatów, jak nazwa wskazuje służy do kolejkowania kolejnych zadań, operacji w sposób asynchroniczny co oznacza,
że odbiorca (konsumer) i nadawca wiadomości (producent) nie muszą łączyć się z kolejką w tym samym czasie.
System kolejkowy używa kolejek do przesyłania wiadomości, do przekazywania sterowania lub danych.
Może być również wykorzystywany wewnętrznie do komunikacji międzyprocesowej lub do międzywątkowej komunikacji.
Większość aplikacji czasu rzeczywistego takich jak czaty opiera się często na systemie kolejkowym. Systemy MQ często są też wykorzystywane do
przetwarzania danych, tesktowych, graficznych itp. Ze względu na to iż ten proces mógłbym zająć więcej niż użytkownik jest skłonny czekać na wynik.

RabbitMQ - RMQ
--------------

Jeden z najbardziej popularnych systemów kolejkowych napisany w języku Erlang, który znany jest ze swojej wydajności,
zwłaszcza w kwestii przetwarzania równoległego i rozproszonego.

docker
------

https://store.docker.com/editions/community/docker-ce-desktop-windows
https://download.docker.com/kitematic/Kitematic-Windows.zip

instalacja RabbitMQ na docker
-----------------------------

![image](./images/docker_rmq_1.PNG)
![image](./images/docker_rmq_2.PNG)
![image](./images/docker_rmq_3.png)

instalacja bezpośrednio na systemie
-----------------------------------

https://www.rabbitmq.com/download.html

biblioteka Pythonowa
--------------------

`pip install pika`

dokumentacja
------------

https://pika.readthedocs.io

Consumer Pythonowy
------------------

```python
import pika

def on_message(channel, method_frame, header_frame, body):
    print(method_frame.delivery_tag)
    print(body)
    channel.basic_ack(delivery_tag=method_frame.delivery_tag)

parameters = pika.URLParameters('amqp://guest:guest@localhost:32785/%2f')

connection = pika.BlockingConnection(parameters)
channel = connection.channel()
channel.basic_consume(on_message, 'test_que')
try:
    channel.start_consuming()
except KeyboardInterrupt:
    channel.stop_consuming()
connection.close()

connection.close()
```

Producer Pythonowy
------------------

```python
import pika

parameters = pika.URLParameters('amqp://guest:guest@localhost:32785/%2f')
connection = pika.BlockingConnection(parameters)
channel = connection.channel()
channel.basic_publish(
    'test_exchange',
    'test_routing_key',
    'message body value',
    pika.BasicProperties(
        content_type='text/plain',
        delivery_mode=1
    )
)

connection.close()

connection.close()

```

Bazy danych - Not Only SQL
--------------------------

Bazy NoSQL to bazy danych o wysokiej wydajności oparte - w przeciwieństwie do baz relacyjnych - o organizację danych w dokumenty,
grafy, pary klucz-wartość lub kolumny.

MongoDB
-------

Database - baza danych to fizyczny kontener, MongoDB z reguły zawiera wiele z nich.

Collection - jest to kolekcja dokumentów, odpowiednik tabeli w SQL. Wiele kolekcji może być w jednej bazie.

Document - coś a'la JSON, czyli zbiór zestawień klucz-wartość, o dynamicznym schemacie.

instalacja MongoDB na docker
----------------------------

![image](./images/docker_mongo.PNG)

instalacja bezpośrednio na systemie
-----------------------------------

https://www.mongodb.com/download-center?jmp=homepage#community

biblioteka Pythonowa
--------------------

pip install pymongo

dokumentacja
------------

https://api.mongodb.com/python/current/tutorial.html

CRUD
----

```python
from pymongo import MongoClient

host = 'localhost'
port = 32769
# podłączenie do serwera
client = MongoClient(host, port)
# wybranie bazy danych
db = client['pylove_db']
# wybranie kolekcji
collection = db['pylove_col']

# losowe dane:
post = {
    "author_id": 1,
    "subject": "My first subject post!",
    "text": "My first blog post!",
    "tags": ["mongodb", "python", "pymongo"],
    "date": {
        'created': "wczoraj"
    }
}
post_b = {
    "author_id": 2,
    "subject": "My B subject post!",
    "text": "My B blog post!",
    "tags": ["mongodb"],
    "date": {
        'created': "dzisiaj"
    }
}

# Create
post_id = collection.insert_one(post).inserted_id

collection.insert_many([post, post_b])

# Read - Search
a_post_1 = collection.find_one({"author_id": 1})

a_post_2 = collection.find_one({"_id": post_id})

for pst in collection.find({"author_id": 1}):
    print(pst)
# Update
collection.update_one(
    {
        '_id': post_id
    },
    {
        '$set': {  # ustalenie wartosci
            'author_id': 1,
            'date.created': "po jutrze"
        }
    },
    upsert=False)

collection.update_one(
    {
        '_id': post_id
    },
    {
        '$inc': {  # inkrementacja
            'author_id': 1
        }
    },
    upsert=False)

# Delete
collection.DeleteOne(
    {
        '_id': post_id
    }
)

# Count
collection.count()
collection.find({"author_id": 1}).count()
collection.find({"author_id": 1}).count()
```

