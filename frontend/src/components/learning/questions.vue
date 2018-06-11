<template>
    <div>
        <h3> {{ testType }}: {{ quiz.title }}</h3>
        <progress-bar-wrapper>
            <progress-bar :value='progress'> {{ progress }}</progress-bar>
        </progress-bar-wrapper>
        <b-card no-body>
            <b-tabs pills card vertical>
                <b-tab v-for="quest in quiz.all_questions" :key="quest.id">
                    <template slot="title">{{ quest.question_order }} <span v-if="quest.question_details.answered"
                                                                            class="badge badge-success">Done</span>
                    </template>
                    <question :question="quest.question_details" :test-type="testType" :testid="testid"
                              :quiz="quiz" :answer_only_once="answer_only_once"></question>
                </b-tab>
            </b-tabs>
        </b-card>
    </div>
</template>

<script>
    import axios from 'axios';

    import ProgressBarWrapper from '../common_components/ProgressWrapper.vue'
    import ProgressBar from '../common_components/ProgressBar.vue'

    import question from "./question.vue"

    export default {
        name: "questions",
        components: {
            ProgressBarWrapper,
            ProgressBar,
            question
        },
        data() {
            return {
                quiz: {
                    all_questions: [],
                    progress: 0
                },
                testid: 0
            }
        },
        props: {
            testType: {
                type: String,
                required: true
            },
            answer_only_once: {
                type: Boolean,
                required: false,
                default: false
            }
        },
        created() {
            let self = this;
            self.testid = self.$route.params.id;
            axios.get('/' + self.testType + '/' + self.testid).then((resp) => {
                resp.data.all_questions.forEach(function (e) {
                    e.question_details.answered = e.question_details.answer !== '';
                });
                self.quiz = resp.data;
            })
        },
        computed: {
            progress() {
                return Math.ceil(this.quiz.progress / this.quiz.all_questions.length * 100)
            }
        }
    }
</script>

<style scoped>

</style>