<template>
    <b-container>
        <h1 class="page-header">{{ testName }}: Create</h1>
    </b-container>
</template>

<script>
    import axios from 'axios';

    export default {
        name: "commonCreate",
        data() {
            return {
                test: {},
            }
        },
        props: {
            testType: {
                type: String,
                required: true,
            },
            testName: {
                type: String,
                required: true,
            },
        },
        computed: {},
        methods: {
        }
    }
</script>

<style scoped>

</style>