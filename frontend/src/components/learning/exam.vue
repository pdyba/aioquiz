<template>
    <b-container>
        <questions test-type="exam"></questions>
    </b-container>
</template>

<script>
    import Questions from './questions.vue'

    export default {
        components: {
            Questions
        },
        name: "exams"
    }
</script>

<style scoped>

</style>