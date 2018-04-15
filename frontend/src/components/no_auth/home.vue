<template>
    <b-container>
        <div class="section-colored text-center">
            <b-container>
                <b-row>
                    <b-col lg="12">
                        <h1>PyLove.org</h1>
                        <h2>Bezpłatna nauka programowania w Pythonie</h2>
                    </b-col>
                </b-row>
            </b-container>
        </div>

        <div class="section">
            <b-container>
                <b-row>
                    <b-col md="6">
                        <h3><i class="fa fa-calendar"></i>Kiedy?</h3>
                        <h2>Wtorki 18:45</h2>
                        <p>Zajęcia będą trwały pełne dwie godziny do 20:45 i
                            poprowadzą je doświadczeni mentorzy – programiści
                            Pythona.
                        </p>
                        <br>
                        <p><a href="#/program">Szczegółowy program spotkań</a></p>
                    </b-col>
                    <b-col md="6">
                        <h3><i class="fa fa-location-arrow"></i>Gdzie?</h3>
                        <h2>Na Collegium Da Vinci!</h2>
                        <b-img fluid class="img-responsive img-home-portfolio"
                               src="images/cdv_logo.png"></b-img>
                        <p>ul. gen. Tadeusza Kutrzeby 10, 61-719 Poznań</p>
                        <p>Collegium Da Vinci to jedna z najstarszych niepublicznych
                            uczelni w Poznaniu. Od 20 lat działa na polskim rynku
                            edukacyjnym i w tym okresie stała się jedną z wiodących
                            szkół wyższych w Wielkopolsce. </p>
                        <br>

                        <p><a href="http://cdv.pl">Strona Collegium Da Vinci</a> | <a
                                href="https://goo.gl/maps/GiVUq7iASbM2">Mapka</a></p>
                    </b-col>
                </b-row>
            </b-container>
        </div>


        <div class="section-colored">
            <b-container>
                <b-row>
                    <b-col md="4">
                        <h3><i class="fa fa-check-circle"></i> Staże i praktyki</h3>
                        <p>Dla najlepszych uczestniczek/uczestników czekają płatne
                            staże i praktyki u naszych partnerów.</p>
                    </b-col>
                    <b-col md="4">
                        <h3><i class="fa fa-pencil"></i>Materiały po polsku</h3>
                        <p> Nasi mentorzy przygotowują materiały w formie lekcji,
                            ćwiczeń, zadań domowych i pytań sprawdzających w języku
                            polskim.</p>
                    </b-col>
                    <b-col md="4">
                        <h3><i class="fa fa-folder-open"></i>Społeczność</h3>
                        <p>Dzięki tym warsztatom macie szansę dołączyć do grona
                            programistów języka Python, zdaniem wielu najbardziej
                            otwartej społeczności programistów na świecie.</p>
                    </b-col>
                </b-row>
            </b-container>
        </div>


        <b-col class="section">
            <b-container>
                <b-row>
                    <b-col lg="12"  class="text-center">
                        <h2>Zdjęcia z warsztatów prowadzonych przez naszych
                            mentorów.</h2>
                        <hr>
                    </b-col>
                    <b-col lg="4" v-for="img in images_home">
                        <b-img fluid class="img-responsive img-home-portfolio"
                               :src="'images/' + img + '.jpg'"></b-img>
                    </b-col>

                </b-row>
            </b-container>
        </b-col>


        <div class="section-colored">
            <b-container>
                <b-row>
                    <div class="col-lg-6 col-md-6 col-sm-6">
                        <h2>Warunki uczestnictwa:</h2>
                        <p>W spotkaniach może wziąć udział każdy, niezależnie od płci,
                            wieku (16+), wykształcenia, czy wykonywanego zawodu.
                            Konieczne są:</p>
                        <ul>
                            <li>Własny laptop</li>
                            <li>Zainstalowane środowisko:
                                <ul>
                                    <li>
                                        <a href="https://www.youtube.com/watch?v=0d6znPZb3PQ&t=3s">
                                            Python: instrukcja dla systemu Windows
                                        </a></li>
                                    <li><a href="https://youtu.be/ebgy92mgh-E">
                                        PyCharm: instrukcja dla systemu Windows</a>
                                    </li>
                                    <li>
                                        <a href="https://www.youtube.com/watch?v=vzV2qrrEKaA&t=1s">
                                            PyCharm: instrukcja dla systemu Linux
                                        </a></li>
                                </ul>
                            </li>
                            <li>Zarejestrowanie się w <a
                                    href="https://pylove.org/#/register">naszym
                                systemie</a>
                            </li>
                            <li>Podstawowa znajomość języka angielskiego. <i>(Spotkania
                                będą prowadzone w języku polskim, jednakże dla
                                opanowania składni języka Python znajomość języka
                                angielskiego będzie niewątpliwie pomocna)</i>
                            </li>
                        </ul>
                    </div>
                    <div class="col-lg-6 col-md-6 col-sm-6">
                        <b-img fluid class="img-responsive" src="images/home_0010.jpg"></b-img>
                    </div>
                </b-row>
            </b-container>
        </div>


        <div class="section">
            <b-container>
                <h1>Partner strategiczny</h1>
                <b-row>
                    <div class="col-lg-4 col-md-4">
                        <b-img fluid class="img-responsive"
                               src="http://pypolska.org/img/pypolska_logo.png"></b-img>
                    </div>
                    <div class="col-lg-8 col-md-8">
                        <h3>Stowarzyszenie PyPolska</h3>
                        <p></p>
                        <p class="text-justify">
                            PyPolska to stowarzyszenie miłośników języka Python. Naszym nadrzędnym celem jest dzielenie
                            się tym
                            zamiłowaniem z innymi. Promujemy wymianę wiedzy organizując m.in. największą w Polsce
                            konferencję
                            programistów Pythona - PyCon PL. Aktywnie działamy w kierunku tworzenia nowego pokolenia
                            programistów - w ramach projektu Microbit:Polska organizujemy i prowadzimy warsztaty dla
                            dzieci,
                            młodzieży oraz nauczycieli. Ponadto wspieramy lokalne inicjatywy i społeczności związane z
                            językiem
                            Python. Współpracujemy również z innymi organizacjami pozarządowymi i podmiotami
                            zainteresowanymi
                            językiem Python, w tym z Python Software Foundation.
                        </p>
                        <a href="http://pypolska.org">http://pypolska.org</a>
                    </div>
                </b-row>
            </b-container>
        </div>


        <div class="section-colored">
            <b-container>
                <h1>Sponsorzy i partnerzy u których będą się odbywać praktyki</h1>
                <b-row>
                    <div class="col-lg-4 col-md-4">
                        <h3>F-Secure</h3>
                        <br>
                        <b-img fluid class="img-responsive"
                               src="https://www.f-secure.com/documents/assets/images/logo-f-secure-black.svg"></b-img>
                        <br>
                        <p class="text-justify">
                            F-Secure Polska zadeklarowało się, że przyjmie
                            przynajmniej <b> jedną
                            osobę na płatny staż</b> w Poznaniu! To ta sama firma,
                            gdzie już w tym
                            roku trafiły na staż dwie absolwentki zeszłorocznego kursu
                            i skąd mamy wielu mentorów!
                        </p>
                        <p class="text-justify">Oto co piszą o sobie:<br>
                            F-Secure to firma, która wprowadza innowacje w
                            dziedzinie cyberbezpieczeństwa, chroniąc dziesiątki
                            tysięcy firm i miliony użytkowników. Wykorzystuje swoje
                            ogromne doświadczenie, aby chronić przedsiębiorstwa i
                            konsumentów przed wszelkimi zagrożeniami - od
                            zaawansowanych cyberataków i naruszeń bezpieczeństwa
                            danych po powszechne ataki ransomware. Eksperci firmy
                            pracują w wielu laboratoriach bezpieczeństwa na
                            świecie, tworząc spójne podejście określane jako Live
                            Security. Specjaliści ds. zabezpieczeń z F-Secure
                            uczestniczyli w większej liczbie dochodzeń związanych z
                            cyberprzestępczością, niż pracownicy innych firm na
                            rynku.
                            Dla F-Secure cyberbezpieczeństwo to więcej niż produkt,
                            to sposób postrzegania świata. Z produktów tej firmy
                            korzystają dziesiątki milionów konsumentów i ponad 100
                            000 klientów biznesowych na całym świecie.
                            F-Secure to firma założona 1988 roku, zatrudniająca
                            ponad 1000 pracowników w 25 biurach na całym świecie.
                            Jest notowana na giełdzie NASDAQ OMX Helsinki Ltd.
                            <br>
                            <a href="https://www.f-secure.com">F-Secure</a>
                        </p>
                    </div>
                    <div class="col-lg-4 col-md-4">
                        <h3>Egnyte</h3>
                        <br>
                        <b-img fluid class="img-responsive"
                               src="https://www.egnyte.com/assets/6/images/logos/egnyte-lightbg-hirespng.png"></b-img>
                        <br>
                        <p class="text-justify">
                            <a href="https://www.egnyte.com">EGNYTE Poland</a> zadeklarował się, że
                            przyjmie przynajmniej <b>2 uczestniczki na płatny staż</b>
                            po zakończeniu całego programu warszatów!
                        </p>
                        <p class="text-justify"> Oto kilka słów o Nich:<br>
                            Zespół Egnyte Poland w Poznaniu tworzy rozwiązania, dzięki
                            którym można łatwo, bezpiecznie i inteligentnie udostępniać
                            pliki za pomocą chmury lub własnej infrastruktury. W
                            telegraficznym skrócie to elastyczność, przejrzystość i
                            kontrola nad obsługą plików, pozwalająca na współpracę
                            pomiędzy pracownikami danej organizacji, jak również
                            osobami z zewnątrz. Od 2012 roku Egnyte posiada centrum R&D
                            w Poznaniu na ulicy Mostowej. Zespół liczy sobie już ponad
                            100 osób... i ciągle rośnie! Naszą platformę tworzymy przy
                            wykorzystujac takie technologie jak Python, Java czy
                            JavaScript. W poznańskim biurze pracują także Inżynierowie
                            DevOps, Inżynierowie Danych, Inżynierowie Testów, jak i
                            Projektanci Grafiki oraz Interfejsu Użytkownika. Do
                            zobaczenia na warsztatach!
                            <br>
                            <a href="https://www.facebook.com/EgnytePoland">Egnyte na
                                Facebook</a>
                        </p>
                    </div>
                    <div class="col-lg-4 col-md-4">
                        <h3>DLabs</h3>
                        <br>
                        <b-img fluid class="img-responsive"
                               src="https://www.dlabs.pl/static/img/dLabs-logo.svg?cb=1.0.0.4"></b-img>
                        <br>
                        <p class="text-justify">
                            <br>
                            <br>
                            DLabs zadeklarowało, że przyjmie
                            <b> jedną
                                osobę na płatny staż</b> w 100% zdalnie!
                        </p>
                        <p class="text-justify">
                            Oto co piszą o sobie:
                            <br>
                            Na naszym firmowym torcie zdmuchniemy niebawem dwie
                            świeczki. Mimo że działamy dopiero od 2015 roku na swoim
                            koncie mamy wiele sukcesów, zadowolonych klientów,
                            ambitnych
                            projektów oraz gotowych rozwiązań, które implementowane są
                            w
                            małych i dużych firmach przynosząc oczekiwane przez
                            przedsiębiorców rezultaty.
                            <br>
                            Nasz zespół to specjaliści
                            posiadający wiedzę z obszarów: przetwarzania dużych ilości
                            zbiorów danych (big data), analizy danych (data science),
                            uczenia maszynowego (machine learning) oraz sztucznej
                            inteligencji (AI). Naszym celem jest realizacja usług,
                            wdrażanie produktów oraz prowadzenie prac badawczo -
                            rozwojowych związanych z analityką danych.
                            <br>
                            <a href="https://www.dlabs.pl/">DLabs</a>
                        </p>
                    </div>
                </b-row>
            </b-container>
        </div>
    </b-container>
</template>

<script>
    export default {
        name: 'home',
        data() {
            return {
                images_home: [
                    'home_0001',
                    'home_0002',
                    'home_0003',
                    'home_0004',
                    'home_0005',
                    'home_0005'
                ]
            }
        }
    }
</script>

<style scoped>

    img.center {
        display: block;
        margin: 0 auto;
        text-align: center;
    }

    img {
        margin: 1rem;
    }

    div.section-colored {
        background-color: #3b5998;
        color: #efefef
    }

    div.section {
        background-color: #efefef;
    }

    .section {
        padding-top: 25px;
        padding-bottom: 25px;
    }

    .section-colored {
        padding-top: 25px;
        padding-bottom: 25px;
    }
</style>