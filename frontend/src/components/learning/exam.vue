<template>
    <b-container>
        <h3> Exam: {{ exam.title }}</h3>
    </b-container>
</template>

<script>
    import axios from 'axios';

    export default {
        data() {
            return {
                exam: {},
            }
        },
        components: {},
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