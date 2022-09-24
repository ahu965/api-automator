<template>
  <div class="api-header">
    <table-form :initData="initData"></table-form>
  </div>
</template>

<script setup>
import { ref } from "vue";
import TableForm from "@/components/TableForm.vue";

const initData = ref([
  {
    key: "name-1",
    value: "18",
    desc: "1111",
  },
]);
</script>

<style scoped></style>
