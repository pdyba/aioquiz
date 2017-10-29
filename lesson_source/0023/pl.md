PyLadies 1.3 Biblioteki zewnętrzne i REST API
=============================================

Instalacja bibliotek zewnętrznych
---------------------------------

pip - menadżer pakietów w języku python

    :::bash
    pip
    pip help

Instalacje pojedyńczej paczki:

    :::bash
    pip install requests

Instalacje pojedyńczej paczki w konkretnej wersji:

    :::bash
    pip install requests==2.18.4

Upgrade:

    :::bash
    pip install -U

Instalacja wszystkich zależności:


    :::bash
    pip install -r requirements

Usuwanie pakietów:

    :::bash
    pip uninstall

Aktualnie zaintalowane pakiety:

    :::bash
    pip freeze


Protokół HTTP
-------------

Protokołu do przesyła dokumentów sieci WWW np. stron internetowych, plików, obiektów oraz informacje z formularzy.

Metody protokołu HTTP

GET – pobranie zasobu wskazanego przez URI, może mieć postać warunkową jeśli w nagłówku występują pola warunkowe takie jak "If-Modified-Since”
POST – przyjęcie danych przesyłanych od klienta do serwera (np. wysyłanie zawartości formularzy)
PUT – przyjęcie danych przesyłanych od klienta do serwera, najczęściej aby zaktualizować wartość encji
DELETE – żądanie usunięcia zasobu, włączone dla uprawnionych użytkowników
HEAD – pobiera informacje o zasobie, stosowane do sprawdzania dostępności zasobu
OPTIONS – informacje o opcjach i wymaganiach istniejących w kanale komunikacyjnym
TRACE – diagnostyka, analiza kanału komunikacyjnego
CONNECT – żądanie przeznaczone dla serwerów pośredniczących pełniących funkcje tunelowania
PATCH – aktualizacja części danych

URL
---

URL:

URL's types:

http://dyba.com.pl
http://dyba.com.pl/api
http://dyba.com.pl/api?country=Poland



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

GET
---


POST
----




Przygotowanie do zadań
----------------------



https://swapi.co/api/

Pobierz dane wszystkich mieszkańców planety Tatooin
Wyświetl wszystkie nazwy ras gatunków wystepujących w V częsci Gwiezdnych Wojen (Imperium kontratakuje).
Policz BMI wszystkich pilotów Milenium Falcona I wyswietl je wraz z ich imionami.
Wyświetl imiona wszytkich Gunganów w języku Wooki.
