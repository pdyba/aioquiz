Zmienne, pobieranie danych od użytkownika
=========================================

Zmienna
-------

definica zmiennej

> Konstrukcja programistyczna posiadająca podstawowe atrybuty:
> 
> * symboliczną nazwę  (identyfikator)
> * miejsce przechowywania (w pamięci)
> * wartość  
> * typ
>
> pozwalająca w kodzie źródłowym odwoływać się przy pomocy nazwy do wartości lub miejsca przechowywania. 

symboliczną nazwę jest głownym sposobem w Pythonie do odwoływania się do zmiennej, w 99,9% przypadków nie będzie nas
interesowała jej lokalizacja w pamięci. Nie w Pythonie każda zmienne posiada swój typ, mimo że jest on dynamiczny w pełni
zależny od wartości zmiennej.

Przypisanie zmiennej zmiennej
------------------

Definiując zmienną w Pythonie

```python 
company = "Acme Inc"
print(company)
```
company - w tym przypadku jest *nazwą* naszej zmiennej
\= - jest znakiem przypisania, w Pythonie zawsze oznacza dokłądnie to samo - przypisanie zmiennej - w postaci deklaracji lub jej nadpisania.
"Acme Inc" - jest tutaj wartością zmiennej (o typi str)

powyższy przykład był typową definicją zmiennej, kolejny przykład pokazuje jak zmienną nadpisać 

```python 
company = "Acme Inc"
print(company)
company = "Lucas Arts"
print(company)
```

lub 

```python 
company = "Lucas Arts"
company = company + " & Films"
print(company)
```

oba te przykłady są edycją zmiennej przez jej nadpisanie (tak zwane nie w miejscu)
Zmienną można też edytować w tak zwanym miejscu najczęściej wykorzystanym tego przykładem są listy.

```python 
zakupy = ["jaja", "szynka"]
print(zakupy)
zakupy.append("maslo")
print(zakupy)
```
  
Typ zmiennej
------------

Zmienne dzielą się na dwie podstawowe kategorie mutowalne (mutable) i niemutowalne (immutable).
Jak sama nazwa wskazuje pierwsze możemy łatwo edytować a tych drugich nie można w domyśle edytować.

Mutowalne: 
* list
* dict
* set

Nie mutowalne: 
* bool
* int
* float
* str
* tuple

Co się oczywiście pokrywa z możliwością ich edycji w miejscu lub nie, co oznacza że w Pythonie nie ma funkcji która
potrafi zmienić wartość zmiennej po jej zdefiniowaniu bez jej nadpisywania w przypadku zmiennych z kategorii niemutowalnych. 


Sprawdzanie typu zmiennej
-------------------------

Na potrzeby debugowania (szukania gdzie jest problem) wykorzystuje się funkcję `type` np.

```python 
company = "Acme Inc"
print(type(company))
```

ale w czasie sprawdzania zgodności typu szczególnie w funkcjach warunkowych wykorzystuje się funkcje `isinstance`, która zwraca nam tylko binarne prawda fałsz

```python 
company = "Acme Inc"
print(isinstance(company, str))
```

Typ danych bool
---------------

Bool - typ dany boolowski lub prawda / fałsz, jest to najbardziej podstawowy typ danych w informatyce, który dosłownie zero-jedynkowo określa
czy coś jest prwadą (True) lub fałszem (False). W Pythonie:

prawdą jest `True` - zastrzeżone słowo ale też uznaje się że prawdą będzie 1 co jeszcze może być prawdą omówimy przy tworzeniu warunków

fałsz czyli `False` - również zastrzeżone słowo, którego odpowiednikiem jest 0 i tak jak w przypadku prawdy fałszów może być więcej.

ostatnim bardzo nie typowym rodzajem danych w informatyce jest ich brak tak zwana "nicość"  czyi w Pythonie `None`.
None nie jest ani prawdą ani fałszem.


Pobieranie danych od użytkownika
--------------------------------

Aby pobrać dane od uzytkownika musimy użyć kolejnej wbydowanej funkcji - `input`.

```python 
print("podaj swoj rozmiar buta: ")
rozmiar_buta = input()
print("Twoj rozmiar buta wynosi", rozmiar_buta)
```

albo trochę krócej:

```python 
rozmiar_buta = input("podaj swoj rozmiar buta: ")
print("Twoj rozmiar buta wynosi", rozmiar_buta)
```

Ważną informacją jest to że input zawsze będzie o typie str.

Mapowanie typów zmiannych
-------------------------

Żeby zmienić typ zmiennej musimy wykorzystać jedną z wbudowanych funkcji odzwierciedlajacych typ:

* bool
* int
* float
* str
* tuple
* list
* dict
* set

jeśli Python będzie wiedział (miał zdefinowane) taką "translację" to zwróci nam formę danych przez nas oczekiwaną:

```python 
rozmiar_buta = input("podaj swoj rozmiar buta: ")
rozmiar_buta = int(rozmiar_buta) + 2
print("Twoj rozmiar buta wyniesie za 2 lata", rozmiar_buta)
```

Gdybyśmy nie zmienili typu nasz kod by napotkał błąd `TypeError: can only concatenate str (not "int") to str`
