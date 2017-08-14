Python data storage types
=========================

Python has five standard data types −
- Numbers
- String
- List
- Tuple
- Dictionary
We already used numbers(ints and floats), string and tuples. Now it is time to learn about Lists and Dictionaries.
Cute Wabbit

A little girl goes into a pet show and asks for a wabbit. The shop
keeper looks down at her, smiles and says:

"Would you like a lovely fluffy little white rabbit, or a cutesy
wootesly little brown rabbit?"

"Actually", says the little girl, "I don't think my python would
notice."

Now lets get back to learning :)

List
====

Still we haven’t said anything about lists, as they do not differ much
from the intuitive concept of lists in the everyday life. We can easily
think of lists in Python as we think of any other list (a shopping list,
a guest list, exam results etc.) written on a paper and numbered.

Let's start with a blank page by starting a new python interpreter:

	>>> L = []
	>>> L
	[]

At any time we can check how many items we have saved on our list by
using the function len.

	>>>  len(L) 0

Let's make another list (which can have the same name or a different
one):

	>>>  L = ["Ala", "Ola", "Jacek"]
	>>> len(L)
	3

As in the case of tuples, consecutive elements of the list are separated
by commas. Unlike tuples, brackets `[` and `]` are obligatory.

Accessing Values in Lists
-------------------------

To preview a particular position of an element on the list (remember
that we count the positions from 0 ):

	>>>  L = ["Ala", "Ola", "Jacek"]
	>>> L[0] 'Ala'
	>>>  L[1] 'Ola' >>> L[2] 'Jacek'
	>>>
	>>>  L[3] Traceback (most recent call last): File "<stdin>", line
	>>>  1, in <module> IndexError: list index out of range

We can also use the loop for,to execute instructions for every element
of the list:

	>>>  for name in L:
	... print("Name:", name)
	Name: Ala
	Name: Ola
	Name: Jacek

In the same way, we can print the first part of our half of the
Christmas tree:

	>>>  lst = [1, 2, 3]
	>>> for n in lst:
	... print("*"*n)

Basic List Operations
---------------------

Lists respond to the + and * operators much like strings; they mean
concatenation and repetition here too, except that the result is a new
list, not a string.

In fact, lists respond to all of the general sequence operations we used
on strings in the prior chapter.

	>>>  len([1, 2, 3]) # Length 3
	>>> [1, 2, 3] + [4, 5, 6] # Concatenation
	[1, 2, 3, 4, 5, 6]
	>>> ['Hi!'] * 4 # Repetition
	['Hi!', 'Hi!', 'Hi!', 'Hi!']
	>>>  3 in [1, 2, 3] # Membership True
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
	>>>  L[1:3] # L[3] will end up with error !
	['Ola', 'Jacek']

Range
-----

Well, unfortunately we still have to type the entire contents of the
list. This problem can be solved by the function range. Check
`help(range)` for the full story, or check these quick examples:

	>>>  list(range(2))
	[0, 1]
	>>> list(range(1, 11))
	[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
	>>> list(range(1, 11, 2))
	[1, 3, 5, 7, 9]

    :::python3
    for i in range(10):
        print(i)

Updating Lists
--------------

You can update single or multiple elements of lists by giving the slice
on the left-hand side of the assignment operator, and you can add to
elements in a list with the append() method.

	>>>  list = ['physics', 'chemistry', 1997, 2000]
	>>>  print(list[2])
	>>> list[2] = 2001
	>>>  print(list[2])

	>>>  list_2 = ['a', 'b']
	>>> list_2.append('c')
	>>>  print(list_2)

Delete List Elements
--------------------

To remove a list element, you can use either the del statement if you
know exactly which element(s) you are deleting or the remove() method if
you do not know. For example −

	>>>  list1 = ['physics', 'chemistry', 1997, 2000]
	>>>  print(list1) >>> del list1[2] >>>
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

	>>> a_dict = {'Name': 'Martha', 'Age': 21, 'Profession': 'Python Developer'}
	>>> a_dict['Age'] = 8 # update existing entry
	>>> a_dict['Profession'] = 'Student' # update existing entry
	>>> a_dict['School'] = "Primary School" # Add new entry
	>>> print(a_dict['Age'])
	>>> print(a_dict['School'])

Delete Dictionary Elements
--------------------------

You can either remove individual dictionary elements or clear the entire
contents of a dictionary. You can also delete entire dictionary in a
single operation.

To explicitly remove an entire dictionary, just use the del statement.
Following is a simple example −

	>>> a_dict = {'Name': 'Martha', 'Age': 21, 'Profession': 'Python Developer'}
	>>> del a_dict['Name'] # remove entry with key 'Name'
	>>> print(a_dict)
	>>> a_dict.clear() # remove all entries in dict
	>>> print(a_dict)
	>>> del a_dict # delete entire dictionary

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