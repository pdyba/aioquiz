# nasza_funkcja()


## Definicja i wywołanie

```python
def nasza_funkcja():
    print("Hey You!")

nasza_funkcja()
```

## Argumenty

```python
def nasza_funkcja(fname):
    print("Hey " + fname + "!")

nasza_funkcja("Piotr")
```

```python
def nasza_funkcja(fname, lastname):
    print("Hey " + fname + " " + lastname + "!")

nasza_funkcja("Piotr", "Dyba")
```

```python
def nasza_funkcja(fname, lastname):
    fname = fname.capitalize()
    lastname = lastname.capitalize()
    print("Hey " + fname + " " + lastname + "!")

nasza_funkcja("tRoLoOl", "loLO")
```

## Argumenty opcjonalne z wartością domyślną

```python
def nasza_funkcja(fname="You", lastname=""):
    fname = fname.capitalize()
    lastname = lastname.capitalize()
    print("Hey " + fname + " " + lastname + "!")

nasza_funkcja()
nasza_funkcja("tRoLoOl", "loLO")
nasza_funkcja(lastname="loLO", fname="tRoLoOl")
```



## Zwracanie wartości

```python
def nasza_funkcja(fname="You", lastname=""):
    fname = fname.capitalize()
    lastname = lastname.capitalize()
    return "Hey " + fname + " " + lastname + "!"

nasza_funkcja()
nasza_funkcja("tRoLoOl", "loLO")
nasza_funkcja(lastname="loLO", fname="tRoLoOl")


print(nasza_funkcja())
print(nasza_funkcja("tRoLoOl", "loLO"))
print(nasza_funkcja(lastname="loLO", fname="tRoLoOl"))
```



```python
def nasza_funkcja(fname, lastname=""):
    fname = fname.capitalize()
    lastname = lastname.capitalize()
    return "Hey " + fname + " " + lastname + "!"

nasza_funkcja("piotr")
nasza_funkcja("tRoLoOl", "loLO")
nasza_funkcja(lastname="loLO", fname="tRoLoOl")


print(nasza_funkcja("piotr"))
print(nasza_funkcja("tRoLoOl", "loLO"))
print(nasza_funkcja(lastname="loLO", fname="tRoLoOl"))