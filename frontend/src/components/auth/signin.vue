<template>
    <b-container fluid>
        <b-row>
            <b-col sm="3" offset-sm="2" class="signin-form" order="2">
                <h2>Login</h2>
                <b-form @submit.prevent="onSubmit">
                    <b-form-group>
                        <b-form-input
                                type="email"
                                id="email"
                                v-model="email"
                                placeholder="e-mail">
                        </b-form-input>
                    </b-form-group>
                    <b-form-group>
                        <b-form-input
                                type="password"
                                id="password"
                                v-model="password"
                                placeholder="password">
                        </b-form-input>
                    </b-form-group>

                    <b-btn variant="primary" type="submit">Log in!</b-btn>
                </b-form>
            </b-col>
            <b-col sm="3" class="signin-form" order="1">

                <h2>Magic Login</h2>
                <p>Clicking this will send You an e-mail with a magic link that allows password-less login.</p>
                <b-btn color="primary" @click.prevent="magicLink()">Magic Link</b-btn>

            </b-col>
            <b-col sm="3" class="signin-form" order="3">
                <h2>Register</h2>
                <p>Join us in a wonderful learning adventure with Python</p>
                <b-link to="/signup">
                    <b-btn variant="danger" class="right">Register</b-btn>
                </b-link>
            </b-col>

        </b-row>
    </b-container>
</template>

<script>
    import axios from 'axios'

    export default {
        data() {
            return {
                email: '',
                password: ''
            }
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