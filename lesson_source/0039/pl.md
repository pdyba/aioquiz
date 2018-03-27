1.19 Zaawansowane konstrukty w Pythonie
=======================================

Najpopularniejsze konstrukty danych wykorzystywane na co dzień to:
* dict
* list
* tuple
* set

oraz równie często używane:
* datetime
* Counter
* defaultdict
* namedtuple


set
----------------------

Struktura zbliżona do listy z dwoma cechami:
* nieuporządkowana
* unikalna (nie zawiera powtarzających się elementów)



#### Create

    :::python3
    jakis_tam_set = set()
    jakis_tam_set = {'a', 'b', 'c'}

#### Read

Tylko w czasie iterowania np.:

    :::python3
    jakis_tam_set = {'a', 'b', 'c'}
    for el in jakis_tam_set:
        print(el)

#### Update

    :::python3
    a = {'a', 'b', 'c'}
    a.add('a')
    a.add('d')
    assert len(a) == 4
    
    a = {'a', 'b', 'c'}
    a.update({'g', 'f'})
    a.update(['z', 'x'])
    a.update(('p', 'o'))
    a.update({'u':'1', 't':'2'})
    

#### Delete

    :::python3
    a = {'a', 'b', 'c'}
    a.clear()
    assert a == set()
    
    a = {'a', 'b', 'c'}
    a.remove('d')
    a.remove('a')
    assert 'a' not in a
    
    a = {'a', 'b', 'c'}
    a.discard('d')
    a.discard('a')
    assert 'a' not in a

    a = {'a', 'b', 'c'}
    b = a.pop()
    assert b not in a

#### Operacje na zbiorach


* difference - różnica jednostronna
* difference_update
* intersection - część wspólna
* intersection_update
* symmetric_difference  - różnica obustronna - przeciwieństwo części wspólnej
* symmetric_difference_update
* union  - suma zbiorów


    :::python3
    a = {'a', 'b', 'c'}
    b = {'c', 'd', 'e'}
    
    a.difference(b)
    {'a', 'b'}
    a - b
    {'b', 'a'}
    
    a.intersection(b)
    {'c'}
    
    a.symmetric_difference(b)
    {'b', 'a', 'd', 'e'}
    
    a.union(b)
    {'b', 'd', 'a', 'c', 'e'}

#### Sprawdzenia 

    :::python3
    # sprawdzanie braku części wspólnej
    a = {'a', 'b', 'c'}
    b = {'c', 'd', 'e'}
    assert a.isdisjoint(b) == false
    
    # sprawdzanie czy zbiór jest podzbiorem innego zbioru
    a = {'a', 'b', 'c', 'd'}
    b = {'c', 'd'}
    assert b.issubset(a) == True
    
    # sprawdzanie czy zbiór jest nadzbiorem innego zbioru
    assert a.issuperset(b) == True


datetime
----------------------

#### imporotwanie modułów

    :::python3
    from datetime import date
    from datetime import time
    from datetime import datetime
    from datetime import timedelta


#### date

Do przechowywania tylko daty (bez czasu)

    :::python3
    from datetime import date
    
    a_date = date(day=12, month=8, year=2009)
    today = date.today()
        
    today.day
    today.month
    today.year
    today.weekday() # 0 = poniedzialek, 6 = niedziela
    today = today.replace(day=12, year=2009, month=8)     
        
    date.fromtimestamp(1) #epoh (1970, 1, 1)
    date.fromtimestamp(1234123141) # (2009, 2, 8)
    
    today - a_date

#### time

Do przechowywania tylko czasu (bez daty)

    :::python3
    from datetime import time
    a_time = time(minute=12, second=13, hour=4)
    a_time.hour
    a_time.minute
    a_time.microsecond
    
#### datetime
 
 Do przechowywania dat i czasu
 
     :::python3   
    from datetime import datetime
    a_date = datetime(2017, 3, 26, 23, 41, 45, 620822)
    str(a_date)
    start = datetime.now()
    diff = datetime.now() - start

#### timedelta

Do przechowywania różnicy w dacie i czasie.

    :::python3   
    from datetime import timedelta
    td = timedelta(days=1, seconds=0, microseconds=0, milliseconds=0, minutes=0, hours=0, weeks=0)
    a_date = datetime(2017, 3, 26, 23, 41, 45, 620822) 
    a_date += td
    a_date i= td

defaultdict
----------------------

Słownik, który ma domyślne typy wartości, tworzone w locie.

    :::python3
    from collections import defaultdict
    a = defaultdict(list)
    a['x'].append('1')
    
    b = defaultdict(str)
    b['b'] += 'ma kota'
    b['b'] += 'ma kota'
    
    a = defaultdict(dict)
    a = defaultdict(int)



Counter
----------------------

Klasa służąca do zliczania elementów iterowalnych obiektów np. stringów, list, tupli itp. 

    from collections import Counter
    
    # count elements from a string
    c = Counter('abcdeabcdabcaba') 
    # count elements from a list
    c = Counter(['a', 'b', 'c', 'd', 'e', 'a', 'b', 'c', 'd', 'a', 'b', 'c', 'a', 'b', 'a'])  
    c.most_common()     #  most common elements
    c.most_common(3)    # three most common elements
    sum(c.values())     # suma wszystkich elementow



namedtuple
----------------------

Tworzenie prostych klas do przechowywania danych. Łatwe w użyciu, optymalizuje zużycie pamięci.

    from collections import namedtuple

    :::python3
    Point = namedtuple('Point', ['x', 'y'])
    p = Point(x=11, y=22)


Kod do zadania 1.19.5
----------------------

    :::python3
    class Ojciec:
        def __init__(self, imie, nazwisko, data_ur):
            self.imie = imie
            self.nazwisko = nazwisko
            self.data_ur = data_ur