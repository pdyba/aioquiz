<template>
    <div class="col-lg-4 col-md-4">
        <h3>{{ sponsor.name }}</h3>
        <br>
        <b-img fluid class="img-responsive"
               :src="sponsor.logo"></b-img>
        <br>
        <p class="text-justify">
            {{ sponsor.description }}
            <br>
            <a :href="sponsor.webpage">{{ sponsor.name }}</a>
        <ul class="list-unstyled list-inline list-social-icons">
            <li class="tooltip-social facebook-link"
                v-if="sponsor.facebook"><a
                    href=" user.facebook "
                    data-toggle="tooltip"
                    data-placement="top"
                    title="Facebook"><i
                    class="fa fa-facebook-square fa-2x"></i></a>
            </li>
            <li class="tooltip-social linkedin-link"
                v-if="sponsor.linkedin"><a
                    href=" user.linkedin "
                    data-toggle="tooltip"
                    data-placement="top"
                    title="LinkedIn"><i
                    class="fa fa-linkedin-square fa-2x"></i></a>
            </li>
            <li class="tooltip-social twitter-link"
                v-if="sponsor.twitter"><a href=" user.twitter "
                                          data-toggle="tooltip"
                                          data-placement="top"
                                          title="Twitter"><i
                    class="fa fa-twitter-square fa-2x"></i></a>
            </li>
        </ul>
        </p>
    </div>
</template>

<script>
    export default {
        name: "sponsor-desc",
        props: {
            sponsor: {
                type: Object,
                required: true
            }
        }
    }
</script>

<style scoped>

</style>