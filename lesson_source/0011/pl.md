# Zabawy ze stringami

Ostatnią kwestią, o której wspomnieliśmy wcześniej był problem ze zbyt
wieloma cyframi po przecinku w otrzymanym BMI. Z trzech problemów, jakie
mieliśmy, ten jest najłatwiejszy do rozwiązania.

Dlatego właśnie zostawiliśmy go na koniec naszej "przygody"
z kalkulatorem BMI. Wiemy, że stringi można dodawać do siebie i mnożyć
przez liczby całkowite. Zobaczycie, że możemy je także formatować.
Ale zanim to zrobimy, potrzebny jest nam jeszcze jeden typ danych
(poza stringami i liczbami, które już poznaliśmy).

## Formatowanei stringów 

Specjalnie pominiemy formatowanie Yolo:

```python
kto = "ala"
kogo = "kota"
print(kto + " ma " + kogo + ".")
```

### Formatowanie dla PYthonów  3.7+

Od tej wersji PYthona możemy używać zmiannych i funkcji zdefinowanych w kodzie żeby sformatować docelowy string.

```python
imie = 'ala'
print(f"{imie} ma kota.")
```

lub

```python
print(f"{input('kto ma kota?')} ma kota.")
```

Zaokrąglanie

```python
print(f"PI to {round(3.14312312312, 2)}")

pi = 3.14312312312
print(f"PI to {pi:.2f}")
```


**Ważną rzeczą jest to że ten string zostanie zbudowany odrazu w momencie tworzenia.**

### Formatowanie dla Pythona  < 3.7 i nie tylko

Do wersji Pythona 3.7, królował inny sposó formatowania, który nadal ma zastosowanie.

```python
imie = 'ala'
print("{imie} ma kota.".format(imie=imie))


print("{} ma kota.".format(imie))
```


lub

```python
print("{} ma kota".format(input('kto ma kota?')))
```

troche trudniej się robi przy zaokrągleniach gdyż musimy explicityl zaookrąglać:

```python
print("PI to {}".format(round(3.14312312312, 2)))


print("PI to {:.2f}".format(3.14312312312))
```


### Formatowanie Leniwe (prawie nie używane już)


Wracając do naszego programu: obecnie wynik jest zredukowany do
pojedynczej linii. Chcemy zaś stworzyć taki kalkulator BMI, który
poda nam wynik oraz przedział, w którym się on mieści, czyli:

Twój BMI wynosi: 21.39 (prawidłowa waga)

Zmodyfikuj swój istniejący program tak, by obliczone BMI było dostępne
pod zmienną `bmi`, a nazwa przedziału pod nazwą `kategoria`. Użyj print,
aby wyświetlić otrzymany wynik:

```python
bmi = 21.387755102040817
kategoria = "prawidłowa waga"
print("Twój BMI wynosi:", bmi, "(" + kategoria + ")")

Twój BMI wynosi: 21.387755102040817 (prawidłowa waga)
```

Cóż, prawie... Nadal mamy zbyt wiele liczb po przecinku. Napotkamy
także problem, jeśli będziemy chcieli utworzyć taki string i nadać
mu nazwę, bo użyliśmy funkcji print oddzielając składniki. Na szczęście
jest lepszy sposób:

```python
>>> bmi = 21.387755102040817
>>> kategoria = "prawidłowa waga"
>>> wynik = "Twój BMI wynosi: %f (%s)" % (bmi, kategoria)
>>> wynik
'Twój BMi wynosi: 21.387755 (prawidłowa waga)'
>>> print(wynik)
Twój BMI wynosi: 21.387755 (prawidłowa waga)
```

Użyliśmy tutaj stringa i tupli połączonych znakiem `%`. String jest
szablonem, który zostaje uzupełniony wartościami z tupli. Miejsca,
które mają być uzupełnione są oznaczone znakiem procentu (`%`). Litera
następująca po nim definiuje typ zmiennej, jaką chcemy wstawić. Liczby
całkowite są tu reprezentowane przez `i` (ang. **integer**). Możemy
również użyć `d` jako **decimal** (z ang. liczba dziesiętna). Stringi są
reprezentowane jako `s` od **string**, a liczby zmiennoprzecinkowe
jako `f` od **float** (ang. pływać, unosić się):

```python
	>>>  "String: %s, Numery: %d %f" % ("Ala", 10, 3.1415)
	'String: Ala, Numery: 10 3.141500'
```

Teraz, zamiast dziewięciu miejsc po przecinku, za każdym razem otrzymamy
sześć, ale formatowanie ma tę zaletę, że umożliwia nam kontrolę nad
tym, poprzez wstawianie dodatkowej informacji pomiędzy znak `%` a literę
`f`, np. jeśli chcielibyśmy wyświetlać tylko dwa miejsca po przecinku,
zamiast sześciu:

```python
>>> "%.2f" % 3.1415
'3.14'
>>> "%.2f" % 21.387755102040817
'21.39'
```

Istnieje mnóstwo opcji formatowania. Niestety nie pokażemy ich tu wszystkich.
Jedna z najbardziej użytecznych to wyrównywanie do określonej ilości
znaków:

```python
WIDTH = 28

print("-" * WIDTH)
print("| Imię i nazwisko |  Waga  |")
print("-" * WIDTH)
print("| %15s | %6.2f |" % ("Łukasz", 67.5))
print("| %15s | %6.2f |" % ("Pudzian", 123))
print("-" * WIDTH)

--------------------------------
|    Imię nazwisko    |  Waga  |
--------------------------------
|              Łukasz |  67.50 |
|             Pudzian | 123.00 |
--------------------------------
```

Możemy również wyrównać string do lewej, umieszczając `-` przed
ilością liter:

```python
WIDTH = 28

print("-" * WIDTH)
print("| Imię i nazwisko |  Waga  |")
print("-" * WIDTH)
print("| %-15s | %6.2f |" % ("Łukasz", 67.5))
print("| %-15s | %6.2f |" % ("Pudzian", 123))
print("-" * WIDTH)

-------------------------------
|    Imię nazwisko  |   Waga  |
-------------------------------
| Łukasz            |  67.50  |
| Pudzian           | 123.00  |
-------------------------------
```

Wyrównanie do centrum pozostawiamy Tobie :).

String Slicing
==============

Spróbuj:

```python
>>> text = “ala ma kota”
>>> text[0]     # string[int]
>>> text[2:]    # string[int:]
>>> text[:5]    # string[:int]
>>> text[3:7]   # string[int:int]
>>> text[::2]   # string[::int]
>>> text[::-1]  # string[::int]
>>> text[4:100] # string[int:int] :)
```

Pamiętaj! Twój komputer zawsze liczy od 0.

Metody
======

Istnieje obecnie mnóstwo metod formatowania stringów:

1.  capitalize() - zamienia pierwszą literę stringa z małej na wielką
2.  count(str, beg= 0,end=len(string)) - liczy, ile razy str pojawia się
w stringu lub podstringu stringa, gdzie beg to początowy index, a end
to index kończący.
3.  endswith(suffix, beg=0, end=len(string)) - ustala, czy string lub
podstring striga kończy się podanym przyrostkiem (suffix), zwraca
true, jeśli tak lub false, jeśli nie.
4.  find(str, beg=0 end=len(string)) - ustala, czy str pojawia się w stringu
lub w podstringu stringa, gdy podano index początkowy beg i index końcowy
end; zwraca index, jeśli odnajdzie str, a w przeciwnym razie zwraca -1.
5.  index(str, beg=0, end=len(string)) - podobna do metody find(), ale zgłasza błąd,
gdy nie znajdzie str.
6.  isalnum() - zwraca true, jeśli string ma co najmniej jeden znak i wszystkie
znaki są alfanumeryczne, jeśli nie - zwraca false.
7.  isalpha() - zwraca true, jeśli string ma conajmniej jeden znak i wszystkie
znaki są literami, jeśli nie - zwraca false.
8.  isdigit() - zwraca true, jeśli string zawiera tylko cyfry lub false,
jeśli nie zawiera.
9.  islower() - zwraca true, jeśli string zawiera co najmniej jedną literę
i wszystkie litery są małe. W przeciwnym razie zwraca false.
10. isnumeric() - zwraca true, jeśli string unicode zawiera tylko cyfry,
zaś false w przeciwnym razie.
11. isspace() - zwraca true, jeśli string zawiera wyłącznie spacje, zaś false
w przeciwnym razie.
12. istitle() - zwraca true, jeśli wielkość liter w stringu odpowiada zasadom
tworzenia tytułów (w ortografii anglojęzycznej), zaś false w przeciwnym wypadku.
13. isupper() - zwraca true, jeśli string zawiera co najmniej jedną literę
i wszystkie litery są wielkie. W przeciwnym razie zwraca false.
14. join(seq) - scala (łączy) sekwencję stringów dodając pomiędzy te stringi
wybrany separator.
15. len(string) - zwraca długość stringa.
16. lower() - zamienia wszystkie wielkie litery stringa na małe.
17. lstrip() - usuwa wszystkie spacje z początku stringa.
18. max(str) - zwraca najwyższą literę alfabetu ze stringa str.
19. min(str) - zwraca najniższą literę alfabetu ze stringa str.
20. replace(old, new \[, max\]) - zastępuje wszystkie wystąpienia stringa old
stringiem new, a w przypadku podania ilości wystąpień max, zastępuje
wystąpienia w ilości max.
21. rfind(str, beg=0,end=len(string)) - podobna do metody find(), ale przeszukuje
od końca stringa wstecz.
22. rindex( str, beg=0, end=len(string)) - podobna do metody index(), ale
przeszukuje od końca stringa wstecz.
23. rstrip() - usuwa wszystkie spacje na końcu stringa.
24. split(str="", num=string.count(str)) - rozbija string na podstawie
podanego rozgranicznika (domyślnie spacji) i zwraca listę podstringów.
Po podaniu parametru num rozbija string tylko do ilości num podstringów.
25. splitlines( num=string.count('n')) - rozbija string na wszystkie (lub
na podaną ilość num) NOWE LINIE i zwraca listę linii z usuniętym znakiem NOWA LINIA.
26. startswith(str, beg=0,end=len(string)) - ustala, czy string lub podstring stringa
(jeśli początkowy index beg i końcowy index end zostały podane) zaczyna się
od podstringu str; zwraca true, a w przeciwnym razie zwraca false.
27. strip(\[chars\]) - przeprowadza jednocześnie metody lstrip() i rstrip() na stringu.
28. swapcase() - zamienia litery wielkie na małe, a małe na wielkie.
29. title() - zwraca "tytułową" wersję stringu, czyli wszystkie słowa zaczynające się
wielką literą, a pozostałe elementy małą literą (według anglojęzycznej ortografii).
30. upper() - zamienia wszystkie małe litery stringa na wielkie.

Istnieje jeszcze ponad 10 innych metod, ale są one znacznie bardziej zaawansowane i często rzadko wykorzystywane.
