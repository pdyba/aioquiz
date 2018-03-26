1.19 Zaawansowane konstrukty w Pythonie
=======================================

Najpopularniejsze strukty danych wykorzystywane na codzien to:
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
* unikalna



### Create

    :::python3
    jakis_tam_set = set()
    jakis_tam_set = {'a', 'b', 'c'}

### Read

Tylko w czasie iterowania np:

    :::python3
    jakis_tam_set = {'a', 'b', 'c'}
    for el in jakis_tam_set:
        print(el)

### Update

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
    

### Delete

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

### Operacje na zbiorach


* difference - różnica jedno storna
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

###

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

defaultdict
----------------------

from collections import defaultdict

Counter
----------------------

from collections import Counter





namedtuple
----------------------

from collections import namedtuple

Point = namedtuple('Point', ['x', 'y'])
p = Point(11, y=22)
