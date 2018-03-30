<template>
    <a :is="tag" :href="href" :class="className">
        <slot></slot>
        <img v-if="src" :src="src" :class="imgClass"/></a>
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
                default: "#"
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
</style>
