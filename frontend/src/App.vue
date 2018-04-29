<template>
    <div id="app">
        <app-header></app-header>

        <router-view></router-view>

        <app-footer></app-footer>
    </div>
</template>

<script>
    import Header from './components/_base/header.vue'
    import Footer from './components/_base/footer.vue'

    export default {
        name: 'app',
        components: {
            'app-header': Header,
            'app-footer': Footer
        },
        created() {
            this.$store.dispatch('tryAutoLogin')
        }
    }
</script>

<style>
    body, html {
        margin-top: 35px;
        font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
    }
    img {
        margin: 1rem;
        width: 100%;
    }
</style>