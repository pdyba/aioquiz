<template>
    <b-container>
        <navbar position="top" class="indigo navbar-dark" alt="PyLove.org" href="/" scrolling src="./images/pylove_white.png">
            <navbar-collapse>
                <navbar-nav right>
                    <!--<help v-if="auth"></help>-->
                    <navbar-item href="/about">{{ $t('about') }}</navbar-item>
                    <navbar-item href="/lessons" v-if="auth">{{ $t('lessons') }}</navbar-item>
                    <navbar-item href="/quiz" v-if="auth">{{ $t('quiz') }}</navbar-item>
                    <navbar-item href="/feedback" v-if="auth">{{ $t('feedback') }}</navbar-item>
                    <navbar-item href="/exam" v-if="auth">{{ $t('exam') }}</navbar-item>

                    <divider v-if="mentor || org"></divider>
                    <dropdown tag="li" class="nav-item" v-if="mentor">
                        <dropdown-toggle tag="a" navLink color="indigo">Mentor</dropdown-toggle>
                        <dropdown-menu>
                            <!--<dropdown-item href="/mentor/questions">Questions</dropdown-item>-->
                            <!--<dropdown-item href="/mentor/lesson">Lesson: status</dropdown-item>-->
                            <!--<dropdown-item href="/mentor/homework">Homework: grade</dropdown-item>-->
                            <!--<dropdown-item href="/mentor/live_quiz">Live Quiz: Overview</dropdown-item>-->
                            <dropdown-item href="/mentor/quiz">Quiz: Grade</dropdown-item>
                            <dropdown-item href="/mentor/exam">Exam: Grade</dropdown-item>
                            <dropdown-item href="/mentor/users">Users: Overview</dropdown-item>
                        </dropdown-menu>
                    </dropdown>

                    <dropdown tag="li" class="nav-item" v-if="org">
                        <dropdown-toggle tag="a" navLink color="indigo">Organiser</dropdown-toggle>
                        <dropdown-menu>
                            <!--<dropdown-item>Lesson: Create</dropdown-item>-->
                            <dropdown-item href="/organiser/attendee_review">Attendee: Review</dropdown-item>
                            <dropdown-item href="/organiser/lessons">Lesson: Manage</dropdown-item>
                            <!--<dropdown-item>Question: Manage</dropdown-item>-->
                            <!--<dropdown-item>Question: Create</dropdown-item>-->
                            <dropdown-item href="/organiser/quiz-create">Quiz: Create</dropdown-item>
                            <dropdown-item href="/organiser/quiz-manage">Quiz: Manage</dropdown-item>
                            <dropdown-item href="/organiser/live-quiz-create">Live Quiz: Create</dropdown-item>
                            <dropdown-item href="/organiser/live-quiz-manage">Live Quiz: Manage</dropdown-item>
                            <dropdown-item href="/organiser/exam-create">Exam: Create</dropdown-item>
                            <dropdown-item href="/organiser/exam-manage">Exam: Manage</dropdown-item>
                            <dropdown-item href="/organiser/users">Users</dropdown-item>
                            <dropdown-item href="/organiser/users/review">Users: Review</dropdown-item>
                        </dropdown-menu>
                    </dropdown>

                    <divider v-if="admin"></divider>
                    <dropdown tag="li" class="nav-item" v-if="admin">
                        <dropdown-toggle tag="a" navLink color="indigo">Admin</dropdown-toggle>
                        <dropdown-menu>
                            <dropdown-item href="/admin/email">E-mail</dropdown-item>
                            <dropdown-item href="/admin/users">Users</dropdown-item>
                            <dropdown-item href="/admin/config">Config</dropdown-item>
                            <dropdown-item href="/admin/events">Events</dropdown-item>
                        </dropdown-menu>
                    </dropdown>
                    <event-context-picker v-if="admin || org"></event-context-picker>
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
                    <language-picker></language-picker>
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
    import LanguagePicker from './language_picker.vue';
    import EventContextPicker from './event_context.vue';
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
            LanguagePicker,
            help,
            EventContextPicker
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

<i18n>
{
  "en": {
    "lessons": "Lessons",
    "about": "About",
    "quiz": "Quiz",
    "feedback": "Feedback",
    "exam": "Exam"
  },
  "pl": {
    "lessons": "Lekcje",
    "about": "O Nas",
    "quiz": "Kartkówka",
    "feedback": "Informacja Zwrotna",
    "exam": "Egzamin"
  }
}
</i18n>