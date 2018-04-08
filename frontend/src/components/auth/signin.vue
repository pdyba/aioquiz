<template>
    <container fluid>
        <row>
            <column md="5" offset-md="2" class="signin-form">
                <form @submit.prevent="onSubmit">
                    <div class="input">
                        <h3>Log in:</h3>
                        <label for="email">Mail</label>
                        <input
                                type="email"
                                id="email"
                                v-model="email">
                    </div>
                    <div class="input">
                        <label for="password">Password</label>
                        <input
                                type="password"
                                id="password"
                                v-model="password">
                    </div>

                    <btn color="primary" type="submit">Submit</btn>

                </form>
            </column>
            <column md="3" class="signin-form">
                <div class=".input">
                    <h2>Magic Login</h2>
                    <b-btn color="primary" @click.prevent="magicLink()">Magic Link</b-btn>
                    <p>Clicking this will send You an e-mail with a magic link that allows password-less login.</p>
                </div>
            </column>

        </row>
    </container>
</template>

<script>
    import Btn from '../../material_components/Button.vue';
    import Container from '../../material_components/Container.vue';
    import Row from '../../material_components/Row.vue';
    import Column from '../../material_components/Col.vue';

    import axios from 'axios'

    export default {
        data() {
            return {
                email: '',
                password: ''
            }
        },
        components: {
            Btn,
            Container,
            Row,
            Column
        },
        methods: {
            onSubmit() {
                const formData = {
                    email: this.email,
                    password: this.password,
                };
                this.$store.dispatch('login', {email: formData.email, password: formData.password})
            },
            magicLink() {
                let self = this;
                this.$swal({
                    title: "Magic Link",
                    text: "Please provide valid email",
                    input: "email",
                    showConfirmButton: true,
                    showLoaderOnConfirm: true,
                    allowOutsideClick: () => !swal.isLoading(),
                    closeOnConfirm: false,
                    preConfirm: (email) => {
                        return axios.post('/auth/magic_link', {email: email})
                    }
                }).then((response) => {
                    self.$swal({text: response.value.data.msg});
                })
            }

        }
    }
</script>

<style scoped>
    .signin-form {
        width: 100%;
        margin: 30px auto;
        border: 1px solid #eee;
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

    .input input {
        font: inherit;
        width: 100%;
        padding: 6px 12px;
        box-sizing: border-box;
        border: 1px solid #ccc;
    }

    .input input:focus {
        outline: none;
        border: 1px solid #521751;
        background-color: #eee;
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