<template>
    <b-container>
        <h1 class="page-header">Admin: Users</h1>
        <h3>All registered users:</h3>
        <b-table hover small :items="allUsers" :fields="fields_users">
        </b-table>
    </b-container>
</template>

<script>
    import axios from 'axios';
    export default {
        name: "mentor_users",
        data: () => {
            return {
                allUsers: [],
                users_stats: [],
                fields_users: {
                    id: {
                        sortable: true
                    },
                    name: {
                        sortable: true
                    },
                    surname: {
                        sortable: true
                    }
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
            axios.get('/users/?mentor=False&confirmation=ack&sort_by=surname').then((resp) => {
                resp.data.forEach(function (e) {
                    e._rowVariant = amap(e)
                });
                self.allUsers = resp.data;
            });
        }
    }
</script>

<style scoped>
</style>