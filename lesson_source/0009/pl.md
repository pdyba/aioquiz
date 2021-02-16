# Funkcje wbudowane


## Wywoływanie funkcji


Nasz program wygląda dobrze, ale aby użytkownik mógł policzyć swój BMI,
musimy nadal jeszcze zmienić zawartość programu. Poznaliśmy juz komendy 
`input` oraz `print` teraz czas na więcej. 

Aby napisać taki program, musimy nauczyć się używać funkcji. Pierwszą funkcją,
jakiej się nauczymy jest help:

> help Type help() for interactive help, or help(object) for help about object.

Funkcja help jest bardzo przyjazna i wyjasni nam sama jak powinniśmy jej używać.

```python
help(help)
```

Może też powiedzieć Wam, jak używać innych funkcji:


```python
help(input)
```

```
Help on function input in module builtins:

input(...) input(\[prompt\]) -> string
Read a string from standard input. The trailing newline is stripped.

If the user hits EOF (Unix: Ctl-D, Windows: Ctl-Z+Return), raise EOFError.
On Unix, GNU readline is used if enabled. The prompt string, if given,
is printed without a trailing newline before reading.
```

Użyjemy funkcji input, by załadować dane podane przez użytkownika.
W opisie czytamy, że dane użytkownika input odczytuje jako string:

```python
>>> input()
Ala has a cat
'Ala has a cat'

'Ala has a cat'
```

Teraz nauczycie się, co oznacza wyrażenie "wywołać funkcję". Możecie
wywołać funkcję, używając `()`. Jest to informacja dla interpretera,
by wywołał funkcję. Wywołanie funkcji uruchomi funkcję. Jeśli zapomnicie
użyć `()` po nazwie funkcji, funkcja nie zostanie wywołana. **W takiej
sytuacji nie otrzymacie komunikatu o błędzie, ponieważ komenda, którą
wpisaliście jest wciąż prawidłowa.**

Ogólnie mówiąc, wywołana funkcja **zwraca** pewne wartości. Funkcja
input zwraca string, a zatem możemy użyć jej w ten sam sposób, jak
wcześniej używaliśmy stringów.

Na przykład możemy użyć `input()`, by zachować podany string jako nazwę:

```python
>>> name = input()
Joanna
>>> name
'Joanna'
>>> print("Masz na imię:", name)
Masz na imię: Joanna
```

## Istotne Funkcje wbydowane w Pythona


### Związane z typami danych (do konwersji)


* int()
* str()
* bytes()
* float()
* set()
* dict()
* ascii()
* bool()
* ord()
* chr()
* frozenset()
* list()
* tuple()


### Związane z operacjami matematycznymi

* abs()
* min()
* hex()
* divmod()
* oct()
* bin()
* sum()
* pow()
* max()
* round()
* complex()

### Pozostałe często używane

* print()
* input()
* help()
* dir()
* len()
* type()
* open()
* range()
* sorted()
* filter()
* reversed()
* isinstance()

### Pozostałe często używane (zaawansowane)

* all()
* any()
* hash()
* enumerate()
* breakpoint()
* map()
* zip()

### Dedykowane pracy z klasami

* getattr()
* delattr()
* setattr()
* hasattr()
* staticmethod()
* issubclass()
* super()
* property()
* classmethod()

### Pozostałe
		
* callable()
* memoryview()
* next()
* slice()
* id()
* object()
* globals()
* bytearray()
* iter()
* format()
* vars()
* locals()
* repr()

### Zakazane !

* eval()
* exec()
* compile()



