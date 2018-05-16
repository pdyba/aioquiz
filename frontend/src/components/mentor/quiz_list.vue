<template>
    <b-container>
        <common-list testType="quiz" testName="Quiz"></common-list>
    </b-container>
</template>

<script>
    import commonList from './common_list.vue'

    export default {
        components: {
            commonList
        },
        name: "quizList"
    }
</script>

<style scoped>

</style>