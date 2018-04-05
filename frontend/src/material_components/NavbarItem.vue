<template>
    <b-link :to="href" class="nav-link" active-class="active">
        <slot></slot>
    </b-link>
</template>

<script>
    import waves from '../mixins/waves';

    export default {
        props: {
            tag: {
                type: String,
                default: 'li'
            },
            href: {
                type: String,
                default: '#'
            },
            waves: {
                type: Boolean,
                default: false
            },
            wavesFixed: {
                type: Boolean,
                default: false
            }
        },
        mixins: [waves],
    };
</script>

<style scoped>

</style>
