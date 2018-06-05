1.25 Docker
===========

Docker
-------

####Co to

Praktyczna definicja dockera to kolejny mechanizm do ruchamiania kontenerow linksowych.
Opisowa definicja dockera to "lzejsza" maszyna wirtualna. <br>
Uruchamiajac VM odpalamy zwykle caly system operacyjny, w przypadku kontenera to moze byc tylko jeden proces.

####Po co

Pozwala uruchamiac aplikacje i separowac je od infrastruktury. 
Tak samo jak VM, mozemy uruchomic wiele instancji kontenerow na jednej maszynie/serwerze.

Play with docker
----------------
https://labs.play-with-docker.com


Kilka pojec
-----------

* Obraz (docker image) - gotowe obrazy dockera do uruchomienia
* Kontener - pojedynczy uruchomiony obraz
* Repozytoria (docker registry) - tak jak repozytoria kodu, tylko z obrazami kontenerow 


Warto miec na uwadze, ze nasz kontener istnieje tak dlugo jak proces ktory byl uruchomiony wewnatrz (po napisaniu )



Dockerfile
----------
To zestaw instrukcji pozwalajacych nam opisac kontener ktory chemy uruchomic. 
Skladnia jest specyficzna dla Dockera, ale glownie sprowadza sie to do komend shellowych




Pliki txt do zadań
------------------

* [Zadanie 4.](./images/Dockerfile)
* [Zadanie 4.](./images/hello.py)