<template>
    <dropdown tag="li" class="nav-item">
        <!--Clicking on the flag it self does not work ;/-->
        <dropdown-toggle tag="a" navLink color="indigo"><img :src="get_current_lang"></dropdown-toggle>
        <dropdown-menu class="small">
            <b-link @click.prevent="setLang(key)" v-for="(val, key) in languages" :key="key" :class="['nav-link', 'small-link']">
                <img :src="val.img">
            </b-link>
        </dropdown-menu>
    </dropdown>
</template>

<script>
    import Dropdown from '../common_components/Dropdown.vue';
    import DropdownMenu from '../common_components/DropdownMenu.vue';
    import DropdownToggle from '../common_components/DropdownToggle.vue';

    export default {
        name: "LanguagePicker",
        data() {
            return {
                languages: {
                    'pl': {img: '/images/pl.png'},
                    'en': {img: '/images/en.png'}
                }
            }
        },
        components: {
            DropdownMenu,
            DropdownToggle,
            Dropdown
        },
        methods: {
            setLang(language) {
                this.$store.dispatch('changeLanguage', language);
                this.$i18n.locale = language;
            },
        },
        computed: {
            get_current_lang() {
                let language = this.$store.getters.language;
                this.$i18n.locale = language;
                return this.languages[language].img
            }
        }
    }
</script>

<style scoped>
    img {
        max-height: 1rem;
        max-width: 1rem;
        padding: 0;
        margin: 0;
    }
    .small {
        min-width: 1.2rem;
    }
    .small-link {
        padding: 0.1rem !important;
        margin: 0.1rem !important;
    }
</style>
