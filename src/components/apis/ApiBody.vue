<template>
  <div class="api-body">
    <a-tabs v-model:activeKey="apiReuqest.reqBodyType" type="card">
      <a-tab-pane key="NONE" tab="none">不需要请求体</a-tab-pane>
      <a-tab-pane key="JSON" tab="json">
        <api-coder
            :lang="'json'"
            :initHeight="'250px'"
            :content="apiReuqest.reqJsonBody"
            @updateScript="updateContent"
        ></api-coder>
      </a-tab-pane>
      <a-tab-pane key="FORM" tab="form-data">
        <table-form :initData="apiReuqest.reqFormBody"></table-form>
      </a-tab-pane>
      <a-tab-pane key="BINARY" tab="binary">Content of Tab Pane 3</a-tab-pane>
    </a-tabs>
  </div>
</template>

<script setup>
import TableForm from "@/components/TableForm.vue";
import ApiCoder from "@/components/ApiCoder.vue";
import {useApiRequestStore} from "@/stores/api";

const apiReuqest = useApiRequestStore();

const updateContent = (content) => {
  apiReuqest.reqJsonBody = content;
};
</script>

<style scoped></style>
