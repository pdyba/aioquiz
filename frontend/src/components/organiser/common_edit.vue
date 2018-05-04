<template>
    <b-container>
        <common-create :testType="testType" :testName="testName" :testData="test"></common-create>
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
            axios.get('/' + self.testType + '/' + self.$route.params.id).then((resp) => {
                self.test = resp.data;
            })
        }
    }
</script>

<style scoped>

</style>