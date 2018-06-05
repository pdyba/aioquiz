1.25 Docker
===========

# Docker

#### Co to

Praktyczna definicja dockera to kolejny mechanizm do ruchamiania kontenerow linksowych.
Opisowa definicja dockera to "lzejsza" maszyna wirtualna. <br>
Uruchamiajac VM odpalamy zwykle caly system operacyjny, w przypadku kontenera to moze byc tylko jeden proces.

#### Po co

Pozwala uruchamiac aplikacje i separowac je od infrastruktury. 
Tak samo jak VM, mozemy uruchomic wiele instancji kontenerow na jednej maszynie/serwerze.

# Play with docker

https://labs.play-with-docker.com


# Kilka pojec

* Obraz (docker image) - gotowe obrazy dockera do uruchomienia
* Kontener - pojedynczy uruchomiony obraz
* Repozytoria (docker registry) - tak jak repozytoria kodu, tylko z obrazami kontenerow 

# Let's play with docker!

`docker run hello-world`

`docker run -it python (python --version)`

`docker ps (-a); `

Warto miec na uwadze, ze nasz kontener istnieje tak dlugo jak proces ktory byl uruchomiony wewnatrz (po napisaniu )

`docker images`

`docker history python`



# Dockerfile

To zestaw instrukcji pozwalajacych nam opisac obraz, ktory chemy zapisac. 
Skladnia jest specyficzna dla Dockera, ale glownie sprowadza sie to do komend shellowych

FROM - podajemy obraz na ktorym chemy bazowac
RUN - uruchmiamy komende shellowa podczas budowania obrazy
COPY - kopiujemy lokalny plik do obrazu
CMD - uruchamiamy komende podczas uruchomienia obrazu


`docker build -t myimage .`
`docker run -it myimage`

# Udostepnienie obrazu

`docker push myimage`

# Uruchomienie dockera jako serwis

Do tej pory nasze kontenery ginely zaraz po tym jak je opuscilismy, mozna jednak odpalic usluge, ktora bedzie dzialac caly czas. <br>
budjemy jeszcze raz obraz z samym serwerem http (tym razem okrelslimy dockerfile z ktorego chcemy stworzyc obraz)
`docker build -t mynginx -f dockerfile_nginx .`

Kiedy may obraz wystarczy uzyc  przelacznika -d
`docker run -d mynginx`

Zeby podlaczyc sie do dzialajacego kontnera
`docker exec -it e018c69efb21 /bin/bash`


# Komunikacja z kontenerem

Domyslnie wszelka komunikacja z kontenerem jest zablokowana, podczas uruchomienia kontenera mozemy dokladnie okreslic co chcemy udostepnic

`docker run -p 80:80 -d mynginx`
`curl -XGET 127.0.0.1:80`


# Zlozone aplikacje, czyli docker compose

Docker compose pozwala nam uruchamia wiele kontenerow w jednym pliku konfiguracyjnym, przykladm ponizej

```yaml
version: '3'
services:
  web:
    build: 
      context: .
      dockerfile: app_dockerfile
    ports:
     - "5000:5000"
  redis:`
    image: myngix
```


# Pliki txt do zadań

* [Zadanie 4.](./images/hello.py)
* [Zadanie 5.](./images/app.py)
* [Zadanie 5.](./images/app_dockerfile)
* [Zadanie 5.](./images/requirements.txt)