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

Okazuje się, listy reagują na wszystkie ogólne operacje dla sekwencji, które
używalismy na stringach w poprzednim rozdziale.

	>>>  len([1, 2, 3])   # Długość 
	>>> [1, 2, 3] + [4, 5, 6]     # Konkatenacja
	[1, 2, 3, 4, 5, 6]
	>>>  ['Hi!'] * 4    # Powtórzenie 
	['Hi!', 'Hi!', 'Hi!', 'Hi!']
	>>>  3 in [1, 2, 3]   # Zawieranie się 
	True 
	>>> L = ["Ala", "Ola", "Jacek"] 
	>>> L[1] 
	'Ola'
	>>>  L[-1] 
	'Jacek' 
	>>> L[1:] 
	['Ola', 'Jacek'] 
	>>>  L[:1] 
	['Ala'] 
	>>> L[1:2] 
	['Ola'] 
	>>>  L[1:3] # komenda L[3] wywoła błąd! 
	['Ola', 'Jacek']

Range (Zakres)
--------------

Cóż, niestety ciągle musimy sami pisać całą zawartość listy. Ten problem
może być rozwiązany dzięki użyciu funkcji range. Wypróbuj komendę
`help(range)`, aby zapoznać się z wszystkimi możliwościami funkcji range lub wykonaj
tych kilka przykładów: 

	>>>  list(range(2)) 
	[0, 1] 
	>>> list(range(1, 11))
	[1, 2, 3, 4, 5, 6, 7, 8, 9, 10] 
	>>> list(range(1, 11, 2))
	[1, 3, 5, 7, 9]

    	:::python3
    	for i in range(10):
        	print(i)

Aktualizowanie list
-------------------

Możesz zmienić jeden lub wiele elementów listy poprzez wybranie elementu,
który chcesz zmienić i nadanie mu nowej wartości. Możesz również dodawać do listy
nowe elementy używając metody append().

	>>>  lista = ['fizyka', 'chemia', 1997, 2000\]
	>>>  print(lista[2]) 
	>>>  lista[2] = 2001
	>>>  print(list[2])

	>>>  lista_2 = ['a', 'b'] 
	>>>  lista_2.append('c')
	>>>  print(lista_2)

Usuwanie elementów listy
------------------------

Aby usunąć element z listy, możesz użyć komendy del, jeśli wiesz dokładnie,
który element chcesz usunąć lub metody remove(), jeśli tego nie wiesz.
Na przykład:

	>>>  lista1 = \['fizyka', 'chemia', 1997, 2000\]
	>>>  print(lista1) 
	>>>  del lista1[2]
	>>>  print(lista1)

Słownik
=======

Słownik jest typem danych złożonym z zestawu par (klucz, wartość) takim, 
że każdy klucz pojawia się tylko jeden raz w zestawie. Poza tym jedynym
warunkiem słownik pythonowy jest bardzo podobny do zwykłego słownika.

Każdy klucz jest oddzielony od wartości dwukropkiem (:), elementy słownika
są oddzielone przecinkami, a cały zestaw jest otoczony nawiasami klamrowymi.
Pusty słownik, nie posiadający elementów jest zapisywany jako dwa nawiasy
klamrowe, czyli {}.

Klucze w obrębie słownika są unikatowe, ale wartości nie muszą. Wartości
słownika mogą być dowolnym typem danych, ale klucze muszą być niezmiennymi
typami danych, takimi jak stringi, liczby lub tuple.

Dostęp do wartości w słowniku
-----------------------------

Aby uzyskać dostęp do wartości słownika, należy podać klucz ujęty w znanych Ci
już nawiasach kwadratowych. Oto przykład:

    :::python3
    słownik = {'Imię': 'Marta', 'Wiek': 21, 'Zawód': 'Python Developer'}
    print(słownik['Imię'])
    print(słownik['Wiek'])
    print(słownik['Zawód'])

Po wykonaniu powyższego kodu uzyskujemy następujący rezultat:

	Martha
	21
	Python Developer

Zmienianie zawartości słownika
------------------------------

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
