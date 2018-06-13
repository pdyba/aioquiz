<template>
    <b-container>
        <h1 class="page-header">{{ testName }} - Question: {{ $route.params.id }}</h1>
        <p>Question: {{ question.question }}</p>
        <p v-if="question.possible_answer">Possible Answer: {{ question.possible_answer }}</p>

        <b-row class="mb-12" className="card-deck" v-for="i in rowCount" :key="i.id">
            <b-col sm="12" v-for="(x, index) in itemCountInRow(i)" :key="x.id">
                <card className="samesize card-dark card-cascade">
                    <card-header>{{ index }}
                        <b-badge v-if="grated[index]" :variant="get_color(x.status)">{{ x.status }}</b-badge>
                    </card-header>
                    <card-body>
                        <pre class="language-python"><code class="language-python">{{ x.answer }}</code></pre>
                    </card-body>
                    <card-footer>
                        <b-form>
                            <b-form-group>
                                <b-form-textarea
                                        v-model="x.comment"
                                        placeholder="Enter comment"
                                        :rows="1"
                                        :max-rows="9">
                                </b-form-textarea>
                            </b-form-group>
                            <b-form-group>
                                <input
                                        type="number"
                                        v-model="x.score">
                            </b-form-group>
                        </b-form>
                        <b-btn v-if="grated[index]"  size="sm" @click.stop="score_update(x)">Update Grade</b-btn>
                        <b-btn v-else size="sm" @click.stop="score(x)">Grade</b-btn>
                    </card-footer>
                </card>
            </b-col>
            <br>
        </b-row>
    </b-container>
</template>

<script>
    import axios from 'axios';

    import Card from '../common_components/Card.vue';
    import CardHeader from '../common_components/CardHeader.vue';
    import CardBody from '../common_components/CardBody.vue';
    import CardFooter from '../common_components/CardFooter.vue';


    export default {
        name: "test_question_score",
        data() {
            return {
                question: {},
                answers: [],
                itemsPerRow: 1
            }
        },
        props: {
            testType: {
                type: String,
                required: true,
            },
            testName: {
                type: String,
                required: true,
            },
        },
        components: {
            Card,
            CardHeader,
            CardFooter,
            CardBody,
        },
        created() {
            let self = this;
            axios.get('/mentor/grade/' + self.testType + '/' + self.$route.params.id).then(
                function (response) {
                    self.question = response.data;
                    self.answers = response.data.answers.map(function (item) {
                        item.status = item.score !== -1 ? 'scored' : 'notscored';
                        return item;
                    });
                    Prism.highlightAll();
                }
            );
        },
        computed: {
            rowCount: function () {
                return Math.ceil(this.answers.length / this.itemsPerRow);
            },
            grated: function () {
                return this.answers.map(function (item) {
                    return item.status === 'scored';
                });

            }
        },
        methods: {
            score(answer) {
                let self = this;
                axios.post('/mentor/grade/' + self.testType + '/' + self.$route.params.id, answer).then(
                    function (response) {
                        self.$swal({
                            title: "Lesson Code",
                            text: response.data.msg,
                            type: "success",
                        });
                        answer.status = 'scored'
                    }
                );
            },
            score_update(answer) {
                let self = this;
                axios.put('/mentor/grade/' + self.testType + '/' + self.$route.params.id, answer).then(
                    function (response) {
                        self.$swal({
                            title: "Lesson Code",
                            text: response.data.msg,
                            type: "success",
                        })
                    }
                );
            },
            itemCountInRow: function (index) {
                return this.answers.slice((index - 1) * this.itemsPerRow, index * this.itemsPerRow)
            },
            get_color(status) {
                if (status === 'scored') {
                    return 'success'
                } else {
                    return 'info'
                }

            }
        }
    }
</script>

<style scoped>

</style>