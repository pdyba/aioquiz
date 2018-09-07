<template>
    <b-row v-if="show">
        <b-col sm="2">
            <h3>{{ event.title }}</h3>
            <h4>{{ event.city }}</h4>
            <h5 v-if="event.event_active"><b v-if="event.start_date < new Date()">Startujemy już</b><b v-else>Wystartowaliśmy </b>
                {{
                event.start_date | moment("calendar") }} !</h5>
            <h5 v-else> Warsztat zakończył się {{
                event.end_date | moment("calendar") }} !</h5>
        </b-col>
        <b-col sm="3">
            <b-img fluid class="img-responsive" :src="event.address_picture">
            </b-img>
        </b-col>
        <b-col sm="7">
            <p>{{ event.description }}</p>
            <div v-if="event.reg_active">
                <p>Zapisy trwają od {{ event.registration_start_date | moment("calendar") }} do {{
                    event.registration_end_date | moment("calendar") }}</p>
                <b-btn @click="sign_me" v-if="!auth || !event.user_data" variant="success">Zapisz mnie</b-btn>
                <h4 v-else>Już się zapisałeś/zapisałaś</h4>
                <b-btn @click="unsign_me" v-if="auth && event.user_data" variant="warning">Rezygnuję</b-btn>
                <b-btn :href="'event/' + event.id">Więcej szczegółów</b-btn>
            </div>
            <p v-else>
                Zapisy już się zakończyły
                <br>
                <b-btn :href="'event/' + event.id">Więcej szczegółów</b-btn>
            </p>

        </b-col>
    </b-row>
</template>

<script>
    import axios from 'axios'

    export default {
        name: "event-desc",
        props: {
            event: {
                type: Object,
                required: true
            },
            filter: {
                type: String,
                required: true
            }
        },
        computed: {
            auth() {
                return this.$store.getters.isAuthenticated
            },
            show() {
                if (this.filter === 'all') {
                    return true
                } else if (this.filter === 'active') {
                    return this.event.event_active === true
                } else if (this.filter === 'inactive')
                    return this.event.event_active === false
                else {
                    return false
                }
            }
        },
        methods: {
            sign_me() {
                if (this.auth) {
                    let self = this;
                    self.$swal({
                        title: "Sign Up",
                        type: "info",
                        text: "You are about to sign for workshop in " + self.event.city,
                        showCancelButton: true,
                        confirmButtonText: "Yes",
                        cancelButtonText: "No",
                        showLoaderOnConfirm: true,
                        allowOutsideClick: true,
                    }).then((value) => {
                        if (value.value === true) {
                            axios.post('/event', {
                                users: self.$store.getters.user.id,
                                event: self.event.id
                            }).then((response) => {
                                self.$swal({
                                    text: response.data.msg,
                                    title: 'Unsigned',
                                    type: "info",
                                    showConfirmButton: true,
                                    timer: 3000
                                })
                            })
                        } else {
                            self.$swal({
                                text: "See You there",
                                title: 'Cancelation',
                                type: 'success',
                                showConfirmButton: true,
                                timer: 3000
                            });
                        }
                    })
                }
                else {
                    this.$swal({
                        text: "You need to register an account first",
                        type: 'warning',
                        showConfirmButton: true,
                        timer: 3000
                    }).then((value) => {
                        this.$router.push({name: 'signin'})
                    });
                }
            },
            unsign_me() {
                if (this.auth) {
                    let self = this;
                    self.$swal({
                        title: "Sign Up",
                        type: "warning",
                        text: "You are about to unsign for workshop in " + self.event.city,
                        showCancelButton: true,
                        confirmButtonText: "Yes",
                        cancelButtonText: "No",
                        showLoaderOnConfirm: true,
                        allowOutsideClick: true,
                    }).then((value) => {
                        if (value.value === true) {
                            axios.delete('/event/' + self.event.id).then((response) => {
                                self.$swal({
                                    text: response.data.msg,
                                    title: 'Signed up',
                                    type: "info",
                                    showConfirmButton: true,
                                    timer: 3000
                                })
                            })
                        } else {
                            self.$swal({
                                text: "OK maybe later?",
                                title: 'Cancleation',
                                type: 'success',
                                showConfirmButton: true,
                                timer: 3000
                            });
                        }
                    })
                }
                else {
                    this.$swal({
                        text: "You need to register an account first",
                        type: 'warning',
                        showConfirmButton: true,
                        timer: 3000
                    }).then((value) => {
                        this.$router.push({name: 'signin'})
                    });
                }
            }
        }
    }
</script>

<style scoped>

</style>