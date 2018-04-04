<template>
    <div class="panel panel-default text-center">
        <strong>{{ exercise.title }}</strong>
        <span v-if="exercise.answared" class="label label-success">Done</span>

            <ul class="list-group">
                <li class="list-group-item task-content">
                    <div>{{ exercise.task }}</div>
                </li>
                <li class="list-group-item">
                    <div class="form-group" v-if="exercise.answared">
                        <label class='left'>Answer:</label>
                        <textarea type="text" class="form-control" v-model="exercise.answare"
                                  required></textarea>
                        <a class="btn btn-success" @click="answare()">Submit
                            !</a>
                    </div>
                    <div v-if="exercise.answared" class="lesson-answer">
                        <pre>{{ exercise.answare }}</pre>
                        <label class='left' for="new_answare">New
                            answer:</label>
                        <textarea type="text" name="new_answare" id="new_answare" class="form-control"
                                  v-model="exercise.answare" required></textarea>
                        <a class="btn btn-success" @click="new_answare()">Update</a>
                    </div>
                </li>
            </ul>
        </div>
</template>

<script>
    import Prism from 'vue-prismjs'

    export default {
        name: "exercise",
        props:{

        },
        data() {
            return {
                exercise: {}
            }
        },
        methods: {
            answare() {
                data = {
                    "answare": this.exercise.answare,
                    "exercise": this.exercise.id,
                    "status": "Done"
                };
                axios.post('/api/exercise/', data)
            },

            new_answare() {
                data = {
                    "answare": this.exercise.answare,
                    "exercise": this.exercise.id
                };
                axios.put('/api/exercise/', data)
            }
        }
    }
</script>

<style scoped>

</style>