<template>
    <div>
        <navbar-item class="need-help" v-if="!i_need_help" @click.prevent="help()">
            HELP
        </navbar-item>
        <navbar-item class="need-help-clicked" v-if="i_need_help" @click.prevent="help_stop()">
            THX
        </navbar-item>
    </div>
</template>

<script>
    import NavbarItem from '../../material_components/NavbarItem.vue';

    import axios from 'axios';


    export default {
        name: "help",
        data() {
            return {
                i_need_help: false
            }
        },
        components: {
            NavbarItem,
        },
        methods: {
            help: () => {
                if (!user_seat) {
                    this.$swal({
                        title: "Nope",
                        text: "You need to pick a seat before calling for help",
                        type: "error",
                        timer: 2000,
                        showConfirmButton: false
                    })
                } else {
                    axios.get('/user/i_need_help/').then(
                        function (response) {
                            this.$store.user.seat.i_need_help = true;
                            this.$swal({
                                title: "Yey",
                                text: response.data.msg,
                                type: "success",
                                timer: 2000,
                                showConfirmButton: false
                            })
                        }
                    )
                }
            },
            help_stop: () => {
                axios.delete('/user/i_need_help/').then(
                    function (response) {
                        this.$store.user.seat.i_need_help = false;
                        this.$swal({
                            title: "Yey",
                            text: response.data.msg,
                            type: "success",
                            timer: 2000,
                            showConfirmButton: false
                        })
                    }
                )
            },
        }
    }
</script>

<style scoped>
    .navbar .dropdown-menu a:hover {
        color: inherit !important;
    }

    .need-help {
        background-color: #E51E41;
        color: #efefef !important;
        background-image: linear-gradient(rgb(229, 30, 65) 0px, rgb(229, 30, 65) 100%);
    }

    .need-help:hover {
        background-color: #efefef;
        color: #E51E41 !important;
        background-image: None;
    }

    .need-help-clicked {
        background-color: #8ce554;
        color: #efefef !important;
        background-image: linear-gradient(rgb(140, 229, 84) 0px, rgb(140, 229, 84) 100%);
    }

    .need-help-clicked:hover {
        background-color: #efefef;
        color: #8ce554 !important;
        background-image: None;
    }
</style>