1.9 Command-line interface (or interpreter, or input)
=============================================

**CLI** - Jest programem uruchamianym z wiersza poleceń który akceptuje parametry wejściowe

Dzisiaj dla standardowego użytkownika wyparte przez GUI, jednak dalej bardzo często stosowane przez developerów i administratorów do konfigurowania maszyn, instalacji oprogramowania i dostępu do funkcji niedostępnych przez interfejsy graficzne.

Programy CLI są tworzone tak ich działanie mogło być parametryzowane co ułatwia ich ponowne użycie. 

Przykłady:
-
#####PIP:
Linux/Mac:
```
pip install mysoftware
```

Windows:
```
C:\>pip install mysoftware
```

Inne przykłady systemowych CLI:
- Linux/Mac: `ls, cd, cp, mv, mkdir`
- Windows: `dir, cd, copy, move, type`

Nazewnictwo
-

Nazewnictwo nie jest oficjalnie ustandaryzowane. Przyjmuje się:
- Komenda jest całym wyrażeniem wykonanym w wierszu poleceń
- Składa się ona z argumentów
- Argument 0 jest nazwą wykonywanego programu, argument 1 kolejnym elementem itd.
- Te argumenty są często nazywane `positional parameters`
```
$ ls -la /tmp /var/tmp
arg0 = ls
arg1 = -la
arg2 = /tmp
arg3 = /var/tmp
```

- Opcja jest typem argumentu który który modyfikuje działanie programu, na przykład `-v` lub `--verbose` gdy chcemy uzystać dodatkowe informacje o działającym programie
- Opcje najczęściej nie są wymagane.
- Jeśli opcja nie ma parametrów nazywana jest `flag` lub `switch`
- Parametr jest argumentem który przekazuje informację do samego programu (np. `ls /var`) lub do opcji (np. `ls -`), czasami taka opcja jest nazywana `option-argument`
- Wartości opcji są zaimplementowane w programie (możemy używać tylko dostępnych), wartości parametrów są najczęściej dowolne dowolne
- Programy same w sobie mogę implementować "subkomendy" które posiadają własne zestawy opcji i parametrów, np. `git --git-dir a.git status -s` - w tym przypadku uruchamiamy program `git` z opcją `--git-dir` a następnie subkomendę `status` z opcją `-s`

Python
-
Dostęp do wszystkich argumentów wiersza poleceń jest zapewniony przez zmienną `sys.argv`. Jest to lista zainicjowana wartościami kolejnych argumentów.

Wykonanie takiego programu:
```python
import sys
print(sys.argv)
```

W taki sposób powinno zwrócić wynik:
```bash
$ python main.py -o option
['main.py', '-o', 'option']
``` 

Analogicznie `sys.argv[1:]` zwróci tylko argumenty bez nazwy programu.

Do elementów `sys.argv` odwołujemy się jak do normalnej listy.

`sys.argv` jest dostępna globalnie. Nie jest stałą, więc jej zawartość może być modyfikowana w czasie działanie programu.  

argparse
-
argparse jest modułem który ułatwia przetwarzanie parametrów wejściowych programu. Programista definiuje listę wymaganych i opcjonalnych parametrów, domyślne wartości, zachowania a `argparse` dba o to, aby sparsować `sys.argv` w poprawny sposób.

Przykład wykorzystania:
```python
import argparse

parser = argparse.ArgumentParser(description='CLI example')

parser.add_argument("square", help="display a square of a given number",
                    type=int)

parser.add_argument("--verbose", help="increase output verbosity",
                    action="store_true")

args = parser.parse_args()

if args.verbose:
    print(f"Arguments: {args}")

print(args.square ** 2)
```

Click
-
Click jest najbardziej zaawansowaną biblioteką do budowania skomplikowanych CLI, jest używany przez wiele innych bibliotek na przykład przez Flask albo Black.

Instalacja:
`pip install click`

Przykład:
```python
import click


@click.command()
@click.option('--count', default=1, help='Number of greetings.')
@click.option('--name', prompt='Your name',
              help='The person to greet.')
def hello(count, name):
    for x in range(count):
        click.echo(f"Hello {name}!")


hello()
```

Uruchomienie takiego programu będzie wyglądło następująco:
```
$ python hello.py --count=2
Your name: Patryk
Hello Patryk!
Hello Patryk!
```

Click bazuje na tworzeniu komand za pomocą dekoratora `click.command()`. Do takiej funkcji można dodawać następnie parametry które będą automatycznie parsowane z parametrów wejściowych a strona pomocy będzie automatycznie generowana. 

####Opcje w Click:
```python
@click.command()
@click.option('-s', '--string-to-echo')
def echo(string_to_echo):
    print(string_to_echo)
```

Opcje tworzy się za pomocą dekoratora `@click.option`, następnie wartość jest dostępna w argumencie samej funkcji pod taką samą nazwą jak parametr. 
Click pozwala na dodawanie modyfikatorów do opcji:
- `default` - pozwana na nadanie wartości domyślnej
- `required` - wymusza konieczność podania wartości
- `nargs` - pozwala na przekazanie kilku wartości w jednej opcji
- `type` - pozwala na określenie typu parametru (domyślnie str)
- `is_flag` - zamienia opcje w flagę (nie wymaga wartości flagi), przykład:

```python
@click.command()
@click.option('--debug', is_flag=True)
def main(debug):
    if debug:
        print("Debug")
    print("Hello")
```
Wykonanie:
```
$ python main.py
Hello

$ python main.py --debug
Debug
Hello
```

Opcje pozwalają na zdefiniowanie tylko wybranych wartości:

```python
@click.command()
@click.option('--type', type=click.Choice(['type1', 'type2'], case_sensitive=False))
def main(type):
    print(type)
```
Wykonanie:
```
$ python main.py --type type1
type1

$ python main.py --type type3
Usage: main.py [OPTIONS]
Try 'main.py --help' for help.

Error: Invalid value for '--type': invalid choice: type3. (choose from type1, type2)
```

Click pozwala na prompt z pytaniem o wartość opcji jeśli ta nie zostanie podana:

```python
@click.command()
@click.option('--name', prompt="Your name")
def main(name):
    click.echo(f"Hello {name}")
```
Wykonanie:
```
$ python main.py
Your name: Patryk
Hello Patryk
```

Dodatkowo wpisywana wartość może zostać ukryta dodając argument `hide_input=True` i może zostać dodana konieczność potwierdzenie wartości za pomocą argumentu `confirmation_prompt=True` .

Prompt może wykorzystywać domyślnie wartości, także dynamicze:
```python
@click.command()
@click.option('--profile', prompt=True, default=lambda: os.environ.get('AWS_PROFILE', ''))
def main(profile):
    print(profile)
```
Wykonanie:
```
export AWS_PROFILE=TEST

$ python main.py
Profile [AWS_TEST]: 
```

Kompletna dokumentacja opcji wraz z przykładami: https://click.palletsprojects.com/en/7.x/options/

####Argumenty w Click:

Argumenty są bardzo podobne do opcji z tym że są pozycyjne. Tworzy się je za pomocą dekoratora `@click.argument`.
```python
@click.command()
@click.argument('arg1')
@click.argument('arg2')
def main(arg1, arg2):
    print(arg1)
    print(arg2)
```
Wykonanie:
```
$ python main.py value1 value2
value1
value2
```

Specjalnym typem argumentu jest plik, który pozwala automatycznie sprawdzać czy plik istnieje i otwierać go:
```python
@click.command()
@click.argument('input', type=click.File('rb'))
def main(input):
    content = input.read().decode('utf-8')
    print(content)
``` 
Wykonanie:
```
$ python main.py file.txt
Content: content of the file

$ python main.py another_file.txt
Error: Invalid value for 'INPUT': Could not open file: test.txt: No such file or directory```
```

Kompletna dokumentacja argumentów wraz z przykładami: https://click.palletsprojects.com/en/7.x/arguments/

####Komendy w Click:
Chcąc tworzyć komendy należy najpierw utworzyć grupę za pomocą dekoratora `@click.group()`. Funkcja z takim dekoratorem zostałe główną komendą a następnie można dodawać do niej subkomendy:
```python
@click.group()
def cli():
    pass


@click.command()
def install():
    print('Installing software')


@click.command()
def uninstall():
    click.echo('Uninstalling software')


cli.add_command(install)
cli.add_command(uninstall)
```

Wykonanie:
```
$ python main.py install
Installing software

$ python main.py uninstall
Uninstalling software

$ python main.py --help
Usage: main.py [OPTIONS] COMMAND [ARGS]...

Options:
  --help  Show this message and exit.

Commands:
  install
  uninstall
```

Takie subkomendy mogą posiadać własne listy opcji i argumentów, własne strony pomocy a takie kolejne zagnieżdżone komendy

Kompletna dokumentacja komend wraz z przykładami: https://click.palletsprojects.com/en/7.x/commands/

####Żródła:
- https://www.w3schools.com/whatis/whatis_cli.asp
- https://stackoverflow.com/questions/36495669/difference-between-terms-option-argument-and-parameter/36495940#36495940
- https://realpython.com/python-command-line-arguments
- https://click.palletsprojects.com/