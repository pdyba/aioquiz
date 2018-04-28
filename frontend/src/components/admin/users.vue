<template>
    <b-container>
        <h1 class="page-header">Admin: Users</h1>
        <h3>Stats</h3>
        <b-table hover small :items="users_stats" :fields="fields_stats">
        </b-table>

        <h3>All registered users:</h3>
        <b-table hover small :items="allUsers" :fields="fields_users">
            <template slot="actions" slot-scope="cell">
                <usersActions :user="cell.item"></usersActions>
            </template>
        </b-table>
    </b-container>
</template>

<script>
    import axios from 'axios';
    import usersActions from "./users_actions.vue";

    export default {
        name: "admin_users",
        data: () => {
            return {
                allUsers: [],
                users_stats: [],
                fields_stats: {
                    0: {
                        label: 'user',
                        sortable: true
                    },
                    1: {
                        label: 'amount',
                        sortable: true
                    }
                },
                fields_users: {
                    id: {
                        sortable: true
                    },
                    email: {
                        sortable: true
                    },
                    name: {
                        sortable: true
                    },
                    surname: {
                        sortable: true
                    },
                    actions: {},
                }
            }
        },
        components: {
            usersActions,
        },
        created() {
            let self = this;

            function amap(e) {
                if (e.admin) return 'danger';
                if (e.mentor) return 'success';
                if (e.organiser) return 'warning';
                return null

            }
            axios.get('/users/').then((resp) => {
                resp.data.forEach(function (e) {
                    e._rowVariant = amap(e)
                });
                self.allUsers = resp.data;
            });
            axios.get('/users_stats').then((resp) => {
                self.users_stats = Object.keys(resp.data).map(function (key) {
                    return [key, resp.data[key]];
                });
            });
        }
    }
</script>

<style scoped>
</style>