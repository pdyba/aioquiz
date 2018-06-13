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
                    email: {
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
                    intern: {
                        sortable: true
                    },
                    intern_why: {
                        sortable: true
                    },
                    intern_1: {
                        sortable: true
                    },
                    intern_2: {
                        sortable: true
                    },
                    intern_3: {
                        sortable: true
                    },
                    intern_details: {
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
                                        self.intern = response.data.intern;
                                        resp.data.forEach(function (e) {
                                            e.absence = self.absence[e.id];
                                            e.exam = self.exams[e.id];
                                            if (self.intern[e.id]) {
                                                e.intern = self.intern[e.id].intern;
                                                e.intern_why = self.intern[e.id].why;
                                                e.intern_1 = self.intern[e.id]["1"];
                                                e.intern_2 = self.intern[e.id]["2"];
                                                e.intern_3 = self.intern[e.id]["3"];
                                                e.intern_details = self.intern[e.id].details;
                                            }
                                            e.exercises = self.exercises[e.id];
                                            e.absence_prc = Math.ceil(self.absence[e.id] / self.max_abs * 100);
                                            e.exercises_prc = Math.ceil(self.exercises[e.id] / self.max_exercises * 100);
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