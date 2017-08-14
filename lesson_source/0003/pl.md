Wprowadzenie do Pythona
=======================

Rozpocznijmy od uruchomienia interpretera Pythona, którego
zainstalowaliśmy w poprzednim rozdziale. Proszę uruchomcie:

    :::bash
    (workshops) ~$ python
    Python 3.4.0 (...)
    Type "copyright", "credits" or "license" for more information.

    >>>


Wcześniej pracowaliśmy w wierszu poleceń systemu operacyjnego i mogliśmy
wprowadzać komendy. Znakiem zachęty był `~$`. Po uruchomieniu komendy `python`, 
znak zachęty zmienił się na `>>>`. Oznacza to dla nas, że od tej chwili możemy
używac tylko komend języka Python. Wcześniej poznane komendy (takie, jak
'cd', 'mkdir') nie będą działały. Nadszedł moment rozpoczęcia nauki
nowego języka!

Nie wpisujemy znaku zachęty `>>>` (podobnie jak `~$`) - interpreter zrobi to za nas.

Policzmy coś, na przykład: `2 + 2`:

	>>>  2 + 2 4

Python jest świetny jako kalkulator:

	>>>  6 \* 7 42 >>> 1252 - 38 \* 6 1024 >>>
	>>>  (3 - 5) \* 7 -14 >>> 21 / 7 3.0 >>> 3\*\*2 9
	>>>  5 / 2 2.5 >>> 5 % 2 1

Zwróćcie proszę szczególną uwagę na zapis liczb dziesiętnych: używajcie
kropki, a nie przecinka. Przecinki będą używane do definiowania tupli
<bmi-tuples> (więcej o tym wkrótce). Operator % to modulo, czyli reszta
z dzielenia.

Przedstaw się
=============

Stringi
-------

Jednakże liczby nie wystarczają, by efektywnie się komunikować. A zatem
musimy się nauczyć jak używać 'stringów'. Oto kilka przykładów:

	>>>  "Hello World" 'Hello World' >>> 'Foo Bar' 'Foo
	>>>  Bar' >>> "Rock 'n' Roll" "Rock 'n' Roll" >>> 'My
	>>>  name is "James"' 'My name is "James"'

Stringi możecie dodawać w następujący sposób:

	>>>  'My name is ' + '"James"' 'My name is "James"'

lub mnożyć przez liczby całkowite:

	>>>  'Hastur' \* 3 'HasturHasturHastur'

String zawsze musi zaczynać się i kończyć tym samym znakiem. Może to być 
pojedynczy cudzysłów (`'`) lub podwójny cudzysłów (`"`). Nie ma to wpływu na
wartość stringa, np. wpisanie `"Batman"` tworzy string `Batman` -
cudzysłowia nie są jego częścią, wskazują tylko, że jest to string 
(niestety, Python nie jest wystarczająco bystry, by to samemu odgadnąć).

Drukowanie stringów
-------------------

W jaki sposób prezentujemy wartości, by móc je przeczytać? Możemy to zrobić
przy użyciu komendy print:

	>>>  print("Hello World") Hello World

W podobny sposób możemy napisać kilka stringów w tej samej linii bez
konieczności dodawania ich do siebie. Będą one oddzielone spacjami:

	>>>  print("Hi, my name is", "Łukasz") Hi, my name is Łukasz

Komenda print ma wiele więcej zastosowań, gdyż może wyświetlić prawie
wszystko. W tej chwili jedynymi znanymi nam wartościami są liczby:

	>>>  print(1) 1 >>> print(1, 2, 3) 1 2 3 >>>
	>>>  print("2 + 2 =", 2 + 2) 2 + 2 = 4

Kończymy chwilowo z konsolą intraktywną. Aby z niej wyjść, wpiszcie
\`quit()::

    >>> quit()

lub przytrzymajcie Ctrl+D\` (dla Linuxa) lub `Ctrl+Z` (dla Windows).

Pliki źródłowe
==============

Dotychczas nasz kod był wykonywany w sposób interaktywny. Podawaliśmy 
poszczególne komendy i natychmiast otrzymywaliśmy odpowiedź. To świetny sposób,
by eksperymentować i uczyć się nowych składników języka, stąd ostatecznie
wrócimy to tego sposobu.

Nasz pierwszy program będzie wyglądał tak:

    print("Hi, my name is Lucas")

Aby napisać i zapisać kod w pliku, musimy użyć edytora tekstu. Poszukajcie
edytora tekstu, który działa w Waszym OS (patrz: [lista edytorów tekstów w Wikipedii]
(http://en.wikipedia.org/wiki/List_of_text_editors), by
znaleźć przykłady). Rekomendujemy Wam PyCharm lub Sublime. Sublime jest
napisany w Pythonie :). Wpiszcie w edytorze powyższy kod w Pythonie i zapiszcie
go w nowym pliku o nazwie `visitingcard.py`. Następnie uruchomcie Wasz 
pierwszy program w Pythonie w wierszu poleceń przy użyciu:

    :::bash
    (workshops) ~$ python visitingcard.py
    Hi, my name is Lucas
    (workshops) ~$

Pojedynczy program może zawierać więcej niż jedną komendę. Każda z nich
powinna być w osobnym wierszu. Na przykład:

    :::python3
    print("Hi,")
    print()

    print("my name is Lucas")

    print()
    print("Bye.")

Aby zwiększyć przejrzystość pliku `visitingcard.py`, w dowolnym jego
miejscu możemy wprowadzać puste wiersze. Tutaj oddzieliśmy nagłówek
wiadomości od jej zawartości i zakończenia.


Kalkulator BMI
==============

Napiszemy teraz prosty program do oblicznia BMI ([Body Mass
Index](http://pl.wikipedia.org/wiki/Body_Mass_Index)). Formuła do
jego obliczania wygląda nastepująco:

    BMI = (mass (kg)) / (height (m)) do kwardratu

Wiemy już jak dzielić, podnosić do potęgi i wyświetlać liczby.
Stwórzmy nowy plik o nazwie `bmi.py` i napiszmy program, który oblicza BMI:

Uruchomcie nasz program przy użyciu:

    $ python bmi.py

Otrzymujemy następujący wynik:

Jak widzicie, nasz program wymaga jeszcze poprawek:

1.  Jeśli ktoś chciałby używać tego programu, musimy zmienić zawartość
    pliku `bmi.py`.
2.  Dla kogoś, kto nie pamięta tabeli BMI, wartość 21.387755102 nie 
    będzie nic znaczyła.
3.  Wyświetlanie tak wielu miejsc dziesiętnych nie jest konieczne.
    BMI jest mierzone z dokładnością do dwóch miejsc po przecinku.

Programowanie jest sztuką rozwiązywania probelmów, a zatem... do pracy! 
Będziemy mieli możliwość nauczenia się kilku nowych właściwości Pythona.

Nazwy
=====

Spróbujmy rozwiązać pierwszy problem. Chcielibyśmy, aby nasz program był
bardziej czytelny, tzn. gdy użytkownik będzie czytał wyniki, będzie dla 
niego oczywiste, która wartość jest wagą, a która wzrostem.

Oto dlaczego tym wartościom nadajemy nazwy​​:

Wynik się nie zmienił:

Aby lepiej zrozumieć, jak funcjonują nazwy, wróćmy na chwilę do trybu
interaktywnego i nadajmy nazwy kilku wartościom:

	>>>  x = 42 >>> PI = 3.1415 >>> name =
	>>>  "Amelia" >>> print("Things:", x, PI, name) Things: 42 3.1415
	>>>  Amelia

Jedna wartość może mieć kilka nazw:

	>>>  y = x >>> print(x, y) 42 42

Możemy również zmieniać wartość przypisaną do nazwy. Nowa wartość
nie musi być tego samego typu co poprzednia wartość:

	>>>  x = 13 >>> print(x) 13 >>> x = "Scarab"
	>>>  print(x) Scarab

Nazwy są od siebie niezależne. Właśnie przypisaliśmy nową wartość
do `x`, ale wartość przypisana do `y` pozostała niezmieniona:

	>>>  print(y) 42

<div class="admonition note">

Dla tych, którzy znają już inne języki programowania:

Na pewno zastanawiacie się dlaczego nie używamy wyrażenia "zmienna".
Wynika to z tego, że nazwy w Pythonie nie funkcjonują w ten sam sposób
jak zmienne. W większości języków operacja `y = x` stworzy kopię `x` i wprowadzi
ją do zmiennej `y`.

W Pythonie nic nie jest sekretnie kopiowane.  `y` staje sie tylko alternatywną nazwą
dla tej samej wartości. Jeśli zmienicie tę wartość, zarówno `x` jak i `y`
pokaża tę samą rzecz.

W naszym przykładzie nie zmieniliśmy wartości liczby `42`, lecz tylko
wartośc przypisaną do `x` (wartości liczb nie są modyfikowane, pomimo
faktu, że w 1897 roku izba niższa stanu Indiana głosowała za zmianą wartości
liczby π na `3` - co zostało odrzucone przez Senat). Dlatego też `print(y)` da nam `42`.

</div>

Jak zobaczyliśmy w naszym programie, możemy również nadawać nazwy wynikom 
obliczeń i używać nazw w obliczeniach:

	>>>  w = 65.5 >>> h = 175.0 / 100.0 >>> bmi
	>>>  = w / h\*\*2 >>> print(w, h, bmi) 65.5 1.75
	>>>  21.387755102040817

Po obliczeniu wartość nie jest modyfikowana:

	>>>  w = 64 >>> print(w, h, bmi) 64 1.75
	>>>  21.387755102040817

Dopóki nie podamy Pythonowi komendy, by powtórzył obliczenie:

	>>>  bmi = w / h\*\*2 >>> print(w, h, bmi) 64 1.75
	>>>  20.897959183673468

Nadszedł czas, by dodać komentarze do naszego programu, aby użytkownik
(i my też!) pamiętał, że waga ma być podana w kilogramach:

Komentarze pozwalają nam wpisać dowolny teskt do naszego pythonowego 
programu. Zostaną one zignorowane przez interpreter.

Komentarzem w Pythonie jest wszystko, co wpiszemy po znaku `#` aż do
końca wiersza:

    # Weight in kilograms
    weight = 65.5

    # Height in meters
    height = 1.75

    bmi = weight / height**2 # Count BMI
    print("Your BMI is:", bmi)

Wywoływanie funckcji
==================

Nasz program wygląda dobrze, ale jeśli użytkownik zechce policzyć swój BMI, 
musimy nadal jeszcze zmienić zawartość programu. Będzie wygodniej wprowadzać
potrzebne wartości w konsoli po otwarciu programu i w ten sposób otrzymać
wynik BMI.

Aby napisać taki program, musimy nauczyć się używać funkcji. Pierwszą funcją,
jakiej się nauczymy jest help:

	>>>  help Type help() for interactive help, or help(object)
	>>>  for help about object.

Funkcja help jest bardzo przyjazna i mówi nam, jak powinniśmy jej używać.
Może też powiedzieć Wam, jak używać innych funkcji:

	>>>  help(input) Help on function input in module builtins:
	>>>  <BLANKLINE> input(...) input(\[prompt\]) -> string
	>>>  <BLANKLINE> Read a string from standard input. The trailing
	>>>  newline is stripped. If the user hits EOF (Unix: Ctl-D, Windows:
	>>>  Ctl-Z+Return), raise EOFError. On Unix, GNU readline is used if
	>>>  enabled. The prompt string, if given, is printed without a trailing
	>>>  newline before reading. <BLANKLINE>

Użyjemy funkcji input, by załadować dane podane przez użytkownika.
W opisie czytamy, że dane użytkownika input odczytuje jako string:

    :::python3
    >>> input()
    Ala has a cat
    'Ala has a cat'


Teraz nauczycie się co oznacza wyrażenie "wywołać funkcję". Możecie 
wywołać funkcję używając `()`. Jest to informacja dla interpretera, 
by wywołał funkcję. Wywołanie funkcji uruchomi funkcję. Jeśli zapomnicie
użyć `()` po nazwie funkcji, funkcja nie zostanie wywołana. W takiej
sytuacji nie otrzymacie komunikatu o błędzie, ponieważ komenda, którą
wpisaliście jest wciąż prawidłowa.

Ogólnie mówiąc, wywołana funkcja **zwraca** pewne wartości. Funkcja
input zwraca string, a zatem możemy użyć jej w ten sam sposób, jak 
wcześniej używaliśmy stringów.

Na przykład możemy użyć `input()`, by zachować podany string jako nazwę:

Czy to wystarczy, by ulepszyć nasz program?

Jak widzicie, Python nie wie, jakiego wyniku oczekujemy. Stringi (`str`)
i liczby (`int`) mogą być dodawane. Python nie wie, czy odnosimy się do
liczby `63.5` czy do stringa `"60.5"`.
Tylko my to wiemy, a zatem musimy zawrzeć tę informację w programie.

Wprowadźmy dwie nowe funkcje:

	>>>  help(int) \# doctest: +NORMALIZE\_WHITESPACE Help on
	>>>  class int in module builtins: <BLANKLINE> class int(object) |
	>>>  int(x=0) -> integer | int(x, base=10) -> integer | | Convert a
	>>>  number or string to an integer, or return 0 if no arguments | are
	>>>  given. If x is a number, return x.\_\_int\_\_(). For floating point |
	>>>  numbers, this truncates towards zero. | | ...

i

	>>>  help(float) \# doctest: +NORMALIZE\_WHITESPACE Help on
	>>>  class float in module builtins: <BLANKLINE> class float(object)
	>>>  | float(x) -> floating point number | | Convert a string or number
	>>>  to a floating point number, if possible. | | ...

Funkcja help nie waha się poinformować nas, że w rzeczywistości int i float
nie są funkcjami, ale klasami (będzie o tym mowa później), stąd dowiadujemy się
dodatkowo, że możemy ich użyć również do wielu innych rzeczy. W tej chwili
jednak potrzebujemy tylko ich podstawowej funkcjonalności - przekształcania
stringów w liczby określonego typu.

Przetestujmy int i float:

	>>>  int("0") 0 >>> int(" 63 ") 63 >>>
	>>>  int("60.5") Traceback (most recent call last): File "<stdin>",
	>>>  line 1, in <module> ValueError: invalid literal for int() with
	>>>  base 10: '60.5' >>> float("0") 0.0 >>> float(" 63 ")
	>>>  63.0 >>> float("60.5") 60.5

Zanim użyjemy w naszym programie funkcji, których właśnie się nauczyliśmy,
zaplanujmy, jak powinien on działać:

1.  Zapytaj użytkownika o wzrost.
2.  Uzyskaj string od użytkownika i zachowaj go pod nazwą `height`.
3.  Przekształć string z liczbą w liczbę z ułamkiem.
4.  Poproś użytkownika o wprowadzenie wagi.
5.  Uzyskaj string od użytkowniak i zachowaj go pod nazwą `weight`.
6.  Przekształć string z liczbą w liczbę z ułamkiem.
7.  Oblicz BMI wykorzystując zapamiętane wartości i zachwaj BMI jako `bmi`.
8.  Wyświetl obliczone BMI.

Nie ma w tym nic zaskakującego, że te osiem punktów może być wprost
przetłumaczone na osiem wierszy naszego programu (nie licząc spacji):

Możecie zapisać program do `bmi.py` i uruchomić `python bmi.py`. Resultat
powinien wyglądać następująco:

Podsumowując, aby wywołać funckję, musimy znać jej nazwę (do tej chwli
nauczyliśmy się szeregu funkcji: print, help, input, float i int) i jakich
danych ta funkcja od nas oczekuje (nazywanych listą argumentów).

Wprowadzenie samej nazwy nie uruchamia funkcji. Zostanie wyłącznie wyświetlona
informacja, że jest to funkcja:

	>>>  input \# doctest: +SKIP <built-in function input>

Aby wywołać funcję, musimy użyć nawiasów po nazwie funcji:

	>>>  input() \# doctest: +SKIP

Teraz Python wykona funkcję.

Wszystkie argumenty podajemy w nawiasach. Aby wyszczególnić więcej niż jeden,
oddzielcie je przecinkiem:

	>>>  int("FF", 16) 255


Podsumowanie
============

W tym rozdziale nauczyliśmy się podstaw składni Pythona. Odkryliśmy, jak 
wyświetlać liczby całkowite, liczby dziesiętne, stringi i tuple.

Nauczyliśmy się funkcji print, która wyświetla informacje użytkownikowi
oraz funckji input, która je pobiera.

Pomyślnie stworzyliśmy przechowywany w pliku program i uruchomiliśmy go.
Nasz program zadaje użytkownikowi kilka prostych pytań, wykonuje obliczenia
i wyświetla wyniki w formie użytecznej dla użytkownika.
