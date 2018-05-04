<template>
    <b-container>
        <common-edit testType="exam" testName="Exam"></common-edit>
    </b-container>
</template>

<script>
    import commonEdit from './common_edit.vue'

    export default {
        components: {
            commonEdit
        },
        name: "examEdit"
    }
</script>

<style scoped>

</style>