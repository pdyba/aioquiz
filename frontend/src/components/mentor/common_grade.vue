<template>
    <b-container>
        <h1 class="page-header">{{ testName }} - Question: {{ $route.params.id }}</h1>
        <p>Question: {{ question.question }}</p>
        <p v-if="question.possible_answer">Possible Answer: {{ question.possible_answer }}</p>
        <b-table :items="question.answers" :fields="fields">
            <!--<template slot="comment_form" slot-scope="cell">-->
            <template slot="Actions" slot-scope="cell">
                <b-form>
                    <b-form-group>
                        <b-form-textarea
                            v-model="cell.comment"
                            placeholder="Enter comment"
                            :rows="1"
                            :max-rows="9">
                        </b-form-textarea>
                    </b-form-group>
                <!--</b-form>-->
            <!--</template>-->
            <!--<template slot="grade_form" slot-scope="cell">-->
                <!--<b-form>-->
                    <b-form-group>
                        <input
                            type="text"
                            v-model="cell.grade">
                    </b-form-group>
                </b-form>
            <!--</template>-->

                 <b-btn size="sm" @click.stop="grade(cell.user, cell.grade, cell.comment)">Grade</b-btn>
            </template>
        </b-table>
        {{ question }}
        <br>
        {{ question.answers }}
    </b-container>
</template>

<script>
    import axios from 'axios';

    export default {
        name: "test_question_grade",
        data() {
            return {
                question: [],
                fields: [
                    'answer',
                    // 'comment_form',
                    // 'grade_form',
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
            axios.get('/mentor/grade/' + self.testType + '/' + self.$route.params.id).then(
                function (response) {
                    self.question = response.data;
                }
            );
        },
        computed: {},
        methods: {
            grade(lid, grade) {
                console.log(lid, grade, comment)
                // let self = this;
                // let data = {};
                // axios.post('/mentor/grade/' + self.testType + '/' + self.$route.params.id, data).then(
                //     function (response) {
                //         self.$swal({
                //             title: "Lesson Code",
                //             html: "<h1>" + response.data.code + "</h1><h3><br>will expire at:<br>" + response.data.time_ended + "</h3>",
                //             type: "success",
                //         })
                //     }
                // );
            },
            update_grade(lid, grade) {
                let self = this;
                let data = {};
                axios.put('/mentor/grade/' + self.testType + '/' + self.$route.params.id, data).then(
                    function (response) {
                        self.$swal({
                            title: "Lesson Code",
                            html: "<h1>" + response.data.code + "</h1><h3><br>will expire at:<br>" + response.data.time_ended + "</h3>",
                            type: "success",
                        })
                    }
                );
            },
        }
    }
</script>

<style scoped>

</style>