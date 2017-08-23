Strings and how to play with them
=================================

The last issue which we have mentioned above was the problem with too
many digits in a printed BMI. Out of the three problems we had, this one
is the easiest to solve.

That’s why we left it for the end of our "adventure" with the BMI
calculator. We already know that we can add strings to each other and
multiply them by integers. You will see that we can also format them.
But first we will need one more type of data (except the strings and the
numbers we already know).

Tuples
======

At the beginning we mentioned that we can not use commas in numbers,
because we will need them later while using tuples. And here they are:

	>>>  1, 2, 3 (1, 2, 3) >>> ("Ala", 15) ('Ala', 15)
	>>>  x = 1,5 >>> print(x) (1, 5)

A tuple is nothing more than a few values grouped into one. The values
we want to group should be separated by commas. The whole thing can be
enclosed in parentheses to make it more clear, but it is not required.
Except when we want to group none of the elements (however strange it
may sound):

	>>>  () ()

Tuples can be combined:

	>>>  names = ("Paulina", "Kowalska") >>> details =
	>>>  (27, 1.70) >>> names + details ('Paulina', 'Kowalska', 27,
	>>>  1.7)

They may also contain other tuples e.g. information on a point on the
map can be grouped as follows:

	>>>  point = ("Name of point", (x, y))

where `x` and `y` are numbers.

We can refer to the grouped values by using their positions in the tuple
(counting form zero) e.g.:

	>>>  p = (10, 15) >>> p\[0\] \# first value 10
	>>>  p\[1\] \# second value 15

Formatting plain
================

Going back to our program: currently the result is reduced to a single
line. Now we want to write the BMI as a number and the interval in which
it is located, that is to say:

    Your BMI is equal: 21.39 (normal weight)

Modify the current program so that the calculated BMI would be available
under the name of `bmi`,and the name of the interval under the name of
`category`. Then we can use print and obtain the required result:

Well, almost….We still have too many digits. We would also have a
problem if we wanted to generate such a string and save with a name,
because we use print to separate the elements. Fortunately, there is a
better way:

	>>>  bmi = 21.387755102040817 >>> category = "normal
	>>>  weight" >>> result = "Your BMI: %f (%s)" % (bmi, category)
	>>>  result 'Your BMI: 21.387755 (normal weight)' >>>
	>>>  print(result) Your BMI: 21.387755 (normal weight)

We have here a string and a tuple joined by `%`. The string is a
template which will be completed with values from the tuple. The spaces
to be filled are also labeled with the percentage (`%`). . The letter
that follows defines the type of a value we want to insert. The integers
are represented by `i` as **integer** (we can also use `d` as
**decimal**), strings are represented by `s` as **string**, and
floating-point numbers are represented by `f` for **float**:

	>>>  "String: %s, Numbers: %d %f" % ("Ala", 10, 3.1415)
	>>>  'String: Ala, Numbers: 10 3.141500'

Now instead of nine decimal places we always get six, but the formatting
has the advantage that it allows us to have more control by putting
between `%` and `f` additional information, e.g. if you want to display
only two places after the decimal point:

	>>>  "%.2f" % 3.1415 '3.14' >>> "%.2f" %
	>>>  21.387755102040817 '21.39'

There are plenty options of formatting, so we will not show them all
here. One of the most useful is the option of aligning to a specific
number of characters:

We can also align the string `-` to the left by putting before the
number of characters:

Aligning towards the centre is an additional exercise for you :).

Formatting more Pythonic way
============================

String Slicing
==============

Try it out: >>> text = “ala ma kota” >>> text\[0\] \#
string\[int\] >>> text\[2:\] \# string\[int:\] >>>
text\[:5\] \# string\[:int\] >>> text\[3:7\] \#
string\[int:int\] >>> text\[::2\] \# stirng\[::int\]
	>>>  text\[::-1\] \# stirng\[::int\]

Always remember computer counts from 0.

Methods
=======

With string there is a lot of methods implemented already.

1.  capitalize() - Capitalizes first letter of string
2.  count(str, beg= 0,end=len(string)) - Counts how many times str
    occurs in string or in a substring of string if starting index beg
    and ending index end are given.
3.  endswith(suffix, beg=0, end=len(string)) - Determines if string or a
    substring of string (if starting index beg and ending index end are
    given) ends with suffix; returns true if so and false otherwise.
4.  find(str, beg=0 end=len(string)) - Determine if str occurs in string
    or in a substring of string if starting index beg and ending index
    end are given returns index if found and -1 otherwise.
5.  index(str, beg=0, end=len(string)) - Same as find(), but raises an
    exception if str not found.
6.  isalnum() - Returns true if string has at least 1 character and all
    characters are alphanumeric and false otherwise.
7.  isalpha() - Returns true if string has at least 1 character and all
    characters are alphabetic and false otherwise.
8.  isdigit() - Returns true if string contains only digits and false
    otherwise.
9.  islower() - Returns true if string has at least 1 cased character
    and all cased characters are in lowercase and false otherwise.
10. isnumeric() - Returns true if a unicode string contains only numeric
    characters and false otherwise.
11. isspace() - Returns true if string contains only whitespace
    characters and false otherwise.
12. istitle() - Returns true if string is properly "titlecased" and
    false otherwise.
13. isupper() - Returns true if string has at least one cased character
    and all cased characters are in uppercase and false otherwise.
14. join(seq) - Merges (concatenates) the string representations of
    elements in sequence seq into a string, with separator string.
15. len(string) - Returns the length of the string
16. lower() - Converts all uppercase letters in string to lowercase.
17. lstrip() - Removes all leading whitespace in string.
18. max(str) - Returns the max alphabetical character from the string
    str.
19. min(str) - Returns the min alphabetical character from the string
    str.
20. replace(old, new \[, max\]) - Replaces all occurrences of old in
    string with new or at most max occurrences if max given.
21. rfind(str, beg=0,end=len(string)) - Same as find(), but search
    backwards in string.
22. rindex( str, beg=0, end=len(string)) - Same as index(), but search
    backwards in string.
23. rstrip() - Removes all trailing whitespace of string.
24. split(str="", num=string.count(str)) - Splits string according to
    delimiter str (space if not provided) and returns list of
    substrings; split into at most num substrings if given.
25. splitlines( num=string.count('n')) - Splits string at all (or num)
    NEWLINEs and returns a list of each line with NEWLINEs removed.
26. startswith(str, beg=0,end=len(string)) - Determines if string or a
    substring of string (if starting index beg and ending index end are
    given) starts with substring str; returns true if so and false
    otherwise.
27. strip(\[chars\]) - Performs both lstrip() and rstrip() on string
28. swapcase() - Inverts case for all letters in string.
29. title() - Returns "titlecased" version of string, that is, all words
    begin with uppercase and the rest are lowercase.
30. upper() - Converts lowercase letters in string to uppercase.

There is over 10 more methods but they are much more advanced.


Summary
=======

We also know now that indentations can be important, especially when we
want to use the instruction if (also in connection with else and elif).

This is quite a lot like for a first program. We still have a lot of
work, anyhow you can be proud of what we have done so far!

And if You did the obligatory task 1 You know there are some easter eggs
in python and thats not all of them. Here is one more:

	>>>  True + True

:-)
