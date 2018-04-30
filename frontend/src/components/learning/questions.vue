<template>
    <div>
        <b-card no-body>
            <b-tabs pills card vertical>
                <b-tab v-for="quest in questions" :key="quest.id">
                    <template slot="title">
                        {{ quest.question_order }} <i class="fa fa-check-circle ml-2" v-if="quest.answered"></i>
                    </template>
                    <question :question="quest.question_details" :test-type="testType" :testid="testid"> </question>
                </b-tab>
            </b-tabs>
        </b-card>
    </div>
</template>

<script>
    import question from "./question.vue"

    export default {
        name: "questions",
        components: {
            question
        },
        props: {
            questions: {
                type: Array,
                required: true
            },
            testType: {
                type: String,
                required: true
            },
            testid: {
                type: Number,
                required: true
            }
        }
    }
</script>

<style scoped>

</style>