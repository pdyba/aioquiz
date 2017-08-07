Instalacja
============

Podczas naszego warsztatu będziecie potrzebowali interpretera Python 3.4. 
Poniżej znajdziecie kilka wskazówek jak sprawdzić, czy macie już zainstalowany 
ten interpreter i jak go zainstalować wraz z kilkoma innymi potrzebnymi narzędziami.

Windows
-------

Możecie ściągnąć Pythona dla Windows bezpośrednio ze strony [python.org].
Po ściągnięciu pliku ".msi" otwórzcie go i wykonujcie kolejne instrukcje. 
Ważne, żebyście zapamiętali ścieżkę dostępu - folder, w którym zainstalowaliście 
Pythona - ponieważ będziemy potrzebowali tej informacji podczas instalacji
narzędzi <Narzędzia>.

[Instrukcja na YouTube](https://www.youtube.com/watch?v=0d6znPZb3PQ&t=3s)

Linux (Ubuntu, Fedora, itp.) lub Mac
-----------------------------------

W celu sprawdzenia wersji Pythona, wprowadźcie następującą komendę w 
wierszu poleceń:

    :::bash
    $ python --version
    Python 3.5.0


Jesli komenda `python` nie jest dostępna lub wyświetla się zła wersja:

### Ubuntu

Wprowadźcie w wierszu poleceń:

    :::bash
    sudo apt-get install python3.4


### Fedora

Wprowadźcie w wierszu poleceń:

    :::bash
    sudo yum install python3.4
****

### OS X

Ściągnijcie pakiet dla Twojego systemu z [python.org] .

### Inne

Użyjcie systemu palkietu zgodnego z Twoim systemem. Jeśli nie ma odpowiedniego 
systemu lub nie możecie znaleźć Pythona, możecie zainstalować go wykorzystując 
źródła na stronie [python.org]. Będzie wymagany kompilator i biblioteka readline.

Nieoficjalnie - zakładamy, że użytkowicy mniej popularnych (ale przecież nie gorszych!)
dystrybucji zdołają wykonać to zadanie bez większych problemów :).

Narzędzia
---------

### Wiersz poleceń Windows

Będziemy pracować głównie w wierszu poleceń. Aby uruchomić wiersz 
poleceń w Windows, naciśnijcie 'Win+R'. W nowo otwartym okienku wpiszcie 'cmd'
i kliknijcie 'OK'. Pojawi się nowe okienko z białym tekstem na czarnym tle:

    :::bash
    Microsoft Windows [Version 6.1.7601]
    Copyright (c) 2009 Microsoft Corporation. All rights reserved.

    C:\Users\Name>

Tekst może się różnić, w zależności od wersji Windows, jaką używacie.

`C:\Users\Name>` to prompt. Informuje nas o tym, na jakim obecnie dysku 
(lub w jakim folderze) jesteśmy i oczekuje na naszą komendę.
W dalszej części warsztatu zamiast `C:\Users\Name>` będziemy stosować `~$`, 
niezależnie od tego, z jakiego systemu korzystacie (Windows, Linux, MacOS).

Dzięki wierszowi poleceń możiecie eksplorować zawartość swojego dysku (w ten
sam sposób jak w 'Mój Komputer'). Możecie to robić wprowadzając komendę
i naciskając `Enter`. Uzycie komendy:

`dir`

Wyświetla zawartość aktualnego foldera. Na przykła jeśli
`prompt` pokazuje `C:\Users\Name`, komenda `dir` wyświetli zawartość twojego
głównego foldera.

Komenda: 

`cd directory`

pozwala zmieniać aktualny folder na inny. Na przykład jeśli jesteście w
`C:\Users\Name`, możeice wejść do foldera ze swoimi dokumentami by
entering `cd Documents`. If you execute the `dir` command, you will
see something familiar. The command `cd..` will move you one level
up in the directory tree, that is, to the directory that cont


[python.org](http://python.org)
