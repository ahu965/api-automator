<template>
  <div class="api-header">
    <table-form :initData="apiRequest.reqHeaders"></table-form>
  </div>
</template>

<script setup>
import TableForm from "@/components/TableForm.vue";
import {useApiRequestStore} from "@/stores/api";

const apiRequest = useApiRequestStore();
</script>

<style scoped></style>
