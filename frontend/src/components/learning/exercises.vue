<template>
    <div v-if="exercises.length > 0">
        <h1>Exercises: </h1>
        <b-card no-body>
            <b-tabs pills card vertical>
                <b-tab v-for="ex in exercises" :key="ex.id">
                    <template slot="title">
                        {{ ex.title }} <i class="fa fa-check-circle ml-2" v-if="ex.answered"></i>
                    </template>
                    <exercise :exercise="ex">&#f058;</exercise>
                </b-tab>
            </b-tabs>
        </b-card>
    </div>
</template>

<script>
    import axios from 'axios';

    import exercise from "./exercise.vue"

    export default {
        name: "exercises",
        data() {
            return {
                exercises: [],
                answer: '',
                new_answer: ''
            }
        },
        components: {
            exercise
        },
        created() {
            let self = this;
            axios.get('/exercise/' + this.$route.params.id).then(
                function (response) {
                    self.exercises = response.data;
                })
        }
    }
</script>

<style scoped>

</style>