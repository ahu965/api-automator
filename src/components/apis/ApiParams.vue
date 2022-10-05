<template>
  <div class="api-params">
    <table-form :initData="initData"></table-form>
  </div>
</template>

<script setup>
// import { defineExpose } from "vue";
import TableForm from "@/components/TableForm.vue";

const props = defineProps({
  initData: {
    type: Array,
  },
});

const getData = () => {
  return props.initData;
};
defineExpose({
  getData,
});
</script>

<style lang="scss">
.api-params {
}
</style>
