Pętla for: Drzewko Bożonarodzeniowe
===================================

Idą święta, czas prezentów i choinki. Żeby poćwiczyć, spróbujemy narysować
drzewko w naszej konsoli.

Zaczniemy od najbardziej podstawowej wersji ćwiczenia, aby potem rozszerzyć
je do bardziej funkcjonalnej wersji. Na pczątek zróbmy połowę choinki:

    .. testcode::

    print("*")
    print("**")
    print("***")
    print("*")
    print("**")
    print("***")
    print("****")
    print("*")
    print("**")
    print("***")
    print("****")
    print("*****")
    print("******")


Wygląda nieźle, ale musieliśmy dużo pisać. I co, gdybyśmy chcieli mniejsze drzewko?
Albo większe, zbudowane z setek elementów na stronie rozmiaru A0?
Zdecydowanie za dużo pisania, nawet jesli chcielibyśmy wykorzystać
mnożenie stringów  (`"*" * 100`, i tak dalej).
Ale przecież jest to tak powtarzalna czynność, że możemy sprawić, by
program zrobił to za nas.

Pętla `for`
===========

Pętle służa do poradzenia sobie z takimi powtarzalnymi czynnościami.
Pozostając w świątecznej atmosferze, wyobraźmy sobie, że jesteśmy Świętym
Mikołajem i musimy przynieść każdemu prezent.

Jak wiecie, Święty Mikołaj ma listę osób, które zasługują na prezent.
Najprostszy sposób, by upewnić się, że nikt nie zostanie pominięty, to
sprawdzanie kolejno listy i dostarczanie prezentów po kolei.
Poza fizycznym aspektem tego zadania, procedura dostarczania prezentów 
mogłaby wyglądać tak:

    Niechaj Lista Ludzi zawiera ludzi, którzy powinni dostać prezenty.

    Dla każdej osoby (zwanej Osobą), która jest na Liście Ludzi:
    	Dostarcz prezent do Osoby
    
Formatowanie powyższego tekstu nie jest przypadkowe. Jest to mianowicie
program Pythona w przebraniu:

    Lista_Ludzi = ludzie_którzy_zasłużyli_na_prezenty()

    for osoba in lista_ludzi:
        dostarcz_prezent(osoba)
        print("Prezent dostarczony do:", osoba)
    print("Dostarczono wszystkie prezenty")

Większość rzeczy powinna być Ci znajoma. Uruchamiamy tutaj dwie funkcje:
ludzie_którzy_zasłużyli_na_prezenty() i dostarcz_prezent. Ich działanie
jest znane tylko Świętemu Mikołajowi. Rezultat pierwszej funkcji możemy nazwać
lista_prezentów, abyśmy mogli odwołać się do niej później (tak jak opisaliśmy
powyżej).

Nowym dla nas elementem jest sama pętla, która składa się z:

-   słowa for,
-   nazwy, jaką chcemy nadać kolejnym elementów,
-   słowa in,
-   wartości listy lub nazwie, która się do niej odnosi,
-   zawartości wciętej o jeden poziom (w taki sam sposób jak w przypadku if).

Funcja range nie tworzy listy bezpośrednio, ale zwraca tzw. generator.
Generatory generują jeden na raz element sekwencji, dzięki czemu unikamy 
przechowywania w pamięci całej sekwencji. W celu uzyskania listy sekwencji, 
używamy funkcji list. Jeśli opuścimy wywołanie funkcji list, rezultat będzie
wyglądał tak:

	>>>  range(1, 4) 
	range(1, 4)

Funkcja range może przybierać trzy formy. Najbardziej podstawowa i najczęściej
używana tworzy sekwencję od zera do podanej liczby. Kolejna forma pozwala
rozpocząć zakres od wybranej liczby i ustalić tzw. krok. Utworzona przez range 
sekwencja nigdy nie zawiera liczby podanej jako górna granica zakresu.

Wydrukujmy zatem większą choinkę:

	>>>  lst = range(1, 11) 
	>>> for i in lst: 
	.... print("*"*i) 
	*
	**
	***
	****
	*****
	******
	*******
	********
	*********
	**********

Funkcja range zaoszczędziła nam mnóstwo czasu. Możemy go zaoszczędzić
jeszcze więcej, jesli pominiemy nazwanie listy:

	>>>  for i in range(1, 5):
	... print(i\*"\#")
	#
	##
	###
	####

Gdy używamy słowa kluczowego for, nie musim uzywac listy. for obsługuje
generator podany przez range. Dlatego możemy tak bardzo uprościć nasz program.

Nic nie stoi na przeszkodzie, by umieścić pętlę w innej pętli, a zatem zróbmy to!
Pamiętajcie tylko, by użyć własciwej indentacji i zastosowac różne nazwy, np.
Nothing prevents us to put one loop inside another loop, so let's do it!
`i` i `j` (lub też lepiej odzwierciedlające zawartość listy):

	>>>  for i in range(1, 3): 
	.... for j in range(11, 14): 
	........print(i, j) 
	1 11 
	1 12 
	1 13 
	2 11 
	2 12 
	2 13


Mamy tu wewnętrzną pętlę iterującą od 11 do 13 (pamiętajcie, że 14 nie
jest zawarte w sekwencji w przypadku funcji `range`) i zewnętrzną pętlę
, która iteruje od 1 do 2.
Ja widzicie, elementy z wewętrznej pętli są wydrukowane dwukrotnie, dla
każdej iteracji pętli zewnętrznej.

Używając tej techniki, możemy powtórzyć fragment naszej choinki:

	>>>  for i in range(3):     # powtarzamy 3 razy 
	.... for rozmiar in range(1, 4): 
	........ print(rozmiar *"*")
	*
	**
	***
	*
	**
	***
	*
	**
	***

Zanim przejdziemy do kolejnego rozdziału, stwórzcie plik `choinka.py` 
z powyższym programem i spróbujcie go tak zmodyfikować, by dla każdego
z trzech powtórzeń pierwszej (zewnętrznej pętli), drugie było wykonane powtórnie.
W ten sposób powinnysmy otrzymać choinkę opisaną na początku rozdziału.

Definiowanie funkcji
====================

Zobaczyliśmy, w jaki sposób funkcje mogą rozwiązać wiele problemów. Jednakże
nie rozwiązują one wszystkich - a przynajmniej nie w sposób, w jaki chcielibyśmy,
by je rozwiązały. Czasami problem musimy rozwiązać sami. Jesli taka sytuacja powtarza
się często, byłoby miło mieć funcję, która temu zaradzi.

Możemy zrobić to w Pythonie w ten sposób:

	>>>  def wydrukuj_trójkąt(n):
	.... for rozmiar in range(1, n+1):
	........ print(rozmiar*"*") 
	>>> wydrukuj_trójkąt(3)
	*
	**
	***
	>>> wydrukuj_trójkąt(5)
	*
	**
	***
	****
	*****

Przyjrzyjmy się bliżej funkcji wydrukuj_trójkąt:

    def wydrukuj_trójkąt(n):
        for rozmiar in range(1, n+1):
            print(rozmiar*"*")

Definicja funkcji zawsze zaczyna się od słowa def. Nastwpniw, musimy
nadać nazwę naszej funkcji. W nawiasach wskazujemy, jakie nazwy powinny mieć 
jej argumenty, gdy funkcja jest wywoływana. W kolejnych wierszach podajemy
instrukcje do wykonania przez funkcję.

Jak pokazano w przykładzie, instrukcje w funkcji mogą zawierać nazwy, które
podaliśmy jako nazwy argumentów. Zasada działania wygląda następująco - 
przykład dla funkcji z trzema argumentami:

	>>>  def foo(a, b, c): 
	.... print("FOO", a, b, c)

Gdy wywołasz tę nową funckję, musisz wskazać wartości każdego argumentu.
Podobnie, jak w przypadku funkcji, które wywoływaliśmy wcześniej:

	>>>  foo(1, "Ala", 2 + 3 + 4) 
	FOO 1 Ala 9 
	>>>  x = 42
	>>>  foo(x, x + 1, x + 2) 
	FOO 42 43 44

Zauważcie, że nazwa argumentu to tylko etykieta. Gdy zmienimy wartość powiązaną 
z etykietą na inną, pozostałe etykiety się nie zmienią. To samo dzieje
się w przypadku argumentów:

	>>>  def dodaj_pięć(n): 
	.... n = n + 5 
	.... print(n)
	>>>  x = 43 
	>>> dodaj_pięć(x) 
	48 
	>>> x 
	43

Są to zwykłe nazwy (zmienne), które widzieliśmy wcześniej. Sa tylko
dwie różnice:

Po pierwsze, nazwy argumentów funkcji sa definiowane przy każdym wywołaniu funkcji, 
a Python łączy odpowiednią wartość argumentu z każdą nazwą argumentu, jaką
właśnie stworzył.

Po drugie, nazwy argumentów nie są dostępne na zewnątrz funkcji, ponieważ
są tworzone, gdy funkcja jest wywoływana i zapominane, gdy funkcja zakończy
swe działanie. Czyli, jeśli spróbujesz teraz powołać się na nazwę argumentu 
`n` zdefiniowaną w funkcji dodaj_pięć poza kodem funkcji, Python poinformuje 
Cię, że nie jest ona zdefiniowana:

	>>>  n Traceback (most recent call last): File
	>>>  "<stdin>", line 1, in <module> NameError: name 'n' is not
	>>>  defined

Czyli nasz porządnicki Python sprząta swój pokój po każdym wywołaniu funkcji :)

Zwracanie wartości
------------------

Funkcje, których wcześniej używaliśmy posiadają jedną ważną cechę, której brakuje 
funkcjom stworzonym przez nas - oddają wartość, którą wyliczyły, zamiast ją
drukować. Aby osiągnąć taki sam efekt, musisz użyć instrukcji return.
Jest to specjalna instrukcja, którą można znaleźć tylko w funkcjach.

Możemy poprawić teraz nasz kalkulator BMI dodając funkcję, która zwróci BMI:

    :::python3
    def oblicz_bmi(wzrost, waga):
        return waga / (wzrost ** 2)

Na koniec, jako ostatni przykład funkcji, podajemy rozwiązanie problemu
z końca poprzedniego rozdziału:

    .. testcode::

    # choinka.py

    def wydrukuj_trójkąt(n):
        for rozmiar in range(1, n+1):
            print(rozmiar * "*")

    for i in range(2, 5):
        wydrukuj_trójkąt(i)

    .. testoutput::

    *
    **
    *
    **
    ***
    *
    **
    ***
    ****


Kompletna choinka
=================

Poprzedni rozdział był dość teoretyczny, wykorzystamy zatem teraz tę wiedzę,
aby ukończyć nasz program wyświetlający choinkę.

A zatem:

    :::python3
    # choinka.py

    def wydrukuj_trójkąt(n):
        for rozmiar in range(1, n+1):
            print(rozmiar * "*")

    for i in range(2, 5):
        wydrukuj_trójkąt(i)

How can we improve the function print\_triangle, o display the entire
segment of the Christmas tree, not just half of it?

First of all, let’s determine how we want our result to look like for
the exact value of argument `n`. It seems to make sense that, `n` would
be the width. Then for `n = 5`, we would expect:

    *

	>>>  *\**

	>>>  ------------------------------------------------------------------------

It is worth noting that each line consists of two asterix more than the
previous one. So we can use the third argument range:

It is not exactly what we have wanted, as it should be aligned in the
centre. The method/function unicode.center mentioned in the previous
section, helps us:

	>>>  *\**

	>>>  ------------------------------------------------------------------------

However, a new problem appears:

	>>>  #### **\* \***\*
>
	>>>  > \*
>
	>>>  > *\**
>
	>>>  > ------------------------------------------------------------------------
>
	>>>  ------------------------------------------------------------------------

If we know in advance, what size the widest segment is, we can add an
additional argument to print\_segment, to align to the width. Combining
all of the knowledge we have acquired up to the moment:

---
title: while loop
---

We discoused the for loop, but there is also a while loop

:::python3
while expression:
    statement(s)

    :::python3
    number = 0
    while (number < 9):
       print('Number:', count)
       number = number + 1

    print("Finished!")


A loop becomes infinite loop if a condition never becomes FALSE. You
must use caution when using while loops because of the possibility that
this condition never resolves to a FALSE value. This results in a loop
that never ends. Such a loop is called an infinite loop.



    :::python3
    number = 1
    while number:
       print('Number:', count)
       number = number + 1

    print("Finished!")


Above example goes in an infinite loop and you need to use CTRL+C (or
CTRL+D) to exit the program.

Else in while loop:
===================

If the else statement is used with a while loop, the else statement is
executed when the condition becomes false.

    :::python3
    number = 0
    while number < 6:
       print(number, " is  less than 6")
       number = number + 1
    else:
       print(number, " is not less than 6")

    print("Finished!")
