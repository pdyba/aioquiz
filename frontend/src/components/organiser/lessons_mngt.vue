<template>
    <b-container>
        <h1 class="page-header">Lessons: Management</h1>
        <b-table :items="lessons" :fields="fields">
            <template slot="Management" slot-scope="cell">
                <b-btn size="sm" variant="primary" @click.stop="activate(cell.item.id)" v-if="!cell.item.active">Activate</b-btn>
                <b-btn size="sm" variant="danger" @click.stop="deactivate(cell.item.id)" v-if="cell.item.active">Deactivate</b-btn>
                <b-btn size="sm" variant="success" @click.stop="attendance(cell.item.id)">Attendance</b-btn>
                <b-btn size="sm" variant="outline-success" @click.stop="extend(cell.item.id)">Extend</b-btn>
            </template>
        </b-table>
    </b-container>
</template>

<script>
    import axios from 'axios';

    export default {
        name: "lessons_mngt",
        data() {
            return {
                lessons: [],
                fields: [
                    'id',
                    'title',
                    'active',
                    'Management'
                ],
            }
        },
        created() {
            let self = this;
            axios.get('/lessons').then(
                function (response) {
                    self.lessons = response.data;
                }
            );
        },
        computed: {},
        methods: {
            activate(lid) {
            },
            deactivate(lid) {
            },
            attendance(lid) {
                let self = this;
                axios.get('/attendance/' + lid).then(
                    function (response) {
                        self.$swal({
                            title: "Lesson Code",
                            type: "success",
                            html: "<h1>" + response.data.code + "</h1><h3><br>will expire at:<br>" + response.data.time_ended + "</h3>",
                        })
                    }
                );
            },
            extend(lid) {
                let self = this;
                axios.post('/attendance/' + lid, {}).then(
                    function (response) {
                        self.$swal({
                            title: "Lesson Code",
                            html: "<h1>" + response.data.code + "</h1><h3><br>will expire at:<br>" + response.data.time_ended + "</h3>",
                            type: "success",
                        })
                    }
                );
            },
            show_attendance(lid) {
            }
        }
    }
</script>

<style scoped>

</style>