<template>
    <b-container>
        <common-edit testType="quiz" testName="Quiz"></common-edit>
    </b-container>
</template>

<script>
    import commonEdit from './common_edit.vue'

    export default {
        components: {
            commonEdit
        },
        name: "quizEdit"
    }
</script>

<style scoped>

</style>