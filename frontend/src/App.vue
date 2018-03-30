<template>
    <div id="app">
        <app-header></app-header>

        <router-view></router-view>

        <app-footer></app-footer>
    </div>
</template>

<script>
    import Header from './components/_common/header.vue'
    import Footer from './components/_common/footer.vue'

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
        margin: 35px;
        font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
    }
</style>