<template>
    <b-container>
        <progress-bar-wrapper>
            <progress-bar value=40 color="red" animated></progress-bar>
        </progress-bar-wrapper>
        <h3> Exam: {{ exam.title }}</h3>
    </b-container>
</template>

<script>
    import axios from 'axios';
    import ProgressBarWrapper from '../common_components/ProgressWrapper.vue'
    import ProgressBar from '../common_components/ProgressBar.vue'

    export default {
        data() {
            return {
                exam: {},
            }
        },
        components: {
            ProgressBarWrapper,
            ProgressBar
        },
        name: "exam",
        created() {
            let self = this;
            axios.get('/exam/' + self.$route.params.id).then((resp) => {
                self.exam = resp.data;
            })
        },
    }
</script>

<style scoped>

</style>