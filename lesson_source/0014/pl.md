# Łapanie błędów

Obsługa błedów najprostsza, które się unika.
```python
try:
    a = 20 / 2
except:
    print("nie dzielimy przez zero")
```


Obsługa błędów akceptowalna
```python
try:
    a = 20 / 'a'
except Exception as err:
    print(err)
```

Obsługa błedów rekomendowana
```python
a = input("wzrost")
try:
    a = 20 / a
except ZeroDivisionError:
    print("Nie mozna dzielic prez zero")
except TypeError:
    print("Podales zly typ danych")
except Exception as err:
    print(err)
```

Obsługa błedów rekomendowana gdy pracujemy z zasobem, połączeniem które wymaga zamknięcia:
```python
a = input("wzrost")
try:
    a = 20 / a
except ZeroDivisionError:
    print("Nie mozna dzielic prez zero")
except TypeError:
    print("Podales zly typ danych")
except Exception as err:
    print(err)
finally:
    print("Finito")
```

Działanie finally nie jest oczywiste:
```python
def funk():
    a = input("wzrost")
    try:
        a = 20 / a
    except Exception as err:
        print(err)
        return 0
    finally:
        print("Finito")
```

```python
def funk():
    a = input("wzrost")
    try:
        a = 20 / a
    except Exception as err:
        print(err)
        return 0
    print("Finito")
```