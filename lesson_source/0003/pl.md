Wprowadzenie do Pythona
=======================

Rozpocznijmy od uruchomienia interpretera Pythona, którego
zainstalowaliśmy w poprzednim rozdziale. Proszę uruchomcie:

    :::bash
    (workshops) ~$ python
    Python 3.4.0 (...)
    Type "copyright", "credits" or "license" for more information.

    >>>


Wcześniej pracowaliśmy w wierszu polecen systemu operacyjnego i mogliśmy
wprowadzac komendy. Promptem był `~$`. Po uruchomieniu komendy `python`, 
prompt zmienił się na `>>>`. Oznacza to dla nas, że od tej chwili możemy
używac tylko komend języka Python. Wcześniej poznane komendy (takie jak
'cd', 'mkdir') nie będą działały. Nadszedł moment rozpoczęcia nauki
nowego języka!

Nie wpisujemy prompta `>>>` (podobnie jak `~$`) - interpreter zrobi to za nas.

Policzmy coś, na przykład: `2 + 2`:

	>>>  2 + 2 4

Python jest świetny jako kalkulator:

	>>>  6 \* 7 42 >>> 1252 - 38 \* 6 1024 >>>
	>>>  (3 - 5) \* 7 -14 >>> 21 / 7 3.0 >>> 3\*\*2 9
	>>>  5 / 2 2.5 >>> 5 % 2 1

Zwróćcie proszę szczególną uwagę na zapis liczb dziesiętnych: używajcie
kropki,  anie przecinka. Przecinki będa używane do definiowania tupli
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

Strongi możecie dodawać w następujący sposób:

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
osobne komendy i natychmiast otrzymywaliśmy odpowiedź. To świetny sposób,
by eksperymentować i uczyć się nowych składników języka, stąd ostatecznie
wrócimy to tego sposobu.

Nasz pierwszy program będzie wyglądał tak:

    print("Hi, my name is Lucas")

Aby napisac i zapisać kod w pliku, musimy użyć edytora tekstu. Poszukajcie
edytora tekstu, który działa w waszym OS (patrz: [list of text editors on
Wikipedia](http://en.wikipedia.org/wiki/List_of_text_editors) by
znaleźc przykłady). Rekomendujemy Wam PyCharm lub Sublime. Sublime jest
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

Aby zwiększyć przejrzystość pliku `visitingcard.py` w dowolnym jego
miejscu możemy wprowadzać puste wiersze. Tutaj, oddzieliśmy nagłówek
wiadomości od jej zawartości i zakończenia.


Kalkulator BMI
==============

Napiszemy teraz prosty program do oblicznia BMI ([Body Mass
Index](http://pl.wikipedia.org/wiki/Body_Mass_Index)). Formuła do
jego obliczania wygląda nastepująco:

    BMI = (mass (kg)) / (height (m)) do kwardratu

Wiemy już jak dzielić, podnosic do potęgi i wyświetlać liczby.
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

Jedna wartośc może mieć kilka nazw:

	>>>  y = x >>> print(x, y) 42 42

Możemy również zmieniać wartość przypisaną do nazwy. Nowa wartość
nie musi być tego samego typu co poprzednia wartość:

	>>>  x = 13 >>> print(x) 13 >>> x = "Scarab"
	>>>  print(x) Scarab

Nazwy są od siebie niezależne. Właśnie przypisaliśmy nową wartość
do `x`, ale wartośc przypisana do `y` pozostała niezmieniona:

	>>>  print(y) 42

<div class="admonition note">

Dla tych, którzy znają już inne języki programowania.

Na pewno zastanawiacie się dlaczego nie używamy wyrażenia "zmienna".
Wynika to z tego, że nazwy w Pythonie nie funkcjonują w ten sam sposób
jak zmienne. W większości języków operacja `y = x` stworzy kopię `x` i wprowadzi
ją do zmiennej `y`.

W Pythonie nic nie jest sekretnie kopiowane.  `y` staje sie tylko alternatywną nazwą
dla tej samej wartości. Jesli zmienicie tę wartość, zarówno `x` jak i `y`
pokaża tę samą rzecz.

W naszym przykładzie nie zmieniliśmy wartości liczby `42`, lecz tylko
wartośc przypisaną do `x` (wartości liczb nie są modyfikowane, pomimo
faktu, że w 1897 roku izba niższa stanu Indiana głosowała za zmianą wartości
liczby π na `3` - co zostało odrzucone przez Senat). Dlatego też `print(y)` da nam `42`.

</div>

Jak zobaczyliśmy  wnaszym programie, możemy również nadawac nazwy wynikom 
obliczeń i używać nazw w obliczeniach:

	>>>  w = 65.5 >>> h = 175.0 / 100.0 >>> bmi
	>>>  = w / h\*\*2 >>> print(w, h, bmi) 65.5 1.75
	>>>  21.387755102040817

Po obliczeniu wartość nie jest modyfikowana:

	>>>  w = 64 >>> print(w, h, bmi) 64 1.75
	>>>  21.387755102040817

Until we give the Python the command to repeat the calculation again:

	>>>  bmi = w / h\*\*2 >>> print(w, h, bmi) 64 1.75
	>>>  20.897959183673468

Now is time to add some comments to our program so that the user (and us
too!) remembers that the weight has to be given in kilograms.

Comments allow us to put arbitrary text in our python program. Comments
will be ignored by the interpreter.

A comment in Python is everything after the character `#` until the end
of the line:

    # Weight in kilograms
    weight = 65.5

    # Height in meters
    height = 1.75

    bmi = weight / height**2 # Count BMI
    print("Your BMI is:", bmi)

Calling a function
==================

Our program looks good, but if a user wants to calculate his/her BMI,
they still have to change the content of the program. It would be more
convenient to enter the required values in the console after opening the
program and get the BMI result.

To write such a program, we need to learn how to use the functions. The
first function we are going to learn is help:

	>>>  help Type help() for interactive help, or help(object)
	>>>  for help about object.

The help function is very friendly and tells us how we should use it. It
can also tell you how to use the other functions:

	>>>  help(input) Help on function input in module builtins:
	>>>  <BLANKLINE> input(...) input(\[prompt\]) -> string
	>>>  <BLANKLINE> Read a string from standard input. The trailing
	>>>  newline is stripped. If the user hits EOF (Unix: Ctl-D, Windows:
	>>>  Ctl-Z+Return), raise EOFError. On Unix, GNU readline is used if
	>>>  enabled. The prompt string, if given, is printed without a trailing
	>>>  newline before reading. <BLANKLINE>

We will use input to load data from the user. As we read in the
description, input reads the string:

    :::python3
    >>> input()
    Ala has a cat
    'Ala has a cat'


Now you will learn what "calling a function" means. You can call a
function using `()`, which is an information for the interpreter to call
a function. Calling a function will run a function. If you forget to
type `()` after the function name, the function is not called. In this
situation, you will not get any informations about errors, because the
command you typed is still correct.

Generally, function calls **return** some values. The input function
returns a string, that’s why we can use it the same way that we used
strings before.

For example, we can use `input()` to save a given string as a name:

Is that enough to improve our program?

As you can see, Python doesn’t know what result we expect. Both strings
(`str`), and numbers (`int`) can't be added together. Python does not
know if we are referring to the number `63.5` or to the string `"60.5"`.
Only we know that, so we have to include this information in the
program.

Let’s introduce two more functions:

	>>>  help(int) \# doctest: +NORMALIZE\_WHITESPACE Help on
	>>>  class int in module builtins: <BLANKLINE> class int(object) |
	>>>  int(x=0) -> integer | int(x, base=10) -> integer | | Convert a
	>>>  number or string to an integer, or return 0 if no arguments | are
	>>>  given. If x is a number, return x.\_\_int\_\_(). For floating point |
	>>>  numbers, this truncates towards zero. | | ...

and

	>>>  help(float) \# doctest: +NORMALIZE\_WHITESPACE Help on
	>>>  class float in module builtins: <BLANKLINE> class float(object)
	>>>  | float(x) -> floating point number | | Convert a string or number
	>>>  to a floating point number, if possible. | | ...

The help function does not hesitate to inform us that, in fact, int and
float are not functions but classes (we will talk about those later),
hence the information about all the other things that you can use them
for. For now, we are only interested in the basic functionality of
converting strings into numbers of a determined type.

Let’s test int and float:

	>>>  int("0") 0 >>> int(" 63 ") 63 >>>
	>>>  int("60.5") Traceback (most recent call last): File "<stdin>",
	>>>  line 1, in <module> ValueError: invalid literal for int() with
	>>>  base 10: '60.5' >>> float("0") 0.0 >>> float(" 63 ")
	>>>  63.0 >>> float("60.5") 60.5

Before we use the newly learnt functions in our program, let’s make a
plan of how it should work:

1.  Ask the user to enter the height.
2.  Load the string from the user and save it under the name `height`.
3.  Change the string with the number to a number with a fraction.
4.  Ask the user to enter the weight.
5.  Load the string from the user and save it under the name of
    `weight`.
6.  Change the string with the number to a number with a fraction.
7.  Using the remembered values calculate BMI and save as `bmi`.
8.  Print the calculated BMI.

It should not surprise us that these eight points can be directly
translated into eight lines of our program (not counting spaces):

You can save this program to `bmi.py` and run `python bmi.py`. The
result should look like this:

In conclusion, to call a function we need to know its name (until now we
learnt a bunch of functions: print, help, input, int, float and quit),
and what data it expects from us (called the list of arguments).

Entering just the name does not activate the function. It will tell us
only that it is a function:

	>>>  input \# doctest: +SKIP <built-in function input>

In order to call the function, we must put parentheses after its name:

	>>>  input() \# doctest: +SKIP

Now Python will execute the function.

All arguments are given in parentheses. To specify more than one,
separate them with a comma:

	>>>  int("FF", 16) 255


Summary
=======

In this chapter we learned basics of Python syntax. We discovered how to
print integers, floating-point numbers, strings and tuples.

We learnt the function print, that prints information for the user and
the function input, which reads it.

We successfully created a program stored in a file and ran it. Our
program asks the user to answer a few simple questions, performs
calculations and presents results in the form which is useful for the
user.
