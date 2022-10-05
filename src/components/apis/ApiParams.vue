<template>
  <div class="api-params">
    <table-form :initData="apiRequest.reqParams"></table-form>
  </div>
</template>

<script setup>
import TableForm from "@/components/TableForm.vue";
import {useApiRequestStore} from "@/stores/api";

const apiRequest = useApiRequestStore();

</script>

<style lang="scss">
.api-params {
}
</style>
