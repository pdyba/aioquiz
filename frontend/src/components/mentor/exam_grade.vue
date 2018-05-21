<template>
    <b-container>
        <common-grade testType="exam" testName="Exam"></common-grade>
    </b-container>
</template>

<script>
    import commonGrade from './common_grade.vue'

    export default {
        components: {
            commonGrade
        },
        name: "examGrade"
    }
</script>

<style scoped>

</style>