<template>
    <b-container>
        <div class="section-colored">
            <b-container>
                <b-row>
                    <b-col md="3">
                        <b-img fluid  class="img-responsive center" src="/images/program.jpg"
                               style="max-height: 200px;"> </b-img>
                    </b-col>
                    <b-col md="9">
                        <h2>Program edukacyjny:</h2>
                        <p>Pełen program edukacyjny jest dostępny tutaj:
                            <a href="#/program">Program</a></p>
                        <h2>Educational program:</h2>
                        <p>The complete educational program for the whole year is
                            accessible
                            here: <a href="#/program">Program</a></p>
                    </b-col>
                </b-row>
            </b-container>
        </div>

        <div class="section">
            <b-container>
                <b-row>
                    <div class="col-md-3">
                        <b-img fluid  class="img-responsive center" src="/images/logo.png"
                             style="max-height: 200px;">
                        </b-img>
                    </div>
                    <div class="col-md-9">
                        <h2>AioQuiz</h2>
                        <p>AioQuiz jest autorską aplikacją do przeprowadzania
                            warsztatów rozwijaną przez Piotra Dybę. Wszystkie uwagi
                            można kierować do niego,
                            najlepiej tworząc Issue na Githubie.</p>
                        <p>Aplikacja jest napisana w Pythonie i wykorzystuje Sanic,
                            PostgresSQL oraz AngularJS.</p>
                        <p>AioQuiz is opensource application for recruitment and
                            execution of workshops, developed by Piotr Dyba. If you
                            are
                            having any issues direct them directly to him,
                            preferably
                            using github issues.</p>
                        <p>It is written in Python using asynchronous framework
                            Sanic,
                            PostgresSQL and AngularJS.</p>
                    </div>

                </b-row>
            </b-container>
        </div>


        <div class="section-colored">
            <b-container>
                <b-row>
                    <div class="col-md-6">
                        <b-img fluid  class="img-responsive"
                             src="/images/code-of-conduct.png">
                        </b-img>
                    </div>
                    <div class="col-md-6">

                        <h2>Kodeks Postępowania</h2>
                        <p>Na naszych zajęciach oraz wydarzeniach,
                            dbamy o dobre samopoczucie wszystkich uczestników oraz
                            mentorów, dlatego obowiązuje na nich kilka ważnych dla
                            nas
                            zasad. Opis zachowań, do których zachęcamy, a także
                            tych,
                            których staramy się unikać, dostępny jest pod adresem:
                            <a
                                    href="http://berlincodeofconduct.org/pl/">Berlin
                                Code of Conduct</a> CoC jest rozszerzeniem
                            regulaminu.
                        </p>
                        <h2>Code of Conduct</h2>
                        <p>We have chosen <a
                                href="http://berlincodeofconduct.org/en/">Berlin
                            Code of Conduct</a>, which has been
                            adopted by many other conferences and groups.
                            In case of Code of Conduct violation or other similar
                            problems please contact
                            Zuzanna Kunik by e-mail zuza(at)pylove.org
                            or coc(at)pylove.org
                            CoC is extension of the rules.
                        </p>
                    </div>
                </b-row>
            </b-container>
        </div>
        <div v-if="auth">
            <div class="section">
                <b-container>
                    <b-row>
                        <div class="col-lg-12">
                            <h1>Nasz Zespół</h1>
                        </div>

                        <div class="col-lg-12">
                            <h2>Główni organizatorzy</h2>
                        </div>
                        <short-user-profile :user="user" v-for="user in admins" v-if="user.admin" :key="user.id"></short-user-profile>
                    </b-row>
                </b-container>
            </div>
            <div class="section-colored">
                <b-container>
                    <b-row>
                        <div class="col-lg-12">
                            <h2>Organizatorzy</h2>
                        </div>
                        <short-user-profile :user="user" v-for="user in organisers" v-if="user.organiser && !user.admin" :key="user.id"></short-user-profile>
                    </b-row>
                </b-container>
            </div>
            <div class="section">
                <b-container>
                    <b-row>
                        <div class="col-lg-12">
                            <h2>Mentorzy</h2>
                        </div>
                        <short-user-profile :user="user" v-for="user in mentors" v-if="user.mentor && !user.admin && !user.organiser" :key="user.id"></short-user-profile>
                    </b-row>
                </b-container>
            </div>
        </div>
    </b-container>
</template>

<script>
    import globalAxios from 'axios'
    import ShortUserProfile from './short_user_profile.vue'

    export default {
        name: "about",
        data() {
            return {
                organisers: [],
                mentors: [],
                admins: []
            }
        },
        components: {
            ShortUserProfile
        },
        beforeMount() {
            if (this.$store.getters.isAuthenticated) {
                globalAxios.get('/users/?organiser=True&sort_by=surname').then(resp => {
                    this.organisers = resp.data
                });
                globalAxios.get('/users/?admin=True&sort_by=surname').then(resp => {
                    this.admins = resp.data
                });
                globalAxios.get('/users/?mentor=True').then(resp => {
                    this.mentors = resp.data
                });
            }
        },
        computed: {
            auth() {
                return this.$store.getters.isAuthenticated
            },
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