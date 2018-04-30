<template>
    <b-container>
        <h3> quiz: {{ quiz.title }}</h3>
        <progress-bar-wrapper>
            <progress-bar :value='progress'> {{ progress }}</progress-bar>
        </progress-bar-wrapper>
        <p> {{ quiz }}</p>
    </b-container>
</template>

<script>
    import axios from 'axios';
    import ProgressBarWrapper from '../common_components/ProgressWrapper.vue'
    import ProgressBar from '../common_components/ProgressBar.vue'

    export default {
        data() {
            return {
                quiz: {},
                progress: 0,
            }
        },
        components: {
            ProgressBarWrapper,
            ProgressBar
        },
        name: "quiz",
        created() {
            let self = this;
            axios.get('/quiz/' + self.$route.params.id).then((resp) => {
                self.quiz = resp.data;
            })
        },
    }
</script>

<style scoped>

</style>