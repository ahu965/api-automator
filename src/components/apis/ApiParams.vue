<template>
  <div class="api-params">
    <table-form :initData="initData"> </table-form>
  </div>
</template>

<script setup>
import { ref, defineExpose } from "vue";
import TableForm from "@/components/TableForm.vue";

const initData = ref([]);

const getData = () => {
  return initData.value;
};
defineExpose({
  getData,
});
</script>

<style lang="scss">
.api-params {
}
</style>
