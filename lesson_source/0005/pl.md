Stringi i jak się nimi bawić
============================

Ostatnią kwestią, o której wspomnieliśmy wcześniej był problem ze zbyt
wieloma cyframi po przecinku w otrzymanym BMI. Z trzech problemów, jakie
mieliśmy, ten jest najłatwiejszy do rozwiązania.

Dlatego własnie zostawiliśmy go na koniec naszej "przygody" 
z kalkulatorem BMI. Wiemy, że stringi można dodawac do siebie i mnożyć
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
przecinkami. Zbiór zwykle otaczamy nawiasami zwykłymi, ale nie jest to
konieczne. Chyba, że chcemy objąć zbiorem zero elementów (jakkolwiek 
dziwnie to może brzmieć):

	>>> () 
	()

Tuple możemy łączyć:

	>>> names = ("Paulina", "Kowalska") 
	>>> details = (27, 1.70) 
	>>> names + details ('Paulina', 'Kowalska', 27, 1.7)

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
poda nam wynik oraz przedział, w którym się sie on mieści, czyli:

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


Cóż, prawie... Naal mamy zbyt wiele liczb po przecinku. Napotkamy
także problem, jeśli będziemy chcieli utworzyć taki string i nadać 
mu nazwę, bo użyliśmy funkcji print oddzielając składniki. Na szczęście
jest lepszy sposób:

Well, almost….We still have too many digits. We would also have a
problem if we wanted to generate such a string and save with a name,
because we use print to separate the elements. Fortunately, there is a
better way:

    >>> bmi = 21.387755102040817
    >>> kategoria = "prawidłowa waga"
    >>> wynik = "Twój BMI wynosi: %f (%s)" % (bmi, kategoria)
    >>> wynik
    'Twój BMi wynosi: 21.387755 (prawidłowa waga)'
    >>> print(wynik)
    Twój BMI wynosi: 21.387755 (normal weight)

Użyliśmy tutaj stringa i tupli połączonych znakiem `%`. String jest 
szablonem, który zostaje uzupełniony wartościami z tupli. Miejsca,
które mają być uzupełnione są oznaczone znakiem procentu (`%`). Litera
następująca po nim definiuje typ zmiennej, jaką chcemy wstawić. Liczby
całkowite sa tu reprezentowane przez `i` (ang. **integer**). Możemy 
również użyć `d` jako **decimal** (z ang. liczba dziesiętna). Stringi są
reprezentowane jako `s` od **string**, a liczby zmiennoprzecinkowe
jako `f` od **float** (ang. pływać, unosić się):


We have here a string and a tuple joined by `%`. The string is a
template which will be completed with values from the tuple. The spaces
to be filled are also labeled with the percentage (`%`). . The letter
that follows defines the type of a value we want to insert. The integers
are represented by `i` as **integer** (we can also use `d` as
**decimal**), strings are represented by `s` as **string**, and
floating-point numbers are represented by `f` for **float**:

	>>>  "String: %s, Numery: %d %f" % ("Ala", 10, 3.1415)
	'String: Ala, Numery: 10 3.141500'

Teraz zamiast dziewięciu miejsc po przecinku za każdym razem otrzymamy 
sześć, ale formatowanie ma tę zaletę, że umożliwia nam na kontrolę nad
tym, poprzez wstawianie dodatkowej informacji pomiędzy znak `%` i literę
`f`, np. jesli chcielibyśmy wyświetlać tylko dwa miejsca po przecinku,
zamiast sześciu:
Now instead of nine decimal places we always get six, but the formatting
has the advantage that it allows us to have more control by putting
between `%` and `f` additional information, e.g. if you want to display
only two places after the decimal point:

	>>> "%.2f" % 3.1415 
	'3.14' 
	>>> "%.2f" % 21.387755102040817 
	'21.39'

Istenieje mnóstwo opcji formatowania. Nie pokażemy ich tu wszystkich.
Jdna z najbardziej użytecznych to wyrównywanie do określonej ilości
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

1.  capitalize() - Zamienia pierwszą literę stringa z małej na wielką
2.  count(str, beg= 0,end=len(string)) - Liczy, ile razy str pojawia się
    w stringu lub opodstringu stringa, gdzie beg to początowy index, a end
    to index kończący.
3.  endswith(suffix, beg=0, end=len(string)) - ustala, czy string lub
    podstring striga kończy się podanym przyrostkiem (suffix), zwraca 
    true, jeśli tak lub false, jeśli nie.
4.  find(str, beg=0 end=len(string)) - Determine if str occurs in string
    or in a substring of string if starting index beg and ending index
    end are given returns index if found and -1 otherwise.
5.  index(str, beg=0, end=len(string)) - Same as find(), but raises an
    exception if str not found.
6.  isalnum() - Returns true if string has at least 1 character and all
    characters are alphanumeric and false otherwise.
7.  isalpha() - Returns true if string has at least 1 character and all
    characters are alphabetic and false otherwise.
8.  isdigit() - Returns true if string contains only digits and false
    otherwise.
9.  islower() - Returns true if string has at least 1 cased character
    and all cased characters are in lowercase and false otherwise.
10. isnumeric() - Returns true if a unicode string contains only numeric
    characters and false otherwise.
11. isspace() - Returns true if string contains only whitespace
    characters and false otherwise.
12. istitle() - Returns true if string is properly "titlecased" and
    false otherwise.
13. isupper() - Returns true if string has at least one cased character
    and all cased characters are in uppercase and false otherwise.
14. join(seq) - Merges (concatenates) the string representations of
    elements in sequence seq into a string, with separator string.
15. len(string) - Returns the length of the string
16. lower() - Converts all uppercase letters in string to lowercase.
17. lstrip() - Removes all leading whitespace in string.
18. max(str) - Returns the max alphabetical character from the string
    str.
19. min(str) - Returns the min alphabetical character from the string
    str.
20. replace(old, new \[, max\]) - Replaces all occurrences of old in
    string with new or at most max occurrences if max given.
21. rfind(str, beg=0,end=len(string)) - Same as find(), but search
    backwards in string.
22. rindex( str, beg=0, end=len(string)) - Same as index(), but search
    backwards in string.
23. rstrip() - Removes all trailing whitespace of string.
24. split(str="", num=string.count(str)) - Splits string according to
    delimiter str (space if not provided) and returns list of
    substrings; split into at most num substrings if given.
25. splitlines( num=string.count('n')) - Splits string at all (or num)
    NEWLINEs and returns a list of each line with NEWLINEs removed.
26. startswith(str, beg=0,end=len(string)) - Determines if string or a
    substring of string (if starting index beg and ending index end are
    given) starts with substring str; returns true if so and false
    otherwise.
27. strip(\[chars\]) - Performs both lstrip() and rstrip() on string
28. swapcase() - Inverts case for all letters in string.
29. title() - Returns "titlecased" version of string, that is, all words
    begin with uppercase and the rest are lowercase.
30. upper() - Converts lowercase letters in string to uppercase.

There is over 10 more methods but they are much more advanced.


Summary
=======

We also know now that indentations can be important, especially when we
want to use the instruction if (also in connection with else and elif).

This is quite a lot like for a first program. We still have a lot of
work, anyhow you can be proud of what we have done so far!

And if You did the obligatory task 1 You know there are some easter eggs
in python and thats not all of them. Here is one more:

	>>>  True + True

:-)
