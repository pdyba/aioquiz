<template>
    <span @click.prevent="save_attendence()">Attendance</span>
</template>

<script>
    import axios from 'axios';

    export default {
        name: "attendance",
        methods: {
            save_attendence() {
                let self = this;
                self.$swal({
                    title: 'Attendance',
                    input: 'text',
                    text: 'Please provide lesson code',
                    showCancelButton: true,
                    confirmButtonText: 'Submit',
                    showLoaderOnConfirm: true,
                    allowOutsideClick: true,
                }).then((value) => {
                    axios.put('/attendance', {'code': value.value}).then((response) => {
                        let mtype = "error";
                        if (response.data.success) {
                            mtype = "success";
                        }
                        self.$swal({
                            text: response.data.msg,
                            title: 'Attendance',
                            type: mtype,
                            showConfirmButton: true,
                            timer: 2000
                        });
                    })
                })
            }
        }
    }
</script>

<style scoped>

</style>