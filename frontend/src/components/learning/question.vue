<template>
    <div class="panel panel-default">
        <strong>{{ question.question }} </strong>
        <span v-if="question.answered" class="badge badge-success">Done</span>
        <div v-if="!submitted && can_answare">
            <b-form-group v-if="question.qtype === 'abcd'">
                <b-form-radio-group
                        v-model="question.answer"
                        :options="JSON.parse(question.answers)">
                </b-form-radio-group>

            </b-form-group>


            <b-form-group v-if="question.qtype === 'plain'">
                <b-form-textarea
                        v-model="question.answer"
                        placeholder="Enter answer"
                        :rows="4"
                        :max-rows="9">
                </b-form-textarea>
            </b-form-group>


            <b-form-group v-if="question.qtype === 'bool'">
                <b-form-radio-group
                        v-model="question.answer"
                        :options="[true, false]">
                </b-form-radio-group>
            </b-form-group>


            <div v-if="question.qtype === 'code'">
                <b-row>
                    <div class="editor_form">
                        <editor v-model="question.answer" @init="editorInit" lang="python" theme="chrome" width="100%"
                                height="100%"></editor>
                    </div>
                </b-row>
            </div>
            <br>
            <b-btn @click.prevent="answer()" v-if="!answered && !submitted" variant="success">Save</b-btn>
            <b-btn @click.prevent="new_answer()" v-if="answered && !submitted && can_answare" variant="warning">Update</b-btn>
            <b-btn @click.prevent="submit_test()" v-if="quiz.status === 'Done' && !submitted && can_answare" variant="danger">Submit
            </b-btn>
        </div>
        <div v-else>
            <pre class="language-python"><code class="language-python">{{ question.answer }}</code></pre>
        </div>
    </div>

</template>

<script>
    import axios from 'axios';
    import Prism from 'prismjs'
    const loadLanguages = require('prismjs/components/index.js');
    loadLanguages(['python']);


    export default {
        name: "question",
        props: {
            question: {
                type: Object,
                required: true
            },
            testType: {
                type: String,
                required: true
            },
            testid: {
                type: String,
                required: true
            },
            quiz: {
                type: Number,
                required: true
            },
            answer_only_once: {
                type: Boolean,
                required: false,
                default: false
            }
        },
        data() {
            return {
                answered: false
            }
        },
        components: {
            editor: require('vue2-ace-editor')
        },
        methods: {
            answer() {
                let data = {
                    "answer": this.question.answer,
                    "question": this.question.id,
                };
                axios.post('/' + this.testType + '/' + this.testid, data).then((resp) => {
                    this.answered = true;
                    this.quiz.progress += 1
                    if (Math.ceil(this.quiz.progress / this.quiz.all_questions.length * 100) === 100) {
                        this.quiz.status = "Done";
                    }
                    this.$swal('Done', resp.data.msg, "success")
                })
            },
            new_answer() {
                let data = {
                    "answer": this.question.answer,
                    "question": this.question.id
                };
                axios.put('/' + this.testType + '/' + this.testid, data).then((resp) => {
                        this.$swal('Done', resp.data.msg, "success")
                    }
                )
            },
            submit_test() {
                axios.patch('/' + this.testType + '/' + this.testid).then((resp) => {
                        this.$swal('Done', resp.data.msg, "success")
                    }
                );
                this.quiz.status = 'Submitted';
            },
            editorInit() {
                require('brace/ext/language_tools');
                require('brace/mode/python');
                // require('brace/theme/dracula'); TODO: add ability to change themes
                require('brace/theme/chrome');
            }
        },
        mounted() {
            if (this.question.answer === '') {
                this.answered = false
            } else {
                this.answered = true
            }
            Prism.highlightAll();
        },
        computed: {
            submitted() {
                return this.quiz.status === 'Submitted'
            },
            can_answare() {
                return !(this.answer_only_once && this.answered)
            }
        }
    }
</script>

<style scoped>
    .editor_form {
        min-height: 400px;
        min-width: 100%;
    }
</style>