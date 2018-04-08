<template>
    
</template>

<script>
    import axios from 'axios'

    export default {
        name: "magic_link_handler",
        created() {
            let self = this;
            let ml = self.$route.query.ml;
            axios.get('/auth/magic_link/' + ml).then(function (response) {
                if (response.data.success) {
                    self.$store.dispatch('loginUser', response.data);
                    self.$swal({
                        text: "Logged in successfully",
                        title: 'Logged in',
                        type: 'success',
                        showConfirmButton: true,
                        timer: 2000
                    });
                } else {
                    self.$swal({
                        text: response.data.msg,
                        title: 'Error using Magic link login',
                        type: 'error',
                        showConfirmButton: true
                    });
                }
            });
        }
    }
</script>

<style scoped>

</style>