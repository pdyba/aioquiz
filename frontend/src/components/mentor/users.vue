<template>
    <b-container>
        <h1 class="page-header">Mentor: Users</h1>
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
            axios.get('/users/?mentor=False&confirmation=ack&sort_by=surname').then((resp) => {
                self.allUsers = resp.data;
            });
        }
    }
</script>

<style scoped>
</style>