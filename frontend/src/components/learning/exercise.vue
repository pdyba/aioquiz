<template>
    <div class="panel panel-default">
        <strong>{{ exercise.title }} </strong><span v-if="exercise.answared" class="badge badge-success">Done</span>
        <br>
        {{ exercise.task }}
        <br>
        <br>
        <row>
            <column sm="6" a>
                <b-form>
                    <b-form-group label="New answer:" id="ex_answare_text">
                        <b-form-textarea
                                v-model="exercise.answare"
                                required :rows="6">
                        </b-form-textarea>
                    </b-form-group>
                </b-form>
            </column>
            <column sm="6">
                <span v-if="exercise.answared">Old answer:</span>
                <span v-else>Preview</span>
                <prism language="python" :code="exercise.answare"></prism>
                <div class="form-actions">
                    <b-button type="submit" variant="success" @click.prevent="answer()" v-if="!exercise.answared">
                        Submit
                    </b-button>
                    <b-button variant="warning" @click.prevent="new_answer()" v-if="exercise.answared">Update
                    </b-button>
                </div>
            </column>
        </row>
    </div>
</template>

<script>
    import axios from 'axios';
    import Prism from 'vue-prismjs'
    import 'prismjs/themes/prism.css'

    import Row from '../../material_components/Row.vue';
    import Column from '../../material_components/Col.vue';

    export default {
        name: "exercise",
        props: {
            exercise: {
                type: Object,
                required: true
            }
        },
        components: {
            Prism,
            Row,
            Column
        },
        methods: {
            answer() {
                let data = {
                    "answare": this.exercise.answare,
                    "exercise": this.exercise.id,
                    "status": "Done"
                };
                axios.post('/exercise/', data).then((resp) => {
                    this.exercise.answared = true
                    this.exercise.status = "Done"
                    this.$swal('Done', "Answer saved", "success")
                })
            },

            new_answer() {
                let data = {
                    "answare": this.exercise.answare,
                    "exercise": this.exercise.id
                };
                axios.put('/exercise/', data).then(
                    this.$swal('Done', "Answer updated", "success")
                )
            }
        }
    }
</script>

<style scoped>

</style>