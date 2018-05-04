<template>
    <b-container>
        <common-mngt testType="exam" testName="Exam"></common-mngt>
    </b-container>
</template>

<script>
    import commonMngt from './common_mngt.vue'

    export default {
        components: {
            commonMngt
        },
        name: "examMngt"
    }
</script>

<style scoped>

</style>