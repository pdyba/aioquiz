<template>
    <b-container>
        <b-tabs>
            <b-tab title="Lesson">
                <h3> Lesson: {{ lesson.lesson_no }}</h3>
                <vue-markdown :source="lesson_content"></vue-markdown>
            </b-tab>
            <b-tab title="Exercises">
                <exercises lid="lesson.id"></exercises>
            </b-tab>
            <b-tab title="Live Quiz">
                ...
            </b-tab>
            <b-tab title="Feedback">
                ...
            </b-tab>
            <b-tab title="Home Work">
                ...
            </b-tab>
        </b-tabs>
    </b-container>
</template>

<script>
    import axios from 'axios';
    import alt_axios from '../../alternative_axions';
    import Prism from 'prismjs'

    import VueMarkdown from 'vue-markdown'
    import exercises from './exercises.vue'

    const loadLanguages = require('prismjs/components/index.js');
    loadLanguages(['python']);

    export default {
        data() {
            return {
                lesson: {},
                lesson_content: ""
            }
        },
        components: {
            VueMarkdown,
            exercises,
        },
        name: "lesson",
        created() {
            let self = this;
            axios.get('/lessons/' + self.$route.params.id).then((resp) => {
                self.lesson = resp.data;
                alt_axios.get('lesson_source/' + resp.data.file.substr(0, 4) + '/pl.md').then((resp) => {
                    self.lesson_content = resp.data;

                })
            })
        },
        updated() {
            Prism.highlightAll();
        }
    }
</script>

<style scoped>
    img {
        margin: 1rem;
        width: ;
    }
</style>