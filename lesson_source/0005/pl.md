Python jako Kalkulator
======================

Policzmy coś, na przykład: `2 + 2`:

```python
>>>  2 + 2
4
```

Python jest świetny jako kalkulator:

```python
>>>  6 * 7
42
>>> 1252 - 38 * 6
1024
>>>  (3 - 5) * 7
-14
>>> 21 / 7
3.0
>>> 3**2
9
>>>  5 / 2
2.5
>>> 5 % 2
1
```

Zwróćcie proszę szczególną uwagę na zapis liczb dziesiętnych: używajcie
kropki, a nie przecinka. Przecinki będą używane do definiowania tupli
<bmi-tuples> (więcej o tym wkrótce). Operator % to modulo, czyli reszta
z dzielenia.

* \+ - dodawania
* \- - odejmowanie
* \* - mnożenie
* / - dzielenie
* ** - potęgowanie
* // - dzielenie do części całych zaokrąglając zawsze w dół
* % - modulo czyli reszta z dzielenia

Kalkulator BMI
==============

Napiszemy teraz prosty program do ustalania BMI ([Body Mass
Index](http://pl.wikipedia.org/wiki/Body_Mass_Index)). Formuła do
jego obliczania wygląda następująco:

BMI = mass (kg) / ((height (m) do kwadratu)

Wiemy już, jak dzielić, podnosić do potęgi i wyświetlać liczby.
Stwórzmy nowy plik o nazwie `bmi.py` i napiszmy program, który oblicza BMI:

print("Twój BMI wynosi:", 65.5 / (1.75 ** 2))

Uruchomimy nasz program przy użyciu:

$ python bmi.py

Otrzymujemy następujący wynik:

Twój BMI wynosi: 21.387755102040817

Jak widzicie, nasz program wymaga jeszcze poprawek:

1.  Gdyby ktoś inny chciał używać tego programu, musimy zmienić zawartość
pliku `bmi.py`.
2.  Dla kogoś, kto nie pamięta tabeli BMI, wartość 21.387755102 nie
będzie nic znaczyła.
3.  Wyświetlanie tak wielu miejsc dziesiętnych nie jest konieczne.
BMI jest mierzone z dokładnością do dwóch miejsc po przecinku.

Programowanie jest sztuką rozwiązywania problemów, a zatem... do pracy!
Będziemy mieli możliwość nauczenia się kilku nowych właściwości Pythona.
