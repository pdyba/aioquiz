<template>
    <b-container>
        <h3> Quiz: {{ quiz }}</h3>
    </b-container>
</template>

<script>
    import axios from 'axios';

    export default {
        data() {
            return {
                quiz: {},
            }
        },
        components: {},
        name: "Quiz",
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