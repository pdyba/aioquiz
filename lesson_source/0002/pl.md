Wprowadzenie do algorytmów
==========================

Algorytm jest zestawem operacji do wykonania krok po kroku. 
Jak przepis kucharski.


Przykład
--------

**Przykład z jajecznicą:**

Składniki:

-   jajka
-   szynka
-   cebula
-   masło
-   pieprz
-   sól

**Przepis:**

W kubku lub małej miseczce roztrzep widelcem jajka z pieprzem i solą. 
Pokroj szynkę i cebulę na drobne kawałki. Roztop masło w rondelku na
małym ogniu.
Podsmażaj cebulę i szynkę, aż cebula się zezłoci.
Wlej jajka i mieszaj podrzewając, aż do otrzymania pożądanej konsystencji.
Nie gotuj za długo.

Schemat blokowy
---------------

![image](./images/scambled_eggs_diagram.png)

Pseudokod
---------

    :::python3
    składniki = jajka, szynka, cebula, masło, pieprz, sól
    moje_składniki = weź(składniki)
    jeśli długość(moje_składniki) < składniki - idź na zakupy
    roztrzep(jajka, pieprz, sól)
    pokroj(szynka)
    pokroj(cebula)
    jeśli masło.stan != 'płynny': roztop_w_rondelku(masło)
    jeśli cebula.kolor != 'złoty': podsmaż(cebula, szynka)
    jeśli jajka.stan != pożądany_stan: gotuj_i_mieszaj(wszystko)
    zjedz(wszystko)


Ćwiczenia
---------

Zabawa w kształt:

1.  Nazwijcie swoją drużynę.
2.  Każda drużyna niechaj stworzy na kartce dowolną zamkniętą 
    figurę geometryczną używając 4-8 odcinków, na przykład kwadrat
    lub ośmiokąt.
3.  Podpiszcie swoją kartkę nazwą drużyny.
4.  Roztasujcie kartki wśród wszystkich drużyn.
5.  Po otrzymaniu kartki od innej drużyny: stwórzcie instrukcję, która
    pozwoli innej drużynie odtworzyć taką samą figurę jak najbardziej
    podobną do pierwotnej figury.
6.  Podpiszcie instrukcję nazwą poprzedniej drużyny i dodajcie nazwę 
    swojej drużyny.
7.  Roztasujcie wśród wszystkich drużyn tylko instrukcje.
8.  Po otrzymaniu instrukcji od innej drużyny wykonajcie ją i narysujcie
    według niej figurę geometryczną.

9.  Podpiszcie rysunek nazwą poprzedniej drużyny i dodajcie nazwę swojej
    drużyny.

Porównajcie rysunki z oryginałami i instrukcjami. Zwróćcie uwagę na różnice
i zastanówcie się, jaka jest ich przyczyna.

Głuchy telefon:

1.  Każda z drużyn tworzy dowolne zdanie o długości masymalnie 20 liter.
2.  Podpiszcie kartkę nazwą swojej drużyny.
3.  Roztasujcie zdania wśród wszystkich drużyn.
4.  Każda z drużyn tworzy algortym kodujący (szyfrujący) nie dłuższy
    niż 6 kroków.
5.  Używając algorytmu zakodujcie otrzymane zdanie i napiszcie sekretną
    wiadomość na kartce zawierającej algorytm kodujący.
6.  Podpiszcie kartkę nazwą poprzedniej drużyny i swojej drużyny.
7.  Roztasujcie wszystkie zakodowane zdania i mechanizm kodujący pomiędzy drużyny.
8.  Każda drużyna odkodowuje otrzymaną wiadomość i zapisuje algorytm dekodujący
    na nowej kartce.
9.  Zapiszcie otrzymane zakodowane zdanie na kartce z algorytmem rozkodowującym.
10. Podpiszcie kartkę nazwami poprzednich drużyn i nazwą swojej drużyny.
11. Każda drużyna rozszyfrowuje zdanie.
12. Podpiszcie kartkę nazwami poprzednich drużyn i nazwą swojej drużyny.
13. Sprawdźcie czy zdania pasują? Co się z nimi stało?

Czy widzicie jak użyteczne są algorytmy i jak często ich używacie?

