Stringi i jak się nimi bawić
============================

Ostatnią kwestią, o której wspomnieliśmy wcześniej był problem ze zbyt
wieloma cyframi po przecinku w otrzymanym BMI. Z trzech problemów, jakie
mieliśmy, ten jest najłatwiejszy do rozwiązania.

Dlatego właśnie zostawiliśmy go na koniec naszej "przygody" 
z kalkulatorem BMI. Wiemy, że stringi można dodawać do siebie i mnożyć
przez liczby całkowite. Zobaczycie, że możemy je także formatować.
Ale zanim to zrobimy, potrzebny jest nam jeszcze jeden typ danych 
(poza stringami i liczbami, które już poznaliśmy).

Tuple
=====

Na początku wspomnieliśmy, że nie możemy używać przecinków w liczbach,
bo będziemy potrzebowali ich w tuplach. Doszliśmy właśnie do tego
momentu:

	>>>  1, 2, 3
	(1, 2, 3) 
	>>> ("Ala", 15)
	('Ala', 15)
	>>>  x = 1,5 
	>>> print(x) 
	(1, 5)

Tupla to nic innego, jak zbiór kilku wartości. Wartości te odddzielamy
przecinkami. Zbiór najczęściej otaczamy nawiasami zwykłymi, ale nie jest to
konieczne. Chyba, że chcemy objąć zbiorem zero elementów (jakkolwiek 
dziwnie to może brzmieć):

	>>> () 
	()

Tuple możemy łączyć:

	>>> mazwy = ("Paulina", "Kowalska") 
	>>> szczegóły = (27, 1.70) 
	>>> nazwy + szczegóły ('Paulina', 'Kowalska', 27, 1.7)

Możemy w nich także zawrzeć inne tuple, np. punkty na mapie możemy
zgrupować nastepująco:

	>>>  punkt = ("Nazwa punktu", (x, y))

gdzie `x` i `y` to liczby.

Możemy odwoływać się do tak zgrupowanych wartości poprzez ich kolejną
pozycję w tupli (zaczynając od zera), np.:

	>>> p = (10, 15)
	>>> p[0] # pierwsza wartość 
	10
	>>> p[1] # druga wartość
	15

Proste formatowanie
===================

Wracając do naszego programu: obecnie wynik jest zredukowany do
pojedynczej linii. Chcemy zaś stworzyć taki kalkulator BMI, który
poda nam wynik oraz przedział, w którym się on mieści, czyli:

    Twoje BMI wynosi: 21.39 (prawidłowa waga)

Zmodyfikuj swój istniejący program tak, by obliczone BMI było dostępne
pod zmienną `bmi`, a nazwa przedziału pod nazwą `kategoria`.  Użyj print,
aby wyświetlić otrzymany wynik:

    .. testsetup::

    bmi = 21.387755102040817
    kategoria = "prawidłowa waga"
    
    .. testcode::

    print("Twój BMI wynosi:", bmi, "(" + kategoria + ")")
    
    .. testoutput::
    :hide:

    Twój BMI wynosi: 21.387755102040817 (prawidłowa waga)


Cóż, prawie... Nadal mamy zbyt wiele liczb po przecinku. Napotkamy
także problem, jeśli będziemy chcieli utworzyć taki string i nadać 
mu nazwę, bo użyliśmy funkcji print oddzielając składniki. Na szczęście
jest lepszy sposób:

    >>> bmi = 21.387755102040817
    >>> kategoria = "prawidłowa waga"
    >>> wynik = "Twój BMI wynosi: %f (%s)" % (bmi, kategoria)
    >>> wynik
    'Twój BMi wynosi: 21.387755 (prawidłowa waga)'
    >>> print(wynik)
    Twój BMI wynosi: 21.387755 (prawidłowa waga)

Użyliśmy tutaj stringa i tupli połączonych znakiem `%`. String jest 
szablonem, który zostaje uzupełniony wartościami z tupli. Miejsca,
które mają być uzupełnione są oznaczone znakiem procentu (`%`). Litera
następująca po nim definiuje typ zmiennej, jaką chcemy wstawić. Liczby
całkowite sś tu reprezentowane przez `i` (ang. **integer**). Możemy 
również użyć `d` jako **decimal** (z ang. liczba dziesiętna). Stringi są
reprezentowane jako `s` od **string**, a liczby zmiennoprzecinkowe
jako `f` od **float** (ang. pływać, unosić się):

	>>>  "String: %s, Numery: %d %f" % ("Ala", 10, 3.1415)
	'String: Ala, Numery: 10 3.141500'

Teraz, zamiast dziewięciu miejsc po przecinku, za każdym razem otrzymamy 
sześć, ale formatowanie ma tę zaletę, że umożliwia nam kontrolę nad
tym, poprzez wstawianie dodatkowej informacji pomiędzy znak `%` i literę
`f`, np. jeśli chcielibyśmy wyświetlać tylko dwa miejsca po przecinku,
zamiast sześciu:

	>>> "%.2f" % 3.1415 
	'3.14' 
	>>> "%.2f" % 21.387755102040817 
	'21.39'

Istnieje mnóstwo opcji formatowania. Niestety nie pokażemy ich tu wszystkich.
Jedna z najbardziej użytecznych to wyrównywanie do określonej ilości
znaków:

    .. testcode::

    WIDTH = 28

    print("-" * WIDTH)
    print("| Name and last name |  Weight  |")
    print("-" * WIDTH)
    print("| %15s | %6.2f |" % ("Łukasz", 67.5))
    print("| %15s | %6.2f |" % ("Pudzian", 123))
    print("-" * WIDTH)
    
    .. testoutput::

    --------------------------------
    | Name and last name  |  Weight|
    --------------------------------
    |              Łukasz |  67.50 |
    |             Pudzian | 123.00 |
    --------------------------------


Możemy również wyrównać string do lewej, umieszczając `-` przed
ilością liter:

    .. testcode::

    WIDTH = 28

    print("-" * WIDTH)
    print("| Name and last name |  Weight |")
    print("-" * WIDTH)
    print("| %-15s | %6.2f |" % ("Łukasz", 67.5))
    print("| %-15s | %6.2f |" % ("Pudzian", 123))
    print("-" * WIDTH)
    
    .. testoutput::

    -------------------------------
    | Name and last name|  Weight |
    -------------------------------
    | Łukasz            |  67.50  |
    | Pudzian           | 123.00  |
    -------------------------------


Wyrównanie do centurm pozostawiamy Tobie :).

Formatowanie bardziej po Pythonowemu
====================================

String Slicing
==============

Spróbuj: 

    >>> text = “ala ma kota” 
    >>> text[0] #string[int] 
    >>> text[2:] # string[int:] 
    >>> text[:5] # string[:int] 
    >>> text[3:7] #string[int:int] 
    >>> text[::2] # string[::int]
    >>>  text[::-1] # string[::int]

Pamiętaj! Twój komputer zawsze liczy od 0.


Metody
======

Istnieje obecnie mnóstwo metod formatowania stringów:

1.  capitalize() - zamienia pierwszą literę stringa z małej na wielką
2.  count(str, beg= 0,end=len(string)) - liczy, ile razy str pojawia się
    w stringu lub opodstringu stringa, gdzie beg to początowy index, a end
    to index kończący.
3.  endswith(suffix, beg=0, end=len(string)) - ustala, czy string lub
    podstring striga kończy się podanym przyrostkiem (suffix), zwraca 
    true, jeśli tak lub false, jeśli nie.
4.  find(str, beg=0 end=len(string)) - ustala, czy str pojawia się w stringu
    lub w podstringu stringa, gdy podano index początkowy beg i index końcowy
    end, zwraca index, jeśli odnajdzie str lub -1 w przeciwnym razie
5.  index(str, beg=0, end=len(string)) - podobna do metody find(), ale zgłasza błąd,
    gdy nie znajdzie str.
6.  isalnum() - Zwraca true, jeśli string ma conajmniej jeden znak i wszystkie
    znaki są alfanumeryczne, jeśli nie - zwraca false.
7.  isalpha() - Zwraca true, jeśli string ma conajmniej jeden znak i wszystkie 
    znaki sa literami, jeśli nie - zwraca false.
8.  isdigit() - Zwraca true, jeśli string zawira tylko cyfry lub false,
    jeśli nie zawiera.
9.  islower() - Zwraca true, jeśli string zawiera co najmniej jedną literę
    i wszystkie litery są małe. W przeciwnym razie zwraca false.
10. isnumeric() - Zwraca true, jeśli string unicode zawiera tylko cyfry,
    zaś false w przeciwnym razie.
11. isspace() - Zwraca true, jeśli string zawiera wyłącznie spacje, zaś false
    w przeciwnym razie.
12. istitle() - Zwraca true, jeśli wielkość liter w stringu odpowiada zasadom
    tworzenia tytułów, zaś false w przeciwnym wypadku.
13. isupper() - Zwraca true, jeśli string zawiera co najmniej jedną literę
    i wszystkie litery są wielkie. W przeciwnym razie zwraca false.
14. join(seq) - Scala (łączy) sekwencję stringów dodając pomiędzy te stringi
    wybrany separator.
15. len(string) - Zwraca długość stringa.
16. lower() - Zamienia wszystkie wielkie litery stringa na małe.
17. lstrip() - Usuwa wszystkie spacje z początku stringa.
18. max(str) - Zwraca najwyższą literę alfabetu ze stringa str.
19. min(str) - Zwraca najniższą literę alfabetu ze stringa str.
20. replace(old, new \[, max\]) - Zastępuje wszystkie wystąpienia stringa old
    stringiem new, a w przypadku podania ilości wystąpień max, zastępuje 
    wystąpienia w ilości max.
21. rfind(str, beg=0,end=len(string)) - podobna do metody find(), ale przeszukuje
    od końca stringa wstecz.
22. rindex( str, beg=0, end=len(string)) - podobna do metody index(), ale 
    przeszukuje od końca stringa wstecz.
23. rstrip() - Usuwa wszystkie spacje na końcu stringa.
24. split(str="", num=string.count(str)) - Rozbija string na podstawie
    podanego rozgranicznika (domyślnie spacji) i zwraca listę podstringów.
    Po podaniu parametru num rozbija string tylko do ilości num podstringów.
25. splitlines( num=string.count('n')) - Rozbija string na wszystkie (lub 
    na podaną ilość num) NOWE LINIE i zwraca listę linii z uusniętym znakiem NOWA LINIA.
26. startswith(str, beg=0,end=len(string)) - Ustala, czy string pod podstring stringa
    (jeśli początkowy index beg in końcowy index end zostały podane) zaczyna się 
    od podstringu str; zwraca true, a w przeciwnym razie zwraca false.
27. strip(\[chars\]) - Przeprowadza jednocześnie metody lstrip() i rstrip() na stringu
28. swapcase() - Zamienia litery wielkie na małe, a małe na wielkie.
29. title() - Zwraca "tytułową" wersję stringu, czyli wszystkie słowa zaczynające się 
    wielką literą, a pozostałe elementy małą literą (według anglojęzycznej ortografii).
30. upper() - Zamienia wszystkie małe litery stringa na wielkie.

Istnieje jeszcze ponad 10 innych metod, ale są one znacznie bardziej zaawansowane.


Podsumowanie
============

Dowiedzieliśmy się, jak ważna jest indentacja, zwłaszcza jeśli chcemy użyć
instrukcji if (również w połączeniu z else i elif).

To dość dużo, jak na pierwszy program. Mamy jeszcze wiele do zrobienia, mimo to
możecie być dumni z tego, co zrobiliśmy do tej pory!

A jesli zrobiliście obowiązkowe zadanie nr 1, przekonaliście się, że w Pythonie
występują jajeczka-niespodzianki i jest ich więcej. Oto kolejne:

	>>>  True + True

:-)
