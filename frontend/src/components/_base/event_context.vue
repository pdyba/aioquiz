<template>
    <dropdown tag="li" class="nav-item">
        <dropdown-toggle tag="a" navLink color="indigo">Event Context</dropdown-toggle>
        <dropdown-menu>
            <context-field :event="event" v-for="event in events" :key="event.id"></context-field>
        </dropdown-menu>
    </dropdown>
</template>

<script>
    import axios from 'axios'

    import Dropdown from '../common_components/Dropdown.vue';
    import DropdownMenu from '../common_components/DropdownMenu.vue';
    import DropdownToggle from '../common_components/DropdownToggle.vue';
    import ContextField from './context_field.vue';

    export default {
        name: "event-context-picker",
        data() {
            return {
                events: []
            }
        },
        components: {
            DropdownMenu,
            DropdownToggle,
            Dropdown,
            ContextField
        },
        beforeMount() {
            axios.get('/events').then(resp => {
                this.events = resp.data
            });
        }
    }
</script>

<style scoped>

</style>