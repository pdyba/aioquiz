PyLadies 1.3 Biblioteki zewnętrzne i REST API
=============================================

API - application programming interface - interfejs programistyczny


Representational State Transfer (**REST**, ang. zmiana stanu poprzez reprezentacje) –
styl architektury oprogramowania HTTP dla systemów rozproszonych. REST wykorzystuje m.in.

* jednorodny interfejs
* bezstanową komunikację

Instalacja bibliotek zewnętrznych
---------------------------------

pip - menadżer pakietów w języka python - taki AppStore/GooglePlay ;)

    :::bash
    pip
    pip help

Instalacje pojedyńczej paczki:

    :::bash
    pip install requests

Instalacje pojedyńczej paczki w konkretnej wersji:

    :::bash
    pip install requests==2.18.4

Instalacje pojedyńczej paczki z pliku:

    :::bash
    pip install requests-2.18.4-py2.py3-none-any.whl


Upgrade:

    :::bash
    pip install -U requests

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

* GET – pobranie zasobu wskazanego przez URI
* POST – przyjęcie danych przesyłanych od klienta do serwera (np. wysyłanie zawartości formularzy, JSONów, plików)

* PUT – przyjęcie danych przesyłanych od klienta do serwera, najczęściej aby zaktualizować wartość encji
* DELETE – żądanie usunięcia zasobu, włączone dla uprawnionych użytkowników

* HEAD – pobiera informacje o zasobie, stosowane do sprawdzania dostępności zasobu
* OPTIONS – informacje o opcjach i wymaganiach istniejących w kanale komunikacyjnym
* PATCH – aktualizacja części danych


Kody http
---------

Klasy kodów odpowiedzi serwera HTTP:
* 1xx - kody informacyjne
* 2xx - kody powodzenia
* 3xx - kody przekierowania
* 4xx - kody błędu aplikacji klienta
* 5xx - kody błędu serwera

1xx - są rzadko spotykane
2xx:
* 200 - OK
* 201 - Created - wysłany dokument został zapisany na serwerze
3xx:
* 301 - Moved Permanently - trwale przeniesiony - żądany zasób zmienił swój URI częsta odpowiedź na POSTa

4xx:
* 400 - Bad Request	- nieprawidłowe zapytanie – żądanie nie może być obsłużone przez serwer z powodu błędnej składni zapytania
* 401 - Unauthorized - nieautoryzowany dostęp
* 403 - Forbidden - Zabroniony – serwer zrozumiał zapytanie lecz konfiguracja bezpieczeństwa zabrania mu zwrócić żądany zasób
* 404 - Not Found - nie znaleziono – serwer nie odnalazł zasobu według podanego URL
* 405 - Method Not Allowed - niedozwolona metoda – metoda zawarta w żądaniu nie jest dozwolona dla wskazanego zasobu
* 408 - Request Timeout	koniec czasu oczekiwania na żądanie – klient nie przesłał zapytania do serwera w określonym czasie
* 413 - Request Entity Too Large	encja zapytania zbyt długa – całkowita długość zapytania jest zbyt długa dla serwera
* 414 - Request-URI Too Long	adres URI zapytania zbyt długi – długość zażądanego URI jest większa niż maksymalna
* 415 - Unsupported Media Type	nieznany sposób żądania – serwer odmawia przyjęcia zapytania, ponieważ jego składnia jest niezrozumiała dla serwera

5xx:

* 500 - Internal Server Error - wewnętrzny błąd serwera – serwer napotkał niespodziewane trudności, które uniemożliwiły zrealizowanie żądania
* 501 - Not Implemented - nie zaimplementowano – serwer nie dysponuje funkcjonalnością wymaganą w zapytaniu; ten kod jest zwracany, gdy serwer otrzymał nieznany typ zapytania
* 502 - Bad Gateway - błąd bramy – serwer – spełniający rolę bramy lub pośrednika – otrzymał niepoprawną odpowiedź od serwera nadrzędnego i nie jest w stanie zrealizować żądania klienta
* 503 - Service Unavailable - usługa niedostępna – serwer nie jest w stanie w danej chwili zrealizować zapytania klienta ze względu na przeciążenie

Specjalne:

* 418 - I'm a teapot - :D

requests
--------

[http://python-requests.org](http://python-requests.org/)


Requests jest biblioteką HTTP na licencji Apache2, w języku Python, dla istot ludzkich.

Większość istniejących modułów Pythona używanych do wysyłania żądań HTTP jest niezwykle rozwlekła i niewygodna. Wbudowany w Pythona moduł urllib2 oferuje większość potrzebnych możliwości HTTP, ale API jest całkowicie zepsute. Wymaga olbrzymiej ilości pracy (nawet nadpisywania metod) żeby wykonać najprostsze zadania.

[http://py.net/requests](http://py.net/requests)

    :::bash
    pip install requests-2.18.4-py2.py3-none-any.whl

    LUB:

    python -m pip install requests-2.18.4-py2.py3-none-any.whl

URL
---

URL:

URL's types:

* http://dyba.com.pl
* http://dyba.com.pl/api
* http://dyba.com.pl/api?country=Poland

![image](images/url_1.jpg)
![image](images/url_2.jpg)

GET
---

    :::python3
    import requests
    resp = requests.get('http://py.net/health')

odpowiedź `data` z dokumentacji biblioteki requests:

* `content` - content of the response, in bytes.
* `cookies`  - A CookieJar of Cookies the server sent back.
* `elapsed` - The amount of time elapsed between sending the request and the arrival of the response (as a timedelta)
* `headers` - Case-insensitive Dictionary of Response Headers. For example, headers['content-encoding'] will return the value of a 'Content-Encoding' response header.
* `json` - Returns the json-encoded content of a response, if any.
* `status_code` - Integer Code of responded HTTP Status.
* `text` - Content of the response, in unicode.
* `url` - Final URL location of Response.


Przykład:

    :::python3
    import requests
    resp = requests.get('http://py.net/health')
    resp_json = resp.json()  # <- to jest metoda ją trzeba wywołać
    resp_text = resp.text  # <- to nie jest metoda jej nie trzeba wywoływac
    resp_time = resp.elapsed
    resp_url = resp.url

Zapisanie pliku:

    :::python3
    import requests
    resp = requests.get('http://py.net/somefile')
    with open('file.pdf', 'wb') as file:
        file.write(resp.content)


POST
----

Wysłanie jsona:

    :::python3
    url = 'http://mywebsite.org/post'
    a_dict = {"random_key": "with_random_value"}
    resp = requests.post(url, json=a_dict)

Upload pliku:

    :::python3
    url = 'http://mywebsite.org/post'
    files = {'file': open('report.xls', 'rb')}
    resp = requests.post(url, files=files)




Przygotowanie do zadań
----------------------

Dokumentacja py.net API:

Health:

    /health
    GET
    proper response:
        200: {'health': "OK"}

Status - get

    /status
    GET
    proper response:
        200: {'status': string}


Status - set

    /status/set
    POST
    requires:
        "status": string
    proper response:
        200: {'success': True}

Register:

    /register
    POST
    requires:
        "name": string
        "password": string
    proper response:
        200: {'success': True}


Login:

    /auth
    POST
    requires:
        "name": string
        "password": string
    proper response:
        {'api_key': string, 'name': string}


User status - get:

    /user_status
    GET
    proper response:
        200: {string: string}

User status - set:

    /user_status/set
    POST
    requires:
        "api_key": string
        "status": string
    proper response:
        {'success': True}


Random cat img:

    /cat
    GET
    proper response:
        200: data

Query string zabawa:

    /query_string
    GET
    proper response:
        200: {
        "parsed": bool,
        "args": dict,
        "url": dict,
        "query_string": dict
    }

Requests lib whl:

    /requests
    GET
    proper response:
        200: data

Requests lib tar:

    /requests_tar
    GET
    proper response:
        200: data


Do reszty zadań:
https://swapi.co/api/
