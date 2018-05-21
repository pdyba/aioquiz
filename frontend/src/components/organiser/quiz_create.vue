<template>
    <b-container>
        <common-create testType="quiz" testName="Quiz"></common-create>
    </b-container>
</template>

<script>
    import commonCreate from './common_create.vue'

    export default {
        components: {
            commonCreate
        },
        name: "quizCreate"
    }
</script>

<style scoped>

</style>