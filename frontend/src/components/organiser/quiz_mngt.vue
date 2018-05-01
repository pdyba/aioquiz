<template>
    <b-container>
        <common-mngt testType="quiz" testName="Quiz"></common-mngt>
    </b-container>
</template>

<script>
    import commonMngt from './common_mngt.vue'

    export default {
        components: {
            commonMngt
        },
        name: "quizMngt"
    }
</script>

<style scoped>

</style>