1.24 Zaawansowane funkcje w Pythonie
====================================

Funkcja anonimowa - lambda
--------------------------

jest to funkcji, która nie musi być powiązana z identyfikatorem. 
Funkcje anonimowe są często: argumentami przekazywanymi funkcjom wyższego rzędu.
Oraz używane do budowania wyniku funkcji wyższego rzędu, która musi zwracać funkcję.

Funkcja anonimowa bez argumentów
```python
x = lambda: print('x')
x()
```
Funkcja anonimowa z 1 argumentem
```python
x = lambda a: a * 4
print(x('a'))
print(x(4))
```

Funkcja anonimowa z 2 argumentami
```python
x = lambda a, b: a * b
print(x('a', 4))
print(x(4, 5))
```

Przykłądu zastosowania:

sorted
funkcja zwraca nam generator z posortowanymi danymi.

```python
a_list = [('piotr', 185), ('zuza', 170), ('luke', 145)]
a_sorted = sorted(a_list, key=lambda a: a[1])
a_revers_sorted = sorted(a_list, key=lambda a: a[1], reverse=True)
```

filter
funkcja zwraca nam generator z niezbędnymi danymi po ich odfiltorwaniu.

```python
a_list = [('piotr', 185), ('zuza', 170), ('luke', 145)]
filtered = filter(lambda a: a[1] > 180, a_list)
print(list(filtered))
```

map
funkcja, które wykonuje inną funkcję (zwykła jak i anonimową) na każdym elemencie listy/etc zwraca generator.

```python
a_list = [('piotr', 185), ('zuza', 170), ('luke', 145)]
mapped = map(lambda a: (a[0], a[1] + 5), a_list)
print(list(mapped))
```


Comprehension 
-------------

Czyli tworzenie list w locie, mocno upraszcza i zmniejsza ilość potrzebnego kodu w naturanly i przyjmny sposób.

list
```python
a_list = [a ** 2 for a in range(2, 10)]
```

dict
```python
a_dict = {v:v ** 3 for v in range(7, 15)}
```

z warunkiem
```python
a_list = [a ** 2 for a in range(2, 10) if a % 2 == 0]
```

Generator - yield
-----------------

Funkcja, która zwraca kolejne elementy, zachowująca stan.
Optymalizująca pamięć.

```python
def szesciany_kolejne(start, end):
    for i in range(start, end):
        yield i ** 3

# Przykład użycia
        
x_3 = szesciany_kolejne(3, 60)        
print(x_3) # <generator object szesciany_kolejne at 0x10eb74678>
for x in x_3:
    print(x)
print(list(x_3)) # pusta lista
```