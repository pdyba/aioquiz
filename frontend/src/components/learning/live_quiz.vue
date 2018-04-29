<template>
    <b-container>
        <h3> LiveQuiz: {{ live_quiz }}</h3>
    </b-container>
</template>

<script>
    import axios from 'axios';

    export default {
        data() {
            return {
                live_quiz: {},
            }
        },
        components: {},
        name: "liveQuiz",
        created() {
            let self = this;
            axios.get('/live_quiz/' + self.$route.params.id).then((resp) => {
                self.live_quiz = resp.data;
            })
        },
    }
</script>

<style scoped>

</style>