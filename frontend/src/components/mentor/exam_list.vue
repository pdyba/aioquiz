<template>
    <b-container>
        <common-list testType="exam" testName="Exam"></common-list>
    </b-container>
</template>

<script>
    import commonList from './common_list.vue'

    export default {
        components: {
            commonList
        },
        name: "examList"
    }
</script>

<style scoped>

</style>