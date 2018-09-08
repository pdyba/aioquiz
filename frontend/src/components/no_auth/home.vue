<template>
    <b-container>
        <div class="section-colored text-center">
            <b-container>
                <b-row>
                    <b-col lg="12">
                        <b-row>
                            <b-col md="4" offset="4" align-self="center">
                                <b-img fluid class="img-responsive img-home-portfolio" alt="PyLove.org"
                                       src="images/pylove_white.png"></b-img>
                            </b-col>
                            <b-col md="4"></b-col>
                        </b-row>
                        <h2>Bezpłatna nauka programowania w Pythonie</h2>
                    </b-col>
                </b-row>
            </b-container>
        </div>


        <div class="section">
            <b-container>
                <b-row>
                    <b-col md="6">
                        <p>PyLove jest orgnizacją non profit, której celem jest nauka i promowanie języka Python
                            niezależnie
                            od płci, wieku, rasy, przekonań czy orientacji. Akceptujemy białych mężczyzn ;) Naszym celem
                            jest pomóc
                            ludzią w dotarci do poziomu stażysty/juniora w programowaniu przy użyciu Pythona aby mogli
                            rozpocząc oni swoją przygodę w IT.
                        </p>
                    </b-col>
                    <b-col md="6">
                        <p>PyLove is a non profit organization that promotes and teaches Python regardless of age, sex,
                            race,
                            believes or orientation. We accept white man ;) Our purpose is to help people get to
                            intern/junior
                            level in Python to start their adventure in IT world.
                        </p>
                    </b-col>
                </b-row>
            </b-container>
        </div>


        <div class="section-colored">
            <b-container>
                <event-desc :event="event" v-for="event in events" filter="active" :key="event.id"></event-desc>
            </b-container>
        </div>


        <div class="section">
            <b-container>
                <b-row>
                    <b-col md="10" align-self="center" offset="1">
                        <h2>Jeśli chcesz wystartować PyLove w swoim mieście napisz do nas!</h2>
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
                    <b-col lg="12" class="text-center">
                        <h2>Zdjęcia z warsztatów prowadzonych przez naszych
                            mentorów.</h2>
                        <hr>
                    </b-col>
                    <b-col lg="4" v-for="img in images_home" :key="img.id">
                        <b-img fluid class="img-responsive img-home-portfolio"
                               :src="'images/' + img + '.jpg'"></b-img>
                    </b-col>

                </b-row>
            </b-container>
        </b-col>


        <div class="section-colored">
            <b-container>
                <b-row>
                    <div class="col-md-6">
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
                            <li><b>Zapisanie się na konkretny kurs/wydarzenie</b></li>
                            <li>Podstawowa znajomość języka angielskiego. <i>(Spotkania
                                będą prowadzone w języku polskim, jednakże dla
                                opanowania składni języka Python znajomość języka
                                angielskiego będzie niewątpliwie pomocna)</i>
                            </li>
                        </ul>
                    </div>
                    <div class="col-md-6">
                        <b-img fluid class="img-responsive" src="images/home_0010.jpg"></b-img>
                    </div>
                </b-row>
            </b-container>
        </div>


        <div class="section">
            <b-container>
                <h1>Partner strategiczny</h1>
                <b-row>
                    <div class="col-md-4">
                        <b-img fluid class="img-responsive"
                               src="http://pypolska.org/img/pypolska_logo.png"></b-img>
                    </div>
                    <div class="col-md-8">
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
                <h2>Sponsorzy i partnerzy u których odbyły się już praktyki lub wsparli nas w inny sposób!</h2>
                <b-row>
                    <sponsor-desc :sponsor="sponsor" v-for="sponsor in sponsors" :key="sponsor.id"></sponsor-desc>
                </b-row>
            </b-container>
        </div>

        <div class="section">
            <b-container>
                <event-desc :event="event" v-for="event in events" filter="inactive" :key="event.id"></event-desc>
            </b-container>
        </div>

    </b-container>
</template>

<script>
    import axios from 'axios'
    import EventDesc from './event_desc.vue'
    import SponsorDesc from './sponsor_desc.vue'

    export default {
        name: 'home',
        data() {
            return {
                events: [],
                sponsors: [],
                images_home: [
                    'home_0001',
                    'home_0002',
                    'home_0003',
                    'home_0004',
                    'home_0005',
                    'home_0005'
                ]
            }
        },
        beforeMount() {
            axios.get('/events').then(resp => {
                this.events = resp.data
            });
            axios.get('/sponsor').then(resp => {
                this.sponsors = resp.data
            });
        },
        components: {
            EventDesc,
            SponsorDesc
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