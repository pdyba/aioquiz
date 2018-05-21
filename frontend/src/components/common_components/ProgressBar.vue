<template>
    <div :is="tag" :class="className" role="progressbar" :style="'width: ' + value + '%'" :aria-valuenow="value"
         aria-valuemin="0" aria-valuemax="100">
        <slot></slot>
    </div>
</template>

<script>
    import classNames from 'classnames';

    export default {
        props: {
            tag: {
                type: String,
                default: "div"
            },
            value: {
                type: Number,
                default: 0
            },
            striped: {
                type: Boolean,
                default: false
            },
            animated: {
                type: Boolean,
                default: true
            }
        },
        data() {
            return {};
        },
        computed: {
            color() {
                if (this.value <= 25) {
                    return "bg-danger"
                } else if (this.value <= 50) {
                    return "bg-warning"
                } else if (this.value <= 75) {
                    return 'bg-info'
                } else {
                    return 'bg-success'
                }
            },
            className() {
                return classNames(
                    'progress-bar',
                    this.striped ? 'progress-bar-striped' : '',
                    this.color,
                    this.animated ? 'progress-bar-animated' : '',
                    'w-' + this.value
                )
            },
        }
    };
</script>

<style scoped>
</style>
