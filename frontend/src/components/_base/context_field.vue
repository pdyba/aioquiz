<template>
    <dropdown-item @click="setEventContext(event.id)">
        {{ event.id }}: {{ event.title }}
    </dropdown-item>
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
                console.log(event_id);
                // this.$store.dispatch('storeEventContext', event_id);

            },
        },
        computed: {
            current_context() {
                console.log(this.$store.getters.context);
                return this.$store.getters.context
            }
        }
    }
</script>

<style scoped>
    .red {
        color: red;
    }
</style>