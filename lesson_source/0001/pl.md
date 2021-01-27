Instalacja
============

Podczas naszego warsztatu będziecie potrzebowali interpretera Python 3.8. 
Poniżej znajdziecie kilka wskazówek jak sprawdzić, czy macie już zainstalowany 
ten interpreter i jak go zainstalować wraz z kilkoma innymi potrzebnymi narzędziami.

Windows
-------

Możecie ściągnąć Pythona dla Windows bezpośrednio ze strony [python.org].
Po ściągnięciu pliku "*.msi" otwórzcie go i wykonujcie kolejne instrukcje. 
Ważne, żebyście zapamiętali ścieżkę dostępu - katalog, w którym zainstalowaliście 
Pythona - ponieważ będziemy potrzebowali tej informacji podczas instalacji
narzędzi <Narzędzia>.

[Instrukcja na YouTube](https://www.youtube.com/watch?v=0d6znPZb3PQ&t=3s)

Linux (Ubuntu, Fedora, itp.) lub Mac
-----------------------------------

W celu sprawdzenia wersji Pythona, wprowadźcie następującą komendę w 
wierszu poleceń:

```bash
$ python --version
Python 3.8

Python 3.8

```

Jeśli komenda `python` nie jest dostępna lub wyświetla się zła wersja:

### Ubuntu

Wprowadźcie w wierszu poleceń:

```bash
sudo apt-get install python3.6

sudo apt-get install python3.6

```

### Fedora

Wprowadźcie w wierszu poleceń:

```bash
sudo yum install python3.6
```

### OS X

Ściągnijcie pakiet dla swojego systemu z [python.org] .

### Inne

Użyjcie systemu pakietów zgodnego z Waszym systemem. Jeśli nie ma odpowiedniego 
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

```bash
Microsoft Windows [Version 6.1.7601]
Copyright (c) 2009 Microsoft Corporation. All rights reserved.

C:\Users\Name>

C:\Users\Name>

```

Tekst może się różnić, w zależności od wersji Windows, jakiej używacie.

`C:\Users\Name>` to znak zachęty. Informuje o tym, w jakim obecnie katalogu
(lub w jakim folderze) jesteście i oczekuje na Waszą komendę.
W dalszej części warsztatu zamiast `C:\Users\Name>` będziemy stosować `~$`, 
niezależnie od tego, z jakiego systemu korzystacie (Windows, Linux, MacOS).

Dzięki wierszowi poleceń możecie eksplorować zawartość swojego dysku (w ten
sam sposób jak w 'Mój Komputer'). Możecie to robić wprowadzając komendę
i naciskając `Enter`. Użycie komendy:

`dir`

wyświetla zawartość aktualnego katalogu. Na przykład jeśli
prompt pokazuje `C:\Users\Name`, komenda `dir` wyświetli zawartość Waszego
głównego katalogu.

Komenda: 

`cd katalog`

pozwala zmieniać aktualny folder na inny. Na przykład jeśli jesteście w
`C:\Users\Name`, możecie wejść do katalogu ze swoimi dokumentami wpisując
`cd Documents`. Wykonując komendę `dir`, zobaczycie coś bardzo podobnego.
Natomiast komenda `cd..` przeniesie Was o jeden poziom wyżej w drzewku
katalogów, czyli do katalogu, który zawiera Twój bieżący katalog.

``mkdir directory``
tworzy nowy katalog.

Środowisko wirtualne
--------------------

Musimy teraz wybrać katalog dla naszego wirtualnego środowiska. Środowisko wirtualne pozwoli nam
odizolować naszą pracę od reszty systemu. Na przykład możecie wybrać swój katalog domowy (użytkownika).

 Dla Windows 7 ścieżka do katalogu domowego użytkownika ``Ala`` będzie wyglądać tak:
``C:\Users\Ala\`` . Możecie wybrać inny katalog, ale ważne, aby zapamiętać, gdzie zachowaliście plik.
Musi być łatwo dostępny, bo będziemy go często używać.

Na przykład jeśli wasz domowy katalog to: ``C:\Users\lrekucki``, wiersz poleceń będzie wyglądał tak:

.. code-block:: bat

:: Windows
C:\Users\lrekucki> C:\Python34\python -m venv workshops

.. code-block:: sh

# Linux or Mac
~$ python3.4 -m venv workshops

.. Uwaga::
Ubuntu 14.04 ma błąd (https://bugs.launchpad.net/ubuntu/+source/python3.4/+bug/1290847), który sprawia
że moduł `venv` Pythona 3.4 nie działa podczas instalacji za pomocą `pip`.
Aby ominąć ten kłopot, użyjcie następujących komend, by stworzyć środowisko wirtualne:

    ~$ python -m venv --without-pip workshops
    ~$ source workshops/bin/activate
    ~$ wget https://bootstrap.pypa.io/get-pip.py
    ~$ python get-pip.py
    ~$ pip --version

Sprawdźcie _`https://pip.pypa.io/en/latest/installing.html` aby uzyskać więcej informacji o instalacji pip.

W waszym katalogu domowym stworzymy katalog ``workshops`` zawierający tak zwane  “wirtualne środowisko”.
Musimy je teraz aktywować:

.. code-block:: bat

:: Windows
C:\Users\lrekucki> workshops\Scripts\activate

.. code-block:: sh

# Linux or Mac
~$ source workshops/bin/activate

Komenda ``python`` uruchomi właściwą wersję Pythona, więc nie będziemy musieli wprowadzać
pełnej ścieżki, ani wersji.

Upewnij się, że uzyskałeś prawidłową konfigurację:

.. code-block:: bat

:: Windows
(workshops) C:\Users\lrekucki>where python
C:\Users\lrekucki\workshops\Scripts\python.exe
...

(workshops) C:\Users\lrekucki>where pip
C:\Users\lrekucki\workshops\Scripts\pip.exe
...

(workshops) C:\Users\lrekucki>python --version
3.8

.. code-block:: sh

# Linux or Mac
(workshops) ~$ which python
/home/lrekucki/workshops/bin/python
(workshops) ~$ which pip
/home/lrekucki/workshops/bin/pip
...

(workshops) ~$ python --version
3.8

.. _python.org: http://python.org/download/releases/3.8/

.. Uwaga::
Być może masz już w swoim systemie dostępną komendę ``pip``. Pamiętaj o sprawdzaniu, którą wersję pip używasz
przy pomocy komendy: ``pip --version``.
Możesz to wykonać uruchamiając jedną z tych komend:

.. code-block:: sh

    ~$ pip --version
    ~$ pip3 --version
    ~$ pip3.4 --version

Otrzymasz wersję pip oraz ścieżkę do katalogu twojego środowiska wirtualnego.

Jeśli nie możesz odszukać swojego ``pip`` albo masz problem po wpisaniu ``which pip`` (``where pip`` na windows),
byc może musisz re-instalować pip:


.. code-block:: sh

    ~$ python -m pip uninstall pip
    ~$ python -m ensurepip


Podsumowanie
------------

Instalacja nowego środowiska wirtualnego:

.. code-block:: bat

:: Windows
C:\Users\lrekucki> C:\Python34\python -m venv workshops

.. code-block:: sh

# Linux or Mac
~$ python3.4 -m venv workshops

Aktywacja środowiska wirtualnego:

.. code-block:: bat

:: Windows
C:\Users\lrekucki> workshops\Scripts\activate

.. code-block:: sh

# Linux or Mac
~$ source workshops/bin/activate

Upewnij się, że używasz prawidłowej wersji Pythona:

.. code-block:: sh

(workshops) ~$ python --version
3.8


[python.org](http://python.org)
