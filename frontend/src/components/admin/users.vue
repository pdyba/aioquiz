<template>
    <div class="container">
        <div class="row">
            <div class="col-lg-12">
                <h1 class="page-header">Admin
                </h1>
            </div>


            <h3>Stats</h3>

            <div class="table-responsive">
                <table class="table">
                    <thead>
                    <tr>
                        <th>Type</th>
                        <th>Count</th>
                    </tr>
                    </thead>

                    <tbody>
                    <tr v-for="(user, count) in users_stats"
                        v-class="{'danger': user === 'admins', 'success': ['mentors', 'confirmed'].indexOf(user) !== -1, 'warning': ['organisers', 'accepted'].indexOf(user) !== -1, 'info': user === 'attendees'}">
                        <td>{{ user }}</td>
                        <td>{{ count }}</td>
                    </tr>
                    </tbody>
                </table>
            </div>

            <h3>All registered users x:</h3>
            <div class="table-responsive">
                <table class="table">
                    <thead>
                    <tr>
                        <th>ID</th>
                        <th>E-mail</th>
                        <th>Name</th>
                        <th>Surname</th>
                        <th>Active</th>
                        <th>Delete</th>
                        <th>Make Organiser</th>
                        <th>Make Mentor</th>
                        <th>New Password</th>
                    </tr>
                    </thead>

                    <tbody>
                    <tr v-for="user in allUsers"
                        v-class="{'danger': user.admin, 'success': user.mentor, 'warning': user.organiser, 'info': !user.mentor}">
                        <td>{{ user.id }}</td>
                        <td>{{ user.email }}</td>
                        <td>{{ user.name }}</td>
                        <td>{{ user.surname }}</td>
                        <td v-if="!user.active"><a v-click="makeActive(user)"
                                                   class="btn btn-xs btn-success">Make Active</a></td>
                        td>
                        <td v-if="user.active && !user.admin"><a v-click="makeInactive(user)"
                                                                 class="btn btn-xs btn-danger">Deactivate</a></td>
                        td
                        <td v-if="user.admin">Yeah</td>
                        <td><a v-hide="user.admin" v-click="deleteUser(user.id)"
                               class="btn btn-xs btn-danger">Delete</a>
                            <x v-show="user.admin">Nope</x>
                        </td>
                        <td><a v-if="!user.admin" v-show="!user.organiser" v-click="makeOrganiser(user)"
                               class="btn btn-xs btn-primary">Make Organiser</a>
                            <a v-hide="user.admin || !user.organiser" v-show="user.organiser"
                               v-click="removeOrganiser(user)"
                               class="btn btn-xs btn-danger">Remove Organiser</a>
                            <x v-show="user.admin">Nope</x>

                        <td><a v-hide="user.mentor || user.admin" v-click="makeMentor(user)"
                               class="btn btn-xs btn-info">Make Mentor</a>
                            <a v-show="user.mentor && !user.admin" v-click="removeMentor(user)"
                               class="btn btn-xs btn-info">Remove Mentor</a>
                            <x v-show="user.admin">Nope</x>
                        </td>
                        <td>
                            <a v-show="!user.admin" v-click="newPassword(user)"
                               class="btn btn-xs btn-info">NewPass</a>
                            <x v-show="user.admin">Nope</x>
                        </td>
                    </tr>
                    </tbody>
                </table>
            </div>

        </div>
    </div>

</template>

<script>
    export default {
        name: "admin_users",
        data: () => {
            return {
                allUsers: {},
                users_stats: {}
            }
        }
    }
</script>

<style scoped>

</style>