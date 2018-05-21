<template>
    <b-container>
        <common-edit testType="live_quiz" testName="Live Quiz"></common-edit>
    </b-container>
</template>

<script>
    import commonEdit from './common_edit.vue'

    export default {
        components: {
            commonEdit
        },
        name: "liveQuizEdit"
    }
</script>

<style scoped>

</style>