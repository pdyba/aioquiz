1.20 Wyrażenia regularne
=======================================

Wyrażenia regularne - what & why?
----------------------
* ang. *regular expressions*, *regex*, *regexp*
* Wzorce, które opisują łańcuchy symboli (ciągi znaków)
* Używane do wyszukiwania w długim tekście, edycja długiego tekstu, walidacja (np. maili, nr telefonu)
* Try it yourself - https://regex101.com/ - po lewej wybrać `python`!


Znaki specjalne i surowe ciągi znaków
-------------------------------------
* Większość znaków może być używana "wprost", tj. jeżeli mamy na myśli literę `a`, to piszemy `a`
* Są jednak znaki specjalne, które muszą być poprzedzane ukośnikiem (ang. *backslash*) `\`
    * Znaki specjalne to: `\`, `.`, `^`, `$`, `?`, `+`, `*`, `{`, `}`, `[`, `]`, `|`
    * Zwykle jeżeli nie wstawimy ukośnika `\` przed danym znakiem, zostanie on potraktowany jako część do obsługi wzorca
    * Przykłady: `\\`, `\.`, `\|`
* W surowych ciągach znaków (ang. *raw strings*) nie trzeba korzystać z ukośnika `\`
    * W Pythonie stringi te poprzedzone są literą `r`
    * Dobrą praktyką jest definiowanie wzorców jako surowych łańcuchów

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
| `. `         |  Dowolny znak z wyjątkiem znaku nowej linii (ang. `wildcard`) |
| `\d`         |  Dowolna cyfra                                                |
| `\D`         |  Dowolny znak nie będący cyfrą                                |
| `\w`         |  Dowolny litera lub cyfra (znaki alfanumeryczne)              |
| `\W`         |  Dowolny znak nie będący znakiem alfanumerycznym              |
| `\s`         |  Dowolny biały znak (spacja, tab, nowa linia)                 |
| `\S`         |  Dowolny znak nie będący białym znakiem                       |

* Przykład: `[\D\D\D\D\d\d]` dopasuje każdą sekwencję składającą się z 4 następujących po sobie znaków nie będących cyframi oraz następnie 2 następujących po sobie cyfrach, np. `zuza00`, `hehe37`


Kwantyfikatory
--------------
* Określają liczbę powtórzeń znaków lub sekwencji we wzorcach
* Domyślnie kwantyfikatory są **zachłanne** (ang. `greedy`) tzn. dopasowują **maksymalną** możliwą liczbę znaków w tekście

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

* Przykład 1.: `[zuna]` dopasuje każdą pojedynczą literę `z`, `u`, `n` albo `a`
* Przykład 2.: `[zuna]+` dopasuje każdą sekwencję zawierającą litery `z`, `u`, `n`, `a`, np. `zuza`, `zuzanna`, `zuzuzuza`
* Przykład 3.: `[^\saAlm]+` dopasuje z tekstu `Ala ma kota` słowo `kot` - wyrażenie wyklucza (`^`) użycie spacji (`\s`), liter `a`, `A`, `l`, `m`, a to, co zostało, bierze jako całość (`+`)
* Przykład 4.: `[a-zA-Z]+` dopasuje z dowolnego ciągu znaków (liter, liczb, itd.) wszystkie ciągi liter, niezależnie od wielkości - wyrażenie wyszukuje litery od `a` do `z` (`a-z`), `A` do `Z` (`A-Z`) i dopasowuje je wielokrotnie (`+`)


Kwantyfikatory w wersji niezachłannej
-------------------------------------
* Kwantyfiaktor **niezachłanny** (leniwy, ang. `nongreedy`) dopasowuje **minimalną** możliwą liczbę znaków w tekście
* Dodanie `?` po kwantyfikatorze przekształca go w tryb niezachłanny
* Przykład: `[zuna]{2,4}` dopasowałoby całe słowo `zuza`, natomiast `[zuna]{2,4}?` dopasuje osobno i leniwie `zu` oraz `za`


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

* Przykład: `(ciastka)(dżem)\1+oraz\2+` dopasuje `ciastkadżemciastkaciastkaciastkaorazdżemdżem` - pierwsze `ciastka` zostaną dopasowane i oznaczone jako grupa 1., pierwszy `dżem` zostanie dopasowany i oznaczony jako grupa 2., następnie poszukujemy wielu wystapień grupy 1. (`\1+`), czyli `ciastka`, potem szukamy słowa `oraz`, a potem poszukujemy wielu wystąpień grupy 2. (`\2+`), czyli `dżem`


Asercje
-------
* Pomagają wyznaczyć miejsce w tekście, w którym musi pojawić się dopasowanie


| Asercja  | Dopasowuje                                                                                                           |
|:--------:|----------------------------------------------------------------------------------------------------------------------|
| `^`      | początek tekstu                                                                                                      |
| `$`      | koniec tekstu                                                                                                        |
| `\A`     | początek tekstu                                                                                                      |
| `\Z`     | koniec tekstu                                                                                                        |
| `\b`     | pusty string na początku lub końcu słowa                                                                             |
| `\B`     | pusty string, ale nie na początku lub końcu słowa                                                                    |
| `(?=e)`  | dopasowuje łańcuch, jeśli bezpośrednio po nim następuje wyrażenie pasujące do e (ang. *positive lookeahead*)         |
| `(?!e)`  | dopasowuje łańcuch, jeśli bezpośrednio po nim nie następuje wyrażenie pasujące do e (ang. *negative lookeahead*)     |
| `(?<=e)` | dopasowuje łańcuch, jeśli bezpośrednio przed nim następuje wyrażenie pasujące do e (ang. *positive lookebehind*)     |
| `(?<!e)` | dopasowuje łańcuch, jeśli bezpośrednio przed nim nie następuje wyrażenie pasujące do e (ang. *negative lookebehind*) |

* Przykład 1.: `[\d\B]` z tekstu `zuzuz6uzuza0` dopasuje tylko środkową cyfrę `6`
* Przykład 2.: `[\d\B]` z tekstu `zuzuz6uzuza0` dopasuje tylko ostatnią cyfrę `0`
* Przykład 3.: `(?<=lubie\s)ciastka` z tekstu `lubie ciastka, jem ciastka` dopasuje tylko pierwsze `ciastka`


OK, to jak to zrobić w Pythonie?
--------------------------------
* Należy zaimportować moduł `re` poprzez `import re`


#### re.compile
Tworzy obiekt `Regex`, który dopasowuje dane wyrażenie regularne.

    :::python3
    simple_email_regex = re.compile(r'([a-z]+)@([a-z]+)\.([a-z]{2,3})')


#### re.search
Poszukuje dopasowania w podanym stringu.
Zwróci `None`, jeżeli nie odnaleziono dopasowania.
Jeżeli odnaleziono dopasowanie, zwróci obiekt `Match` **pierwszego** dopasowania.

    :::python3
    found = re.search(r'([a-z]+)@([a-z]+)\.([a-z]{2,3})', 'Moj adres email to: jakis@mail.com')
    # lub jako metoda obiektu Regex:
    simple_email_regex = re.compile(r'([a-z]+)@([a-z]+)\.([a-z]{2,3})')
    found = simple_email_regex.search('Moj adres email to: jakis@mail.com')


#### Match.group
Metoda obiektu `Match`, zwróci całe dopasowanie lub dopasowanie wybranej grupy.

    :::python3
    found = re.search(r'([a-z]+)@([a-z]+)\.([a-z]{2,3})', 'Moj adres email to: jakis@mail.com')
    print(found.group()) # jakis@mail.com
    print(found.group(0))  # jakis@mail.com
    print(found.group(1))  # jakis
    print(found.group(2))  # mail
    print(found.group(3))  # com


#### Match.groups
Metoda obiektu `Match`, zwróci wszystkie grupy naraz.

    :::python3
    simple_email_regex = re.compile(r'([a-z]+)@([a-z]+)\.([a-z]{2,3})')
    found = simple_email_regex.search('Moj adres email to: jakis@mail.com')
    print(found.groups())  # ('jakis', 'mail', 'com')


#### re.split
Dzieli podany string w miejscach, gdzie znajdzie dopasowanie.
Zwraca listę podzielonych części stringa.
Jeżeli w wyrażeniu regularnym istnieją grupy, w liście pojawią się również dopasowania tych grup.

    :::python3
    text = 'Ciastka, dżem, herbata.'
    text_split = re.split(r'\W+', text)
    print(text_split)  # ['Ciastka', 'dżem', 'herbata', '']
    text_split_with_groups = re.split(r'(\W+)', text)
    print(text_split_with_groups)  # ['Ciastka', ', ', 'dżem', ', ', 'herbata', '.', '']


#### re.findall
Poszukuje dopasowania w podanym stringu.
W przeciwieństwie do metody `search`, zwraca listę stringów (jeżeli w wyrażeniu regularnym nie ma grup)
albo listę tupli.

    :::python3
    found = re.findall(r'[a-z]+@[a-z]+\.[a-z]{2,3}', 'Moje adresy email to: jakis@mail.com, inny@email.pl')
    print(found)  # ['jakis@mail.com', 'inny@email.pl']
    found = re.findall(r'([a-z]+)@([a-z]+)\.([a-z]{2,3})', 'Moje adresy email to: jakis@mail.com, inny@email.pl')
    print(found)  # [('jakis', 'mail', 'com'), ('inny', 'email', 'pl')]


#### re.sub
Poszukuje dopasowań w podanym stringu i zastępuje je innym wyrażeniem.
Można zastosować odwołanie do grup z dopasowania.

    :::python3
    text = 'moje tajne haslo: lubieciastka'
    text_changed = re.sub(r'(?<=haslo: )(\w)(\w+)', r'\1***', text)
    print(text_changed)  # 'moje tajne haslo: l***'



Fajne te regexy, co?
--------------------

* http://www.ex-parrot.com/~pdw/Mail-RFC822-Address.html
* https://alf.nu/RegexGolf
* https://regexcrossword.com/

