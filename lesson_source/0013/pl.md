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

Możesz zmienić zawartość słownika poprzez dodanie do niego nowego elementu
lub pary klucz-wartość. Prześledź poniższe przykłady:

	>>>  słownik = {'Imię': 'Marta', 'Wiek': 21, 'Zawód':'Python Developer'} 
	>>>  słownik['Wiek'] = 8  # zmiana wartości w istniejącym elemencie
	>>>  słownik['Zawód'] = 'Uczeń'  # zmiana wartości w istniejącym elemencie
	>>>  słownik['Szkoła'] = "Szkoła podstawowa"  # Dodanie nowego elementu do słownika
	>>>  print(słownik['Wiek'])
	>>>  print(słownik['School'])

Usuwanie elementów słownika
---------------------------

Możesz zarówno usuwać poszczególne elementy słownika, jak i usunąc całą zawartość
słownika. Możesz także usunąć cały słownik przy pomocy jednej operacji.

Aby całkowicie usunąć cały słownik, możesz użyć komendy del. Oto przykład:

	>>>  słownik = {'Imię': 'Marta', 'Wiek': 8, 'Zawód':'Uczeń', 'Szkoła':'Szkoła podstawowa'}
	>>>  del słownik['Imię'] # usuwanie elementu o kluczu 'Imię'
	>>>  print(słownik) 
	>>>  słownik.clear() # usuwanie wszystkich elementów słownika 
	>>>  print(słownik) 
	>>>  del słownik # usuwanie całego słownika

Zagnieżdżanie
=============

W Pythonie możesz tworzyć obiekty zagnieżdżone, na przykład:

    :::python3
    ZOO = {
        'zwierzęta': {
            'pyton': {
                'jedzenie': [
                    'myszy',
                    'króliki',
                    'szczury',
                ]
                'środowisko': {
                    'temperatura': 25,
                    'wilgotność': 80,
                }
                'pomieszczenie': 'klatka',
            },
            'słodki_króliczek': {
                'jedzenie': [
                    'marchewki',
                    'marchewki',
                    'marchewki',
                ]
                'środowisko': {
                    'temperatura': 20,
                    'wilgotność': 35,
                }
                'pomieszczenie': 'na wolności',
            },
        'kontakt': {
            'telefon': 0 700 800 900,
            'email': 'zoo@zoo.zoo'
        }
    }

Jak widzicie, słownik może zawierać na przykład słowniki słowników i listy.

