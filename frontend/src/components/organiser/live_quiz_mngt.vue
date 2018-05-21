<template>
    <b-container>
        <common-mngt testType="live_quiz" testName="Live Quiz"></common-mngt>
    </b-container>
</template>

<script>
    import commonMngt from './common_mngt.vue'

    export default {
        components: {
            commonMngt
        },
        name: "liveQuizMngt"
    }
</script>

<style scoped>

</style>