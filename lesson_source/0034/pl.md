1.10 REST API
=======================

API
---

API (Application Programming Interface) - termin posiadający wiele znaczeń. W kontekście aplikacji internetowych
oznacza zbiór endpointów, które umożliwiają dostęp do danych przechowywanych przez aplikację.
Przykładowo kiedy wchodzimy na stronę YouTube i wyświetlamy film, aplikacja odpowiada nam plikami HTML, CSS, JavaScipt itd.,
które służą eleganckiemu i czytelnemu zaprezentowaniu treści w przeglądarce internetowej. Jednak jeśli chcielibyśmy
pobrać tylko sam film albo np. komentarze, musielibyśmy napisać skomplikowany kod wycinający je z HTML-a.
API YouTube umożliwiałoby pobranie surowych danych (opisów, komentarzy itp.) w postaci plików JSON, które można
łatwo przetworzyć w innej aplikacji.

REST API
--------

REST (REpresentational State Transfer) to zbiór zasad i praktyk sugerujących, w jaki sposób implementować API
w aplikacjach internetowych. Obecnie znakomita większość API udostępnianych przez aplikacje to właśnie tzw. API RESTowe.

### Główne zasady REST API

Jako przykład użyjemy serwisu z opiniami dotyczącymi różnych produktów.

1. Adres URL jest identyfikatorem konkretnego zasobu. Przykłady:
    * `/products` - zbiór produktów
    * `/products/1` - produkt o identyfikatorze `1`
    * `/products/1/reviews` - recenzje produktu o identyfikatorze `1`
    * `/products/1/reviews/2` - recenzja o id `2` produktu o id `1`
    
    Przykład niezgodny z zasadami REST:
    
    * `/products?id=1` - użycie query stringa. Query stringi mogą być używane np. do filtrowania czy wyszukiwania,
    ale nie do identyfikowania konkretnych obiektów.

2. W miarę możliwości należy używać różnych metod HTTP do specyfikowania operacji, którą chcemy wykonać na danym zasobie.
Do tej pory poznaliśmy dwie metody: GET i POST. W REST API wykorzystywane są również PUT, DELETE i ostatnio PATCH.

    * `GET` - służy do pobierania zasobu. Przykład: `GET /products` pobierze JSON zawierający listę produktów,
    `GET /products/1` pobierze JSON zawierający dane produktu o id `1`.
    * `POST` - służy do dodawania nowych elementów do zbioru. Na przykład `POST /products` spowoduje dodanie nowego
    produktu na podstawie przesłanego w zapytaniu pliku JSON.
    * `PUT` - służy do zamiany danego zasobu na inny. Zwykle wykorzystywane do edycji obiektów - np.
    `PUT /products/1` spowoduje zmianę danych produktu `1` na zawarte w przesłanym pliku JSON.
    Teoretycznie `PUT` powinno być używane do całkowitej zmiany zasobu (a więc wszystkich jego atrybutów) -
    obecne sugeruje się, żeby aktualizację części parametrów robić metodą `PATCH`.
    * `PATCH` - służy do aktualizacji danego zasobu.
    * `DELETE` - służy do usuwania zasobów. `DELETE /products/1` usunie produkt o id `1`.
    
    Powyżej przedstawiono najczęściej spotykane wykorzystanie metod HTTP w RESTowych API. Można również wykonywać
    je do nieco mniej oczywistych akcji - np. `DELETE /products` może posłużyć do usunięcia wszsystkich produktów.
    Pytanie brzmi, czy chcemy, aby nasze API udostępniało taką ryzykowną metodę.

    Metody HTTP nie wyczerpują rzecz jasna wszystkich możliwych operacji na naszych obiektach - jeśli np. nasze API
    miałoby umożliwiać opublikowanie recenzji, która do tej pory była prywatna, moglibyśmy to zrobić w następujący sposób:
    `POST /products/1/reviews/2/publish`. Metoda POST nie tworzy tutaj żadnych nowych elementów, jest po prostu
    domyślną metodą stosowaną, gdy protokół HTTP nie udostępnia czegoś bardziej stosownego.
    (Tego typu endpointy warto tworzyć dla bardziej złożonych operacji - przykładowo opublikowanie recenzji mogłoby wysyłać
    powiadomienia dla użytkowników obserwujących dany przedmiot).

Nagłówki HTTP
-------------

Nagłówki HTTP to dodatkowe informacje dotyczące połączenia, komunikacji itp. dołączane do zapytań HTTP.
Przykładowo przeglądarki internetowe zwykle wysyłają nagłówek `User-Agent`, który zawiera informację o przeglądarce.
Stąd strony internetowe mogą wiedzieć jakiej przeglądarki używamy.

W niektórych sytuacjach możemy stosować własne nagłówki. Przykładowo możemy napisać serwer, który wymaga podania nagłówka
`Credentials`, zawierającego nazwę użytkownika i hasło. We Flasku wyglądałoby to tak:

    :::python
    from flask import Flask, request
    
    app = Flask(__name__)
    
    @app.route('/data')
    def get_data():
        user_pass = request.headers.get('Credentials')
        if not user_pass:
            return 'No credentials - access denied'
        # Tutaj sprawdzamy, czy hasło się zgadza i kontynuujemy obsługę zapytania
    
    app.run(debug=True)

Aby dołączyć nagłówki do zapytania przy użyciu biblioteki requests należy dodać argument `headers`:

    :::python
    import requests
    
    requests.get('http://moj.serwer/adres/url', headers={'Credentials': 'grzegorz:mojehaslo'})

Uwaga - wartości nagłówków HTTP to zawsze ciągi znaków.
