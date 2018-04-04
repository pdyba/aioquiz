<template>
    
</template>

<script>
    export default {
        name: "magic_link_handler",
        ml = $routeParams.ml;
    AuthenticationService.ClearCredentials();
    $http.get('/api/auth/magic_link/' + ml).then(function (response) {
        if (response.data.success) {
            AuthenticationService.SetCredentials(response.data, response.data.session_uuid);
            SweetAlert.swal({
                text: "Logged in sucesfully",
                title: 'Logged in',
                type: 'success',
                showConfirmButton: true,
                timer: 1000
            });
        } else {
            SweetAlert.swal({
                text: response.data.msg,
                title: 'Error using Magic link login',
                type: 'error',
                showConfirmButton: true
            });
        }
    });
    }
</script>

<style scoped>

</style>