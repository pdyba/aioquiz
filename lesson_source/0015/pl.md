Pętla dla każdego (for) zrobię coś fajnego
======================
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

Nowym dla nas elementem jest sama pętla, która składa się ze:

-   słowa for,
-   nazwy, jaką chcemy nadać kolejnym elementom,
-   słowa in,
-   wartości listy lub nazwy, która się do niej odnosi,
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

	>>>  lista = range(1, 11)
	>>>  for i in lista:
	........ print("*"*i)
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
jeszcze więcej, jeśli pominiemy nazwanie listy:

	>>>  for i in range(1, 5):
	........ print(i*"#")
	#
	##
	###
	####

Gdy używamy słowa kluczowego for, nie musimy używać listy. for obsługuje
generator podany przez range. Dlatego możemy tak bardzo uprościć nasz program.

Nic nie stoi na przeszkodzie, by umieścić pętlę w innej pętli, a zatem zróbmy to!
Pamiętajcie tylko, by użyć właściwej indentacji i zastosować różne nazwy, np.
`i` i `j` (lub też lepiej odzwierciedlające zawartość listy):

	>>>  for i in range(1, 3):
	........ for j in range(11, 14):
	............. print(i, j)
	1 11
	1 12
	1 13
	2 11
	2 12
	2 13


Mamy tu wewnętrzną pętlę iterującą od 11 do 13 (pamiętajcie, że 14 nie
jest zawarte w sekwencji w przypadku funkcji `range`) i zewnętrzną pętlę,
która iteruje od 1 do 2.
Jak widzicie, elementy z wewnętrznej pętli są wydrukowane dwukrotnie, dla
każdej iteracji pętli zewnętrznej.

Używając tej techniki, możemy powtórzyć fragment naszej choinki:

	>>>  for i in range(3):     # powtarzamy 3 razy
	........ for rozmiar in range(1, 4):
	............ print(rozmiar * "*")
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
W ten sposób powinniśmy otrzymać choinkę opisaną na początku rozdziału.

Definiowanie funkcji
====================

Zobaczyliśmy, w jaki sposób funkcje mogą rozwiązać wiele problemów. Jednakże
nie rozwiązują one wszystkich - a przynajmniej nie w sposób, w jaki chcielibyśmy,
by je rozwiązały. Czasami problem musimy rozwiązać sami. Jeśli taka sytuacja powtarza
się często, byłoby miło mieć funcję, która temu zaradzi.

Możemy zrobić to w Pythonie w ten sposób:

	>>>  def wydrukuj_trójkąt(n):
	........ for rozmiar in range(1, n+1):
	............ print(rozmiar*"*")
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
    .... for rozmiar in range(1, n+1):
    ........ print(rozmiar*"*")

Definicja funkcji zawsze zaczyna się od słowa def. Następnie musimy
nadać nazwę naszej funkcji. W nawiasach wskazujemy, jakie nazwy powinny mieć
jej argumenty, gdy funkcja jest wywoływana. W kolejnych wierszach podajemy
instrukcje do wykonania przez funkcję.

Jak pokazano w przykładzie, instrukcje w funkcji mogą zawierać nazwy, które
podaliśmy jako nazwy argumentów. Zasada działania wygląda następująco -
przykład dla funkcji z trzema argumentami:

	>>>  def foo(a, b, c):
	........ print("FOO", a, b, c)

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
	........ n = n + 5
	........ print(n)
	>>>  x = 43
	>>>  dodaj_pięć(x)
	48
	>>>  x
	43

Są to zwykłe nazwy (zmienne), które widzieliśmy wcześniej. Są tylko
dwie różnice:

Po pierwsze, nazwy argumentów funkcji są definiowane przy każdym wywołaniu funkcji,
a Python łączy odpowiednią wartość argumentu z każdą nazwą argumentu, jaką
właśnie stworzył.

Po drugie, nazwy argumentów nie są dostępne na zewnątrz funkcji, ponieważ
są tworzone, gdy funkcja jest wywoływana i zapominane, gdy funkcja zakończy
swe działanie. Czyli, jeśli spróbujesz teraz powołać się na nazwę argumentu
`n` zdefiniowaną w funkcji dodaj_pięć poza kodem funkcji, Python poinformuje
Cię, że nie jest ona zdefiniowana:

	>>>  n Traceback (most recent call last): File
	     "<stdin>", line 1, in <module> NameError: name 'n' is not
	     defined

Czyli nasz porządnicki Python sprząta swój pokój po każdym wywołaniu funkcji :)

Zwracanie wartości
------------------

Funkcje, których wcześniej używaliśmy posiadają jedną ważną cechę, której brakuje
funkcjom stworzonym przez nas - odostępniają wartość, którą wyliczyły, zamiast ją
drukować. Aby osiągnąć taki sam efekt, musisz użyć instrukcji return.
Jest to specjalna instrukcja, którą można znaleźć tylko w funkcjach.

Możemy poprawić teraz nasz kalkulator BMI dodając funkcję, która zwróci BMI:

    :::python3
    def oblicz_bmi(wzrost, waga):
    .... return waga / (wzrost ** 2)

Na koniec, jako ostatni przykład funkcji, podajemy rozwiązanie problemu
z końca poprzedniego rozdziału:

    .. testcode::

    # choinka.py

    def wydrukuj_trójkąt(n):
    .... for rozmiar in range(1, n+1):
    ........ print(rozmiar * "*")

    for i in range(2, 5):
    .... wydrukuj_trójkąt(i)

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

W jaki sposób możemy poprawić funkcję wydrukuj_trójkąt, aby wyświetlić
cały segment choinki, a nie tylko jego połowę?

Przede wszystkim, ustalmy jak chcemy aby wyglądał rezultat dla określonej
wartości argumentu `n`. Wydaje się mieć sens, że `n` byłby szerokością
A zatem dla `n = 5` oczekiwalibyśmy:

      *
     ***
    *****

Warto zauważyć, że każdy kolejny wiersz zawiera o dwie więcej gwiazdki, niż
poprzedni wiersz. Możemy użyć tu trzeciego argumentu funkcji range:

    .. testcode::

    def wydrukuj_segment(n):
        for rozmiar in range(1, n+1, 2):
            print(rozmiar * "*")

    wydrukuj_segment(5)

    .. testoutput::

    *
    ***
    *****

Nie jest to dokładnie to, czego chcieliśmy, bo segment powinien być wyśrodkowany.
Pomoże nam tutaj metoda/funkcja center():

    .. testcode::

    def wydrukuj_segment(n):
        for rozmiar in range(1, n+1, 2):
            print((rozmiar * "*").center(n))

    print_segment(5)

    .. testoutput::

      *
     ***
    *****

Jednak pojawił się nowy problem:

      *
     ***
       *
      ***
     *****
        *
       ***
      *****
     *******

Gdybyśmy wiedzieli zawczasu, jaki rozmiar ma najszerszy segment, moglibyśmy
wykorzystać dodatkowy argument w funkcji wydrukuj_segment, by wyrównać
choinkę do tej szerokości. Podsumujmy wiedzę, jaką zdobyliśmy do tej pory:

    def wydrukuj_segment(n, łączna_szerokość):
            for rozmiar in range(1, n+1, 2):
                 print((rozmiar * "*").center(łączna_szerokość))

    def wydrukuj_choinkę(rozmiar):
        for i in range(3, rozmiar+1, 2):
            wydrukuj_segment(i, rozmiar)

    print("Wybierz rozmiar choinki:")
    n = int(input())
    wydrukuj_choinkę(n)

    Wybierz rozmiar choinki:
    7
       *
      ***
       *
      ***
     *****
       *
      ***
     *****
    *******



Pętla while
-----------

Omówiliśmy pętlę for, ale istnieje jeszcze pętla while:

    :::python3
    while wyrażenie:
    komenda(y)

    :::python3
    liczba = 0
    while (liczba < 9):
       print('Liczba:', liczba)
       liczba = liczba + 1

    print("Koniec!")


Pętla staje się pętlą nieskończoną, gdy warunek nigdy nie przybiera wartości
FALSE. Musisz uważać używając pętli while, z uwagi na ryzyko, że pętla nigdy
nie osiągnie wartości FALSE. Wynikiem tego jest pętla, która nigdy się nie
kończy. Taką pętlę nazywamy nieskończoną pętlą.


    :::python3
    liczba = 1
    while liczba:
       print('Liczba:', liczba)
       liczba = liczba + 1

    print("Koniec!")

Powyższy przykład generuje pętlę nieskończoną i musisz użyć CTRL+C (lub
CTRL+D), by wyjść z programu.

Else w pętli while
===================

W przypadku użycia komendy else w pętli while, komenda else zostanie
wykonana, gdy warunek przybierze wartość FALSE.

    :::python3
    liczba = 0
    while liczba < 6:
       print(liczba, " jest mniejsze niż 6")
       liczba = liczba + 1
    else:
       print(liczba, " nie jest mniejsze niż 6")

    print("Koniec!")