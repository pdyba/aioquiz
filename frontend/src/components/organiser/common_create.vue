<template>
    <b-container>
        <h1 class="page-header">{{ testName }}: {{ checkCreate ? 'Create' : 'Edit' }}</h1>
        <b-form>
            <b-row>
                <b-col sm="12">

                    <b-form-group>
                        <label>Title</label>
                        <b-form-input v-model="testData.title">
                        </b-form-input>
                    </b-form-group>

                    <b-form-group>
                        <label>Description</label>
                        <b-form-textarea
                                v-model="testData.description "
                                placeholder="Enter something"
                                :rows="4"
                                :max-rows="9">
                        </b-form-textarea>
                    </b-form-group>

                </b-col>
                <b-col sm="6">
                    <h4>Quiz Questions</h4>
                    <draggable class="list-group" element="ul" v-model="testData.all_questions" :options="dragOptions"
                               :move="onMove"
                               @start="isDragging=true" @end="isDragging=false">
                        <transition-group type="transition" :name="'flip-list'">
                            <li class="list-group-item" v-for="element in testData.all_questions"
                                :key="element.question_details.id">
                                <b-badge>{{element.question_order}}</b-badge>
                                <i :class="element.fixed? 'fa fa-anchor' : 'glyphicon glyphicon-pushpin'"
                                   @click=" element.fixed=! element.fixed" aria-hidden="true"></i>
                                {{ element.question_details.question }}
                            </li>
                        </transition-group>
                    </draggable>


                </b-col>
                <b-col sm="6">
                    <h4>Available questions</h4>
                    <draggable element="span" v-model="unused_questions" :options="dragOptions" :move="onMove">
                        <transition-group name="no" class="list-group" tag="ul">
                            <li class="list-group-item" v-for="element in unused_questions"
                                :key="element.question_details.id">
                                <i :class="element.fixed? 'fa fa-anchor' : 'glyphicon glyphicon-pushpin'"
                                   @click=" element.fixed=! element.fixed" aria-hidden="true"></i>
                                {{ element.question_details.question }}
                            </li>
                        </transition-group>
                    </draggable>
                </b-col>
            </b-row>
            <b-btn size="sm" v-if="checkCreate" @click="createNewTest()">Create</b-btn>
            <b-btn size="sm" v-else @click="updateTest()">Update</b-btn>
        </b-form>
    </b-container>
</template>

<script>
    import axios from 'axios';
    import draggable from 'vuedraggable';

    export default {
        name: "commonCreate",
        components: {
            draggable
        },
        data() {
            return {
                editable: true,
                isDragging: false,
                delayedDragging: false,
                createTest: true
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
            unused_questions: {
                type: Array,
                required: false,
                default: function () {
                    return []
                }
            },
            testData: {
                type: Object,
                required: false,
                default: function () {
                    return {all_questions: [{question_details: {question: 'remove me', id: 1}}]}
                }
            }
        },
        computed: {
            dragOptions() {
                return {
                    animation: 0,
                    group: 'description',
                    disabled: !this.editable,
                    ghostClass: 'ghost'
                };
            },
            checkCreate() {
                return this.createTest
            }
        },
        watch: {
            isDragging(newValue) {
                if (newValue) {
                    this.delayedDragging = true
                    return
                }
                this.$nextTick(() => {
                    this.delayedDragging = false
                })
            }
        },
        methods: {
            onMove({relatedContext, draggedContext}) {
                const relatedElement = relatedContext.element;
                const draggedElement = draggedContext.element;
                return (!relatedElement || !relatedElement.fixed) && !draggedElement.fixed
            },
            checkEditCreate() {
                return Object.keys(this.testData).length === 1
            },
            createNewTest() {
                let self = this;
                axios.post('/organiser/' + self.testType  + 's', self.testData).then((resp) => {
                    this.$swal('Done', self.testType + " created \n msg: \n" + resp.data.msg, "success")
                })
            },
            updateTest() {
                let self = this;
                axios.put('/organiser/' + self.testType + 's', self.testData).then((resp) => {
                        this.$swal('Done', self.testType + " updated \n msg: \n" + resp.data.msg, "success")
                    }
                )
            }
        },
        created() {
            let self = this;
            if (self.checkEditCreate()) {
                axios.get('/organiser/' + self.testType + 's/1').then((resp) => {
                    self.unused_questions = resp.data.unused_questions;
                })
            } else {
                self.createTest = false
            }
        }
    }
</script>

<style scoped>
    .flip-list-move {
        transition: transform 0.5s;
    }

    .no-move {
        transition: transform 0s;
    }

    .ghost {
        opacity: .5;
        background: #C8EBFB;
    }

    .list-group {
        min-height: 50px;
    }

    .list-group-item {
        cursor: move;
    }

    .list-group-item i {
        cursor: pointer;
    }
</style>