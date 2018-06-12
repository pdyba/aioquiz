<template>
    <b-col sm="4">
        <b-img fluid class="img-responsive" :src="user.img"
               v-if="user.img">
        </b-img>
        <h3>{{ user.name }} {{ user.surname }}<br>
            <small v-if="user.admin">
                Admin, {{ user.pyfunction }}
            </small>
            <br>
        </h3>
        <p>{{ user.description }}</p>
        <ul class="list-unstyled list-inline list-social-icons">
            <li class="tooltip-social facebook-link"
                v-if="user.facebook"><a
                    href=" user.facebook "
                    data-toggle="tooltip"
                    data-placement="top"
                    title="Facebook"><i
                    class="fa fa-facebook-square fa-2x"></i></a>
            </li>
            <li class="tooltip-social linkedin-link"
                v-if="user.linkedin"><a
                    href=" user.linkedin "
                    data-toggle="tooltip"
                    data-placement="top"
                    title="LinkedIn"><i
                    class="fa fa-linkedin-square fa-2x"></i></a>
            </li>
            <li class="tooltip-social twitter-link"
                v-if="user.twitter"><a href=" user.twitter "
                                       data-toggle="tooltip"
                                       data-placement="top"
                                       title="Twitter"><i
                    class="fa fa-twitter-square fa-2x"></i></a>
            </li>
        </ul>
    </b-col>
</template>

<script>
    export default {
        name: "short_user_profile",
        props: {
            user: {
                type: Object,
                required: true
            }
        }
    }
</script>

<style scoped>

</style>