<template>
    <b-container>
        <h3> quiz: {{ quiz.title }}</h3>
        <progress-bar-wrapper>
            <progress-bar :value='progress'> {{ progress }}</progress-bar>
        </progress-bar-wrapper>
        <questions :questions="quiz.all_questions" :progress="quiz.progress"></questions>
    </b-container>
</template>

<script>
    import axios from 'axios';
    import ProgressBarWrapper from '../common_components/ProgressWrapper.vue'
    import ProgressBar from '../common_components/ProgressBar.vue'
    import Questions from './questions.vue'

    export default {
        data() {
            return {
                quiz: {
                    all_questions: [],
                    progress: 0
                },
            }
        },
        components: {
            ProgressBarWrapper,
            ProgressBar,
            Questions
        },
        name: "quiz",
        beforeCreate() {
            let self = this;
            axios.get('/quiz/' + self.$route.params.id).then((resp) => {
                self.quiz = resp.data;
            })
        },
        computed: {
            progress(){
                return Math.ceil(this.quiz.progress / this.quiz.all_questions.length)
            }
        }
    }
</script>

<style scoped>

</style>