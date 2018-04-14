<template>
    <b-container fluid>

            <h1 class="page-header">Profile:
                <small>{{ user_profile.name }} {{ user_profile.surname }} ({{ user_profile.email }})</small>
            </h1>

        <b-row>
            <b-col>
                <b-img v-if="user_profile.img"
                     :src="user_profile.img" fluid>
                </b-img>
                <br>
                <br>
                <ul class="list-group">
                    <li v-if="user_profile.admin"
                        class="list-group-item list-group-item-danger">Admin
                    </li>
                    <li v-if="user_profile.organiser"
                        class="list-group-item list-group-item-warning">
                        Organiser
                    </li>
                    <li v-if="user_profile.mentor"
                        class="list-group-item list-group-item-success">Mentor
                    </li>
                    <li v-if="!(user_profile.mentor || user_profile.admin || user_profile.organiser)"
                        class="list-group-item list-group-item-info">Attendee
                    </li>
                </ul>
<br>
                <h4>Recrutation status:</h4>
                <ul class="list-group">
                    <li v-if="user_profile.accepted && user_profile.confirmation === 'ack'"
                        class="list-group-item list-group-item-success">You
                        confirmed Your arrival !
                    </li>
                    <li v-if="user_profile.accepted && user_profile.confirmation === 'noans'"
                        class="list-group-item list-group-item-danger">You are
                        accepted but You did not confirmed your arrival yet!
                    </li>
                    <li v-if="user_profile.accepted && user_profile.confirmation === 'rej_user'"
                        class="list-group-item list-group-item-warning">You are
                        accepted but You did not confirmed your arrival in time
                        or You rejected the invitation!
                    </li>
                    <li v-if="user_profile.accepted && user_profile.confirmation === 'rejected'"
                        class="list-group-item list-group-item-warning">Sadly You were not chosen, but there maybe a
                        spot open for you later on.
                    </li>
                    <li v-if="!user_profile.accepted && user_profile.confirmation !== 'rejected'"
                        class="list-group-item list-group-item-info">Your
                        registration is complete.
                    </li>
                </ul>
            </b-col>
            <b-col>

                About:
                <ul class="list-group">
                    <li class="list-group-item">
                        <strong>Description: </strong><br>
                        {{ user_profile.description }}
                    </li>
                    <li class="list-group-item">
                        <strong>Motivation: </strong><br>
                        {{ user_profile.motivation }}
                    </li>
                    <li class="list-group-item"
                        v-if="user_profile.app_idea && user_profile.app_idea != 'null'">
                        <strong>app_idea: </strong><br>
                        {{ user_profile.app_idea }}
                    </li>
                    <li class="list-group-item">
                        <strong>What Can you bring and share to eat/drink: </strong><br>
                        {{ user_profile.what_can_you_bring }}
                    </li>
                    <li class="list-group-item"
                        v-if="user_profile.i_helped">
                        <strong>I helped with: </strong><br>
                        {{ user_profile.helped }}
                    </li>
                    <li class="list-group-item">
                        <strong>City: </strong><br>
                        {{ user_profile.city }}
                    </li>
                    <li class="list-group-item">
                        <strong>operating_system: </strong><br>
                        {{ user_profile.operating_system }}
                    </li>
                </ul>
                <ul class="list-unstyled list-inline list-social-icons">
                    <li class="tooltip-social facebook-link"
                        v-if="user_profile.facebook"><a
                            :href="user_profile.facebook"
                            data-toggle="tooltip"
                            data-placement="top"
                            title="Facebook"><i
                            class="fa fa-facebook-square fa-2x"></i></a>
                    </li>
                    <li class="tooltip-social linkedin-link"
                        v-if="user_profile.linkedin && user_profile.linkedin != 'null'"><a
                            :href="user_profile.linkedin"
                            data-toggle="tooltip"
                            data-placement="top"
                            title="LinkedIn"><i
                            class="fa fa-linkedin-square fa-2x"></i></a>
                    </li>
                    <li class="tooltip-social twitter-link"
                        v-if="user_profile.twitter && user_profile.twitter != 'null'"><a
                            :href="user_profile.twitter"
                            data-toggle="tooltip"
                            data-placement="top"
                            title="Twitter"><i
                            class="fa fa-twitter-square fa-2x"></i></a>
                    </li>
                </ul>
            </b-col>
            <b-col>

                <h4>Attendance:</h4>
                <small>{{ user_attendence.amount }}/{{ user_attendence.max }} => {{ user_attendence.perc }}</small>
                <table class="table">
                    <thead>
                    <tr>
                        <th>Lesson</th>
                        <th>Attendance</th>
                    </tr>
                    </thead>

                    <tbody>
                    <tr v-for="atn in user_attendence.data">
                        <td>{{ atn.lesson }}</td>
                        <td>{{ atn.absent ? '&#10003;' : '&#10060;'}}</td>
                    </tr>
                    </tbody>
                </table>


            </b-col>
        </b-row>
    </b-container>
</template>

<script>
    import axios from 'axios'

    export default {
        name: "lessons",
        data() {
            return {
                user_profile: {},
                user_attendence: {}
            }
        },
        created() {
            let self = this;
            let user = self.$store.getters.user;
            axios.get('/users/' + user.id).then(function (resp) {
                    self.user_profile = resp.data
                }
            );
            axios.get('/stats/attendance').then(
                function (response) {
                    self.user_attendence = response.data;
                }
            );
        },
    }
</script>

<style scoped>

</style>