<template>
    <dropdown tag="li" class="nav-item">
        <dropdown-toggle tag="a" navLink color="indigo">Lang</dropdown-toggle>
        <dropdown-menu>
            <dropdown-item src="/images/pl.png" @click.prevent="setLang('pl')"
                           imgClass="language-img"> </dropdown-item>
            <dropdown-item src="/images/pl.png" @click.prevent="setLang('en')"
                           imgClass="language-img"> </dropdown-item>
        </dropdown-menu>
    </dropdown>
</template>

<script>
    import Dropdown from '../common_components/Dropdown.vue';
    import DropdownMenu from '../common_components/DropdownMenu.vue';
    import dropdownItem from '../common_components/DropdownItem.vue';
    import DropdownToggle from '../common_components/DropdownToggle.vue';

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