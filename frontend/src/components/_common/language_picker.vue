<template>
    <dropdown tag="li" class="nav-item">
        <dropdown-toggle tag="a" navLink color="indigo">Lang</dropdown-toggle>
        <dropdown-menu>
            <dropdown-item src="http://127.0.0.1:5000/images/pl.png" @click.prevent="setLang('pl')"
                           imgClass="language-img"></dropdown-item>
            <dropdown-item src="http://127.0.0.1:5000/images/pl.png" @click.prevent="setLang('en')"
                           imgClass="language-img"></dropdown-item>

        </dropdown-menu>
    </dropdown>
</template>

<script>
    import Dropdown from '../../material_components/Dropdown.vue';
    import DropdownMenu from '../../material_components/DropdownMenu.vue';
    import dropdownItem from '../../material_components/DropdownItem.vue';
    import DropdownToggle from '../../material_components/DropdownToggle.vue';

    export default {
        name: "language_picker",
        components: {
            DropdownMenu,
            dropdownItem,
            DropdownToggle,
            Dropdown
        },
        methods: {
            setLang(language) {

            },
        }
    }
</script>

<style scoped>

</style>