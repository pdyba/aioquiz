<template>
    <container>
        <h3> Lesson: {{ lesson.lesson_no }}</h3>
            <vue-markdown id="lesson_cont" :source="lesson_content"></vue-markdown>
        <exercises lid="lesson.id"></exercises>
    </container>
</template>

<script>
    import axios from 'axios';
    import alt_axios from '../../alternative_axions';
    import Prism from 'prismjs'

    import VueMarkdown from 'vue-markdown'
    import Container from '../../material_components/Container.vue';
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
            Container,
            VueMarkdown,
            exercises,
        },
        name: "lesson",
        created() {
            let self = this;
            axios.get('/lessons/' + self.$route.params.id).then((resp) => {
                self.lesson = resp.data;
                alt_axios.get('http://127.0.0.1:5000/lesson_source/' + resp.data.file.substr(0, 4) + '/pl.md').then((resp) => {
                    self.lesson_content = resp.data;

                })
            })
        },
        mounted() {
            Prism.highlightAll();
            Prism.highlightAllUnder('#lesson_cont', Prism.languages.python, 'python');
        }
    }
</script>

<style scoped>

</style>