<template>
    <b-container>
        <common-details testType="live_quiz" testName="Live Quiz"></common-details>
    </b-container>
</template>

<script>
    import commonDetails from './common_details.vue'

    export default {
        components: {
            commonDetails
        },
        name: "liveQuizDetails"
    }
</script>

<style scoped>

</style>