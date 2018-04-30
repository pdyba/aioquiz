<template>
    <div class="panel panel-default">
        <strong>{{ question.question }} </strong>
        <span v-if="question.answered" class="badge badge-success">Done</span>

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
        <b-btn @click.prevet="answer()" v-if="!answered" variant="success">Save</b-btn>
        <b-btn @click.prevet="new_answer()" v-else variant="warning">Update</b-btn>
    </div>
</template>

<script>
    import axios from 'axios';
    import 'prismjs/themes/prism.css'

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
                    this.question.status = "Done";
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
            editorInit() {
                require('brace/ext/language_tools');
                require('brace/mode/python');
                // require('brace/theme/dracula'); TODO: add ability to change themes
                require('brace/theme/chrome');
            }
        },
        mounted() {
            // let self = this;
            if (this.question.answer === '') {
                this.answered = false
            } else {
                this.answered = true
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