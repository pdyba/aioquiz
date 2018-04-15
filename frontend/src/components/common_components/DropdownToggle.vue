<template>
    <b-link class="nav-link" active-class="active">
        <slot></slot>
    </b-link>
</template>

<script>
    import classNames from 'classnames';
    import waves from '../mixins/waves';

    export default {
        props: {
            tag: {
                type: String,
                default: "button"
            },
            navLink: {
                type: Boolean,
                default: false
            },
            color: {
                type: String,
                default: "default"
            },
            outline: {
                type: String,
            },
            size: {
                type: String
            },
            block: {
                type: Boolean,
                default: false
            },
            active: {
                type: Boolean,
                default: false
            },
            disabled: {
                type: Boolean,
                default: false
            },
            waves: {
                type: Boolean,
                default: false
            },
            wavesFixed: {
                type: Boolean,
                default: false
            },
            srOnly: {
                type: Boolean,
                default: false
            }
        },
        data() {
            return {
                className: classNames(
                    this.navLink ? 'nav-link' : 'btn',
                    this.outline ? 'btn-outline-' + this.outline : 'btn-' + this.color,
                    this.size ? 'btn-' + this.size : '',
                    this.block ? 'btn-block' : '',
                    this.active ? 'active' : '',
                    this.disabled ? 'disabled' : '',
                    'dropdown-toggle'
                ),
            };
        },
        mixins: [waves]
    };
</script>

<style scoped>

</style>
