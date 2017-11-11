PyLove 1.2 Pliki i Json
=========================

Otwieranie plików w Pythonie
----------------------------


    :::python3
    file = open(file_name, mode=access_mode)

    file_name = 'sciezka do pliku'
    access_mode = {
        'r': 'read - odczyt zawartosci',
        'w': 'write - zapis zawartosci',
        'a': 'append  - zapis zawartosci po ostatniej linijce',
        'rb': 'read binary  - odczyt zawartosci w formacie binarnym',
        'wb': 'write binary  - zapis zawartosci w formacie binarnym',
    }


Przykłady komendy open():

    :::python3
    file = open('moj_plik')

    file = open('./moj_plik', 'w')

    file = open('/home/dybapiotr/moj_plik', 'a')

    file = open('moj_obrazek', 'rb')

    file = open('moj_obrazek', 'wb')


Pełen przykład odczytu:

    :::python3
    file = open('moj_plik')
    data = file.read()  # czyta cały plik
    file.close()  # po wcztaniu pliku trzeba go zamknąć
    print(data)  # string

    file = open('moj_plik')
    data = file.readline()  # czyta 1 linie
    data2 = file.readline()  # czyta kolejna linie
    file.close()
    print(data)  # string
    print(data2)  # string

    file = open('moj_plik')
    data = file.readlines()  # czyta wszystkie linie
    file.close()
    print(data)  # lista


Pełen przykład zapisu:

    :::python3
    file = open('moj_plik', 'w')
    file.write('Ala ma kota')  # zapis do pliku string
    file.write('a pies ma konia\n')  # zapis ze znakiem nowej lini
    file.close()

    file = open('moj_plik', 'a')
    file.writelines(['Ala ma kota', 'a pies nie ma konia'])
    file.close()


    :::python3
    file = open('moj_plik', 'a')
    file.write('Ala ma kota')
    file.write('a pies ma konia\n')
    file.close()

Składnia with
-------------

Nie wymaga zamknięcia pliku:

    :::python3
    with open('moj_plik', 'w') as file:
        file.write('losowe dane')

    with open('moj_plik') as file:
        data = file.read()



JSON
----

JavaScript Object Notation – lekki format wymiany, przechowywania danych komputerowych.
JSON jest formatem tekstowym, bazującym na języku JavaScript.


String: '"tekst"'
Int/float: '123'
Słownik: '{"1": 2}' -  klucze w json zawsze są stringami
Lista: '[1, 2 ,3]'

    :::python3
    import json

    x = {1: 2}
    xj = json.dumps(x)
    xj = json.loads(xj)

    x == xj

    y = '{"1": 2}'
    yj = json.loads(y)
    yj = json.dumps(yj)

    y == yj

    with open('pyladies_random', 'w') as file:
        json.dump(x, file)

    with open('pyladies_random') as file:
        data = json.load(file)

load, loads - służą do wczytania foramtu json
dump, dumps - służą do zapisania (zrzucenia) danych do formatu json
json.dump, json.load- służy do pracy z plikiem
json.dumps, json.loads - służy do pracy ze stringiem


Przygotowanie do zadań
----------------------

Pobierz pliki do zadań:
[http://dyba.it/py1.2](http://dyba.it/py1.2)
[http://dyba.it/py1.2.json](http://dyba.it/py1.2.json)

plik do zadania domowego:
[http://dyba.it/py1.2zd.json](http://dyba.it/py1.2zd.json)


