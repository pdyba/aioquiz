1.8 HTML, szablony stron
========================

Frontend
--------

Frontend to wszystko, co widać w przeglądarce. Języki obsługiwane przez przeglądarkę to:

* HTML – struktura strony,
* CSS – wygląd strony,
* JavaScript – zachowanie strony,
* Java, Flash - zabytki.

HTML – elementy i znaczniki
---------------------------

* Elementy tworzą strukturę dokumentu HTML,
* Znaczniki oznaczają początek i koniec elementu,
* Znaczniki:
* `<p>` - znacznik otwierający,
* `</p>` - znacznik zamykający,
* `<p />` - znacznik oznaczający pusty element.
* Atrybuty – umieszczone w znaczniku dodatkowe informacje o elemencie:
* `<img src="cat_image.png">` - atrybut `src` o wartości `cat_image.jpg`,
* `<table border>` - atrybut `border` nie posiadający wartości.

### Elementy

* Elementy:
* `<p>Treść akapitu</p>` - akapit
* `<br />` - nowa linia
* W dokumentach HTML często spotyka się elementy bez znacznika zamykającego:
* `<br>` - też nowa linia

### Zagnieżdżanie elementów

Przykład - akapit zawierający listę

```html
<p>
  Przykładowa lista
  <ul>
    <li>Element 1
    <li>Element 2
  </ul>
</p>

</p>

```

### Podstawowa struktura HTML

```html
<!DOCTYPE html>
<html>
  <head>
    <meta charset="UTF-8">
    <title>Tytuł strony</title>
  </head>
  <body>
  
  </body>
</html>

</html>

```

Element `<title>` zawiera tytuł strony wyświetlany przez przeglądarkę jako nazwa karty.<br>
Element `<body>` ma zawierać całą właściwą treść strony - na dzisiejszych zajęciach wszystko będziemy umieszczać właśnie tam.

### Podstawowe elementy

* `<p>Akapit</p>`
* `<h1>Duży nagłówek</h1>`
* `<h2>Trochę mniejszy nagłówek</h2>`
* ...
* `<h6>Najmniejszy nagłówek</h6>`
* `<br>` - nowa linia (uwaga – zwykłe entery są ignorowane przez przeglądarki!)
* `<hr>` - pozioma linia

#### Lista numerowana

```html
<ol>
  <li>Element 1</li>
  <li>Element 2</li>
</ol>

</ol>

```

#### Lista nienumerowana

```html
<ul>
  <li>Element 1</li>
  <li>Element 2</li>
</ul>

</ul>

```

#### Obrazki

```html
<img src="cat_image.jpg" width="200" height="200">

<img src="cat_image.jpg" width="200" height="200">

```

* `src` - nazwa pliku z obrazkiem, musi być w tym samym folderze co plik strony,
* `width`, `height` - szerokość i wysokość obrazka (opcjonalne).

#### Linki

```html
<a href="https://www.python.org/">Strona Pythona</a>

<a href="https://www.python.org/">Strona Pythona</a>

```

* `href` - adres docelowy linku. Jeśli zaczniemy go od `/` - będzie oznaczać adres w aktualnie wyświetlanej stronie
(np. jeśli nasza strona to `www.sluchamjazzu.pl` to link o adresie `/podstrona` będzie prowadził do adresu
`www.sluchamjazzu.pl/podstrona`).

#### Tabele

```html
<table border>
  <tr>
    <th>Imię</th>
    <th>Nazwisko</th>
  </tr>
  <tr>
    <td>Hiromi</td>
    <td>Uehara</td>
  </tr>
</table>

</table>

```

* `<table>` - nadrzędny element oznaczający tabelę. Atrybut `border` powoduje dodanie ramki do tabeli
* `<tr>` - wiersz tabeli
* `<td>` - komórka tabeli
* `<th>` - komórka nagłówkowa - od zwykłej różni się głównie pogrubioną czcionką

### Pełny przykład

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Przykładowa strona</title>
</head>
<body>
    <h1>To jest przykładowa strona</h1>
    Ta strona zawiera:
    <p>Przykładowy akapit</p>
    <p>Oraz drugi akapit<br>z wstawioną nową linią w środek</p>
    <ol>
        <li>Listę</li>
        <li>numerowaną</li>
    </ol>
    <a href="https://pylove.org">Link do strony PyLove</a>
    <table border>
        <tr>
            <th>Oraz</th>
            <th>Przykładową</th>
        </tr>
        <tr>
            <td>Tabelkę</td>
            <td>z kilkoma</td>
        </tr>
        <tr>
            <td>wierszami</td>
            <td></td>
        </tr>
    </table>
</body>
</html>

</html>

```

### Przykład tabeli do zadania 2.

<table border>
<tr><th>Col 1</th><th>Col 2</th></tr>
<tr><td colspan="2">Wide cell</td></tr>
<tr><td>Cell 1</td><td>Cell 2</td></tr>
</table>

Renderowanie szablonów
----------------------

W aplikacji internetowej często będziemy chcieli utworzyć fragment pliku HTML na podstawie, na przykład, danych z bazy.
Wtedy potrzebujemy szablonu HTML – specjalnego pliku HTML, zawierającego informacje, gdzie wkleić dane.
Nasza aplikacja (czyli Flask) będzie renderować ten szablon, czyli uzupełniać go podanymi informacjami.
Szablony dla Flaska tworzymy przy pomocy języka biblioteki Jinja2: [http://jinja.pocoo.org/docs/2.10/templates/](http://jinja.pocoo.org/docs/2.10/templates/)

### Specjalne elementy szablonu

<code ng-non-bindable>{{ zmienna }}</code> - w tym miejscu umieść wartość zmiennej zmienna.<br>
Wewnątrz <code ng-non-bindable>{{ }}</code> można używać wielu poleceń pythonowych, np.:

* <code ng-non-bindable>{{ liczba + 5 }}</code>
* <code ng-non-bindable>{{ slownik['klucz'] }}</code>

### if

{% if zmienna == 1 %}
    zmienna ma wartość 1
{% else %}
    zmienna ma inną wartość
{% endif %}

### for

{% for element in kolekcja %}
    <p>{{ element }}</p>
{% endfor %}

Jeśli `kolekcja` jest listą `['Queen', 'Pink Floyd']`, to efektem będzie:

<p>Queen</p>
<p>Pink Floyd</p>

### Przykład

#### Backend

```python
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/zespoly")
def lista_zespolow():
    return render_template(
        'zespoly.html',
        naglowek='Zespoły',
        zespoly=['Pink Floyd', 'Queen', 'Led Zeppelin'],
        link=True
    )

app.run(debug=True)

app.run(debug=True)

```

#### Szablon - zespoly.html

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Zespoły</title>
</head>
<body>
    <h1>{{ naglowek }}</h1>
    <ol>
        {% for zespol in zespoly %}
            <li>{{ zespol }}</li>
        {% endfor %}
    </ol>
    {% if link %}
        <a href="//pylove.org">PyLove</a>
    {% endif %}
</body>
</html>

### Uwagi

* Wcięcia, nowe linie itp. nie mają znaczenia w szablonach,
* Szablon musi znajdować się w folderze `templates`, czyli jeśli nasza aplikacja jest w ścieżce 
`C:\projekt\aplikacja.py`, to szablon musi być w ścieżce `C:\projekt\templates\szablon.html`

Formularze
----------

Formularz to fragment strony umożliwiający użytkownikowi wprowadzenie informacji i wysłanie ich do serwera.
Umożliwia wysyłanie zapytań GET i POST.
W przypadku zapytania GET wprowadzone dane trafią do query stringa (np. `http://example.com/search?query=tekst`).
W przypadku zapytania POST dane trafią do treści zapytania, której nie widać w adresie URL.

### Przykład formularza

```html
<form action="/search" method="get">
  <input type="text" name="query">
  <button type="submit">Wyślij</button>
</form>

</form>

```

* `action` oznacza ścieżkę, do której chcemy wysłać zapytanie,
* `method` oznacza metodę (get / post),
* `name` w elemencie `input` to nazwa parametru, do którego trafi wartość wprowadzona przez użytkownika.

### Obsługa formularza w aplikacji

* Dane przesłane w zapytaniu GET znajdą się w zmiennej `request.args` (ta zmienna jest słownikiem),
* W przypadku zapytania POST dane znajdą się w zmiennej `request.form` (która również jest słownikiem).

### Przykład - GET

#### Backend

```python
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/search", methods=['GET'])
def search():
    query = request.args.get('query')
    return render_template('formularz.html', query=query)

app.run(debug=True)

app.run(debug=True)

```

#### Szablon - formularz.html

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Formularz</title>
</head>
<body>
    {% if query %}
        Przesłano {{ query }}
    {% endif %}
    <form action="/search" method="get">
        <input type="text" name="query">
        <button type="submit">Wyślij</button>
    </form>
</body>
</html>
