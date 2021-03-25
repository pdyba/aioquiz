# 1.6 Narzędzia środowisk Pythonowych i debugowanie

## [Pyenv](https://github.com/pyenv)
Narzędzie pozwalające na bardzo łatwą instalację konkretnej wersji Pythona w systemie.

Jedną z największych zalet jest możliwość przypisania konkretnej wersji Pythona do ścieżki w systemie.

### Najważniejsze komendy

#### Lista możliwych wersji Pythona do zainstalowania
```
pyenv install -l
```

#### Instalacja konkretnej wersji Pythona
```
pyenv install <wersja>
```

#### Przypisanie wersji Pythona do katalogu w którym się znajdujesz
```
pyenv local <wersja>
```
Pyenv tworzy plik `.python-version`, w którym zapisana jest wersja Pythona.

## [Virtualenv](https://virtualenv.pypa.io/en/latest/)

Zadaniem virtualenva jest dostarczanie możliwości instalowania konkretnej wersji zależności paczek dla każdego projektu z osobna.

Bez tego mając kilka projektów, które używają różnych wersji tej samej biblioteki musielibyśmy za każdym razem odinstalowywać i instalować inna wersję paczki.

Po wejściu do virtualenva możemy zacząć instalować paczki tak samo jak robimy to globalnie dla całego systemu - używając narzędzia "pip".

Zależności zapisujemy w pliku `requirements.txt`.

### Najważniejsze komendy

#### Stworzenie virtualenva
```
virtualenv venv
```

#### Wejście do virtualenva
```
source venv/bin/activate
```

#### Wyjście z virtualenva
```
deactivate
```

#### Instalacja zależności z pliku
```
pip install -r requirements.txt
```

## [Poetry](https://python-poetry.org/docs/)

Jest to menadżer paczek i zależności. Daje dużo większe możliwości niż virtualenv. Najważniejsze z nich to:
* rozdzielenie zależności produkcyjnych i deweloperskich
* `pyproject.toml` zastępuje pliki `requirements.txt`, `setup.cfg`, `setup.py`, `Pipfile`, `MANIFEST.in`.
* blokowanie na konkretnej wersji zależności paczek w pliku `poetry.lock`

Poetry jest nowocześniejszą alternatywą dla Pipenva.

### Najważniejsze komendy

#### Tworzenie nowego projektu (tylko `pyproject.toml`)
```
poetry init
```

#### Tworzenie nowego projektu (cała struktura)
```
poetry new
```

#### Wejście do virtualenva
```
poetry shell
```

#### Dodanie nowej paczki do zależności
```
poetry add <nazwa_paczki>
```
lub
```
poetry add -D <nazwa_paczki>
```
dla zależności deweloperskich (np. pytest)

#### Usunięcie zależności
```
poetry remove <nazwa_paczki>
```
i analogicznie z flagą `-D` dla zależności deweloperskich.

#### Uruchomienie komendy wewnątrz virtualenva
Pozwala nam wykonać komendę w virtualenvie bez potrzeby wchodzenia do niego.
```
poetry run <komenda>
```

## [PEP8](https://pep8.org/)
Najprościej - biblia zasad reguł, pisowni i stylu dla Pythona. Podstawowe źródło konwencji pisowni kodu.

Przydatne przy poprawianiu błędów lintera i gdy chcemy polepszyć jakość naszego kodu.

## [flake8](https://flake8.pycqa.org/en/latest/)
Jeden z najpopularniejszych linterów dla Pythona. Narzuca określony styl pisania, co pozwala polepszyć jakość kodu.

Opiera się na zasadach pisania kodu z [PEP8](https://pep8.org/)

### Ignorowanie niektórych błędów

Moglibyśmy zrobić to na poziomie wpisywania komendy `flake8`, ale jest to brzydkie rozwiązanie.

#### Ignorowanie w kodzie
Najlepiej wykorzystać możliwość zignorowania błędu dla konkretnego przypadku w kodzie. Robimy to przez dopisanie na końcu linii komentarza z treścią: `# noqa: <kod_błędu>`.
```python
try:
    print("Hello world")
except:  # noqa: E722
    print("Bye world")
```

#### Ignorowanie w konfiguracji
Pozwala nam całkowicie zignorować błąd we wszystkich miejscach, w których się pojawi.

Domyślnie użylibyśmy pliku `setup.cfg`:
```ini
[flake8]
ignore = E722
exclude = .git,__pycache__,docs/source/conf.py,old,build,dist
max-complexity = 10
```

W przypadku Poetry problem jest trochę większy, ponieważ flake8 nie wprwadził oficjalnego wsparcia dla `pyproject.toml`.
Rozwiązaniem jest uruchamianie flake8 z poziomu pytesta (wtyczka pytest-flake8). Wtedy konfiguracja wygląda następująco:
```ini
[tool.pytest.ini_options]
flake8-ignore = E722
```
Bardziej rozbudowana konfiguracja:
```ini
[tool.pytest.ini_options]
flake8-max-line-length = 120
flake8-exclude = [".git,__pycache__", ".venv,node_modules"]
flake8-ignore = [
    ".git/* ALL",
    "__pycache__/* ALL",
    ".venv/* ALL",
    "node_modules/* ALL",
    "nasz_projekt/* E722"]
"""
```
Należy pamiętać, że gdybyśmy wywołali flake8 z jego komendy, a nie z pytesta to konfiguracja zapisana w Poetry zostanie zignorowana!

### Najważniejsze komendy

#### Uruchomienie lintera w aktualnym katalogu
```
flake8
```

#### Uruchomienie lintera w podanym katalogu
```
flake8 <ścieżka>
```

## PDB/IPDB
PDB to interaktywny debugger wbudowany w standardową bibliotekę Pythonową, więc jest dostępny "od ręki".
Pozwala na zatrzymanie się w konkretnym miejscu w kodzie, gdzie możemy badać działanie programu.

IPDB to ulepszony PDB (używa IPythona), jego atuty to kolorowanie składni, autouzupełnianie TABem itd.

### Breakpointy
W miejscu, gdzie chcemy się zatrzymać wklejamy następujący kod:
```python
import pdb
pdb.set_trace()
```
i analogicznie dla ipdb:
```python
import ipdb
ipdb.set_trace()
```
Powyższy kod spowoduje, że program zatrzyma nam się w określonym miejscu i uruchomi się interaktywny debugger.

Bardzo ciekawą i przydatną opcją jest wykorzystanie debuggera w momencie, gdy nasz kod zwraca wyjątek:
```python
from ipdb import launch_ipdb_on_exception

with launch_ipdb_on_exception():
    [...]  # kod, który zwraca wyjątek
```
W tym wypadku interaktywny debugger uruchamia się od razu po wystąpieniu wyjątku i pozwala na zbadanie kodu (np. sprawdzenie wartości zmiennych itd.)

### Poruszanie się po debuggerze
Interaktywny debugger pozwala na wykonanie kodu podobnie, gdyby uruchomić interpreter Pythonowy (`python` czy `ipython`).
Oprócz tego pozwala na wznowienie programu czy wykonanie kilku kolejnych linii kodu, w którym się zatrzymał.

Najważniejsze komendy debuggera:
* `n` - wykonanie kolejnej linii kodu
* `s` - wykonanie kolejnej linii kodu jednocześnie wchodząc do środka innej funkcji, jeśli została wywołana
* `c` - kontynuuje wykonywanie kodu, aż się wykona lub natrafi na kolejny breakpoint
* `a` - wyświetla wartości argumentów dla aktualnej funkcji
* `r` - kontynuuje wykonywanie funkcji aż do zwrócenia `return`
* `w` - wyświetla stack trace

## Przykładowy kod do zadań
```python
import requests

import logging

def get_service(company):
    try:
        print(f"{company.capitalize()} has service: {services()[company]}")
    except:
        logging.error("Service not found!")

def services():
    return {
         "My company": "nginx",
        "Your company": "apache",
        "His company": "caddy"
    }

if __name__ == "__main__":
    get_service("My company")
    get_service("foo bar")
```