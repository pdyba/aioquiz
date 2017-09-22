Zabawy ze stringami
======================

Ostatnią kwestią, o której wspomnieliśmy wcześniej był problem ze zbyt
wieloma cyframi po przecinku w otrzymanym BMI. Z trzech problemów, jakie
mieliśmy, ten jest najłatwiejszy do rozwiązania.

Dlatego właśnie zostawiliśmy go na koniec naszej "przygody"
z kalkulatorem BMI. Wiemy, że stringi można dodawać do siebie i mnożyć
przez liczby całkowite. Zobaczycie, że możemy je także formatować.
Ale zanim to zrobimy, potrzebny jest nam jeszcze jeden typ danych
(poza stringami i liczbami, które już poznaliśmy).

Proste formatowanie
===================

Wracając do naszego programu: obecnie wynik jest zredukowany do
pojedynczej linii. Chcemy zaś stworzyć taki kalkulator BMI, który
poda nam wynik oraz przedział, w którym się on mieści, czyli:

    Twój BMI wynosi: 21.39 (prawidłowa waga)

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
całkowite są tu reprezentowane przez `i` (ang. **integer**). Możemy
również użyć `d` jako **decimal** (z ang. liczba dziesiętna). Stringi są
reprezentowane jako `s` od **string**, a liczby zmiennoprzecinkowe
jako `f` od **float** (ang. pływać, unosić się):

	>>>  "String: %s, Numery: %d %f" % ("Ala", 10, 3.1415)
	'String: Ala, Numery: 10 3.141500'

Teraz, zamiast dziewięciu miejsc po przecinku, za każdym razem otrzymamy
sześć, ale formatowanie ma tę zaletę, że umożliwia nam kontrolę nad
tym, poprzez wstawianie dodatkowej informacji pomiędzy znak `%` a literę
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
    print("| Imię i nazwisko |  Waga  |")
    print("-" * WIDTH)
    print("| %15s | %6.2f |" % ("Łukasz", 67.5))
    print("| %15s | %6.2f |" % ("Pudzian", 123))
    print("-" * WIDTH)

    .. testoutput::

    --------------------------------
    |    Imię nazwisko    |  Waga  |
    --------------------------------
    |              Łukasz |  67.50 |
    |             Pudzian | 123.00 |
    --------------------------------


Możemy również wyrównać string do lewej, umieszczając `-` przed
ilością liter:

    .. testcode::

    WIDTH = 28

    print("-" * WIDTH)
    print("| Imię i nazwisko |  Waga  |")
    print("-" * WIDTH)
    print("| %-15s | %6.2f |" % ("Łukasz", 67.5))
    print("| %-15s | %6.2f |" % ("Pudzian", 123))
    print("-" * WIDTH)

    .. testoutput::

    -------------------------------
    |    Imię nazwisko  |   Waga  |
    -------------------------------
    | Łukasz            |  67.50  |
    | Pudzian           | 123.00  |
    -------------------------------


Wyrównanie do centrum pozostawiamy Tobie :).

Formatowanie bardziej po Pythonowemu
====================================

String Slicing
==============

Spróbuj:

    >>> text = “ala ma kota”
    >>> text[0]     # string[int]
    >>> text[2:]    # string[int:]
    >>> text[:5]    # string[:int]
    >>> text[3:7]   # string[int:int]
    >>> text[::2]   # string[::int]
    >>> text[::-1]  # string[::int]
    >>> text[4:100] # string[int:int] :)

Pamiętaj! Twój komputer zawsze liczy od 0.


Metody
======

Istnieje obecnie mnóstwo metod formatowania stringów:

1.  capitalize() - zamienia pierwszą literę stringa z małej na wielką
2.  count(str, beg= 0,end=len(string)) - liczy, ile razy str pojawia się
    w stringu lub podstringu stringa, gdzie beg to początowy index, a end
    to index kończący.
3.  endswith(suffix, beg=0, end=len(string)) - ustala, czy string lub
    podstring striga kończy się podanym przyrostkiem (suffix), zwraca
    true, jeśli tak lub false, jeśli nie.
4.  find(str, beg=0 end=len(string)) - ustala, czy str pojawia się w stringu
    lub w podstringu stringa, gdy podano index początkowy beg i index końcowy
    end; zwraca index, jeśli odnajdzie str, a w przeciwnym razie zwraca -1.
5.  index(str, beg=0, end=len(string)) - podobna do metody find(), ale zgłasza błąd,
    gdy nie znajdzie str.
6.  isalnum() - zwraca true, jeśli string ma co najmniej jeden znak i wszystkie
    znaki są alfanumeryczne, jeśli nie - zwraca false.
7.  isalpha() - zwraca true, jeśli string ma conajmniej jeden znak i wszystkie
    znaki są literami, jeśli nie - zwraca false.
8.  isdigit() - zwraca true, jeśli string zawiera tylko cyfry lub false,
    jeśli nie zawiera.
9.  islower() - zwraca true, jeśli string zawiera co najmniej jedną literę
    i wszystkie litery są małe. W przeciwnym razie zwraca false.
10. isnumeric() - zwraca true, jeśli string unicode zawiera tylko cyfry,
    zaś false w przeciwnym razie.
11. isspace() - zwraca true, jeśli string zawiera wyłącznie spacje, zaś false
    w przeciwnym razie.
12. istitle() - zwraca true, jeśli wielkość liter w stringu odpowiada zasadom
    tworzenia tytułów (w ortografii anglojęzycznej), zaś false w przeciwnym wypadku.
13. isupper() - zwraca true, jeśli string zawiera co najmniej jedną literę
    i wszystkie litery są wielkie. W przeciwnym razie zwraca false.
14. join(seq) - scala (łączy) sekwencję stringów dodając pomiędzy te stringi
    wybrany separator.
15. len(string) - zwraca długość stringa.
16. lower() - zamienia wszystkie wielkie litery stringa na małe.
17. lstrip() - usuwa wszystkie spacje z początku stringa.
18. max(str) - zwraca najwyższą literę alfabetu ze stringa str.
19. min(str) - zwraca najniższą literę alfabetu ze stringa str.
20. replace(old, new \[, max\]) - zastępuje wszystkie wystąpienia stringa old
    stringiem new, a w przypadku podania ilości wystąpień max, zastępuje
    wystąpienia w ilości max.
21. rfind(str, beg=0,end=len(string)) - podobna do metody find(), ale przeszukuje
    od końca stringa wstecz.
22. rindex( str, beg=0, end=len(string)) - podobna do metody index(), ale
    przeszukuje od końca stringa wstecz.
23. rstrip() - usuwa wszystkie spacje na końcu stringa.
24. split(str="", num=string.count(str)) - rozbija string na podstawie
    podanego rozgranicznika (domyślnie spacji) i zwraca listę podstringów.
    Po podaniu parametru num rozbija string tylko do ilości num podstringów.
25. splitlines( num=string.count('n')) - rozbija string na wszystkie (lub
    na podaną ilość num) NOWE LINIE i zwraca listę linii z usuniętym znakiem NOWA LINIA.
26. startswith(str, beg=0,end=len(string)) - dstala, czy string lub podstring stringa
    (jeśli początkowy index beg i końcowy index end zostały podane) zaczyna się
    od podstringu str; zwraca true, a w przeciwnym razie zwraca false.
27. strip(\[chars\]) - przeprowadza jednocześnie metody lstrip() i rstrip() na stringu.
28. swapcase() - zamienia litery wielkie na małe, a małe na wielkie.
29. title() - zwraca "tytułową" wersję stringu, czyli wszystkie słowa zaczynające się
    wielką literą, a pozostałe elementy małą literą (według anglojęzycznej ortografii).
30. upper() - zamienia wszystkie małe litery stringa na wielkie.

Istnieje jeszcze ponad 10 innych metod, ale są one znacznie bardziej zaawansowane.


Podsumowanie
============

Dowiedzieliśmy się, jak ważna jest indentacja, zwłaszcza jeśli chcemy użyć
instrukcji if (również w połączeniu z else i elif).

To dość dużo, jak na pierwszy program. Mamy jeszcze wiele do zrobienia, mimo to
możecie być dumni z tego, co zrobiliśmy do tej pory!

A jesli zrobiliście obowiązkowe zadanie nr 1, przekonaliście się, że w Pythonie
występują jajeczka-niespodzianki i wierzcie nam - jest ich więcej. Oto kolejne:

	>>>  True + True
cwiczenia
=========
Korzystając printa i inputa napisz funkcje która pobierze i policzy BMI lub pole prostokąta:
BMI waga podzielona przez kwadrat wzrostu
bmi = m / h*h     (h**2)
Pole prostokątna bok * bok
p = a * b

1. Usuń błąd z poprzedniego zadania:
print('Twoje BMI wynosi: ' + input('Podaj wage: ') / input('Podaj  wzrost: ')**2)
print(’Pole prostkoat: ' + input(’Bok A: ') * input(’Bok B: ’))
2. Zamień string ‘123.12’ na int.

1. Sprawdź czy len działa na intach lub floatach
2. Zmień przykład wykorzystując len aby pobierał imię:
>>> print('x' * input('ile liter ma twoje imie? '))
ile liter ma twoje imie? 5
xxxxx


