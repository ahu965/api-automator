<template>
  <div class="api-header">
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

<style scoped></style>
