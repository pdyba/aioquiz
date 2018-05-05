<template>
    <b-container>
        <common-create :testType="testType" :testName="testName" :testData="test" :unused_questions="unused_questions"></common-create>
    </b-container>
</template>

<script>
    import axios from 'axios';
    import commonCreate from './common_create.vue'

    export default {
        name: "commonEdit",
        components: {
            commonCreate
        },
        data() {
            return {
                test: {},
                unused_questions: []
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
        created() {
            let self = this;
            axios.get('/organiser/' + self.testType + '/' + self.$route.params.id).then((resp) => {
                self.test = resp.data;
                self.unused_questions = resp.data.unused_questions
            })
        }
    }
</script>

<style scoped>

</style>