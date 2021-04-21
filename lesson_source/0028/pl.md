1.20 Wyrażenia regularne
=======================================

Wyrażenia regularne - what & why?
----------------------
* ang. *regular expressions*, *regex*, *regexp*
* Wzorce, które opisują łańcuchy symboli (ciągi znaków)
* Używane do wyszukiwania w długim tekście, edycji długiego tekstu, walidacji (np. maili, nr telefonu)
* Try it yourself - https://regex101.com/ - po lewej wybrać `python`!


Znaki specjalne i surowe ciągi znaków
-------------------------------------
* Większość znaków może być używana "wprost", tj. jeżeli mamy na myśli literę `a`, to piszemy `a`
* Są jednak znaki specjalne, które muszą być poprzedzane ukośnikiem (ang. *backslash*) `\`
    * Znaki specjalne to: `\`, `.`, `^`, `$`, `?`, `+`, `*`, `{`, `}`, `[`, `]`, `|`
    * Zwykle jeżeli nie wstawimy ukośnika `\` przed danym znakiem, to zostanie potraktowany jako
      fragment specjalnej składni wyrażenia regularnego (ale nie zawsze - zależy od kontekstu)
    * Przykłady: `\\`, `\.`, `\|`
* W Pythonie pojedynczy backslash służy do umieszczania znaków specjalnych w tekście (np. `\n`),
  więc żeby przekazać backslash do wyrażenia regularnego trzeba zastosować podwójny backslash (`\\\\`)
* W surowych ciągach znaków (ang. *raw strings*) nie trzeba korzystać z podwójnego backslasha
    * W Pythonie raw strings to stringi poprzedzone literą `r`
    * Dobrą praktyką jest definiowanie wzorców jako raw strings

| Zwykły ciąg znaków | Surowy ciąg znaków |
|:------------------:|:------------------:|
| `"zk*"`            | `r"zk*"`           |
| `"zk\\d"`          | `r"zk\d"`          |
| `"\\w\\s\\d"`      | `r"\w\s\d"`        |


Klasy znaków
------------
* Jeżeli chcemy dopasować jeden znak z określonego zbioru, możemy skorzystac z klasy znaków
* Jeżeli po klasie nie będzie podany kwantyfikator, dopasowany będzie dokładnie jeden znak
* Widzimy tutaj w użyciu ukośnik `\` jako jeden ze znaków specjalnych, użyty do obsługi wzorca

| Klasa znaków | Dopasowuje                                                    |
|:------------:|---------------------------------------------------------------|
| `.`         |  Dowolny znak z wyjątkiem znaku nowej linii (ang. `wildcard`) |
| `\d`         |  Dowolna cyfra                                                |
| `\D`         |  Dowolny znak nie będący cyfrą                                |
| `\w`         |  Dowolny litera lub cyfra (znaki alfanumeryczne)              |
| `\W`         |  Dowolny znak nie będący znakiem alfanumerycznym              |
| `\s`         |  Dowolny biały znak (spacja, tab, nowa linia)                 |
| `\S`         |  Dowolny znak nie będący białym znakiem                       |

* Przykład: `\D\D\D\D\d\d` dopasuje każdą sekwencję składającą się z 4 następujących po sobie znaków
  nie będących cyframi oraz następnie 2 następujących po sobie cyfrach, np. `abcd00`, `hehe37`


Kwantyfikatory
--------------
* Określają liczbę powtórzeń znaków lub sekwencji we wzorcach
* Domyślnie kwantyfikatory są **zachłanne** (ang. `greedy`) tzn. dopasowują **maksymalną** możliwą
  liczbę znaków w tekście

| Kwantyfikator| Dopasowuje                        |
|:------------:|-----------------------------------|
| `*`          | 0 lub więcej wystąpień            |
| `+`          | 1 lub więcej wystąpień            |
| `?`          | 0 lub 1 wystąpienie               |
| `{m}`        | dokładnie m wystąpień             |
| `{m,}`       | co najmniej m wystąpień           |
| `{,n}`       | co najwyżej n wystąpień           |
| `{m,n}`      | od m do n wystąpień               |
| `[...]`      | jeden znak spośród zbioru znaków  |
| `[^...]`     | jeden znak spoza zbioru znaków    |

Przykłady:
* `.*` dopasuje dowolny ciąg znaków
* `[a-z]` dopasuje dowolną małą literę
* `[gole]+` dopasuje każdą sekwencję zawierającą litery `g`, `o`, `l`, `e`, np. `google`, `lego`
* `[^\saAlm]+` dopasuje z tekstu `Ala ma kota` słowo `kot` - wyrażenie wyklucza (`^`) użycie spacji (`\s`), liter `a`, `A`, `l`, `m`, a to, co zostało, bierze jako całość (`+`)


Alternatywy
-----------

Czasami chemy znaleźć wystąpienie jednego z kilku predefiniowanych ciągów. Możemy do tego wykorzystać
następującą składnię:

`(opcja1|opcja2|...)`

Przykładowo, żeby znaleźć wszystkie maile w domenach `@nordcloud.com` i `@google.com` możemy użyć
następującego wyrażenia regularnego:

`.+@(nordcloud|google).com`


Asercje
-------
* Pomagają wyznaczyć miejsce w tekście, w którym musi pojawić się dopasowanie


| Asercja  | Dopasowuje                                       |
|:--------:|--------------------------------------------------|
| `^`      | początek tekstu                                  |
| `$`      | koniec tekstu                                    |
| `\A`     | początek tekstu (rzadko stosowana alternatywa)   |
| `\Z`     | koniec tekstu (rzadko stosowana alternatywa)     |

* Przykład: `^witam` dopasuje `witam serdecznie`, ale nie dopasuje `serdecznie witam`


OK, to jak to zrobić w Pythonie?
--------------------------------

* Należy zaimportować moduł `re` poprzez `import re`


#### re.search
Poszukuje dopasowania w podanym stringu.
Zwróci `None` jeżeli nie odnaleziono dopasowania.
Jeżeli odnaleziono dopasowanie, zwróci obiekt `Match` **pierwszego** dopasowania.

```python
found = re.search(r'[a-z]+@[a-z]+\.[a-z]{2,3}', 'Moj adres email to: jakis@mail.com')
```

#### re.compile
Tworzy obiekt `Regex`, który reprezentuje dane wyrażenie regularne. Pozwala uniknąć wielokrotnej
kompilacji tego samego wyrażenia (co miałoby miejsce np. w przypadku użycia `re.search` w pętli).

```python
simple_email_regex = re.compile(r'[a-z]+@[a-z]+\.[a-z]{2,3}')
found = simple_email_regex.search('Moj adres email to: jakis@mail.com')
```

#### re.findall
Poszukuje dopasowania w podanym stringu.
W przeciwieństwie do metody `search`, zwraca listę stringów (jeżeli w wyrażeniu regularnym nie ma grup)
albo listę tupli.

```python
found = re.findall(r'[a-z]+@[a-z]+\.[a-z]{2,3}', 'Moje adresy email to: jakis@mail.com, inny@email.pl')
print(found)  # ['jakis@mail.com', 'inny@email.pl']
```

#### re.split
Dzieli podany string w miejscach, gdzie znajdzie dopasowanie.
Zwraca listę podzielonych części stringa.
Jeżeli w wyrażeniu regularnym istnieją grupy, w liście pojawią się również dopasowania tych grup.

```python
text = 'Ciastka, dżem, herbata.'
text_split = re.split(r'\W+', text)
print(text_split)  # ['Ciastka', 'dżem', 'herbata', '']
```

#### re.sub
Poszukuje dopasowań w podanym stringu i zastępuje je innym wyrażeniem.
Można zastosować odwołanie do grup z dopasowania.

```python
text = 'Moje adresy email to: jakis@mail.com, inny@email.pl'
text_changed = re.sub(r'[a-z]+@[a-z]+\.[a-z]{2,3}', r'***', text)
print(text_changed)  # Moje adresy email to: ***, ***
```

Zaawansowane wyrażenia regularne
================================

Grupowanie
----------
* W wyrażeniach regularnych nawiasy `(`, `)` mają wpływ na kolejność obliczeń oraz definiują tzw. grupy
* Po dopasowaniu grupy we wzorcu można odwoływać się do niej za pomocą jej numeru, np. `\1` dla pierwszej grupy, są to tzw. odwołania wsteczne
* Cały wzorzec tworzy grupę zerową

| Wyrażenie            | Wyjaśnienie                                                                                                                        |
|:--------------------:|------------------------------------------------------------------------------------------------------------------------------------|
| `(...)`              | dopasowanie wyrażenia w nawiasie jako grupy                                                                                        |
| `(?:...)`            | nawiasy nieprzechwytujące - po dopasowaniu nie można odwoływać się do zawartości dopasowanego wyrażenia poprzez odwołania wsteczne |
| `(?P<ciastko>...)`   | tworzy grupę nazwaną `ciastko`                                                                                                     |
| `(?P=ciastko)`       | dopasowuje tekst, który został dopasowany wcześniej przez grupę nazwaną `ciastko`                                                  |

* Przykład: `(ciastka)(dżem)\1+oraz\2+` dopasuje `ciastkadżemciastkaciastkaciastkaorazdżemdżem` - pierwsze `ciastka` zostaną dopasowane i oznaczone jako grupa 1., pierwszy `dżem` zostanie dopasowany i oznaczony jako grupa 2., następnie poszukujemy wielu wystąpień grupy 1. (`\1+`), czyli `ciastka`, potem szukamy słowa `oraz`, a potem poszukujemy wielu wystąpień grupy 2. (`\2+`), czyli `dżem`

### Grupy w Pythonie

#### Match.group
Metoda obiektu `Match`, zwróci całe dopasowanie lub dopasowanie wybranej grupy.

```python
found = re.search(r'([a-z]+)@([a-z]+)\.([a-z]{2,3})', 'Moj adres email to: jakis@mail.com')
print(found.group()) # jakis@mail.com
print(found.group(0))  # jakis@mail.com
print(found.group(1))  # jakis
print(found.group(2))  # mail
print(found.group(3))  # com

# nazwana grupa
found = re.search(r'(?P<user>[a-z]+)@([a-z]+)\.([a-z]{2,3})', 'Moj adres email to: jakis@mail.com')
print(found.group("user")) # jakis
```

#### Match.groups
Metoda obiektu `Match`, zwróci wszystkie grupy naraz.

```python
simple_email_regex = re.compile(r'([a-z]+)@([a-z]+)\.([a-z]{2,3})')
found = simple_email_regex.search('Moj adres email to: jakis@mail.com')
print(found.groups())  # ('jakis', 'mail', 'com')
```

Kwantyfikatory w wersji niezachłannej
-------------------------------------
* Kwantyfikator **niezachłanny** (leniwy, ang. `nongreedy`) dopasowuje **minimalną** możliwą liczbę znaków w tekście
* Dodanie `?` po kwantyfikatorze przekształca go w tryb niezachłanny
* Przykład: `[nord]{2,4}` dopasowałoby całe słowo `nord`, natomiast `[nord]{2,4}?` dopasuje osobno `no` oraz `rd`


Zaawansowane asercje
--------------------

| Asercja  | Dopasowuje                                                                                                           |
|:--------:|----------------------------------------------------------------------------------------------------------------------|
| `\b`     | pusty string na początku lub końcu słowa                                                                             |
| `\B`     | pusty string, ale nie na początku lub końcu słowa                                                                    |
| `(?=e)`  | dopasowuje łańcuch, jeśli bezpośrednio po nim następuje wyrażenie pasujące do e (ang. *positive lookahead*)         |
| `(?!e)`  | dopasowuje łańcuch, jeśli bezpośrednio po nim nie następuje wyrażenie pasujące do e (ang. *negative lookahead*)     |
| `(?<=e)` | dopasowuje łańcuch, jeśli bezpośrednio przed nim następuje wyrażenie pasujące do e (ang. *positive lookbehind*)     |
| `(?<!e)` | dopasowuje łańcuch, jeśli bezpośrednio przed nim nie następuje wyrażenie pasujące do e (ang. *negative lookbehind*) |

* Przykład: `(?<=pass:)\S*` z tekstu `pass:abc123` dopasuje `abc123`


Materiały
---------

* [Regex do walidacji maili](http://www.ex-parrot.com/~pdw/Mail-RFC822-Address.html)
* [RegexGolf](https://alf.nu/RegexGolf)
* [RegexCrossword](https://regexcrossword.com/)


Pliki txt do zadań
------------------

* [Zadanie 2.](./images/wikipedia_python.txt)
* [Zadanie 4. i 5.](./images/program_pylove.txt)
* [Zadanie 6.](./images/celebrities.txt)
