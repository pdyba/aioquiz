<template>
    <b-container>
        <common-mngt testType="quiz"></common-mngt>
    </b-container>
</template>

<script>
    import commonMngt from './common_create.vue'

    export default {
        components: {
            commonMngt
        },
        name: "quizCreate"
    }
</script>

<style scoped>

</style>