PyLove 1.0 Powtórka
=====================

CRUD
----

* C – Create - Stwórz
* R – Read - Odczytaj
* U – Update - Zmodyfikuj
* D – Delete - Usuń

Typy liczbowe
-------------

    :::python3
    # int:
    1 2 123123

    # float:
    1.23     3.22   3.0   123.12311

Na liczbach możemy wykonywać znane nam operacje matematyczne:
+ - * / ** // %
Np. 

    :::python3
    23 + 7 // 2 * 5 % 3
    (2 + 2) * 2 ** 2 + (3 -1) * 2


Typ tekstowy
------------


	:::python3
    'Ala ma kota'
	'Kot ma ale'
	'''Nie Kot	Ma
	Nie Ale'''

Można z nimi robić wiele rzeczy!

    :::python3
    'Ala' + 'Ma' + 'kota'
    '{} ma {}'.format('Pies', 'wilka')


zmienna
-------


C:

    :::python3
    dane = 'kot'
R:

    :::python3
    dane
U:

    :::python3
    dane = 'pies'
D: nie ma potrzeby Python zrobi to za nas.


    :::python3
    moja_lista = ['x', 'y', 'ciecz']
    moj_string = 'PyLadies'
    moja_liczba = 1.23

lista
-----

Przykłady:


    :::python3
	['piotr', 20, 185]
	[1, 3, 6]
C:

    :::python3
    moja_lista = [['magda', 22], ['zosia', 23]]
R:

    :::python3
    moja_lista[0]
    moja_lista[0][1]

U:

    :::python3
    moja_lista[1] = ['cecylia', 55]
    moja_lista[1][0] = 'weronika'
D:

    :::python3
    moja_lista.pop()
    moja_lista[0].remove('magda')


slice - kawałek
---------------

    :::python3
    moja_torebka = ['szminka', 'pomadka', 'portfel', 'okulary']
    moj_string = 'PyLadies.start()'
    moja_torebka[0:2]
    moja_torebka[::2]
    moj_string[2:4]
    moj_string[::3]


slownik
-------

Przykłady:

    :::python3
	{'klucz': 'wartosc', 'klucz_2': 'wartosc'}
	{1: 'jeden', 2: 'dwa', 3: 'trzy'}


C:

    :::python3
    moj_slownik = {'imie': 'piotr', 'wiek': 99}
	moj_slownik['plec'] = 'M'
R:

    :::python3
    moj_slownik['imie']	moj_slownik.get('imie')
	moj_slownik['wiek']
U:

    :::python3
    moj_slownik['imie'] = 'cecylia'
	moj_slownik['wiek'] = 22

D:

    :::python3
    del moj_slownik['wiek']

funkcje wbudowane
-----------------

Ogólne:

	:::python3
    print()
    input()
    abs()
    len()
    round()

Pomocnicze:

    :::python3
    type()
    dir()
    help()

Funkcje do zmiany typu:

    :::python3
	str()
	int()
	float()
	list()

Przykłady:

    :::python3
    str(int(float('123123.123123')))
    list('ala ma kota')

typ bool i if
-------------

Bool może przyjąć jedną z dwóch wartości:
* True 
* False

Składnia funkcji warunkej if:

    :::python3
    if 3 > 5:	
        print('alternatywna matematyka')
    elif 3 == 5:
        print('chyba zmienilismy wszechswiat')
    elif 1 <= 0 or 1 >= 5 and True:
        print('ehhh...')
    else:
        print('wszystko jest ok')


pętla for
---------

    :::python3
    for letter in in 'Ala ma Kota':
        print(letter)

    moja_lista = ['x', 'y', 'ciecz']
    for rzecz in moja_lista:
        print(rzecz)

    # petla o okreslonej liczbie wykonań
    for i in range(10)
        print(i)


pętla while
-----------

    :::python3
    czy_zakonczyc_program = False
    while not czy_zakonczyc_program:
        odp = input('czy zakonczyc program T/N')
        if odp == 'T':
            czy_zakonczyc_program = True


funkcje - def
-------------


    :::python3
    def moja_funkcja():
        print('To jest moja funkcja')

    moja_funkcja()
    moja_funkcja()


    def moje_dodawanie(a, b):
        c = a + b
        print('Twoim wynikiem jest liczba: ' + str(c))

    moje_dodawanie(2, 3)


    def moje_potegowanie(a, b=2):
        c = a ** b
        print('Liczba' + str(a) + ' do ' + str(b) +' jest liczba: ' + str(c))

    moje_potegowanie(2)
    moje_potegowanie(2, b=10)


łapanie wyjatkow - try/except
-----------------------------

    :::python3
    def test_try(alist):
        try:
            return alist[1]
        except IndexError:
            print('Obiekt nie ma tylu elementow')


Przygotowanie do zadań
----------------------

Pobierz plik zawierający bazę krajów z:
[http://dyba.it/countries.py](http://dyba.it/countries.py)

