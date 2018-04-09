<template>
    <container>
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
        <!--<div class="table-responsive">-->
        <!--<table class="table">-->
        <!--<thead>-->
        <!--<tr>-->
        <!--<th>ID</th>-->
        <!--<th>E-mail</th>-->
        <!--<th>Name</th>-->
        <!--<th>Surname</th>-->
        <!--<th>Active</th>-->
        <!--<th>Delete</th>-->
        <!--<th>Make Organiser</th>-->
        <!--<th>Make Mentor</th>-->
        <!--<th>New Password</th>-->
        <!--</tr>-->
        <!--</thead>-->

        <!--<tbody>-->
        <!--<tr v-for="user in allUsers"-->
        <!--v-class="{'danger': user.admin, 'success': user.mentor, 'warning': user.organiser, 'info': !user.mentor}">-->
        <!--<td>{{ user.id }}</td>-->
        <!--<td>{{ user.email }}</td>-->
        <!--<td>{{ user.name }}</td>-->
        <!--<td>{{ user.surname }}</td>-->
        <!--<td v-if="!user.active"><a v-click="makeActive(user)"-->
        <!--class="btn btn-xs btn-success">Make Active</a></td>-->
        <!--td>-->
        <!--<td v-if="user.active && !user.admin"><a v-click="makeInactive(user)"-->
        <!--class="btn btn-xs btn-danger">Deactivate</a></td>-->
        <!--td-->
        <!--<td v-if="user.admin">Yeah</td>-->
        <!--<td><a v-hide="user.admin" v-click="deleteUser(user.id)"-->
        <!--class="btn btn-xs btn-danger">Delete</a>-->
        <!--<x v-show="user.admin">Nope</x>-->
        <!--</td>-->
        <!--<td><a v-if="!user.admin" v-show="!user.organiser" v-click="makeOrganiser(user)"-->
        <!--class="btn btn-xs btn-primary">Make Organiser</a>-->
        <!--<a v-hide="user.admin || !user.organiser" v-show="user.organiser"-->
        <!--v-click="removeOrganiser(user)"-->
        <!--class="btn btn-xs btn-danger">Remove Organiser</a>-->
        <!--<x v-show="user.admin">Nope</x>-->

        <!--<td><a v-hide="user.mentor || user.admin" v-click="makeMentor(user)"-->
        <!--class="btn btn-xs btn-info">Make Mentor</a>-->
        <!--<a v-show="user.mentor && !user.admin" v-click="removeMentor(user)"-->
        <!--class="btn btn-xs btn-info">Remove Mentor</a>-->
        <!--<x v-show="user.admin">Nope</x>-->
        <!--</td>-->
        <!--<td>-->
        <!--<a v-show="!user.admin" v-click="newPassword(user)"-->
        <!--class="btn btn-xs btn-info">NewPass</a>-->
        <!--<x v-show="user.admin">Nope</x>-->
        <!--</td>-->
        <!--</tr>-->
        <!--</tbody>-->
        <!--</table>-->
        <!--</div>-->

    </container>
</template>

<script>
    import axios from 'axios';
    import Container from '../../material_components/Container.vue';
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
            Container,
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
                console.log(self.allUsers)
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