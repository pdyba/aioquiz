1.25 Docker
===========

# Docker

#### Co to

Praktyczna definicja dockera to kolejny mechanizm do ruchamiania kontenerów linuksowych.
Opisowa definicja dockera to "lżejsza" maszyna wirtualna. <br>
Uruchamiając VM odpalamy zwykle cały system operacyjny, w przypadku kontenera to moze byc tylko jeden proces.

#### Po co

Pozwala uruchamiać aplikacje i separować je od infrastruktury. 
Tak samo jak VM, mozemy uruchomić wiele instancji kontenerów na jednej maszynie/serwerze.

# Play with docker

https://labs.play-with-docker.com


# Kilka pojęć

* Obraz (docker image) - gotowe obrazy dockera do uruchomienia
* Kontener - pojedynczy uruchomiony obraz
* Repozytoria (docker registry) - tak jak repozytoria kodu, tylko z obrazami kontenerów 

# Let's play with docker!

`docker run hello-world`

`docker run -it python (python --version)`

`docker ps (-a); `

Warto mieć na uwadze, że nasz kontener istnieje tak długo jak proces, który był uruchomiony wewnątrz (po napisaniu)

`docker images`

`docker history python`



# Dockerfile

To zestaw instrukcji pozwalających nam opisać obraz, który chcemy zapisać. 
Składnia jest specyficzna dla Dockera, ale głównie sprowadza się do komend shellowych

FROM - podajemy obraz na którym chemy bazowac
RUN - uruchmiamy komendę shellową podczas budowania obrazu
COPY - kopiujemy lokalny plik do obrazu
CMD - uruchamiamy komendę podczas uruchomienia obrazu


`docker build -t myimage .`
`docker run -it myimage`

# Udostępnienie obrazu

`docker push myimage`

# Uruchomienie dockera jako serwis

Do tej pory nasze kontenery ginęły zaraz po tym jak je opuścilismy, można jednak odpalić usługę, która będzie działać cały czas. <br>
Budujemy jeszcze raz obraz z samym serwerem http (tym razem określimy dockerfile, z którego chcemy stworzyć obraz)
`docker build -t mynginx -f dockerfile_nginx .`

Kiedy mamy obraz, wystarczy użyć przełącznika -d
`docker run -d mynginx`

Żeby podłączyć się do działającego kontenera
`docker exec -it e018c69efb21 /bin/bash`


# Komunikacja z kontenerem

Domyślnie wszelka komunikacja z kontenerem jest zablokowana, podczas uruchomienia kontenera moąemy dokładnie określić co chcemy udostępnić

`docker run -p 80:80 -d mynginx`
`curl -XGET 127.0.0.1:80`


# Złożone aplikacje, czyli docker compose

Docker compose pozwala nam uruchomić wiele kontenerów w jednym pliku konfiguracyjnym, przykład poniżej:

```yaml
version: '3'
services:
  web:
    build: 
      context: .
      dockerfile: app_dockerfile
    ports:
     - "5000:5000"
  redis:
    image: myngix
```

`docker-compose up -d`

# Pliki txt do zadań

* [Zadanie 4.](./images/hello.py)
* [Zadanie 5.](./images/app.py)
* [Zadanie 5.](./images/app_dockerfile)
* [Zadanie 5.](./images/requirements.txt)