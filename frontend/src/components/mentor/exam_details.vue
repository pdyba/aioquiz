<template>
    <b-container>
        <common-details testType="exam" testName="Exam"></common-details>
    </b-container>
</template>

<script>
    import commonDetails from './common_details.vue'

    export default {
        components: {
            commonDetails
        },
        name: "examDetails"
    }
</script>

<style scoped>

</style>