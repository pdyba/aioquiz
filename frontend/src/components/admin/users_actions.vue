<template>
    <div v-if="!admin">
        <b-btn size="sm" variant="primary" @click.stop="makeActive()" v-if="!active">Activate</b-btn>
        <b-btn size="sm" variant="warning" @click.stop="makeInactive()" v-if="active">Inactivate</b-btn>
        <b-btn size="sm" variant="outline-primary" @click.stop="newPassword()">New Password</b-btn>
        <b-btn size="sm" variant="success" @click.stop="makeMentor()" v-if="!mentor">Mentor</b-btn>
        <b-btn size="sm" variant="warning" @click.stop="removeMentor()" v-if="mentor">Remove Mentor</b-btn>
        <b-btn size="sm" variant="info" @click.stop="makeOrganiser()" v-if="!org">Make Organiser</b-btn>
        <b-btn size="sm" variant="warning" @click.stop="removeOrganiser()" v-if="org">Remove Organiser</b-btn>
        <b-btn size="sm" variant="danger" @click.stop="deleteUser()">Delete</b-btn>
    </div>
</template>

<script>
    import axios from 'axios';

    export default {
        name: "users_actions",
        data() {
            return {
                show: true
            }
        },
        props: {
            user: {
                type: Object,
                required: true
            }
        },
        computed: {
            admin() {
                return this.user.admin === true
            },
            active() {
                return this.user.active === true
            },
            mentor() {
                return this.user.mentor === true
            },
            org() {
                return this.user.organiser === true
            }
        },
        methods: {
            showResp(atext) {
                this.$swal({
                    text: atext,
                    title: 'Done',
                    type: 'success'
                })
            },
            deleteUser() {
                axios.delete('/users/' + this.user.id).then((resp) => {
                    this.showResp('Deleted')
                });
            },
            makeOrganiser() {
                console.log(this.user)
                let data = {
                    'organiser': true,
                    'uid': this.user.id
                };
                axios.post('/admin/user/set_organiser', data).then((resp) => {
                    if (resp.data.success) {
                        this.user.organiser = true;
                        this.showResp('Made Organiser')
                    }
                });
            },
            removeOrganiser() {
                let data = {
                    'organiser': false,
                    'uid': this.user.id
                };
                axios.post('/admin/user/set_organiser', data).then((resp) => {
                    if (resp.data.success) {
                        this.user.organiser = false;
                        this.showResp('Removed Organiser')
                    }
                });
            },
            newPassword() {
                axios.get('/admin/users/new_password/' + this.user.email).then((resp) => {
                    this.showResp(resp.data.msg)
                })
            },
            makeActive() {
                let data = {
                    'active': true,
                    'uid': this.user.id
                };
                axios.post('/admin/user/set_active', data).then((resp) => {
                    if (resp.data.success) {
                        this.user.active = true;
                        this.showResp('is Active')
                    }
                });
            },
            makeInactive() {
                let data = {
                    'active': false,
                    'uid': this.user.id
                };
                axios.post('/admin/user/set_active', data).then((resp) => {
                    if (resp.data.success) {
                        this.user.active = false;
                        this.showResp('was deactivated')
                    }
                });
            },

            makeMentor() {
                let data = {
                    'mentor': true,
                    'uid': this.user.id
                };
                axios.post('/admin/user/set_mentor', data).then((resp) => {
                    if (resp.data.success) {
                        this.user.mentor = true;
                        this.showResp('is Mentor')
                    }
                });
            },
            removeMentor() {
                let data = {
                    'mentor': false,
                    'uid': this.user.id
                };
                axios.post('/admin/user/set_mentor', data).then((resp) => {
                    if (resp.data.success) {
                        this.user.mentor = false;
                        this.showResp('is no longer a mentor')
                    }
                });
            }
        }
    }
</script>

<style scoped>

</style>