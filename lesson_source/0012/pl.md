Warunkowe warunki
======================


Indentacja
----------

Kolejną rzeczą, na którą powinniście zwrócić uwagę w kodzie jest indentacja.
Otwórzcie interpreter i wprowadźcie taki warunek:

    >>> if 2 > 1:
    ...

Do tej pory nic się nie wydarzyło, na co wskazują kropki `...`, zamiast
znaku ponaglenia `>>>`, który widzieliśmy do tej pory. Python spodziewa się,
że podamy dalsze instrukcje, które mają być wykonane, gdy warunek
`2 > 1` okaże się prawdziwy. Spróbujmy sprawić, by Python wydrukował "OK":


    :::python3
    >>> if 2 > 1:
    ... print("OK")
      File "<stdin>", line 2
        print("OK")
            ^
    IndentationError: expected an indented block

Niestety, nie powiodło się. Python musi wiedzieć, czy instrukcja, którą wpisaliśmy
jest kontynuacją warunku if, czy jest kolejną instrukcją nie związaną z warunkiem.
W tym celu musimy w kodzie zastosować indentację:


	>>>  if 2 > 1:
	..... print("OK")
	OK

Wystarczy, że wpiszemy jedną spację lub naciśniemy `TAB`. Ważne jest jednak,
żeby wszystkie linie, które chcemy, by były wykonane po kolei miały identyczną
indentację:


    :::python3
    >>> if -1 < 0:
    ...  print("A")
    ...   print("B")
      File "<stdin>", line 3
        print("B")
        ^
    IndentationError: unexpected indent

    >>> if -1 < 0:
    ...     print("A")
    ...   print("B")
      File "<stdin>", line 3
        print("B")
                ^
    IndentationError: unindent does not match any outer indentation level

    >>> if -1 < 0:
    ...... print("A")
    ...... print("B")
    A
    B

By uniknąć chaosu, większość programistów używa czterech spacji dla
każdego poziomu indentacji. Zróbmy tak samo:

	>>>  if 2 > 1:
	........ if 3 > 2:
	............ print("OK")
	........ else:
	............ print("FAIL")
	.... print("DONE")
	OK
	DONE

A co, jeśli nie?
----------------

Właściwie moglibyśmy napisać nasz program tylko używając if:

    :::python3
    if bmi < 18.5:
        print("niedowaga")
    if bmi >= 18.5:
        if bmi < 25.0:
            print("prawidłowa waga")
    if bmi >= 25.0:
        print("nadwaga")

Możemy także użyć else i elif, aby uniknąć powtarzania takich samych warunków
i poprawić czytelność kodu. W bardziej złożonych programach może nie być
od początku oczywiste, że pewien warunek jest przeciwnością poprzedniego.

Używając else mamy gwarancję, że podane instrukcje będą wykonane tylko,
jeśli instrukcje podane pod if nie zostały wykonane:

    :::python3
    if bmi < 18.5:
        print("niedowaga")
    else:
        # jeśli Twój program wykona tę istrukcję, bmi na pewno jest >= 18.5!
        if bmi < 25.0:
            print("prawidłowa waga")
        else:
            # teraz już na pewno bmi jest >= 25.0, nawet nie musimy sprawdzać
            print("nadwaga")

Zwróć szczególną uwagę na wszystkie indentacje. Każde użycie else spowoduje
zwiększenie indentacji w Twoim kodzie.
To bardzo irytujące, gdy musisz sprawdzać kilka lub jakiś tuzin warunków,
które się wzajemnie wykluczają. Stąd twórcy Pythona dodali małe
'ulepszenie' w formie elif - instrukcję, która pozwala Ci sprawdzić
niezwłocznie kolejny warunek:

    :::python3
    if n < 1:
        print("jeden")
    elif n < 2:
        # jeśli n nie było < 1, a teraz n jest < 2
        print("dwa")
    elif n < 3:
        # jeśli żaden z dwóch wcześniejszych warunków nie był prawdziwy,
        # czyli n >= 1 i n>= 2, ale n < 3
        print("trzy")
    else:
        # trole liczą tylko do trzech
        print("więcej")

Dane do zadań:
==============


| BMI          | KOBIETY         |
|--------------|-----------------|
| < 17,5       | niedowaga       |
| 17,5 – 22,49 | prawidłowa waga |
| 22,5 – 27,49 | nadwaga         |
| ≥ 27,5       | otyłość         |


| BMI          | MĘŻCZYŹNI       |
|--------------|-----------------|
| < 19.99      | niedowaga       |
| 20 – 24,99   | prawidłowa waga |
| 25,0 – 29,99 | nadwaga         |
| ≥ 30,0       | otyłość         |

Podsumowanie
============

A zatem poznaliśmy trochę podstawowej logiki pythonowej i możemy zacząć jej używać.