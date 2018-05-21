<template>
    <b-container>
        <common-create testType="live_quiz" testName="Live Quiz"></common-create>
    </b-container>
</template>

<script>
    import commonCreate from './common_create.vue'

    export default {
        components: {
            commonCreate
        },
        name: "liveQuizCreate"
    }
</script>

<style scoped>

</style>