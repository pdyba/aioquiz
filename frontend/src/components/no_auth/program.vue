<template>
    <b-container>
        <b-row>
            <div class="col-lg-12">
                <h1 class="page-header">Program PyLove</h1>
            </div>
        </b-row>
        <b-row>
            <b-col>
                <h2>Materiał przerobiony w czasie warsztatu weekendowego:</h2>
                <tbl striped bordered hover responsive-sm sm>
                    <tbl-head>
                        <th>LP</th>
                        <th>Lekcja</th>
                    </tbl-head>
                    <tbl-body>
                        <tr v-for="(entry, index) in tab_1" :key="entry.id">
                            <td>{{ index }}</td>
                            <td>{{ entry }}</td>
                        </tr>
                    </tbl-body>
                </tbl>
                <h2>Cotygodniowy warsztat dwugodzinny zaczyna się od lekcji, na
                    której
                    skończył się warsztat weekendowy:</h2>
                <h3>I semestr 14 spotkań od 17.10 do 12.12, od 09.01 do 13.02</h3>
                <tbl striped bordered hover responsive-sm sm>
                    <tbl-head>
                        <th>LP</th>
                        <th>Lekcja</th>
                    </tbl-head>
                    <tbl-body>
                        <tr v-for="(entry, index) in tab_2" :key="entry.id">
                            <td>{{ index }}</td>
                            <td>{{ entry.date }}</td>
                            <td>{{ entry.subject }}</td>
                            <td>{{ entry.author }}</td>
                        </tr>
                    </tbl-body>
                </tbl>
                <h3>II semestr 13 spotkań od 06.03 do 19.06</h3>
                <tbl striped bordered hover responsive-sm sm>
                    <tbl-head>
                        <th>LP</th>
                        <th>Lekcja</th>
                    </tbl-head>
                    <tbl-body>
                        <tr v-for="(entry, index) in tab_3" :key="entry.id">
                            <td>{{ index }}</td>
                            <td>{{ entry.date }}</td>
                            <td>{{ entry.subject }}</td>
                            <td>{{ entry.author }}</td>
                        </tr>
                    </tbl-body>
                </tbl>
            </b-col>
            <!--<div class="col-lg-6">-->
            <!--<h2>Weekend workshops - kickoff:</h2>-->
            <!--<ol>-->
            <!--PyLove - a hands-on manual-->
            <!--What is programming, what is Python and what for can I use it-->
            <!--A friendly introduction to algorithms-->
            <!--First steps with the Python interpreter and PyCharm IDE-->
            <!--Python as a calculator-->
            <!--Variable tdke a woman-->
            <!--How to talk to snakes - data types: character, numerical and Boolean-->
            <!--Fun with strings-->
            <!--Built-in functions-->
            <!--Logical logic-->
            <!--Conditional conditions-->
            <!--Shopping tdsts-->
            <!--Dictionaries from A to Z-->
            <!--Loop for everyone-->
            <!--Loop while I still can-->
            <!--our_function()-->
            <!--Catching unique exceptions and trolls-->
            <!--Importing randomness and other modules-->
            <!--Recap-->
            <!--</ol>-->
            <!--<h3>As far as possible:</h3>-->
            <!--<ol>-->
            <!--Everything is an object - programming objectively-->
            <!--Success and their tree fathers - tolerant inheritance-->
            <!--Hermetizing children - methods types-->
            <!--</ol>-->
            <!--<h2>The weekly two-hour workshop will take it from where the weekend workshop has ended:</h2>-->
            <!--<h3>1st term 14 meetings from 17.10 to 12.12, from 09.01 to-->
            <!--13.02</h3>-->
            <!--<ol>-->
            <!--Revision-->
            <!--Working with files, JSON format-->
            <!--External tdbraries and working with REST API-->
            <!--Git-->
            <!--Everything is an object - introduction to OOP-->
            <!--Everything is an object - cont.-->
            <!--Web apptdcations in Python, intro to Flask-->
            <!--HTML, creating page templates and forms-->
            <!--Recap. Jinja 2-->
            <!--SQL databases-->
            <!--NO-SQL databases-->
            <!--Creating a REST API-->
            <!--Unit Testing and TDD-->
            <!--Scrum, Agile and teamwork project selection-->
            <!--</ol>-->
            <!--<h3>2nd term 13 meetings from 06.03 to 19.06</h3>-->
            <!--<ol>-->
            <!--Overview of team projects-->
            <!--PEP8, Pytdnt, and development methodologies-->
            <!--Storing and creating configuration files-->
            <!--SSH, AWS, and virtual servers-->
            <!--Deployment of web apptdcations-->
            <!--Regular expression-->
            <!--Advanced constructs in Python-->
            <!--Advanced features in Python I-->
            <!--Advanced features in Python II-->
            <!--Team Project I-->
            <!--Team Project II-->
            <!--Year Test-->
            <!--Overview of test results and team projects-->
            <!--</ol>-->
            <!--</div>-->
        </b-row>
    </b-container>
</template>
<script>
    import Tbl from '../common_components/Table.vue';
    import TblHead from '../common_components/TableHead.vue';
    import TblBody from '../common_components/TableBody.vue';

    export default {
        name: "program",
        components: {
            Tbl,
            TblHead,
            TblBody
        },
        data() {
            return {
                tab_1:
                    [
                        'Instrukcja obsługi warsztatu',
                        'Co to jest programowanie, Python, i do czego można go wykorzystać',
                        'Przyjazne wprowadzenie do algorytmiki',
                        'Pierwsze kroki z interpreterem Pythona i IDE Pycharma',
                        'Python jako Kalkulator',
                        'Zmienna niczym kobieta',
                        'Jak wytłumaczyć wężowi o czym mówimy czytd - typy danych:',
                        'znakowy, tdczbowy i boolowski',
                        'Zabawy ze stringami',
                        'Funkcje wbudowane',
                        'Logiczna logika',
                        'Warunkowe warunki',
                        'tdsty zakupów',
                        'Słowniki od A do Z',
                        'Pętla dla każdego (for) zrobię coś fajnego',
                        'Pętla dopóki mogę (while) będę robił coś fajnego',
                        'nasza_funkcja()',
                        'Łapanie wyjątkowych błędów i troltd',
                        'Import losowości i innych modułów',
                        'Powtórka całości',
                        'Wszystko jest obiektem - wstęp do programowania obiektowego',
                        'Sukces i jego trzech ojców – tolerancyjne dziedziczenie',
                        'Hermetyzacja dzieci – rodzaje metod'
                    ],
                tab_2: [
                    {'date': '2017.10.17', 'subject': 'Organizacja i powtórka ', 'author': ' Piotr Dyba'},
                    {'date': '2017.10.24', 'subject': 'Praca z ptdkami, format JSON ', 'author': ' Piotr Dyba'},
                    {
                        'date': '2017.11.07',
                        'subject': 'Bibtdoteki zewnętrzne, praca z API RESTowym ',
                        'author': ' Piotr Dyba'
                    },
                    {'date': '2017.11.14', 'subject': 'Git - system kontrotd wersji ', 'author': ' Magdalena Nowak'},
                    {
                        'date': '2017.11.21',
                        'subject': 'Wszystko jest obiektem wstęp do programowania obiektowego ', 'author': ' Piotr Dyba'
                    },
                    {'date': '2017.11.28', 'subject': 'Wszytko jest obiektem - cd. ', 'author': ' Piotr Dyba'},
                    {
                        'date': '2017.12.05',
                        'subject': 'Aptdkacja webowa w Pythonie, wstęp do Flaska ', 'author': ' Grzegorz Prokopczyk'
                    },
                    {
                        'date': '2017.12.12',
                        'subject': 'HTML oraz tworzenie wzorników stron i formularzy ', 'author': ' Grzegorz Prokopczyk'
                    },
                    {
                        'date': '2018.01.09',
                        'subject': 'Powtórka: pierwsza pełna aptdkacja webowa, Jinja2 ',
                        'author': ' Grzegorz Prokopczyk'
                    },
                    {
                        'date': '2018.01.16',
                        'subject': 'Powtórka całości ',
                        'author': ' Krzysztof Marciniak, Piotr Dyba'
                    },
                    {
                        'date': '2018.01.23',
                        'subject': 'PEP8, Pytdnt i metodologie programistyczne ',
                        'author': ' Piotr Dyba'
                    },
                    {
                        'date': '2018.01.30',
                        'subject': 'SQLAlchemy oraz wybór projektów zespołowych ',
                        'author': ' Piotr Dyba'
                    },
                    {'date': '2018.02.06', 'subject': 'BRAK ZAJĘĆ'},
                    {'date': '2018.02.13', 'subject': 'Bazy danych SQL ', 'author': ' Grzegorz Prokopczyk'},
                    {'date': '2018.02.20', 'subject': 'BRAK ZAJĘĆ'},
                    {
                        'date': '2018.02.27',
                        'subject': 'Tworzenie API RESTowego oraz Przechowywanie i tworzenie ptdków konfiguracyjnych ',
                        'author': ' Grzegorz Prokopczyk oraz Piotr Dyba'
                    }
                ],
                tab_3: [
                    {
                        'date': '2018.03.06',
                        'subject': 'Scrum, Agile i omówienie projektów zespołowych ',
                        'author': ' Piotr Dyba'
                    },
                    {'date': '2018.03.13', 'subject': 'Systemy kolejkowe i bazy danych NOSQL'},
                    {
                        'date': '2018.03.20',
                        'subject': 'Testy Jednostkowe i TDD ',
                        'author': ' Aleksandra Kornecka, Grzegorz Prokopczyk'
                    },
                    {'date': '2018.03.27', 'subject': 'Zaawansowane konstrukty w Pythonie ', 'author': ' Piotr Dyba'},
                    {'date': '2018.04.03', 'subject': 'BRAK ZAJĘĆ'},
                    {'date': '2018.04.10', 'subject': 'Wyrażenie regularne ', 'author': ' Zuzanna Kunik'},
                    {'date': '2018.04.17', 'subject': 'Linux, Bash i SSH wprowadzenie ', 'author': ' Filip Rachwalak'},
                    {
                        'date': '2018.04.24',
                        'subject': 'Deployment aptdkacji webowej ',
                        'author': ' Grzegorz Prokopczyk'
                    },
                    {'date': '2018.05.01', 'subject': 'BRAK ZAJĘĆ'},
                    {'date': '2018.05.08', 'subject': 'VirtualEnv', 'author': ' Piotr Dyba'},
                    {'date': '2018.05.15', 'subject': 'Zaawansowane funkcje w Pythonie', 'author': ' Piotr Dyba'},
                    {'date': '2018.05.22', 'subject': 'Webapp security 101', 'author': ' Krzysztof Marciniak'},
                    {'date': '2018.05.29', 'subject': 'BRAK ZAJĘĆ'},
                    {'date': '2018.06.05', 'subject': 'Docker', 'author': ' Marcin Tamioła'},
                    {
                        'date': '2018.06.12',
                        'subject': 'Test sprawdzający, przygotowanie pod staż ',
                        'author': ' Piotr Dyba'
                    },
                    {
                        'date': '2018.06.19',
                        'subject': 'Prezentacja i omówienie projektów, wyniki testów, rozdanie dyplomów ',
                        'author': ' Piotr Dyba'
                    }
                ]
            }
        }
    }
</script>
<style scoped>
</style>