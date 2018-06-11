<template>
    <div>
        <b-form-group>
            <label v-if="en || !pl">Language:</label>
            <label v-if="pl">Język:</label>
            <b-form-radio-group
                    v-model="user.lang"
                    :options="lang_options"
                    id="lang">
            </b-form-radio-group>
        </b-form-group>

        <h4 v-if="en">Stats</h4>
        <h4 v-if="pl">Statystyka</h4>
        <p v-if="en">
            Below data is just for statistics, that easeas our cooperation
            with partners and sponsors.</p>
        <p v-if="pl"> Poniższe dane są nam potrzebne do statystyk, które potem
            ułatwiają nam współpracę z partnerami i sponsorami.</p>

        <b-form-group class="input" :class="{invalid: $v.user.age.$invalid}">
            <label v-if="en">Age</label>
            <label v-if="pl">Wiek</label>
            <input
                    type="number"
                    id="age"
                    v-model.number="user.age">
            <p v-if="!$v.user.age.minVal">Age of user must be at least 6 years old.</p>
        </b-form-group>
        <b-form-group class="input">
            <label for="city" v-if="en">City</label>
            <label for="city" v-if="pl">Miejscowość</label>
            <input
                    type="text"
                    id="city"
                    v-model="user.city">
        </b-form-group>

        <b-form-group :class="{invalid: $v.user.education.$invalid}">
            <label v-if="en">Education</label>
            <label v-if="pl">Edukacja</label>
            <b-form-select
                    :options="education_options"
                    v-model="user.education">
            </b-form-select>
        </b-form-group>

        <b-form-group :class="{invalid: $v.user.university.$invalid}">
            <label v-if="en">University - ongoing or graduate</label>
            <label v-if="pl">Szkoła wyższa - aktualna lub ukończona</label>
            <b-form-select
                    :options="university_options"
                    v-model="user.university">
            </b-form-select>
        </b-form-group>

        <b-form-group :class="{invalid: $v.user.t_shirt.$invalid}">
            <label>T-Shirt*</label>
            <b-form-select
                    :options="tshirt_options"
                    v-model="user.t_shirt">
            </b-form-select>
        </b-form-group>

        <b-form-group :class="{invalid: $v.user.operating_system.$invalid}">
            <label v-if="en">Operating System</label>
            <label v-if="pl">System Operacyjny</label>
            <b-form-select
                    :options="operating_system_options"
                    v-model="user.operating_system">
            </b-form-select>
        </b-form-group>

        <h4 v-if="en">About You</h4>
        <h4 for="city" v-if="pl">O Tobie</h4>

        <b-form-group :class="{invalid: $v.user.description.$invalid}">
            <label v-if="en">Write something about yourself</label>
            <label v-if="pl">Napisz coś o sobie</label>
            <b-form-textarea
                    v-model="user.description"
                    placeholder="Enter something"
                    :rows="4"
                    :max-rows="9">
            </b-form-textarea>
        </b-form-group>

        <b-form-group :class="{invalid: $v.user.motivation.$invalid}">
            <label v-if="en">Motivation - Why do you want to
                participate in the workshop?</label>
            <label v-if="pl">Motywacja - Dlaczego chcesz wziąć udział w
                warsztatch?</label>
            <b-form-textarea
                    v-model="user.motivation"
                    placeholder="Enter something"
                    :rows="4"
                    :max-rows="9">
            </b-form-textarea>
        </b-form-group>

        <b-form-group :class="{invalid: $v.user.app_idea.$invalid}">
            <label v-if="en">hat are you planning to do with the
                knowledge you gain during this workshop? Do you have an app idea?</label>
            <label v-if="pl">Do czego chciałabyś/chciałbyś wykorzystać
                wiedzę z warsztatów? Czy masz pomysł na własną aplikację?</label>
            <b-form-textarea
                    v-model="user.app_idea"
                    placeholder="Enter something"
                    :rows="4"
                    :max-rows="9">
            </b-form-textarea>
        </b-form-group>

        <b-form-group :class="{invalid: $v.user.experience.$invalid}">
            <label v-if="en">Experience</label>
            <label v-if="pl">Doświadczenie</label>
            <b-form-select
                    :options="expirience_options"
                    text-field="subject"
                    name="experience"
                    v-model="user.experience">
            </b-form-select>
        </b-form-group>
    </div>

</template>

<script>
    import {required,  minValue, minLength} from 'vuelidate/lib/validators'

    export default {
        name: "userEditBase",
        data() {
            return {
                university_options: ['None-Brak', 'UAM', 'PP', 'UP', 'UE', 'UM', 'CDV', 'WSB', 'OTHER'],
                tshirt_options: [
                    'Female-XXS', 'Female-XS', 'Female-S', 'Female-M', 'Female-L', 'Female-XL', 'Female-XXL',
                    'Female-XXXL', 'Male-XS', 'Male-S', 'Male-M', 'Male-L', 'Male-XL', 'Male-XXL', 'Male-XXXL'
                ],
                operating_system_options: ['MacOS', 'Linux', 'Windows'],
                lang_options: ['pl', 'en']
            }
        },
        props: {
            user: {
                type: Object,
                required: true
            }
        },
        validations: {
            user: {
                age: {
                    minVal: minValue(6)
                },
                city: {},
                education: {},
                university: {},
                t_shirt: {},
                operating_system: {},
                description: {},
                motivation: {},
                app_idea: {},
                experience: {},
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
            expirience_options() {
                if (this.pl) {
                    return [
                        'Nie posiadam wcale',
                        'Coś tam robiłam/em, ale nic nie pamiętam',
                        'Znam podstawy',
                        'Umiem programować',
                        'Znam dobrze inny język programowania',
                        'Jestem doświadczonym programistą'
                    ]
                }
                return [
                    'I have none',
                    'I had some but I do not remember anything',
                    'I know the basics',
                    'I can program',
                    'I know another programming language well',
                    'I am an experienced programmer'
                ]
            },
            education_options() {
                if (this.pl) {
                    return [
                        'Podstawowe', 'Gimnazjalne', 'Zawodowe', 'Techniczne', 'Średnie', 'Licencjat', 'Inżynier', 'Magister', 'Doktor'
                    ]
                }
                return [
                    'Elementary', 'Gymnasium', 'Vocational', 'Technician', 'High School', 'BA degree', 'Engineer', 'MA degree', 'PhD'
                ]
            }
        }
    }
</script>

<style scoped>

</style>