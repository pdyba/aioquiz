<template>
    <b-container>
        <h1 class="page-header">{{ testName }}: Management</h1>
        <b-table :items="test" :fields="fields">
            <template slot="Management" slot-scope="cell">
                <b-btn size="sm" variant="primary" @click.stop="activate(cell.item)" v-if="!cell.item.active">
                    Activate
                </b-btn>
                <b-btn size="sm" variant="danger" @click.stop="deactivate(cell.item)" v-if="cell.item.active">
                    Deactivate
                </b-btn>
                <b-link :to="testType + '-edit/' + cell.item.id"><b-btn size="sm">Edit</b-btn></b-link>
            </template>
        </b-table>
    </b-container>
</template>

<script>
    import axios from 'axios';

    export default {
        name: "commonMngt",
        data() {
            return {
                test: [],
                fields: [
                    'id',
                    'title',
                    'active',
                    'creator',
                    'amount',
                    'Management'
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
        methods: {
            activate(lid) {
                let self = this;
                let data = {
                    'active': true,
                    'id': lid.id
                };
                axios.post('/organiser/' + self.testType + '/set_active', data).then((resp) => {
                    if (resp.data.success) {
                        lid.active = true
                    }
                });
            },
            deactivate(lid) {
                let self = this;
                let data = {
                    'active': false,
                    'id': lid.id
                };
                axios.post('/organiser/' + self.testType + '/set_active', data).then((resp) => {
                    if (resp.data.success) {
                        lid.active = false
                    }
                });
            }
        }
    }
</script>

<style scoped>

</style>