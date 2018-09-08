<template>
    <b-link @click.prevent="setEventContext(event.id)" :class="['nav-link', current_context === event.id ? 'red':'']"><slot>{{ event.id }}: {{ event.title }}</slot></b-link>
</template>

<script>
    import dropdownItem from '../common_components/DropdownItem.vue';

    export default {
        name: "context-field",
        props: {
            event: {
                type: Object,
                required: true
            }
        },
        components: {
            dropdownItem,
        },
        methods: {
            setEventContext(event_id) {
                this.$store.dispatch('storeEventContext', event_id);

            },
        },
        computed: {
            current_context() {
                return this.$store.getters.context
            }
        }
    }
</script>

<style scoped>
    .red {
        color: red;
    }
    a {
        padding: 3px;
        max-height: 2rem;
    }
</style>