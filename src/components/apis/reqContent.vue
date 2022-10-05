<template>
  <div class="req-content">
    <api-coder :lang="'json'" :initHeight="'250px'" :content="apiResponse.reqContent"></api-coder>
  </div>
</template>

<script setup>
import ApiCoder from "@/components/ApiCoder.vue";
import {useApiResponseStore} from "@/stores/api";
const apiResponse = useApiResponseStore();
</script>

<style lang="scss">
.req-content {
}
</style>
