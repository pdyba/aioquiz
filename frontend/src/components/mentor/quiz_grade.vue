<template>
    <b-container>
        <common-grade testType="quiz" testName="Quiz"></common-grade>
    </b-container>
</template>

<script>
    import commonGrade from './common_grade.vue'

    export default {
        components: {
            commonGrade
        },
        name: "quizGrade"
    }
</script>

<style scoped>

</style>