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
Podsmażaj cebulę i szynkę aż cebula się zezłoci.
Wlej jajka i mieszaj podrzewając aż do otrzymania pożądanej konsystencji.
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
    pokroj(ocebula)
    jeśli masło.stan != 'płynny': roztol_w_rondelku(masło)
    jeśli cebula.kolor != 'złoty': podsmaż(cebula, szynka)
    jeśli jajka.stan != pożądany_stan: gotuj_i_mieszaj(wszystko)
    zjedz(wszystko)


Ćwiczenia
---------

Ćwiczenia: Zabawa w kształt:

1.  Nazwijcie swoją drużynę.
2.  Każda drużyna niechaj stworzy na kartce dowolną zamkniętą 
    figurę geometryczną używając 4-8 odcinków, na przykład kwadrat
    lub ośmiokąt.
3.  Podpiszcie swoją kartkę nazwą drużyny.
4.  Roztasujcie kartki wśród wszystkich drużyn.
5.  After receiving an image from other team: create instruction that
    will allow another team to recreate the same figure as closely as
    possible can be.
6.  Sign the paper sheet with previous team names and add your team
    name.
7.  Shuffle only instructions across all teams.
8.  After receiving instruction from other team, process the instruction
    and create the image it provides.
9.  Sign the paper sheet with previous team names and add your team
    name.

Lets compare the images with originals, instructions. Think about the
differences and why did they happen.

Deaf phone:

1.  Each team creates random sentence max 20 characters.
2.  Sign the paper sheet with your team name.
3.  Shuffle all sentence across all teams.
4.  Each team creates an encoding (ciphering) algorithm. Not more then 6
    steps.
5.  Using the algorithm encode the received sentence and write the
    secret message on paper with encoding algorithm.
6.  Sign the paper sheet with previous team names and add your team
    name.
7.  Shuffle all encoded sentence with encoding mechanism across all
    teams.
8.  Each team decodes the sentence and writes down the decoding
    algorithm on a new sheet of paper.
9.  Write down the given encoded sentence on decoding algorithm paper
10. Sign the paper sheet with previous team names and add your team
    name.
11. Each team decodes the sentence.
12. Sign the paper sheet with previous team names and add your team
    name.
13. Now lets see if the sentences matches ? What have happened to them ?

Can You now feel how useful is to use algorithm and how often do You use
them

