<template>

    <container>
        <navbar position="top" class="indigo navbar-dark" name="PyLove.org" href="/" scrolling>
            <navbar-collapse>
                <navbar-nav right>

                    <navbar-item class="need-help" v-if="auth && !i_need_help" @click.prevent="help()">HELP
                    </navbar-item>
                    <navbar-item class="need-help-clicked" v-if="auth &&  i_need_help" @click.prevent="help_stop()">
                        THX
                    </navbar-item>
                    <navbar-item href="/about">About</navbar-item>
                    <navbar-item href="/lessons" v-if="auth">Lessons</navbar-item>
                    <navbar-item href="/quiz" v-if="admin">Quiz</navbar-item>
                    <navbar-item href="/live_quiz" v-if="admin">Live Quiz</navbar-item>
                    <navbar-item href="/exam" v-if="admin">Exam</navbar-item>

                    <divider v-if="mentor || org"></divider>
                    <dropdown tag="li" class="nav-item" v-if="mentor">
                        <dropdown-toggle tag="a" navLink color="indigo">Mentor</dropdown-toggle>
                        <dropdown-menu>
                            <dropdown-item>Seats</dropdown-item>
                            <dropdown-item>Lesson</dropdown-item>
                            <dropdown-item>Quiz</dropdown-item>
                            <dropdown-item>Live Quiz</dropdown-item>
                            <dropdown-item>Users List</dropdown-item>
                        </dropdown-menu>
                    </dropdown>

                    <dropdown tag="li" class="nav-item" v-if="org">
                        <dropdown-toggle tag="a" navLink color="indigo">Organiser</dropdown-toggle>
                        <dropdown-menu>
                            <dropdown-item>Lesson: Create</dropdown-item>
                            <dropdown-item>Lesson: List & Manage</dropdown-item>
                            <dropdown-item>Question: List & Manage</dropdown-item>
                            <dropdown-item>Question: Create</dropdown-item>
                            <dropdown-item>Quiz: Create</dropdown-item>
                            <dropdown-item>Quiz: List & Manage</dropdown-item>
                            <dropdown-item>Live Quiz: Create</dropdown-item>
                            <dropdown-item>Live Quiz: List & Manage</dropdown-item>
                        </dropdown-menu>
                    </dropdown>

                    <divider v-if="admin"></divider>
                    <dropdown tag="li" class="nav-item" v-if="admin">
                        <dropdown-toggle tag="a" navLink color="indigo">Admin</dropdown-toggle>
                        <dropdown-menu>
                            <dropdown-item>Attendee: Review</dropdown-item>
                            <dropdown-item href="/admin/email">E-mail</dropdown-item>
                            <dropdown-item href="/admin/users">Users</dropdown-item>
                            <dropdown-item href="/admin/config">Config</dropdown-item>
                        </dropdown-menu>
                    </dropdown>
                </navbar-nav>
                <navbar-nav right>
                    <navbar-item href="/signin" v-if="!auth">Login / Register</navbar-item>

                    <dropdown tag="li" class="nav-item" v-if="auth">
                        <dropdown-toggle tag="a" navLink color="indigo">{{ userName }}</dropdown-toggle>
                        <dropdown-menu>
                            <dropdown-item>My Profile</dropdown-item>
                            <dropdown-item>Edit Profile</dropdown-item>
                            <dropdown-item>My Seat</dropdown-item>
                            <dropdown-item @click.prevent="save_attendence()">Attendance</dropdown-item>
                        </dropdown-menu>
                    </dropdown>
                    <dropdown tag="li" class="nav-item">
                        <dropdown-toggle tag="a" navLink color="indigo">Lang</dropdown-toggle>
                        <dropdown-menu>
                            <dropdown-item src="http://127.0.0.1:5000/images/pl.png" :onclick="setLang('pl')"
                                           imgClass="language-img"></dropdown-item>
                            <dropdown-item src="http://127.0.0.1:5000/images/pl.png" :onclick="setLang('en')"
                                           imgClass="language-img"></dropdown-item>

                        </dropdown-menu>
                    </dropdown>
                    <a @click="onLogout" v-if="auth" class="">
                        <navbar-item>&#10006;</navbar-item>
                    </a>
                </navbar-nav>
            </navbar-collapse>
        </navbar>
    </container>

</template>

<script>
    import Navbar from '../../material_components/Navbar.vue';
    import NavbarItem from '../../material_components/NavbarItem.vue';
    import NavbarNav from '../../material_components/NavbarNav.vue';
    import NavbarCollapse from '../../material_components/NavbarCollapse.vue';
    import Dropdown from '../../material_components/Dropdown.vue';
    import DropdownMenu from '../../material_components/DropdownMenu.vue';
    import dropdownItem from '../../material_components/DropdownItem.vue';
    import DropdownToggle from '../../material_components/DropdownToggle.vue';
    import container from '../../material_components/Container.vue';
    import drop from '../../mixins/drop';
    import divider from './divider.vue';

    import axios from 'axios';

    export default {
        data() {
            return {
                i_need_help: false
            }
        },
        components: {
            Navbar,
            NavbarItem,
            NavbarNav,
            NavbarCollapse,
            DropdownMenu,
            dropdownItem,
            DropdownToggle,
            Dropdown,
            container,
            divider
        },
        mixins: [drop],
        methods: {
            setLang(language) {

            },
            onLogout() {
                this.$store.dispatch('logout')
            },
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

            save_attendence() {
                let self = this;
                self.$swal({
                    title: 'Attendance',
                    input: 'text',
                    text: 'Please provide lesson code',
                    showCancelButton: true,
                    confirmButtonText: 'Submit',
                    showLoaderOnConfirm: true,
                    allowOutsideClick: () => !swal.isLoading(),
                    preConfirm: (value) => {
                        axios.put('/attendance', {'code': value}).then(function (response) {
                            let mtype = "error";
                            if (response.data.success) {
                                mtype = "success";
                            }
                            self.$swal({
                                text: response.data.msg,
                                title: 'Attendance',
                                type: mtype,
                                showConfirmButton: true,
                                timer: 2000
                            });
                        })
                    }
                })
            }
        },
        computed: {
            auth() {
                return this.$store.getters.isAuthenticated
            },
            admin() {
                return this.$store.getters.isAdmin
            },
            org() {
                return this.$store.getters.isOrganiser
            },
            mentor() {
                return this.$store.getters.isMentor
            },
            userName() {
                return this.$store.getters.userName
            }
        }
    };
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
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

