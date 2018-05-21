<template>
    <b-container>
        <h1 class="page-header">Lessons: Management</h1>
        <b-table :items="lessons" :fields="fields">
        </b-table>
    </b-container>
</template>

<script>
    import axios from 'axios';

    export default {
        name: "lesson_status",
        data() {
            return {
                lessons: [],
                fields: [
                    'id',
                    'title',
                    'active',
                    'Management'
                ],
            }
        },
        created() {
            let self = this;
            axios.get('/lessons').then(
                function (response) {
                    self.lessons = response.data;
                }
            );
        },
    }
</script>

<style scoped>

</style>