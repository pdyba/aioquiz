Pythonowe typy przechowywania danych
====================================

Python ma pięć podstawowych typów danych:
- Liczba
- String
- Lista
- Tupla
- Słownik

Używaliśmy już liczb (całkowitych int i zmiennoprzecinkowych float), stringów i tupli. Nadszedł czas, by poznać
listy i słowniki.

Słodki Kłólik

Dziewczynka idzie do sklepu ze zwierzątkami domowymi i pyta o kłólika.
Sprzedawca pochyla się nad nią, uśmiecha i pyta:

"Chciałabyś ślicznego puszystego białego króliczka, 
czy słodkiego kudłatego brązowego króliczka?"

"Właściwie", odpowiada dziewczynka, "Nie sądzę, by mój pyton zauważył różnicę."

A teraz wracajmy do nauki :)

Lista
=====

Nie wspomnieliśmy dotychczas o listach, bo nie różnią się one od intuicyjnej
koncepcji list znanej z codziennego życia. Możemy myśleć o listach w Pythonie
tak samo, jak myślimy o każdej innej liście (liście zakupoów, liście gości,
wynikach egzaminu itd.) spisanej na papierze i ponumerowanej.

Zacznijmy od czystej strony w interpreterze Pythona:


	>>> L = [] 
	>>> L

W każdej chwili możemy sprawdzić, ile elementów przechowujemy w liście
stosując funkcję len:

	>>> len(L) 
	0

Stwórzmy kolejną listę (o takiej samej lub innej nazwie, niż poprzednia lista):

	>>> L = ["Ala", "Ola", "Jacek"] 
	>>> len(L)
	3

Tak, jak w przypadku tupli, kolejne elementy listy są oddzielone przecinkami. 
Zaś w odróżnieniu od tupli, nawiasy `[` i `]` są obowiązkowe.

Dostęp do wartości w liście
---------------------------

By wyświetlić określony element listy (pamiętajcie, że liczymy od zera):

	>>> L = ["Ala", "Ola", "Jacek"] 
	>>> L[0]
	'Ala'
	>>>  L[1]
	'Ola' 
	>>> L[2] 
	'Jacek' 
	>>>  L[3]
	Traceback (most recent call last): File "<stdin>", line
	1, in <module> IndexError: list index out of range

Możemy również użyć pętli, by wykonać instrukcję dla każdego elementu
listy:

	>>>  for imię in L: 
	 ... print ("Imię:", imię) 
	Imię: Ala
	Imię: Ola 
	Imię: Jacek

W ten sam sposób możemy wydrukować pierwszą część choinki bożonarodzeniowej:


	>>>  lista = [1, 2, 3] 
	>>> for n in lista: 
	... print("*"*n)

Podstawowe operacje na listach
------------------------------

Listy reagują na operatory + i \* podobnie, jak stringi. Znaki te oznaczają
również tutaj konkatenację (łączenie tekstów) i powtórzenie, ale rezultatem
jest lista, a nie string.

Faktycznie, listy reagują na wszystkie ogólne operacje dla sekwencji, które
używalismy na stringach w poprzednim rozdziale.
In fact, lists respond to all of the general sequence operations we used
on strings in the prior chapter.

	>>>  len(\[1, 2, 3\]) \# Length 3 >>> \[1, 2, 3\] +
	>>>  \[4, 5, 6\] \# Concatenation \[1, 2, 3, 4, 5, 6\] >>>
	>>>  \['Hi!'\] \* 4 \# Repetition \['Hi!', 'Hi!', 'Hi!', 'Hi!'\]
	>>>  3 in \[1, 2, 3\] \# Membership True >>> L =
	>>>  \["Ala", "Ola", "Jacek"\] >>> L\[1\] 'Ola' >>>
	>>>  L\[-1\] 'Jacek' >>> L\[1:\] \['Ola', 'Jacek'\] >>>
	>>>  L\[:1\] \['Ala'\] >>> L\[1:2\] \['Ola'\] >>>
	>>>  L\[1:3\] \# L\[3\] will end up with error ! \['Ola', 'Jacek'\]

Range
-----

Well, unfortunately we still have to type the entire contents of the
list. This problem can be solved by the function range. Check
`help(range)` for the full story, or check these quick examples:

	>>>  list(range(2)) \[0, 1\] >>> list(range(1, 11))
	>>>  \[1, 2, 3, 4, 5, 6, 7, 8, 9, 10\] >>> list(range(1, 11, 2))
	>>>  \[1, 3, 5, 7, 9\]

    :::python3
    for i in range(10):
        print(i)

Updating Lists
--------------

You can update single or multiple elements of lists by giving the slice
on the left-hand side of the assignment operator, and you can add to
elements in a list with the append() method.

	>>>  list = \['physics', 'chemistry', 1997, 2000\]
	>>>  print(list\[2\]) >>> list\[2\] = 2001
	>>>  print(list\[2\])
>
	>>>  list\_2 = \['a', 'b'\] >>> list\_2.append('c')
	>>>  print(list\_2)

Delete List Elements
--------------------

To remove a list element, you can use either the del statement if you
know exactly which element(s) you are deleting or the remove() method if
you do not know. For example −

	>>>  list1 = \['physics', 'chemistry', 1997, 2000\]
	>>>  print(list1) >>> del list1\[2\] >>>
	>>>  print(list1)

Dictionary
==========

Dictionary is an data type composed of a collection of (key, value)
pairs, such that each possible key appears just once in the collection.
Except the unique condition it is very similar to normal dictionary.

Each key is separated from its value by a colon (:), the items are
separated by commas, and the whole thing is enclosed in curly braces. An
empty dictionary without any items is written with just two curly
braces, like this: {}.

Keys are unique within a dictionary while values may not be. The values
of a dictionary can be of any type, but the keys must be of an immutable
data type such as strings, numbers, or tuples.

Accessing Values in Dictionary:
-------------------------------

To access dictionary elements, you can use the familiar square brackets
along with the key to obtain its value. Following is a simple example −

    :::python3
    a_dict = {'Name': 'Martha', 'Age': 21, 'Profession': 'Python Developer'}
    print(a_dict['Name'])
    print(a_dict['Age'])
    print(a_dict['Profession'])


When the above code is executed, it produces the following result:

	>>>  Martha >>> 21 >>> Python Developer

Updating Dictionary
-------------------

You can update a dictionary by adding a new entry or a key-value pair,
modifying an existing entry as shown below in the simple example −

	>>>  a\_dict = {'Name': 'Martha', 'Age': 21, 'Profession':
	>>>  'Python Developer'} >>> a\_dict\['Age'\] = 8 \# update
	>>>  existing entry >>> a\_dict\['Profession'\] = 'Student' \#
	>>>  update existing entry >>> a\_dict\['School'\] = "Primary
	>>>  School" \# Add new entry >>> print(a\_dict\['Age'\])
	>>>  print(a\_dict\['School'\])

Delete Dictionary Elements
--------------------------

You can either remove individual dictionary elements or clear the entire
contents of a dictionary. You can also delete entire dictionary in a
single operation.

To explicitly remove an entire dictionary, just use the del statement.
Following is a simple example −

	>>>  a\_dict = {'Name': 'Martha', 'Age': 21, 'Profession':
	>>>  'Python Developer'} >>> del a\_dict\['Name'\] \# remove entry
	>>>  with key 'Name' >>> print(a\_dict) >>>
	>>>  a\_dict.clear() \# remove all entries in dict >>>
	>>>  print(a\_dict) >>> del a\_dict \# delete entire dictionary

Nesting
=======

In Python You can create nested objects like:

    :::python3
    ZOO = {
        'animals': {
            'python': {
                'food': [
                    'mice',
                    'rabbits',
                    'rats',
                ]
                'environment': {
                    'temp': 25,
                    'humidity': 80,
                }
                'location': 'cage',
            },
            'cute_little_rabbit': {
                'food': [
                    'carrots',
                    'carrots',
                    'carrots',
                ]
                'environment': {
                    'temp': 20,
                    'humidity': 35,
                }
                'location': 'run free',
            },
        'contact': {
            'telphone': 0 700 800 900,
            'email': 'zoo@zoo.zoo'
        }
    }


As You can see there can be a dict or a list inside of a dict of dicts.
