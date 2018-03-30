<template>

    <container>
        <navbar position="top" class="indigo navbar-dark" name="PyLove.org" href="/" scrolling>
            <navbar-collapse>
                <navbar-nav right>

                    <!--<navbar-item class="need-help" href="#" waves-fixed>HELP</navbar-item>-->
                    <!--<navbar-item class="need-help-clicked" href="#" waves-fixed>THX</navbar-item>-->
                    <navbar-item href="#" waves-fixed>Lessons</navbar-item>
                    <navbar-item href="#" waves-fixed>Quiz</navbar-item>
                    <navbar-item href="#" waves-fixed>Live Quiz</navbar-item>
                    <navbar-item href="#" waves-fixed>About</navbar-item>

                    <divider></divider>
                    <dropdown tag="li" class="nav-item">
                        <dropdown-toggle tag="a" navLink color="indigo" waves-fixed>Overview</dropdown-toggle>
                        <dropdown-menu>
                            <dropdown-item>Seats</dropdown-item>
                            <dropdown-item>Lesson</dropdown-item>
                            <dropdown-item>Quiz</dropdown-item>
                            <dropdown-item>Live Quiz</dropdown-item>
                            <dropdown-item>Users List</dropdown-item>
                        </dropdown-menu>
                    </dropdown>

                    <dropdown tag="li" class="nav-item">
                        <dropdown-toggle tag="a" navLink color="indigo" waves-fixed>Manage</dropdown-toggle>
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

                    <divider></divider>
                    <dropdown tag="li" class="nav-item">
                        <dropdown-toggle tag="a" navLink color="indigo" waves-fixed>Admin</dropdown-toggle>
                        <dropdown-menu>
                            <dropdown-item>Attendee: Review</dropdown-item>
                            <dropdown-item>E-mail</dropdown-item>
                            <dropdown-item>Users</dropdown-item>
                            <dropdown-item>Config</dropdown-item>
                        </dropdown-menu>
                    </dropdown>
                </navbar-nav>
                <navbar-nav right>
                    <navbar-item href="/signin">Login / Register</navbar-item>

                    <dropdown tag="li" class="nav-item">
                        <dropdown-toggle tag="a" navLink color="indigo" waves-fixed>#username</dropdown-toggle>
                        <dropdown-menu>
                            <dropdown-item>My Profile</dropdown-item>
                            <dropdown-item>Edit Profile</dropdown-item>
                            <dropdown-item>My Seat</dropdown-item>
                            <dropdown-item>Attendance</dropdown-item>
                        </dropdown-menu>
                    </dropdown>
                    <dropdown tag="li" class="nav-item">
                        <dropdown-toggle tag="a" navLink color="indigo" waves-fixed>Lang</dropdown-toggle>
                        <dropdown-menu>
                            <dropdown-item src="http://127.0.0.1:5000/images/pl.png" :onclick="setLang('pl')" imgClass="language-img"></dropdown-item>
                            <dropdown-item src="http://127.0.0.1:5000/images/pl.png" :onclick="setLang('pl')" imgClass="language-img"></dropdown-item>

                        </dropdown-menu>
                    </dropdown>
                    <navbar-item>&#10006;</navbar-item>
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
            divider
        },
        mixins: [drop],
        methods: {
            setLang (language) {
            console.log(language)
    }
    }
    };
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
    .navbar .dropdown-menu a:hover {
        color: inherit !important;
    }
</style>

