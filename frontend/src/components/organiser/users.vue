<template>
    <b-container>
        <h1 class="page-header">Organiser: Users</h1>

        <h3>All registered users:</h3>
        <b-table hover small :items="allUsers" :fields="fields_users">
            <template slot="actions" slot-scope="cell">

            </template>
        </b-table>
    </b-container>
</template>

<script>
    import axios from 'axios';

    export default {
        name: "admin_users",
        data: () => {
            return {
                max_abs: 0,
                user_attendence: {},
                allUsers: [],
                fields_users: {
                    name: {
                        sortable: true
                    },
                    surname: {
                        sortable: true
                    },
                    absence: {
                        sortable: true
                    },
                    absence_prc: {
                        sortable: true
                    },
                    exercises: {
                        sortable: true
                    },
                    exercises_prc: {
                        sortable: true
                    },
                    exam: {
                        sortable: true
                    },
                    actions: {},
                }
            }
        },
        created() {
            let self = this;

            function amap(e) {
                if (e.admin) return 'danger';
                if (e.mentor) return 'success';
                if (e.organiser) return 'warning';
                return null

            }

            let uids = [];
            axios.get('/users?gdpr=true&mentor=false&admin=false&organiser=false').then((resp) => {
                resp.data.forEach(function (e) {
                    e._rowVariant = amap(e);
                    uids.push(e.id)
                });
                axios.post('/stats/attendance', uids).then(
                    function (response) {
                        self.max_abs = response.data.max_absences;
                        self.absence = response.data.absences;

                        axios.post('/stats/exercises', uids).then(
                            function (response) {
                                self.max_exercises = response.data.max_exercises;
                                self.exercises = response.data.exercises;

                                axios.post('/stats/exam', uids).then(
                                    function (response) {
                                        self.exams = response.data.exams;


                                        resp.data.forEach(function (e) {
                                            e.absence = self.absence[e.id];
                                            e.exam = self.exams[e.id];
                                            e.exercises = self.exercises[e.id];
                                            e.absence_prc = self.absence[e.id] / self.max_abs * 100;
                                            e.exercises_prc = self.exercises[e.id] / self.max_exercises * 100;
                                        });
                                    });
                            });
                    });
                self.allUsers = resp.data;
            });
        }
    }
</script>

<style scoped>
</style>