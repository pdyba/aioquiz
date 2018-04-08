<template>

    <container>
        <navbar position="top" class="indigo navbar-dark" name="PyLove.org" href="/" scrolling>
            <navbar-collapse>
                <navbar-nav right>
                    <help v-if="auth"></help>
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
                            <!--<dropdown-item>Lesson: Create</dropdown-item>-->
                            <dropdown-item href="/organiser/lessons">Lesson: List & Manage</dropdown-item>
                            <!--<dropdown-item>Question: List & Manage</dropdown-item>-->
                            <!--<dropdown-item>Question: Create</dropdown-item>-->
                            <!--<dropdown-item>Quiz: Create</dropdown-item>-->
                            <!--<dropdown-item>Quiz: List & Manage</dropdown-item>-->
                            <!--<dropdown-item>Live Quiz: Create</dropdown-item>-->
                            <!--<dropdown-item>Live Quiz: List & Manage</dropdown-item>-->
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
                            <dropdown-item href="/user/profile">My Profile</dropdown-item>
                            <dropdown-item href="/user/edit">Edit Profile</dropdown-item>
                            <dropdown-item href="/user/seat">My Seat</dropdown-item>
                            <dropdown-item><attendance></attendance></dropdown-item>
                        </dropdown-menu>
                    </dropdown>
                    <language_picker></language_picker>
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
    import attendance from './attendance.vue';
    import language_picker from './language_picker.vue';
    import help from './help.vue';

    export default {
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
            divider,
            attendance,
            language_picker,
            help
        },
        mixins: [drop],
        methods: {
            onLogout() {
                this.$store.dispatch('logout')
            },
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

<style scoped>

</style>

