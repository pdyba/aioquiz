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

	>>>  range(1, 4) range(1, 4)

The range function has three forms. The most basic and most used one
creates a sequence from 0 to the given number. The other forms allow you
to specify the start of the range and a step. The created sequence never
includes the end of the specified range.

Then let’s print a larger Christmas tree:

	>>>  lst = range(1, 11) >>> for i in lst: ...
	>>>  print("*"*i) \* *\*\****\*\**\***\****\*****\***\***\*

range has saved a lot of our time. We can save even more if we omit
naming the list:

	>>>  for i in range(1, 5): ... print(i\*"\#") \# \#\# \#\#\#
	>>>  \#\#\#\#

When you use the keyword for, we do not have to use the list. for can
handle the generator given by range. Hence, we can simplify our program
even more:

	>>>  for i in range(1, 5): ... print(i\*"\#") \# \#\# \#\#\#
	>>>  \#\#\#\#

Nothing prevents us to put one loop inside another loop, so let's do it!
Just remember to use appropriate indentations and use different names
e.g. `i` and `j` (or more associated with the list content):

	>>>  for i in range(1, 3): ... for j in range(11, 14): ...
	>>>  print(i, j) 1 11 1 12 1 13 2 11 2 12 2 13

Here we have inner loop that iterates from 11 to 13 (remember, 14 is not
included when using `range`) and outer loop that iterates from 1 to 2.
As you can see, items from inner loop are printed twice, for each
iteration of outer loop.

Using this technique, we can repeat our piece of the Christmas tree:

	>>>  for i in range(3): \# repeats 3 times ... for size in
	>>>  range(1, 4): ... print(size\*"*")* *\*\** *\*\** *\**\*\*

Before proceeding to the next chapter, create `xmas.py` file with this
program and try to modify it so that each of the three repetitions of
the first (external) loop, the second one was executed one more time.
This way, we should get our half of the Christmas tree described at the
beginning of the chapter.

Defining a function
===================

We have already seen how functions solve many of our problems. However,
they do not solve all our problems – or at least not exactly the way we
would like functions to solve them. Sometimes we must solve a problem on
our own. If it occurs often in our program, it would be nice to have a
function that solves it for us.

We can do it like this in Python:

	>>>  def print\_triangle(n): ... for size in range(1, n+1):
	>>>  ... print(size\*"*") ... >>> print\_triangle(3)* *\*\*
	>>>  print\_triangle(5)* *\*\****\****\**

Let's have a closer look at the function print\_triangle:

    def print_triangle(n):
        for size in range(1, n+1):
            print(size*"*")

The definition of a function always starts with the word def. Next, we
give the name to our function. Between the parenthesizes, we indicate
what names should be given to its arguments when the function is called.
In the following lines we provide instructions to be executed when we
use the function.

As shown in the example, the instructions in the function may include
names that we have given as the names of the arguments. The principle of
operation is as follows - if you create a function with three arguments:

	>>>  def foo(a, b, c): ... print("FOO", a, b, c)

When you call this new function, you need to specify a value for each
argument. This just like all the functions we called before:

	>>>  foo(1, "Ala", 2 + 3 + 4) FOO 1 Ala 9 >>> x = 42
	>>>  foo(x, x + 1, x + 2) FOO 42 43 44

Note that the argument name is just a label. If we change the value
attached to a label for another one, the other labels will not change –
the same happens with the arguments:

	>>>  def plus\_five(n): ... n = n + 5 ... print(n)
	>>>  x = 43 >>> plus\_five(x) 48 >>> x 43

It is as normal names (variables) we saw before. There are only two
differences:

Firstly, argument names of a function are defined at each function call,
and Python attaches the corresponding argument value to to each of the
argument names it just created.

Secondly, the argument names are not available outside the function as
they are created when the function is called and forgotten after the
call. That is, if you try now to access the argument name `n` we defined
in our plus\_five function outside of the function's code, Python tells
you it is not defined:

	>>>  n Traceback (most recent call last): File
	>>>  "<stdin>", line 1, in <module> NameError: name 'n' is not
	>>>  defined

That is, our prim and proper Python cleans up his room at the end of a
function call :)

Returning values
----------------

The functions which we have previously used had one important property
that is missing in the functions created by ourselves - they gave back
the value they computed instead of printing it immediately. To achieve
the same effect, you need to use the instruction return. This is a
special instruction that can be found only in functions.

We can now improve our BMI calculator by adding a function to compute
BMI:

    :::python3
    def calc_bmi(height, weight):
        return weight / height ** 2


Finally, as a last example on functions, here is a solution to the
problem from the end of the previous chapter:

The Entire Christmas tree
=========================

The previous chapter was fairly theoretical, so now we'll use some of
this new knowledge to complete our program to display a Christmas tree.

For the record:

    :::python3
    # xmas.py

    def print_triangle(n):
        for size in range(1, n+1):
            print(size * "*")

    for i in range(2, 5):
        print_triangle(i)

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
