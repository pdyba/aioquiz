Jak wytłumaczyć wężowi, o czym mówimy, czyli typy danych: znakowy, liczbowy i boolowski
======================================================================================

Pythonowe typy przechowywania danych
====================================

Python ma pięć podstawowych typów danych:
- Liczba
- String
- Lista
- Tupla
- Słownik

Używaliśmy już liczb (całkowitych int i zmiennoprzecinkowych float), stringów i tupli. Nadszedł czas, by poznać
listy i słowniki.

'Słodki Kłólik'

Dziewczynka idzie do sklepu ze zwierzątkami domowymi i pyta o kłólika.
Sprzedawca pochyla się nad nią, uśmiecha i pyta:

"Chciałabyś ślicznego puszystego białego króliczka,
czy słodkiego kudłatego brązowego króliczka?"

"Właściwie", odpowiada dziewczynka, "Nie sądzę, by mój pyton zauważył różnicę."

A teraz wracajmy do nauki :)

Tytulik jakiś fajny
====================================

Wprowadźmy dwie nowe funkcje:

```python
>>> help(int)
Help on class int in module builtins:
<BLANKLINE>
class int(object)
|  int(x=0) -> integer
|  int(x, base=10) -> integer
|
|  Convert a number or string to an integer, or return 0 if no arguments
|  are given.  If x is a number, return x.__int__().  For floating point
|  numbers, this truncates towards zero.
|
|  ...
```

oraz

```python
>>> help(float)  # doctest: +NORMALIZE_WHITESPACE
Help on class float in module builtins:
<BLANKLINE>
class float(object)
|  float(x) -> floating point number
|
|  Convert a string or number to a floating point number, if possible.
|
|  ...
```

Funkcja help nie waha się poinformować nas, że w rzeczywistości int i float
nie są funkcjami, ale klasami (będzie o tym mowa później), stąd dowiadujemy się
dodatkowo, że możemy ich użyć również do wielu innych rzeczy. W tej chwili
jednak potrzebujemy tylko ich podstawowej funkcjonalności - przekształcania
stringów w liczby określonego typu.

Przetestujmy int i float:

```python
>>> int("0")
0
>>> int(" 63 ")
63
>>> int("60.5")
Traceback (most recent call last):
File "<stdin>", line 1, in <module>
ValueError: invalid literal for int() with base 10: '60.5'
>>> float("0")
0.0
>>> float(" 63 ")
63.0
>>> float("60.5")
60.5
```

Zanim użyjemy w naszym programie funkcji, których właśnie się nauczyliśmy,
zaplanujmy, jak powinien on działać:

1.  Zapytaj użytkownika o wzrost.
2.  Uzyskaj string od użytkownika i zachowaj go pod nazwą `height`.
3.  Przekształć string z liczbą w liczbę z ułamkiem.
4.  Poproś użytkownika o wprowadzenie wagi.
5.  Uzyskaj string od użytkownika i zachowaj go pod nazwą `weight`.
6.  Przekształć string z liczbą w liczbę z ułamkiem.
7.  Oblicz BMI, wykorzystując zapamiętane wartości i zachowaj wynik jako `bmi`.
8.  Wyświetl obliczone BMI.

Nie powinno nas dziwić, że te osiem punktów może być wprost
przetłumaczone na osiem wierszy naszego programu (nie licząc spacji):


```python
print("Wprowadź wzrost w metrach:")
height = input()
height = float(height)

print("Wprowadź wagę w kilogramach:")
weight = input()
weight = float(weight)

bmi = weight / (height**2) #oblicz BMI
print("Twoje BMI wynosi:", bmi)
```

Możecie zapisać program do `bmi.py` i uruchomić `python bmi.py`. Rezultat
powinien wyglądać następująco:


Wprowadź wzrost w metrach:
1.75
Wprowadź wagę w kilogramach:
65.5
Twoje BMI wynosi: 21.387755102040817


Podsumowując, aby wywołać funckję, musimy znać jej nazwę (do tej pory
nauczyliśmy się szeregu funkcji: print, help, input, float i int) i jakich
danych ta funkcja od nas oczekuje (nazywanych listą argumentów).

Wprowadzenie samej nazwy nie uruchamia funkcji. Zostanie wyłącznie wyświetlona
informacja, że jest to funkcja:

```python
>>>  input 
```

Aby wywołać funcję, musimy użyć nawiasów po nazwie funcji:

```python
>>>  input()
```

Teraz Python wykona funkcję.

Wszystkie argumenty podajemy w nawiasach. Aby wyszczególnić więcej niż jeden,
oddzielcie je przecinkiem:

```python
>>>  int("FF", 16)
255
''''''

Podsumowanie
============

W tym rozdziale nauczyliśmy się podstaw składni Pythona. Odkryliśmy, jak
wyświetlać liczby całkowite, liczby dziesiętne, stringi i tuple.

Nauczyliśmy się funkcji print, która wyświetla informacje użytkownikowi
oraz funkcji input, która je pobiera.

Pomyślnie stworzyliśmy przechowywany w pliku program i uruchomiliśmy go.
Nasz program zadaje użytkownikowi kilka prostych pytań, wykonuje obliczenia
i wyświetla wyniki w formie użytecznej dla użytkownika.