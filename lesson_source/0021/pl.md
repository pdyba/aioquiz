1.3 Aplikacje internetowe
=========================

Co to jest aplikacja internetowa?
---------------------------------

Aplikacja internetowa to zaawansowana strona internetowa. Większość rzeczy nazywanych stronami internetowymi jest de facto aplikacjami. Przykłady aplikacji internetowych:

* YouTube
* Facebook
* Allegro

### Różnice między stroną a aplikacją

Strona internetowa:

* Wyświetla informacje wprowadzone przez autora strony
* Nie wymaga backendu, tylko pliki HTML, CSS, ew. JavaScript

Aplikacja internetowa:

* Umożliwia również wprowadzanie danych przez użytkowników
* Wymaga napisania backendu (np. w Pythonie)

Komponenty aplikacji internetowej
---------------------------------

### Frontend

Interfejs wyświetlany w przeglądarce. Języki używane do tworzenia frontendu to:

* HTML – struktura i zawartość strony
* CSS – wygląd strony
* JavaScript – zachowanie strony

### Backend

Odpowiada za:

* Przetwarzanie zapytań z frontendu
* Zadania wymagające dużej mocy obliczeniowej
* Kontakt z bazą danych
* Uwierzytelnianie, autoryzację
* Generowanie i wypełnianie frontendu (zależnie od architektury)

Do napisania backendu można wykorzystać różne języki, m. in. Python.

Jak napisać aplikację internetową?
----------------------------------

Do napisania aplikacji internetowej potrzebujemy bibliotekę (tzw. framework). W Pythonie mamy różne opcje, m. in.:

* Django
* Flask
* CherryPy
* Falcon
* Sanic

My będziemy używać Flaska.

Metody HTTP
-----------

Metoda to słowo określające rodzaj operacji jaką chcemy wykonać. Jego interpretacja zależy całkowicie od autora aplikacji.

Najważniejsze metody:

* GET - domyślna metoda używana przez przeglądarki, służy do pobierania danych
* POST - służy do zmiany danych na serwerze

Flask
-----

Strona biblioteki: [http://flask.pocoo.org/](http://flask.pocoo.org/)

Tutorial: [http://flask.pocoo.org/docs/0.12/quickstart/](http://flask.pocoo.org/docs/0.12/quickstart/)

Instalacja:

```bash
pip install Flask

pip install Flask

```

### Aplikacja startowa

```python
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

app.run(debug=True)

app.run(debug=True)

```

### Parametry

```python
@app.route("/hello/<name>")
def welcome(name):
    return "Welcome {}!".format(name)

    return "Welcome {}!".format(name)

```

### Metoda POST

```python
from flask import Flask, request

app = Flask(__name__)

saved = "Data"

@app.route("/save", methods=["POST"])
def save():
    global saved
    data = request.get_json()
    saved = data["value"]
    return "Saved {}".format(data["value"])

@app.route("/read", methods=["GET"])
def read():
    return saved

app.run(debug=True)

app.run(debug=True)

```

### Program testowy

```python
import requests

save_result = requests.post(
    'http://localhost:5000/save',
    json={'value': 'witam'}
)
print(save_result.text)

read_result = requests.get('http://localhost:5000/read')
print(read_result.text)

print(read_result.text)

```

Zadania
-------

Uwaga - jeśli np. zadanie 3b zaczyna się od wielokropka znaczy to, że należy w zadany sposób zmodyfikować aplikację z podpunktu 3a.

### Podpowiedzi do zadań

Najpierw spróbujcie znaleźć rozwiązanie sami ;)

* 1b - [http://flask.pocoo.org/docs/0.12/quickstart/#variable-rules](http://flask.pocoo.org/docs/0.12/quickstart/#variable-rules)
* 3c - [https://docs.python.org/3.6/library/uuid.html](https://docs.python.org/3.6/library/uuid.html)
* 6 - [http://flask.pocoo.org/docs/0.12/quickstart/#redirects-and-errors](http://flask.pocoo.org/docs/0.12/quickstart/#redirects-and-errors)
