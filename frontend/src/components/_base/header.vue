<template>
    <b-container>
        <navbar position="top" class="indigo navbar-dark" name="PyLove.org" href="/" scrolling>
            <navbar-collapse>
                <navbar-nav right>
                    <!--<help v-if="auth"></help>-->
                    <navbar-item href="/about">About</navbar-item>
                    <navbar-item href="/lessons" v-if="auth">Lessons</navbar-item>
                    <!--<navbar-item href="/homework" v-if="auth">HomeWork</navbar-item>-->
                    <navbar-item href="/quiz" v-if="auth">Quiz</navbar-item>
                    <navbar-item href="/live_quiz" v-if="auth">Live Quiz</navbar-item>
                    <navbar-item href="/exam" v-if="auth">Exam</navbar-item>

                    <divider v-if="mentor || org"></divider>
                    <dropdown tag="li" class="nav-item" v-if="mentor">
                        <dropdown-toggle tag="a" navLink color="indigo">Mentor</dropdown-toggle>
                        <dropdown-menu>
                            <!--<dropdown-item href="/mentor/questions">Questions</dropdown-item>-->
                            <dropdown-item href="/mentor/lesson">Lesson: status</dropdown-item>
                            <!--<dropdown-item href="/mentor/homework">Homework: grade</dropdown-item>-->
                            <dropdown-item href="/mentor/quiz">Quiz: grade</dropdown-item>
                            <dropdown-item href="/mentor/live_quiz">Live Quiz: overview</dropdown-item>
                            <dropdown-item href="/mentor/exam">Exam: grade</dropdown-item>
                            <dropdown-item>Users: overview</dropdown-item>
                        </dropdown-menu>
                    </dropdown>

                    <dropdown tag="li" class="nav-item" v-if="org">
                        <dropdown-toggle tag="a" navLink color="indigo">Organiser</dropdown-toggle>
                        <dropdown-menu>
                            <!--<dropdown-item>Lesson: Create</dropdown-item>-->
                            <dropdown-item href="/organiser/attendee_review">Attendee: Review</dropdown-item>
                            <dropdown-item href="/organiser/lessons">Lesson: Manage</dropdown-item>
                            <dropdown-item>Question: Manage</dropdown-item>
                            <dropdown-item>Question: Create</dropdown-item>
                            <dropdown-item href="/organiser/quiz-create">Quiz: Create</dropdown-item>
                            <dropdown-item href="/organiser/quiz-manage">Quiz: Manage</dropdown-item>
                            <dropdown-item href="/organiser/live-quiz-create">Live Quiz: Create</dropdown-item>
                            <dropdown-item href="/organiser/live-quiz-manage">Live Quiz: Manage</dropdown-item>
                            <dropdown-item href="/organiser/exam-create">Exam: Create</dropdown-item>
                            <dropdown-item href="/organiser/exam-manage">Exam: Manage</dropdown-item>
                        </dropdown-menu>
                    </dropdown>

                    <divider v-if="admin"></divider>
                    <dropdown tag="li" class="nav-item" v-if="admin">
                        <dropdown-toggle tag="a" navLink color="indigo">Admin</dropdown-toggle>
                        <dropdown-menu>
                            <dropdown-item href="/admin/email">E-mail</dropdown-item>
                            <dropdown-item href="/admin/users">Users</dropdown-item>
                            <dropdown-item href="/admin/config">Config</dropdown-item>
                            <!--<dropdown-item href="/admin/events">Events</dropdown-item>-->
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
                            <!--<dropdown-item href="/user/seat">My Seat</dropdown-item>-->
                            <dropdown-item><attendance></attendance></dropdown-item>
                        </dropdown-menu>
                    </dropdown>
                    <!--<language_picker v-if="admin"></language_picker>-->
                    <a @click="onLogout" v-if="auth" class="">
                        <navbar-item>&#10006;</navbar-item>
                    </a>
                </navbar-nav>
            </navbar-collapse>
        </navbar>
    </b-container>
</template>

<script>
    import Navbar from '../common_components/Navbar.vue';
    import NavbarItem from '../common_components/NavbarItem.vue';
    import NavbarNav from '../common_components/NavbarNav.vue';
    import NavbarCollapse from '../common_components/NavbarCollapse.vue';
    import Dropdown from '../common_components/Dropdown.vue';
    import DropdownMenu from '../common_components/DropdownMenu.vue';
    import dropdownItem from '../common_components/DropdownItem.vue';
    import DropdownToggle from '../common_components/DropdownToggle.vue';

    import drop from '../mixins/drop';
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

