<template>
  <div class="req-content">
    <api-coder :lang="json" :initHeight="'250px'"></api-coder>
  </div>
</template>

<script setup>
import ApiCoder from "@/components/ApiCoder.vue";
</script>

<style lang="scss">
.req-content {
}
</style>
