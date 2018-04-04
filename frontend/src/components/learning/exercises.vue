<template>
    <div v-if="exercises">
        <h1>Exercises: </h1>
        <b-card no-body>
            <b-tabs pills card vertical>
                <b-tab :title="ex.title" v-for="ex in exercises"><i class="fas fa-check-circle" v-if="ex.answared"></i>
                    <exercise :exercise="ex"></exercise>
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
                answare: '',
                new_answare: ''
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