1.5 Programowanie obiektowe
===========================

Programowanie obiektowe
-----------------------
Paradygmat programowania, w którym programy definiuje się za pomocą obiektów (dane i metody), komunikujących się pomiędzy sobą w celu wykonywania zadań.
W klasycznym rozumieniu składa się z:
* Abstrakcji,
* Hermetyzacji,
* Polimorfizmu,
* Dziedziczenia.

Abstrakcja
----------
Pewnego rodzaju uproszczenie rozpatrywanego problemu, polegające na ograniczeniu zakresu cech manipulowanych obiektów wyłącznie do cech kluczowych.

Cel stosowania abstrakcji jest dwojaki: ułatwienie rozwiązania problemu i zwiększenie jego ogólności.

Dziedziczenie
-------------
Mechanizm współdzielenia funkcjonalności między klasami. Klasa może dziedziczyć po innej klasie, co oznacza, że oprócz swoich własnych atrybutów oraz zachowań, uzyskuje także te pochodzące z klasy, z której dziedziczy. Klasa dziedzicząca jest nazywana klasą potomną (subclass), zaś klasa, z której następuje dziedziczenie — klasą bazową (superclass). Z jednej klasy bazowej można uzyskać dowolną liczbę klas pochodnych. Klasy pochodne posiadają obok swoich własnych metod i pól, również kompletny interfejs klasy bazowej

Przykład: wyobraźmy sobie klasę `But`, która posiada dwie właściwości `rozmiar` i `sezon`. Po `Bucie` dziedziczą m.in. klasy `Trampek` i `Kozak`. Każdy z nich będzie miał swój `rozmiar`, ale w przeciwieństwie do klasy `But` będą miały różne `sezony` (lato, zima).

Hermetyzacja
------------
(inaczej enkapsulacja) Zapewnia, że obiekt nie może zmieniać stanu wewnętrznego innych obiektów w nieoczekiwany sposób. Tylko własne metody obiektu są uprawnione do zmiany jego stanu. Każdy typ obiektu prezentuje innym obiektom swój interfejs, który określa dopuszczalne metody współpracy.

Hermetyzacja polega na ukrywaniu pewnych danych składowych lub metod obiektów danej klasy tak, aby były one dostępne tylko metodom wewnętrznym danej klasy lub funkcjom zaprzyjaźnionym.

w Pythonie **nie** istnieje pełna hermetyzacja, w klasycznym tego rozumieniu. Każdą daną czy funkcję w klasie możemy nadpisać.

w Pythonie popularną konwencją jest używanie _ do oddzielenia metod zwykłych od **prywatnych** i **magicznych**.

* metodą magiczną, którą powszechnie będziemy używać jest `__init__` czyli tak zwany konstruktor klasy (więcej o metodach magicznych na kolejnych zajęciach)
* metody prywatne mają na celu oddzielić zewnętrzny interfejs programistyczny (API) od wewnętrznych funkcji klasy. Wykorzystuje się to, aby ukryć część operacyjną logiki, która nie jest potrzebna z zewnątrz, ale w Pythonie nadal jest dostępna.

Polimorfizm
-----------
Referencje i kolekcje obiektów mogą dotyczyć obiektów różnego typu, a wywołanie metody dla referencji spowoduje zachowanie odpowiednie dla pełnego typu obiektu wywoływanego.

Polimorfizm to możliwość stosowania tego samego kodu dla obiektów różnych typów. Czyli jeśli mam jakiś reużywalny kod (czyli z reguły funkcję), który działa jednocześnie dla danych typu A i danych typu B.

**Przykład:**
jeśli mamy klasę `Figura` (geometryczna) z metodą `policz_pole` to po odziedziczeniu po tej klasie przez klasy `Trójkąt` i `Kwadrat`, mimo zmiany wzoru liczącego na obu obiektach będzie można wykonać tą metodę.

Instancja
---------
Pojedyncze wystąpienie niezależnego kodu zgodnego z danym wzorcem.
Instancjowanie klas, czyli tworzenie obiektów - niezależnych bytów danej klasy.

Klasa w Pythonie
----------------

Do tworzenia klas w Pythonie wykorzystujemy słówko `class`.
Słówko `self` jest pewną abstrakcją dotyczą stworzonej później instancji klasy.

```python
class Creature:
    alive = True  # atrybut

    def is_live(self):  # metoda - czyli funkcja przypisana do klasy
        print('I am alive')

```

Tworzenie instancji
-------------------

Nasza przykładowa klasa:

```python
class Creature:
    alive = True

    def is_live(self):
        print('I am alive')

    def is_dead(self):
        if self.alive:
            self.live()
            return True
        print('I am dead')
        return False

    def kill(self):
        alive = False

```

Nasze przykładowe instancje i ich używanie:

```python
pies = Creature()
kot = Creature()
kot.kill()
pies.is_dead()
kot.is_dead()
```

Przykład w Pythonie
-------------------

```python
class Creature:
    alive = True

    def is_live(self):
        print('I am alive')

    def is_dead(self):
        if self.alive:
            self.live()
            return True
        print('I am dead')
        return False

    def kill(self):
        alive = False

class Animal(Creature):
    def eat(self):
        print('chrum chrum')

class Manmal(Animal):
    def __init__(self, sex):
        self.sex = sex

    def give_milk(self):
        print('Giving some milk')

    def drink_milk(self):
        print('Gulp gulp')

class Cow(Manmal):
    def __init__(self, sex, name):
        super().__init__(sex) # super wyzwale metodę odziedziczoną mimo tej samej nazwy metody
        self.name = name

    def give_milk(self):
        if self.sex == 'female':
            print(self.name + ' ', end='')
            super().give_milk() # super wyzwale metodę odziedziczoną mimo tej samej nazwy metody
        else:
            print('Nope, impossible')
```

Przykład zastosowania:

```python
nasza_obora = [
    Cow('female', 'Puszka'),
    Cow('female', 'Pastuszka'),
    Cow('female', 'Laciata'),
    Cow('male', 'Mordor'),
    Cow('male', 'Potter'),
    Cow('male', 'Byczek'),
]
for krowa in nasza_obora:
    krowa.give_milk()

from random import choice
choice(nasza_obora).kill()
choice(nasza_obora).kill()

for krowa in nasza_obora:
    if not krowa.is_dead():
        print(krowa.name)
```

Zadanie:
Zaimplementuj metody opisane w zadaniach. Na koniec zajęć klasy powinny być zaimplementowane w zbliżony sposób.

```python
class Czlowiek:
    def __init__(self):
        pass

    def speak(self):
        pass

    def count_bmi(self):
        pass

    def diff_to_norm(self):
        pass

    def save_data(self):
        pass

    def to_burn(self):
        pass

    def to_eat(self):
        pass

    def what_to_do(self):
        pass

class Polityk(Czlowiek):    
    def speak(self):
        pass

    def recive_bribe(self):
        pass
```

