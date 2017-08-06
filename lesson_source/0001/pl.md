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

`C:\Users\Name>` is a prompt. It informs us of the directory (or folder)
in which we currently are and waits for a command. Later during the
workshop `C:\Users\Name>` we will refer to it with `~$`, independently
of your operating system (Windows, Linux, MacOS).

Using the command line, you can move around the contents of the disc (in
the same way as in `My Computer`). You can do that by entering commands
and pressing `Enter`. Use the following commands:

`dir`

Displays the contents of the current directory. For example, if the
`prompt` shows `C:\Users\Name`, the `dir` command displays the
contents of our home directory.

`cd directory`

Changes the current directory. For example, if you are in
`C:\Users\Name`, you can access the directory with your documents by
entering `cd Documents`. If you execute the `dir` command, you will
see something familiar. The command `cd..` will move you one level
up in the directory tree, that is, to the directory that cont


[python.org](http://python.org)
