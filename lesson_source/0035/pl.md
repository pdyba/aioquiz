1.15 Zarządzenie plikami konfiguracyjnymi
=======================

Plik konfiguracyjny
-------------------

Jest to plik przechowujący parametry aplikacji, takie jak:
* ścieżki do istotnych plików
* dane do bazy danych (adres, port, login, hasło)
* loginy, hasła i klucze dostępowe do aplikacji zewnętrzynch
oraz wiele innych specyficznych dla danej aplikacji.

Pliki te są często pisane w ASCII, rzadziej w UTF-8, czyli bez użycia Polskich znaków diakrytycznych.

Będziemy omawiać tworzenie tych plików w Pythonie,
 bez wykorzystania zewnętrznych narzędzi (takich jak consul czy zookeeper).

Plik Pythonowy
--------------

Jest to plik z zachowaniem konwencji i formatów pythonowych.
Jedyną wadą jest to iż osoba nie znająca pythona może mieć większe trudności w jego użyciu.

Wariant pierwszy:

plik config.py

    :::python
    DB_IP = "127.0.0.1"
    DB_PORT = 5061
    DB_LOGIN = "admin"
    DB_PASS = "p@ssw0rd"

    SERVER_IP = "127.0.0.1"
    SERVER_PORT = 80

plik main.py

    :::python
    import config

    db = abstract_db.connect(config.DB_IP, config.DB_PORT, config.DB_LOGIN, config.DB_PASS)

Wariant drugi - z wykorzystaniem class:

plik config.py

    :::python
    class DB:
        IP = "127.0.0.1"
        PORT = 5061
        LOGIN = "admin"
        PASS = "p@ssw0rd"

    class SERVER:
        IP = "127.0.0.1"
        PORT = 80

plik main.py

    :::python
    from config import DB, SERVER

    db = abstract_db.connect(DB.IP, DB.PORT, DB.LOGIN, DB.PASS)
    app.start(SERVER.IP, SERVER.PORT)

Plik zewnętrzny
---------------

Wariant pierwszy .ini - configparser:

config.ini

    :::python
    [DB]
    IP = 127.0.0.1
    PORT = 5061
    LOGIN = admin
    PASS = p@ssw0rd

    [SERVER]
    IP = 127.0.0.1
    PORT = 80


main.py

    :::python
    import configparser

    config = configparser.ConfigParser()
    config.read('config.ini')

    db_login = config['DB']['LOGIN']
    host_ip = config['SERVER']['IP']


Wariant drugi .json - JSON:

config.json

    :::javascrip
    {
      "DB": {
        "IP": "127.0.0.1",
        "PORT": 5061,
        "LOGIN": "admin",
        "PASSWORD": "p@ssw0rd"
      },
      "SERVER": {
        "IP": "127.0.0.1",
        "PORT": 80
      }
    }


main.py

    :::python
    import json

    with open('config.json') as file:
        config = json.load(file)

    db_login = config['DB']['LOGIN']
    host_ip = config['SERVER']['IP']



3. Zmienne środowiskowe
-----------------------

Zmienna środowiskowa (ang. environment variable) to nazwana wartość, zazwyczaj zawierająca ciąg znaków, przechowywana
i zarządzana przez powłokę. Zmienna środowiskowa może wpływać na działanie procesów uruchamianych w systemie operacyjnym
i wtedy staje się pewnym mechanizmem komunikacji, lub też przechowywać wartość w celu jej późniejszego wykorzystania.

Popularne przy rozwiązaniach typu Docker.

Aby zapisać konfigurację do zmiennych środowiskowych należy:

**Linux/MacOS**

Na Linuxie/MacOS wykorzystuje się w tym celu polecenie `export`

o składni `export klucz=wartosc` (ważne: dookoła znaku `=` nie może być spacji).

np.:

    :::bash
    export DB_IP="127.0.0.1"
    export DB_PORT=5061

Wartości sprawdzić możemy komendą `env`.

**Windows**

Windows ma polecenie `set` o takiej samej składni jak linux/mac - `set klucz=wartosc`:

    :::bash
    set DB_IP="127.0.0.1"
    set DB_PORT=5061


Wartości sprawdzić możemy komendą `set` (wszystkie zmienne)
lub `set DB_IP` (wyświetlanie wartość konkretnej zmiennej, w tym przypadku DB_IP).



    :::python
    import os

    db_ip = os.environ.get('DB_IP', None)

    if not db_ip:
        raise ValueError('You must have "DB_IP" variable')


Automatyzacja wczytywania config'ów
-----------------------------------

W zależności od sposobu przechowywania pliku konfiracyjnego możemy stworzyć plik config.py

dla plików pytohnowych (1.)

    :::python
    try:
        from config_prod import *
        print('using PRD config')
    except ImportError:
        try:
            from config_dev  import *
            print('using DEV config')
        except ImportError:
            from config_template import *
            print('using ! Template ! config file')
    except Exception as err:
        print(err)
        print('error with config quitting')
        quit()

dla plików json/ini (2.):

    :::python
    import json

    def load_cfg(path):
        with open(path) as file:
            return json.load(file)

    try:
        config = load_cfg('config_prd.json')
        print('using PRD config')
    except FileNotFoundError:
        try:
            config = load_cfg('config_def.json')
            print('using DEF config')
        except FileNotFoundError:
            config = load_cfg('config.json.example')
            print('using ! Template ! config file')
    except Exception as err:
        print(err)
        print('error with config quitting')
        quit()

Dobrą praktyką jest automatyzowanie wszystkiego, włącznie z wczytwanie konfiguracji - ułatwia nam to jej zarządzaniem.
Różne pliki konfiugracyjne trzymamy po to, żeby nie używać produkcyjnych danych w czasie developmentu i żeby tych plików nie edytować.

Warto wspomnieć, iż można wyspecifikować zmienną środowiskową zawierająca infomrację którego pliku z configiem użyć :)
