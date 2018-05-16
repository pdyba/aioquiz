<template>
    <b-container>
        <h1 class="page-header">Lessons: Management</h1>
        <b-table :items="lessons" :fields="fields">
            <template slot="Actions" slot-scope="cell">
                <b-btn size="sm" variant="primary">Details</b-btn>
            </template>
        </b-table>
    </b-container>
</template>

<script>
    import axios from 'axios';

    export default {
        name: "commonGradeList",
        data() {
            return {
                test: [],
                fields: [
                    'id',
                    'title',
                    'active',
                    'creator',
                    'amount',
                    'Actions'
                ],
            }
        },
        props: {
            testType: {
                type: String,
                required: true,
            },
            testName: {
                type: String,
                required: true,
            },
        },
        created() {
            let self = this;
            axios.get('/' + self.testType).then(
                function (response) {
                    self.test = response.data;
                }
            );
        },
        computed: {},
    }
</script>

<style scoped>

</style>