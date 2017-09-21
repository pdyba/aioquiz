Funkcje wbudowane
======================

Wywoływanie funkcji
===================

Nasz program wygląda dobrze, ale aby użytkownik mógł policzyć swój BMI,
musimy nadal jeszcze zmienić zawartość programu. Będzie wygodniej wprowadzać
potrzebne wartości w konsoli po otwarciu programu i w ten sposób otrzymać
wynik BMI.

Aby napisać taki program, musimy nauczyć się używać funkcji. Pierwszą funkcją,
jakiej się nauczymy jest help:

    >>>  help Type help() for interactive help, or help(object) for help about object.

Funkcja help jest bardzo przyjazna i mówi nam, jak powinniśmy jej używać.
Może też powiedzieć Wam, jak używać innych funkcji:

	>>>  help(input)
	Help on function input in module builtins:

	input(...) input(\[prompt\]) -> string
	Read a string from standard input. The trailing newline is stripped.

	If the user hits EOF (Unix: Ctl-D, Windows: Ctl-Z+Return), raise EOFError.
	On Unix, GNU readline is used if enabled. The prompt string, if given,
	is printed without a trailing newline before reading.

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

    >>> name = input()
    Joanna
    >>> name
    'Joanna'
    >>> print("Masz na imię:", name)
    Masz na imię: Joanna

Czy to wystarczy, by ulepszyć nasz program?

    >>> weight = input()
    60.5
    >>> weight
    '60.5'
    >>> print(w + 3)
    Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
    TypeError: Can't convert 'int' object to str implicitly

Jak widzicie, Python nie wie, jakiego wyniku oczekujemy. Stringi (`str`)
i liczby (`int`) mogą być dodawane. Python nie wie, czy odnosimy się do
liczby `63.5` czy do stringa `"60.5"`.
Tylko my to wiemy, a zatem musimy zawrzeć tę informację w programie.
