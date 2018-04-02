<template>
  <div :is="tag" :class="'card mb-4 ' + className" ><slot></slot></div>
</template>

<script>
import classNames from 'classnames';

export default {
  props: {
    tag: {
      type: String,
      default: "div"
    },
    cascade: {
      type: Boolean,
      default: false
    }
  },
  data() {
    return {
      className: classNames(
        this.cascade ? 'card-cascade' : 'card'
      ),
    };
  }
};
</script>

<style scoped>
  div {
    min-height: 100%;
  }
</style>
