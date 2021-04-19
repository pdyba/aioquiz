1.10 Pliki konfiguracyjne
=============================================

**Pliki konfiguracyjne** - Pliki przechowujące paramerty i konfiguracje programów. Pliki takie są przechowywwane na dysku, poza kontekstem wykonywanego programu także są trwałe i reużywane pomiędzy kolejnymi wykonaniami.

Pliki konfiguracyjne mogą mieć różny format - na przykład yaml, json, xml, ini. Wiele programów wykorzystuje swój wykorzystuje swój własny format. 

Systemy operacyjne udostępniają sugerowaną lokalizacja na pilki konfiguracyjne aplikacji. Na przykład dla systemów Windows jest to `C:\Users\<Username>\AppData\` a dla Linux `/etc`. Wiele jednak zalaży czy takie pliki mają być (między innymi) współdzielone między użytkownikami czy też nie. W systemach Linux pliki konfiguracyjne używane przez konkretnego użytkownika mogą być przechowywane przechowywane w jego katalogu domowym (dot files). Istnieją różne konwencje między programami, jednak tak długo jak plik będzie dostępny a ryzyko jego przypadkowej edycji lub usunięcia nie będzie występowało plik taki może być przechowywany gdziekolwiek.

Sam sposób odczytu plików także jest dowolny. Można to robić ładując całą konfiguracje do pamięci na początku działania programu. Można także odczytywać wartość z pliku kiedy zajdzoie taka potrzeba. 

## Python

W pythonie pliki konfiguracyjne mogą być tworzone i przechowywalne w dowolny sposób. Często zależy to od specyfikacji aplikacji lub preferecji samego programisty. 

Przykład dla pliku konfiguracyjnego zapisanego w formacie json:
```python
import json

# Przykładowy config
config = {
    "key1": "value1",
    "key2": "value1"
}

# Zapis do pliku
with open("config.json", "wb") as f:
    f.write(json.dumps(config).encode("utf-8"))


# Odczyt z pliku
with open("config.json", "rb") as f:
    read_config = json.loads(f.read().decode('utf-8'))

print(read_config)
```

Dla plików xml można skorzystać z modułu `xml`

Dla plików yaml można skorzystać z biblioteki `pyyaml` (`pip install PyYAML`) 

Python oferuje także wbudowany moduł configparser który wspiera format INI

## configparser

Moduł ten zawiera klasę ConfigParser, która dostarcza język konfiguracji, który zapewnia strukturę podobną (lub taką samą) do tej, jaką można znaleźć w plikach INI. Można go wykorzystać do pisania programów w Pythonie, które mogą być ładwo konfigurowalne przez użytkowników końcowych.

Po stworzeniu obiektu klasy `ConfigParser` możemy operować nim jak zwykłym słownikiem:
```python
import configparser

config = configparser.ConfigParser()

config['DEFAULT'] = {'ServerAliveInterval': '45', 'Compression': 'yes', 'CompressionLevel': '9'}

config['bitbucket.org'] = {}
config['bitbucket.org']['User'] = 'hg'

config['topsecret.server.com'] = {}
top_secret = config['topsecret.server.com']
top_secret['Port'] = '50022'     # ustawi wartość w `config`
top_secret['ForwardX11'] = 'no'  # tutaj też

config['DEFAULT']['ForwardX11'] = 'yes'

with open('config.ini', 'w') as configfile:
    config.write(configfile)
```

Po zapisaniu (ostatnie 2 linie przykładu powyżej) otrzymamy taki plik:

```ini
[DEFAULT]
serveraliveinterval = 45
compression = yes
compressionlevel = 9
forwardx11 = yes

[bitbucket.org]
user = hg

[topsecret.server.com]
port = 50022
forwardx11 = no
```

Następnie w innym skrypcie możemy za pomocą `configparser` odczytać taki plik:

```python
import configparser

config = configparser.ConfigParser()

config.read('config.ini')
config.sections()  # ['bitbucket.org', 'topsecret.server.com']

config['bitbucket.org']['User']  # 'hg'
config['DEFAULT']['Compression']  # 'yes'

topsecret = config['topsecret.server.com']
topsecret['ForwardX11']  # 'no'

config['bitbucket.org']['compressionlevel']  # 9 (odczytane z DEFAULT)
```

Jak widać odczyt następuje bardzo podobnie jak w słowniku. Należy zwrócić uwagę na sekcje `DEFAULT` która jest "magiczną" sekcją - nie pojawia się w liście wszystkich sekcji, ale dostarcza domyślne wartości gdy nie istnieją one w innch sekcjach. 

Należy zwrócić także uwagę że wszystkie klucze są case-insensitive (a w samym pliku zapisane lowercase).

Wszytskie wartości przechowywane są jako stringi, konwersje na odpowiedni typ powinien wykonać programista. Configparser dostarcza jednak metody `getint()`, `getfloat()` oraz `getboolean()`. Ta ostatnia rozpoznaje wartości `yes/no`, `on/off`, `true/false` oraz `1/0` i zwraca odpowiednią wartość.

Na przykład:

```python
config['topsecret.server.com'].getboolean('forwardx11')  # False
```

Pełna dokumentacja znajduje się pod adresem: https://docs.python.org/3/library/configparser.html