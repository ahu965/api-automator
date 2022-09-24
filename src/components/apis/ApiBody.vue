<template>
  <div class="api-body">
    <a-tabs v-model:activeKey="activeKey" type="card">
      <a-tab-pane key="1" tab="none">不需要请求体</a-tab-pane>
      <a-tab-pane key="2" tab="json">
        <api-coder :lang="json" :initHeight="'250px'"></api-coder>
      </a-tab-pane>
      <a-tab-pane key="3" tab="form-data">
        <table-form></table-form>
      </a-tab-pane>
      <a-tab-pane key="4" tab="binary">Content of Tab Pane 3</a-tab-pane>
    </a-tabs>
  </div>
</template>

<script setup>
import TableForm from "@/components/TableForm.vue";
import ApiCoder from "@/components/ApiCoder.vue";
</script>

<style scoped></style>
