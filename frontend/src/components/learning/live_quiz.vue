<template>
    <b-container>
        <questions test-type="live_quiz"></questions>
    </b-container>
</template>

<script>
    import Questions from './questions.vue'

    export default {
        components: {
            Questions
        },
        name: "live_quizzes"
    }
</script>

<style scoped>

</style>