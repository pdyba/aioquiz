1.6 Programowanie obiektowe II
===========================

Konwencje nazewnictwa klas w Pythonie
-------------------------------------

W Pythonie popularną konwencją jest używanie:

* `_` do nazw metod, zmiennych **prywatnych**,
* `__` po obu stronach nazwy, do metod **magicznych**,
* funkcje zaczynające się od słowa **is** albo **has** (is in) powinny zwracać wartość boolowską (True/False),
* funkcje zaczynające się od słowa **get** powinny zwracać wartość,
* funkcje zaczynające się od słowa **set** powinny ustawiać wartość, dobrą praktyką jest też walidowanie wejścia.

Metody i zmienne prywatne
-------------------------

Ich celem jest "ukrycie" zmiennych i metod pomocniczych w klasie.
Metody prywatne są przydatne do dzielenia zadań na mniejsze części lub do zapobiegania powielaniu kodu, który jest często potrzebny innym metodom w klasie, ale nie powinien być wywoływany poza tą klasą.

Pomyśl o klasie jako o czymś widzianym z zewnątrz, a nie o czymś, co widzisz wewnętrznie.
Na przykład zegarek: może podać informacje o bieżącym czasie i można go ustawić tak, aby wskazywał właściwy czas - metody publiczne.
Prywatne służą tutaj do ukrycia matematyki, czyli dlaczego po 23. jest godzina 0., czy po 59. minucie minuta zerowa.

Popularnym przykładem zmiennej prywatnej są różnego rodzaju mapowania, np. cyfr na ich słowne odpowiedniki czyli 57 to jest zestawienie "pięćdziesiąt" i "siedem" - domyślnie interfejs zwróci "pięćdziesiąt siedem", mimo że w samej klasie zostanie to wzięte np. z dwóch kluczy dla 50 i dla 7.

Metody magiczne
---------------

Prawie wszystko w Pythonie jest obiektem - wyjątkami są słówka, m.in. `class`, `def`, `is`, `in` itp. 
Za to wbudowane funkcje jak np. `str()`, `len()` czy nawet znaki matematyczne (`+`, `-`, `/`, `*`, etc.)
i znaki porównujące (`<`, `>`, `==`, etc). są tak naprawdę wywoływaniami funkcji magicznych:

* `str()` ukrywa się w pod `__str__`,
* `len()` ukrywa się w pod `__len__`,
* `+` ukrywa się w pod `__add__`,
* `*` ukrywa się w pod `__mul__`,
* `<` ukrywa się w pod `__lt__` (less than).

Jedną z najważniejszych metod jest `__init__`, którą poznaliśmy na poprzednich zajęciach - konstruktor.

Są też inne ciekawe atrybuty, na przykład:

* `__doc__` - w której jest przechowywana dokumentacja.

Jednym z najbardziej specyficznych atrybutów jest  `__name__`, który jest dostępny dla klas, ale nie ich instancji domyślnie.
Np. możemy zrobić `print(str.__name__)` lub `print(MojaKlasa.__name__)`,
ale już dla instancji to samo np. `print('xxx'.__name__)` nie zadziała.
To są tak zwane atrybuty klasowe - aby je udostępnić w instancjach,
musimy dodać metodę z **dekoratorem** `@classmethod`. 

Mówiąc o klasach i dekoratorach trzeba też wspomnieć o `@staticmethod`, 
który pozwala nam posiadać w klasie metody, które nie potrzebują instancji, żeby ich używać.

Dekorator
---------

W dużym skrócie jest to funkcja, która **otacza** inną funkcję, metodę lub klasę i może zmieniać jej wynik.
O dekoratorach powiemy jeszcze później. Na razie będą istotne dla nas dwa wymienione wcześniej: `@classmethod` oraz `@staticmethod`

Prosty dekorator w Pythonie wygląda tak:

```python3
@dekorator  # zaczyna się od znaku @ a po nim jest jego nazwa
def funkcja(arg):
    print(arg)

    print(arg)

```

W przypadku naszych dwóch istotnych dekoratorów związanych z klasami używamy je w sposób następujący:

```python3
@dekorator  # zaczyna się od znaku @ a po nim jest jego nazwa
class MojaKlasa:
    def normalna_metoda(self):
        pass

    @classmethod
    def klasowa_metoda(cls):  # cls jest zwyczajowym słowem - skrót od słowa class
        return cls.__name__

    @staticmethod
    def statyczna_metoda():  # nie wymaga ani instancji (self) ani klasy (cls)
        print('no hej')

        print('no hej')

```

classmethod
-----------

Metody klasowe są stosowane, gdy potrzebujemy metod, które nie są specyficzne dla żadnej konkretnej instancji, 
ale nadal angażują klasę w jakiś sposób.

staticmethod
------------

Metody statyczne są używane bardziej dla porządku: 
jeżeli mamy metodę, która mogłaby pozostać funkcją, ale nigdzie poza daną klasą nie jest używana,
warto pozostawić ją w danej klasie jako metodę statyczną.

*args
-----

Kolejne zmienne pozycyjne, które są przekazywane do funkcji jako **krotka(ang.tuple)**. Może być ich dowolna liczba.

```python3
def test_args(an_arg, *args):
    print("first normal arg: {}".format(an_arg))
    for arg in args:
        print("another arg: {}".format(arg))

test_args('foo','python','bar','test')

test_args('foo','python','bar','test')

```

Tak zwany proces rozpakowywania argumentów możemy też sami wymusić na krotkach (ang.tuple), listach i setach.

```python3
x = ('foo','python','bar','test')
y = ['foo','python','bar','test']
z = {'foo','python','bar','test'}  # set, czyli nieuporządkowana lista bez powtórzeń
test_args(*x)
test_args(*y)
test_args(*z)

test_args(*z)

```

Możemy też wykorzystać do tego słownik, ale wtedy pod `*s` znajdą się tylko klucze słownika.

```python3
s = {'foo': 1,'python': 2,'bar': 3,'test': 4}
test_args(*s)

test_args(*s)

```

**kwargs
--------

Kolejne zmienne o określonej nazwie (kluczu), które są przekazane do funkcji jako **słownik**. 
Może być ich dowolna liczba.

```python3
def test_kwargs(klucz="brak", **kwargs):
    print("klucz: {}".format(klucz))
    for key, val in kwargs.items():
        print("another kwarg {}: {}".format(key, val))

test_kwargs(foo=bar, python=test)

test_kwargs(foo=bar, python=test)

```

Tak jak w przypadku rozpakowywania argumentów pozycyjnych, możemy też rozpakowywać argumenty kluczowe:

```python3
s = {'foo': 1,'python': 2,'bar': 3,'test': 4}
test_kwargs(**s)

test_kwargs(**s)

```

*args i **kwargs
----------------

"Pełna wersja" def - tworzenia funkcji/metod:

```python3
def funkcja(arg_1, *args, kwarg_1=None, **kwargs):
    print(arg_1)
    print(args)
    print(kwarg_1)
    print(kwargs)

    print(kwargs)

```

Zastosowanie tego jest szczególnie użyteczne w przypadku dziedziczenia:

```python3
class Ojciec:
    def __init__(self, imie, nazwisko, data_ur):
        self.imie = imie
        self.nazwisko = nazwisko
        self.data_ur = data_ur

class Syn(Ojciec):
    def __init__(self, imie_tata, imie_mama, nazwisko_panienskie, *args, plec='male', **kwargs):
        super().__init__(*args, **kwargs)
        self.imie_tata = imie_tata
        self.imie_mama = imie_mama
        self.nazwisko_panienskie = nazwisko_panienskie
        self.plec = plec

        self.plec = plec

```

Do zadań:
---------

```python3
class Czas:
    def __init__(self):
        pass

    def __str__(self):
        pass

    def set_time(self):
        pass

    def add_time(self):
        pass

    def get_seconds(self):
        pass

    def get_minutes(self):
        pass

    def get_hours(self):
        pass

class Zegar:
    pass

class DokładnyZegar:
    pass


def mojprint():
    pass
    pass
```

