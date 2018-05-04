<template>
    <b-container>
        <h1 class="page-header">{{ testName }}: {{  checkEditCreate() ? 'Create' : 'Edit' }}</h1>
        <b-form>
            <b-row>
                {{ testData.title }}
                {{ testData.description }}
                <b-col sm="6">
                    <h4>Quiz Questions</h4>
                    <draggable class="list-group" element="ul" v-model="testData.all_questions" :options="dragOptions" :move="onMove"
                               @start="isDragging=true" @end="isDragging=false">
                        <transition-group type="transition" :name="'flip-list'">
                            <li class="list-group-item" v-for="element in testData.all_questions" :key="element.question_order">
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
                    <draggable element="span" v-model="available_questions" :options="dragOptions" :move="onMove">
                        <transition-group name="no" class="list-group" tag="ul">
                            <li class="list-group-item" v-for="element in available_questions" :key="element.order">
                                <i :class="element.fixed? 'fa fa-anchor' : 'glyphicon glyphicon-pushpin'"
                                   @click=" element.fixed=! element.fixed" aria-hidden="true"></i>
                                {{ element.name }}
                            </li>
                        </transition-group>
                    </draggable>
                </b-col>
            </b-row>
            <b-btn size="sm" v-if="checkEditCreate()">Create</b-btn>
            <b-btn size="sm" v-else>Update</b-btn>
        </b-form>
        {{ testData }}
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
                available_questions: [],
                editable: true,
                isDragging: false,
                delayedDragging: false
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
            testData: {
                type: Object,
                required: false,
                default: function () { return {} }
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
                return Object.keys(this.testData).length === 0
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
        min-height: 20px;
    }

    .list-group-item {
        cursor: move;
    }

    .list-group-item i {
        cursor: pointer;
    }
</style>