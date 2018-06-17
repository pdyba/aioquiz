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
        <b-btn v-if="can_close" size="sm" @click.stop="CloseTest()">Close Test</b-btn>
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
                can_close: false
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
                self.can_close_fn()
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
        methods: {
            autograde(question) {
                let self = this;
                axios.get('/mentor/autograde/' + self.testType + '/' + question.question).then(
                    function (response) {
                        let mtype = 'error';
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
            },
            CloseTest() {
                let self = this;
                self.$swal({
                    title: 'Close Test',
                    text: 'Are You sure',
                    type: 'warning',
                    showCancelButton: true,
                    confirmButtonText: 'Submit',
                    showLoaderOnConfirm: true,
                    allowOutsideClick: true,
                }).then((value) => {
                    if (value.value) {
                        axios.post('/mentor/' + self.testType + '/' + self.$route.params.id, {}).then(
                            function (response) {
                                let mtype = 'error';
                                if (response.data.success) {
                                    mtype = "success"
                                }
                                self.$swal({
                                    title: "Test Closed",
                                    text: response.data.msg,
                                    type: mtype,
                                });
                            }
                        )
                    }
                })
            },
            can_close_fn: function () {
                let to_grade = 0;
                if (this.test && this.test.all_questions) {
                    this.test.all_questions.map(function (item) {
                        to_grade += item.to_grade;
                    });
                    this.can_close = to_grade === 0
                }
            }
        }
    }
</script>

<style scoped>

</style>