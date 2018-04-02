1.11 PEP 8, Pylint, pdb
=======================

PEP 8
-----

* Zbiór zasad mających na celu zwiększenie czytelności kodu
* Jeśli programiści A i B stosują się do tych zasad, to kod programisty A będzie czytelny dla programisty B i vice versa
* Czasami pomaga uniknąć błędów
* PEP 8 to tylko rekomendacje – w niektórych przypadkach można łamać zasady, na przykład:
* Jeśli w danym miejscu zastosowanie się do PEP 8 powoduje zmniejszenie czytelności kodu,
* Jeśli poprawienie kodu spowodowałoby, że przestanie działać w starszych wersjach Pythona.

### Najważniejsze zasady PEP 8

* 4 spacje jako wcięcie
* Stosujemy spacje zamiast znaków tabulacji
* Maksymalna długość linii - 79 znaków (chyba, że cały zespół zgadza się na większy limit)
* Definicje klas i globalnych funkcji powinny być rozdzielone dwoma pustymi liniami
* Definicje metod wewnątrz klasy powinny być rozdzielone jedną pustą linią
* Importy zawsze na początku pliku, należy unikać "import *"
* Unikamy niepotrzebnych spacji (przykład: `spam(ham[1], {eggs: 2})` zamiast `spam( ham[ 1 ], { eggs : 2 } )`)
* Zwykle robimy spacje wokół operatorów (przykład: `a = 5` zamiast `a=5`), wyjątek - argumenty funkcji (przykład: `complex(real, imag=0.0)` zamiast `complex(real, imag = 0.0)`)
* Nazwy klas - stosujemy CamelCase
* Nazwy zmiennych i funkcji - stosujemy_podkreslenia_w_nazwach
* Można stosować WIELKIE_LITERY do definiowania globalnych stałych
* Żeby sprawdzić, czy lista nie jest pusta, piszemy: `if lista:`, nie np. `if len(lista) > 0:`
* W przypadku zmiennych typu boolean piszemy: `if zmienna:` zamiast `if zmienna == True:`

Pylint
------

Narzędzie służące do wykrywania niezgodności z PEP 8 oraz innych potencjalnych błędów i problemów w naszym kodzie.

Instalacja:

```bash
pip install pylint

pip install pylint

```

Uruchamianie:

```bash
pylint nazwa_pliku.py

pylint nazwa_pliku.py

```

pdb - The Python Debugger
-------------------------

Narzędzie do debugowania kodu - ułatwia znalezienie błędów przez śledzenie wykonania programu krok po kroku.

Aby uruchomić pdb wstawiamy w naszym kodzie następującą linię:

`import pdb; pdb.set_trace()`

Komendy debuggera:

* h(elp) - wypisuje listę dostępnych komend
* l(ist) - wyświetl fragment kodu wokół aktualnie zaznaczonej linii
* s(tep) - wykonaj aktualnie zaznaczoną linię, zatrzymaj się przy pierwszej okazji
* n(ext) - wykonaj aktualnie zaznaczoną linię, zatrzymaj się po dotarciu do kolejnej linii
* c(ont(inue)) - kontynuuj wykonywanie programu do czasu kolejnego punktu zatrzymania (wywołania `pdb.set_trace`)
* q(uit) - wyjdź z debuggera, zatrzymaj program