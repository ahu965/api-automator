<template>
  <div class="api-body">
    <a-tabs v-model:activeKey="body_type" type="card">
      <a-tab-pane key="NONE" tab="none">不需要请求体</a-tab-pane>
      <a-tab-pane key="JSON" tab="json">
        <api-coder
          :lang="json"
          :initHeight="'250px'"
          :content="jsonBody"
          @updateScript="updateContent"
        ></api-coder>
      </a-tab-pane>
      <a-tab-pane key="FORM" tab="form-data">
        <table-form :initData="formBody"></table-form>
      </a-tab-pane>
      <a-tab-pane key="BINARY" tab="binary">Content of Tab Pane 3</a-tab-pane>
    </a-tabs>
  </div>
</template>

<script setup>
import TableForm from "@/components/TableForm.vue";
import ApiCoder from "@/components/ApiCoder.vue";
import { ref, defineExpose, watch } from "vue";

const props = defineProps({
  type: {
    type: String,
    default: "NONE",
  },
  initData: {
    type: String,
  },
});
const body_type = ref("NONE");
watch(
  () => props.type,
  () => {
    body_type.value = props.type;
  },
  { immediate: true } // immediate选项可以开启首次赋值监听
);
const jsonBody = ref("");
const formBody = ref([]);
watch(
  () => props.initData,
  () => {
    switch (props.type) {
      case "JSON":
        jsonBody.value = props.initData;
        break;
      case "FORM":
        formBody.value = JSON.parse(props.initData);
        break;
    }
  },
  { immediate: true } // immediate选项可以开启首次赋值监听
);
const updateContent = (content) => {
  jsonBody.value = content;
};

const getData = () => {
  switch (props.body_type) {
    case "JSON":
      return jsonBody.value;
    case "FORM":
      if (formBody.value.length === 0) {
        return "";
      } else {
        return JSON.stringify(formBody.value);
      }
    default:
      return "";
  }
};

defineExpose({
  props,
  getData,
});
</script>

<style scoped></style>
