<template>
    <b-container>
        <h1 class="page-header">{{ testName }}</h1>
        <b-table :items="test.all_questions" :fields="fields">
            <template slot="Management" slot-scope="cell">
                <router-link :to="'/mentor/grade/' + testType + '/' + cell.item.question">
                    <b-btn size="sm" variant="primary">Grade</b-btn>
                </router-link>
                <b-btn v-if="cell.item.question_details.qtype === 'abcd' || cell.item.question_details.qtype === 'bool'"
                       size="sm" variant="danger" @click.stop="autograde(cell.item)">AutoGrade
                </b-btn>
            </template>
        </b-table>
    </b-container>
</template>

<script>
    import axios from 'axios';

    export default {
        name: "test_details",
        data() {
            return {
                test: [],
                fields: [
                    'question_order',
                    'question_details.question',
                    'question_details.qtype',
                    'graded',
                    'to_grade',
                    'Management'
                ],
            }
        },
        created() {
            let self = this;
            axios.get('/mentor/' + self.testType + '/' + self.$route.params.id).then((resp) => {
                resp.data.all_questions = resp.data.all_questions.map(function (item) {
                    item._rowVariant = item.to_grade === 0 ? 'success' : 'warning';
                    return item;
                });
                self.test = resp.data;
            })
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
        computed: {},
        methods: {
            autograde(question) {
                let self = this;
                axios.get('/mentor/autograde/' + self.testType + '/' + question.question).then(
                    function (response) {
                        let mtype = 'error'
                        if (response.data.success) {
                            question.to_grade = 0;
                            question._rowVariant = 'success';
                            mtype = "success"
                        }
                        self.$swal({
                            title: "Autograde",
                            text: response.data.msg,
                            type: mtype,
                        });
                    })
            }
        }
    }
</script>

<style scoped>

</style>