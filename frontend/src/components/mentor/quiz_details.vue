<template>
    <b-container>
        <common-details testType="quiz" testName="Quiz"></common-details>
    </b-container>
</template>

<script>
    import commonDetails from './common_details.vue'

    export default {
        components: {
            commonDetails
        },
        name: "quizDetails"
    }
</script>

<style scoped>

</style>