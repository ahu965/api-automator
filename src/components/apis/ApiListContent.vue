<template>
  <div class="api-content">
    <a-card title="接口名称" style="width: 100%; height: 100%">
      <template #extra>
        <a-button type="primary" style="margin-right: 10px">Send</a-button>
        <a-button
          type="primary"
          style="background-color: #28bc7e; border-color: #28bc7e"
          >Save</a-button
        >
      </template>
      <a-form
        :model="formState"
        :label-col="{ span: 3 }"
        :wrapper-col="{ span: 21 }"
        labelAlign="left"
      >
        <a-form-item label="名称/描述">
          <a-input v-model:value="formState.name" placeholder="请输入名称" />
          <a-input v-model:value="formState.name" placeholder="请输入描述" />
        </a-form-item>
        <a-form-item label="方法/路径" class="method">
          <a-select placeholder="请选择请求方法">
            <a-select-option value="GET">GET</a-select-option>
            <a-select-option value="POST">POST</a-select-option>
            <a-select-option value="PATCH">PATCH</a-select-option>
            <a-select-option value="DELETE">DELETE</a-select-option>
            <a-select-option value="PATCH">PATCH</a-select-option>
          </a-select>
          <a-input v-model:value="formState.name" placeholder="请输入描述" />
        </a-form-item>
      </a-form>
      <a-tabs>
        <a-tab-pane key="1" tab="请求参数">
          <api-params></api-params>
        </a-tab-pane>
        <a-tab-pane key="2" tab="请求头">
          <api-headers></api-headers>
        </a-tab-pane>
        <a-tab-pane key="3" tab="请求体">
          <api-body></api-body>
        </a-tab-pane>
        <a-tab-pane key="4" tab="前置脚本">Content of Tab Pane 3</a-tab-pane>
        <a-tab-pane key="5" tab="后置脚本">Content of Tab Pane 3</a-tab-pane>
      </a-tabs>
      <a-tabs v-model:activeKey="activeKey">
        <a-tab-pane key="1" tab="响应体">Content of Tab Pane 1</a-tab-pane>
        <a-tab-pane key="2" tab="响应头">Content of Tab Pane 2</a-tab-pane>
        <a-tab-pane key="3" tab="断言">Content of Tab Pane 3</a-tab-pane>
        <a-tab-pane key="3" tab="提取">Content of Tab Pane 3</a-tab-pane>
        <a-tab-pane key="3" tab="请求内容">Content of Tab Pane 3</a-tab-pane>
      </a-tabs>
    </a-card>
  </div>
</template>

<script setup>
import { ref } from "vue";
import ApiParams from "@/components/apis/ApiParams.vue";
import ApiHeaders from "@/components/apis/ApiHeaders.vue";
import ApiBody from "@/components/apis/ApiBody.vue";

const formState = ref({});
</script>

<style lang="scss">
.api-content {
  width: 100%;
  height: 100%;
  .ant-card{
    overflow-y: auto;
  }
  .ant-form-item-control-input-content {
    display: flex;
  }
  .method {
    .ant-select {
      flex: 2;
    }
  }
}
</style>
