<template>
    <b-container fluid>
        <b-row>
            <b-col sm="8" offset-sm="1">
                <b-form @submit.prevent="onSubmit" class="signup-form">
                    <b-form-group>
                        <label v-if="en || !pl">Language:</label>
                        <label v-if="pl">Język:</label>
                        <b-form-radio-group
                                v-model="user.lang"
                                :options="lang_options"
                                id="lang"
                                @input="$v.user.lang.$touch()">
                        </b-form-radio-group>

                    </b-form-group>
                    <div v-show="$v.user.lang.$dirty">
                        <h4 v-if="en">Account</h4>
                        <h4 v-if="pl">Konto</h4>
                        <div v-if="en">
                            This data is needed for you to be able to login to this application,
                            and also for us to contact you and inform you about the outcome of the recruitment process.
                        </div>
                        <div v-if="pl">
                            Poniższe informacje są potrzebne, żeby się z Tobą skontaktować
                            i poinformować o wynikach rekrutacji oraz żebyś mogła/mogł się zalogować do tej aplikacji.
                        </div>
                        <b-form-group class="input" :class="{invalid: $v.user.email.$invalid}" label="e-mail">
                            <input
                                    type="email"
                                    id="email"
                                    v-model="user.email">
                            <p v-if="!$v.user.email.email">Please provide a valid email address.</p>
                            <p v-if="!$v.user.email.required">This field must not be empty.</p>
                        </b-form-group>
                        <b-form-group class="input" :class="{invalid: $v.user.name.$invalid}">
                            <label v-if="en">First name</label>
                            <label v-if="pl">Imię</label>
                            <input
                                    type="text"
                                    id="name"
                                    v-model="user.name">

                            <p v-if="!$v.user.name.required">This field must not be empty.</p>
                        </b-form-group>
                        <b-form-group class="input" :class="{invalid: $v.user.surname.$invalid}" label="Surname">
                            <label v-if="en">Last name</label>
                            <label v-if="pl">Nazwisko</label>
                            <input
                                    type="text"
                                    id="surname"
                                    v-model="user.surname">
                            <p v-if="!$v.user.surname.required">This field must not be empty.</p>
                        </b-form-group>

                        <b-form-group class="input" :class="{invalid: $v.user.password.$invalid}">
                            <label v-if="en">Password</label>
                            <label v-if="pl"> Hasło</label>
                            <input
                                    type="password"
                                    id="password"
                                    v-model="user.password">
                            <p v-if="!$v.user.password.minLen">Minimal length is 8</p>
                        </b-form-group>
                        <b-form-group class="input" :class="{invalid: $v.user.confirmPassword.$invalid}">
                            <label v-if="en">Confirm Password</label>
                            <label v-if="pl">Potwierdź Hasło</label>
                            <input
                                    type="password"
                                    id="confirm-password"
                                    @blur="$v.user.confirmPassword.$touch()"
                                    v-model="user.confirmPassword">
                        </b-form-group>

                        <p v-if="en">
                            <strong>Attendee</strong><br>
                            Tell us about your motivations behind your decision to start learning programming
                            <br><strong>Mentor:</strong><br>
                            If you are new with us, we would like to know you a little bit better; if you are our old
                            fellow, please provide your short bio :)

                        </p>

                        <p v-if="pl">
                            <strong>Uczestnik</strong> <br>
                            Przede wszystkim chcemy poznać Twoje motywy podjęcia decyzji o rozpoczęciu programowania w
                            Pythonie oraz dowiedzieć się, jakie masz doświadczenie.
                            <br><strong>Mentor:</strong><br>
                            Jeśli dopiero zaczynasz przygodę z Pythonem - chcielibyśmy Cię bliżej poznać, a jeśli już z
                            nami
                            współpracowałeś, zamieść tutaj swoje krótkie bio :)
                        </p>


                        <b-form-group>
                            <b-form-radio-group
                                    v-model="user.mentor"
                                    :options="account_type_options"
                                    id="mentor">
                            </b-form-radio-group>
                        </b-form-group>


                        <user-edit :user="user"></user-edit>


                        <b-form-group class="input inline" :class="{invalid: $v.user.accepted_rules.$invalid}">
                            <b-form-checkbox
                                    type="checkbox"
                                    v-model="user.accepted_rules">
                                <p v-if="en">I have read and accepted Rules, Terms and Code of
                                    conduct.</p>
                                <p v-if="pl">Przeczytałem i akceptuję <a href="#/rules">Regulamin</a>
                                    oraz Code of conduct.</p>
                            </b-form-checkbox>
                        </b-form-group>


                        <b-form-group class="input inline" :class="{invalid: $v.user.gdpr.$invalid}">
                            <b-form-checkbox
                                    type="checkbox"
                                    v-model="user.gdpr">
                                <p v-if="en">I have read and accepted <a href="#/privacy_policy">Privacy Policy</a></p>
                                <p v-if="pl">Przeczytałem i akceptuję <a href="#/privacy_policy">Poliykę Prywatności</a>
                                </p>
                            </b-form-checkbox>
                        </b-form-group>

                        <b-form-group class="input inline" :class="{invalid: $v.user.notebook.$invalid}">
                            <b-form-checkbox
                                    type="checkbox"
                                    v-model="user.notebook">
                                <p v-if="en">I know I have to bring my own Notebook.</p>
                                <p v-if="pl">Wiem że muszę przynieść swojego laptopa.</p>
                            </b-form-checkbox>
                        </b-form-group>


                        <b-form-group class="input inline" :class="{invalid: $v.user.python.$invalid}">
                            <b-form-checkbox
                                    type="checkbox"
                                    v-model="user.python">
                                <p v-if="en">Did you already install Python using following link:</p>
                                <p v-if="pl">Czy zainstalowałeś już Pythona używajac tego linku:</p>
                                <a href="https://www.youtube.com/watch?v=0d6znPZb3PQ&t=3s">https://www.youtube.com/watch?v=0d6znPZb3PQ&t=3s</a>
                            </b-form-checkbox>
                        </b-form-group>

                        <b-form-group class="input inline" :class="{invalid: $v.user.attend_weekly.$invalid}">
                            <b-form-checkbox
                                    type="checkbox"
                                    v-model="user.attend_weekly">

                                <p v-if="en">Have you already installed PyCharm?</p>
                                <p v-if="pl">Czy zainstalowałaś/eś już PyCharma?</p>
                            </b-form-checkbox>
                        </b-form-group>

                        <b-form-group class="input inline" :class="{invalid: $v.user.bring_power_cord.$invalid}">
                            <b-form-checkbox
                                    type="checkbox"
                                    v-model="user.bring_power_cord">
                                <p v-if="en">I know that each time my laptop needs to be fully powered
                                    up.</p>
                                <p v-if="pl">Wiem, że za każdym razem muszę przynosić naładowanego
                                    laptopa.</p>
                            </b-form-checkbox>
                        </b-form-group>

                        <b-btn type="submit" :disabled="$v.user.$invalid">Submit</b-btn>
                        <p v-if="en">*At this point we are not sure if there will be any t-shirts for
                            attendees.</p>
                        <p v-if="pl">*Na chwilę obecną nie możemy obiecać, że będą koszulki dla
                            uczestników.</p>
                    </div>
                </b-form>
            </b-col>
        </b-row>
    </b-container>

</template>

<script>
    import {required, email, numeric, minValue, minLength, sameAs, requiredUnless} from 'vuelidate/lib/validators'
    import UserEdit from "../user/_profile_edit.vue";

    function isTrue(value) {
        return value === true
    }

    export default {
        components: {
            UserEdit
        },
        data() {
            return {
                user: {
                    email: '',
                    name: '',
                    surname: '',
                    age: null,
                    password: '',
                    confirmPassword: '',
                    city: 'Poznań',
                    lang: '',
                    university: '',
                    operating_system: '',
                    motivation: '',
                    description: '',
                    app_idea: '',
                    accepted_rules: null,
                    notebook: null,
                    python: null,
                    attend_weekly: null,
                    bring_power_cord: null
                },
                lang_options: ['pl', 'en']
            }
        },
        validations: {
            user: {
                lang: {
                    required: true
                },
                email: {
                    required,
                    email
                },
                name: {
                    required: true
                },
                surname: {
                    required: true
                },
                password: {
                    required,
                    minLen: minLength(8)
                },
                confirmPassword: {
                    sameAs: sameAs('password')
                },
                accepted_rules: {
                    isTrue,
                    required: true
                },
                notebook: {
                    isTrue,
                    required: true
                },
                python: {
                    isTrue,
                    required: true
                },
                attend_weekly: {
                    isTrue,
                    required: true
                },
                bring_power_cord: {
                    isTrue,
                    required: true
                },
                gdpr: {
                    isTrue,
                    required: true
                },
            }
        },
        computed: {
            pl() {
                return this.user.lang === 'pl'
            },
            en() {
                return this.user.lang === 'en'
            },
            mentor() {
                return this.user.mentor
            },
            account_type_options() {
                if (this.pl) {
                    return [
                        {text: "Mentor", value: true},
                        {text: "Uczestnik", value: false},
                    ]
                }
                return [
                    {text: "Mentor", value: true},
                    {text: "Attendee", value: false},
                ]
            },
        },
        methods: {
            onSubmit() {
                this.$store.dispatch('signup', this.user)
            }
        }
    }
</script>

<style scoped>
    .signup-form {
        /*width: 400px;*/
        margin: 30px auto;
        border: 2px solid #eee;
        padding: 20px;
        box-shadow: 0 2px 3px #ccc;
    }

    .input {
        margin: 10px auto;
    }

    .input label {
        display: block;
        color: #4e4e4e;
        margin-bottom: 6px;
    }

    .input.inline label {
        display: inline;
    }

    .input input {
        font: inherit;
        width: 100%;
        padding: 6px 12px;
        box-sizing: border-box;
        border: 1px solid #ccc;
    }

    .input.inline input {
        width: auto;
    }

    .input input:focus {
        outline: none;
        border: 1px solid #521751;
        background-color: #eee;
    }

    .input.invalid label {
        color: red;
    }

    .input.invalid input {
        border: 1px solid red;
        background-color: #ffc9aa;
    }

    .input.inline.invalid input {
        border: 1px solid red;
        background-color: #ffc9aa;
    }

    .input select {
        border: 1px solid #ccc;
        font: inherit;
    }

    .submit button {
        border: 1px solid #521751;
        color: #521751;
        padding: 10px 20px;
        font: inherit;
        cursor: pointer;
    }

    .submit button:hover,
    .submit button:active {
        background-color: #521751;
        color: white;
    }

    .submit button[disabled],
    .submit button[disabled]:hover,
    .submit button[disabled]:active {
        border: 1px solid #ccc;
        background-color: transparent;
        color: #ccc;
        cursor: not-allowed;
    }
</style>