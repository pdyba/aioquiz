<template>
    <b-container>
        <common-list testType="live_quiz" testName="Live Quiz"></common-list>
    </b-container>
</template>

<script>
    import commonList from './common_list.vue'

    export default {
        components: {
            commonList
        },
        name: "liveQuizList"
    }
</script>

<style scoped>

</style>