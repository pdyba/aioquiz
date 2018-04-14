<template>
    <b-form @submit.prevent="update_user" class="signup-form">
        <user-edit :user="user"></user-edit>
        <b-row>
            <b-col>
                <b-btn type="submit">Update</b-btn>
            </b-col>
            <b-col>
                <b-btn @click.prevent="change_password" variant="warning">Change Password</b-btn>
            </b-col>
            <b-col>
                <b-btn @click.prevent="remove_accout" variant="outline-danger">Delete Account</b-btn>
            </b-col>
        </b-row>
    </b-form>
</template>

<script>
    import axios from 'axios'
    import UserEdit from "./_profile_edit.vue";

    export default {
        name: "ProfileEdit",
        data() {
            return {
                user: {},
            }
        },
        components: {
            UserEdit
        },
        created() {
            let self = this;
            let user = self.$store.getters.user;
            axios.get('/users/' + user.id).then(function (resp) {
                    self.user = resp.data
                }
            );
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
                    this.showResp(resp.data.msg)
                });
            },
            update_user() {
                let self = this;
                axios.put('/users/', this.user).then(function (resp) {
                    self.$swal({
                        title: resp.data.msg,
                        type: 'success'
                    })
                });
            },
            remove_accout() {
                let self = this;
                self.$swal({
                    title: "Delete account",
                    type: "warning",
                    text: "Are You sure You want to delete your account",
                    showCancelButton: true,
                    confirmButtonText: "Yes",
                    cancelButtonText: "No",
                    showLoaderOnConfirm: true,
                    allowOutsideClick: true,
                }).then((value) => {
                    console.log(value)
                    if (value.value === true) {
                        axios.delete('/users/' + this.user.id).then((response) => {
                            self.$swal({
                                text: response.data.msg,
                                title: 'Account Deleted',
                                type: "info",
                                showConfirmButton: true,
                                timer: 2000
                            })
                            self.$store.dispatch('logout')
                        })
                    } else {
                        self.$swal({
                            text: "Thanks for trusting in us",
                            title: 'Cancleation',
                            type: 'success',
                            showConfirmButton: true,
                            timer: 3000
                        });
                    }
                })
            },


            change_password() {
                let self = this;
                let change_pass = {};
                self.$swal({
                    title: "Change Password",
                    input: 'password',
                    text: "Please provide current password",
                    showCancelButton: true,
                    confirmButtonText: "Next",
                    cancelButtonText: "Cancel",
                    showConfirmButton: true,
                    closeOnCancel: false,
                    closeOnConfirm: false
                }).then(function (oldpassword) {
                    change_pass.password = oldpassword;
                    self.$swal({
                        title: "Change Password",
                        input: 'password',
                        text: "Please provide new password",
                        showCancelButton: true,
                        confirmButtonText: "Next",
                        cancelButtonText: "Cancel",
                        showConfirmButton: true,
                        closeOnCancel: false,
                        closeOnReject: false,
                        closeOnConfirm: false
                    }).then( function (new_password) {
                        change_pass.new_password = new_password;
                        self.$swal({
                            title: "Change Password",
                            input: 'password',
                            text: "Please provide new password again",
                            showCancelButton: true,
                            confirmButtonText: "Change",
                            cancelButtonText: "Cancel",
                            showConfirmButton: true,
                            closeOnCancel: false,
                            closeOnConfirm: false,
                            closeOnReject: false
                        }).then( function (new_password_2) {
                            change_pass.new_password_2 = new_password_2;
                            axios.post('user/password_change', change_pass).then(function (response) {
                                if (response.data.success) {
                                    self.$swal({
                                        text: response.data.msg,
                                        title: 'Password Change',
                                        type: 'success',
                                        showConfirmButton: true,
                                        timer: 2000
                                    });
                                } else {
                                    self.$swal({
                                        text: response.data.msg,
                                        title: 'Password Change',
                                        type: 'error',
                                        showConfirmButton: true,
                                        timer: 2000
                                    });
                                }
                            });
                        })
                    })
                })
            }
        }
    }
</script>

<style scoped>

</style>