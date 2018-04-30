<template>
    <div>
        <h3> {{ testType }}: {{ quiz.title }}</h3>
        <progress-bar-wrapper>
            <progress-bar :value='progress'> {{ progress }}</progress-bar>
        </progress-bar-wrapper>
        <b-card no-body>
            <b-tabs pills card vertical>
                <b-tab v-for="quest in quiz.all_questions" :key="quest.id"
                       :disabled="!(quest.question_order === quiz.progress + 1) && !(quiz.status === 'Done' || quiz.status === 'Submitted')">
                    <template slot="title">
                        {{ quest.question_order }} <i class="fa fa-check-circle ml-2" v-if="quest.answered"></i>
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