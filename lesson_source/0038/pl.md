1.18 Testy jednostkowe
======================

Testy jednostkowe to fragmenty kodu, które służą do sprawdzania, czy właściwy kod aplikacji działa tak jak powinien.
Do pisania testów jednostkowych najlepiej skorzystać z frameworka. Dla Pythona mamy kilka opcji:

* Unittest - część biblioteki standardowej Pythona
* Pytest - zewnętrzna biblioteka, ale wszędzie najbardziej polecana
* Nose

My będziemy używać frameworka Pytest.

Przykład - prosty test
----------------------

### app/silnia.py

    :::python3
    def silnia(n):
        if n < 2:
            return n
    
        return n * silnia(n - 1)

### tests/test_silnia.py

    :::python3
    from app.silnia import silnia
    
    
    def test_silnia():
        assert silnia(1) == 1
        assert silnia(2) == 2
        assert silnia(5) == 120

### Automatyczne wykrywanie testów

Pytest jest w stanie sam znaleźć testy w naszym kodzie. Aby mu to umożliwić musimy przestrzegać następujących reguł:

* Pliki z testami muszą mieć nazwy zaczynające się od ``test_`` lub kończące się na ``_test``,
* Funkcje testujące muszą mieć nazwy zaczynające się od ``test_``,
* Funkcje testujące można umieszczać w klasach o nazwach zaczynających się od ``Test``.

### Uruchamianie testów

Testy można uruchomić na dwa sposoby:

* Korzystając z terminala / wiersza poleceń wykonać polecenie ``pytest`` w głównym folderze naszej aplikacji
* Utworzyć konfigurację uruchomieniową w PyCharmie (Run -> Edit configurations -> dodać nową konfigurację typu ``py.test``
-> wybrać target ``Custom``)

### Co testować?

* Ścieżki pozytywne (happy paths) - pomyślne wywołania funkcji
* Ścieżki negatywne (unhappy paths) - wywołania funkcji z nieprawidłowymi parametrami, błędy w funkcjach wywoływanych
przez funkcję testowaną
* Testy powinny pokrywać wszystkie możliwe przebiegi działania funkcji, w tym np. wszystkie dane wejściowe,
dla których działanie funkcji jest nietypowe
* W miarę możliwości należy traktować funkcję jako czarną skrzynkę, a więc nie sugerować się kodem funkcji tylko założeniem,
co dana funkcja powinna robić

### Dokładniejszy test funkcji silnia()

    :::python3
    import pytest
    
    from app.silnia import silnia

    def test_silnia():
        assert silnia(0) == 1
        assert silnia(1) == 1
        assert silnia(2) == 2
        assert silnia(5) == 120
    
        with pytest.raises(ValueError):
            silnia(-1)

### Zadanie 1.

Napisz wyczerpujące testy dla kodu znajdującego się pod adresem: [link](./images/user_db.py)

Poszczególne metody klasy ``UserDB`` powinny działać następująco:

* ``add_user`` - dodaje nowego użytkownika. Użytkownik powinien być reprezentowany przez słownik zawierający
dowolne atrybuty. Obowiązkowy jest atrybut ``name`` - musi to być ciąg znaków, poza tym nie może się powtarzać.
Atrybut ``age`` jest opcjonalny, ale jeśli się pojawi, musi to być liczba całkowita.

* ``list_users`` - zwraca listę zawierającą dotychczas dodanych użytkowników.

* ``sort_users`` - sortuje użytkowników względem podanego atrybutu (``name`` (domyślnie) lub ``age``).
Próba sortowania względem innego atrybutu kończy się wyjątkiem. Można sortować rosnąco (domyślnie) albo malejąco -
wtedy należy ustawić parametr ``reverse`` na ``True``. Pusty wiek powinien być interpretowany jako nieskończenie duży.

* ``delete_user`` - usuwa użytkownika o zadanym atrybucie ``name``. Rzuca wyjątkiem jeśli nie ma takiego użytkownika.

* ``report`` - zwraca słownik zawierający dwa klucze: ``total_users``, którego wartością jest liczba dodanych użytkowników,
oraz ``mean_age`` - średni wiek użytkowników, którzy mają zdefiniowany wiek. ``mean_age`` powinno się pojawić tylko wtedy,
kiedy przynajmniej jeden użytkownik ma zdefiniowany wiek. 


Fixtures
--------

Fixture - metoda tworząca obiekty, dane itp. potrzebne w testach. Tworzymy je następująco:

    :::python3
    import pytest

    @pytest.fixture
    def user_db():
        return UserDB()
    
    @pytest.fixture
    def prefilled_user_db():
        user_db = UserDB()
        user_db.add_user({'name': 'John', 'age': 27})
        user_db.add_user({'name': 'Alice', 'age': 29})
        user_db.add_user({'name': 'Susan'})
        return user_db

Do metod testowych możemy teraz dodawać argumenty o nazwach takich, jak nazwy fixture'ów, przykładowo:

    :::python3
    def test_list_users(user_db, prefilled_user_db):
        assert user_db.list_users() == []
        assert len(prefilled_user_db.list_users()) == 3


Mockowanie
----------

Niektóre funkcje, które będziemy chcieli przetestować, mogą odwoływać się do zewnętrznych zasobów (na przykład
wykonywać zapytania HTTP). Do takich zasobów możemy nie mieć dostępu, a nawet jeśli mamy, to raczej nie będziemy chcieli
korzystać z nich w czasie testów, ponieważ powodowałoby to wydłużenie ich działania. Dlatego stosujemy tzw. mocki - atrapy
zasobów zewnętrznych, do których będzie się odwoływać nasz kod w czasie testowania.

### app/swapi.py

    :::python3
    import requests
    
    def get_planet_terrain(name):
        result = requests.get(f'http://swapi.co/api/planets?search={name}').json()
        if result['results']:
            return result['results'][0]['terrain']
        raise ValueError(f'Planet {name} not found')

### tests/test_swapi.py

    :::python3
    import json
    from unittest.mock import patch
    
    from app.swapi import get_planet_terrain
    
    
    @patch('app.swapi.requests')
    def test_get_planet_details(requests_mock):
        with open('tests/planet_Tatooine.json') as file:
            planets = json.load(file)
    
        requests_mock.get.return_value.json.return_value = planets
        assert get_planet_terrain('Tatooine') == 'desert'
        requests_mock.get.assert_called_with('http://swapi.co/api/planets?search=Tatooine')


* ``@patch`` powoduje nadpisanie na czas testu zmiennej podanej jako argument. Uwaga - nie wystarczy podać
``@patch('requests')`` - trzeba podać też ścieżkę do modułu, wewnątrz którego ``requests`` jest importowane.
* Dekorator ``@patch`` spowoduje dodanie do funkcji argumentu, do którego w czasie wykonania testów trafi
utworzony mock patchowanej funkcji.
* Mock to specjalny obiekt, z którego można odczytywać dowolne atrybuty (Python automatycznie utworzy je jako kolejne mocki).
Można mu też ustawiać dowolne atrybuty.
* Ustawienie atrybutu ``return_value`` umożliwia ustalenie, co zwróci dany atrybut jeśli zostanie wywołany jak funkcja.
* Na mocku można wywoływać różne funkcje, żeby sprawdzić, czy został prawidłowo użyty. Przykładowo ``assert_called_with()``
pozwala sprawdzić, czy dany mock został wywołany jako funkcja z podanymi argumentami.
* Opis wszystkich funkcji udostępnianych przez mocki znajduje się w dokumentacji:
[https://docs.python.org/3/library/unittest.mock.html](https://docs.python.org/3/library/unittest.mock.html)


Coverage
--------

Sposób sprawdzania pokrycia kodu testami. Dzięki zastosowaniu Coverage wiemy, które miejsca w naszym kodzie nie są przetestowane.
Najprościej użyć Coverage wbudowanego w PyCharma - należy uruchomić testy klikając ikonę `Run ... with Coverage`.
Uwaga - przy pierwszym uruchomieniu PyCharm zaprotestuje twierdząc, że coverage.py nie jest zainstalowane.
Wystaczy wybrać opcję 'Use bundled coverage' i sprawdzanie pokrycia powinno zadziałać bez problemu.


Testowanie Flaska
-----------------

Patrz przykład: [https://github.com/grzegorzpro/sqldemo](https://github.com/grzegorzpro/sqldemo)


Kod do zadań
------------

[Zadanie 1.](./images/user_db.py)
[Zadanie 3.](./images/swapi.py)
