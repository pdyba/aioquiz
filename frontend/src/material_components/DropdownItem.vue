<template>
    <router-link :to="href" class="nav-link">
        <slot></slot>
        <img v-if="src !== null" :src="src" :class="imgClass"/>
    </router-link>
</template>

<script>
    import classNames from 'classnames';

    export default {
        props: {
            tag: {
                type: String,
                default: "a"
            },
            href: {
                type: String,
                default: "#"
            },
            src: {
                type: String,
                default: ""
            },
            imgClass: {
                type: String,
            },
            disabled: {
                type: Boolean,
                default: false
            }
        },
        data() {
            return {
                className: classNames(
                    'dropdown-item',
                    this.disabled ? 'disabled' : ''
                ),
            };
        }
    };
</script>

<style scoped>
    .language-img {
        max-width: 20px;
        max-height: 20px;
    }
    a {
        padding: 4px;
    }
</style>
