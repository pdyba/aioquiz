<template>
    <b-container>
        <h1 class="page-header">{{ testName }}</h1>
        <b-table :items="tests" :fields="fields">
            <template slot="Actions" slot-scope="cell">
                <router-link :to="'/mentor/' + testType + '/' + cell.item.id"><b-btn size="sm" variant="primary">Details</b-btn></router-link>
            </template>
        </b-table>
    </b-container>
</template>

<script>
    import axios from 'axios';

    export default {
        name: "commonTestList",
        data() {
            return {
                tests: [],
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
            axios.get('/mentor/' + self.testType).then(
                function (response) {
                    self.tests = response.data;
                }
            );
        },
        computed: {},
    }
</script>

<style scoped>

</style>