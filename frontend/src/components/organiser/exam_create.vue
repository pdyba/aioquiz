<template>
    <b-container>
        <common-create testType="exam" testName="Exam"></common-create>
    </b-container>
</template>

<script>
    import commonCreate from './common_create.vue'

    export default {
        components: {
            commonCreate
        },
        name: "examCreate"
    }
</script>

<style scoped>

</style>