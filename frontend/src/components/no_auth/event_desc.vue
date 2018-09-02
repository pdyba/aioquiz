<template>
    <b-row>
        <b-col sm="3">
            <h4>{{ event.city }}</h4>
            <h5><b v-if="event.start_date < new Date()">Startujemy już</b><b v-else>Wystartowaliśmy </b> {{ event.start_date | moment("calendar") }} !</h5>
        </b-col>
        <b-col sm="3">
            <b-img fluid class="img-responsive" :src="event.address_picture">
            </b-img>
        </b-col>
        <b-col sm="5">
            <p>{{ event.description }}</p>
            <p v-if="event.reg_active">Zapisy trwają od {{ event.registration_start_date | moment("calendar") }} do {{ event.registration_end_date | moment("calendar") }}</p>
            <p v-else>Zapisy już się zakończyły</p>
            <b-btn>Zapisz mnie</b-btn>
            <!--<b-btn>Więcej szczegółów</b-btn>-->
        </b-col>
    </b-row>
</template>

<script>
    export default {
        name: "event-desc",
        props: {
            event: {
                type: Object,
                required: true
            }
        }
    }
</script>

<style scoped>

</style>