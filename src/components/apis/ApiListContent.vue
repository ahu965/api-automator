<template>
  <div class="api-content">
    <a-card :title="title" style="width: 100%; height: 100%">
      <template #extra>
        <a-select
            :placeholder="'请选择环境'"
            style="width: 120px"
            v-model:value="enviroment"
        >
          <a-select-option v-for="env in envs" :key="env.id" :value="env.id"
          >{{ env.name }}
          </a-select-option>
        </a-select>
        <a-button type="primary" style="margin: 0px 10px" @click="sendApi"
        >Send
        </a-button
        >
        <a-button
            type="primary"
            style="background-color: #28bc7e; border-color: #28bc7e"
            @click="saveApi"
        >Save
        </a-button>
      </template>
      <a-form
          :model="formState"
          :label-col="{ span: 3 }"
          :wrapper-col="{ span: 21 }"
          labelAlign="left"
      >
        <a-form-item label="名称/描述">
          <a-input v-model:value="formState.name" placeholder="请输入名称"/>
          <a-input v-model:value="formState.desc" placeholder="请输入描述"/>
        </a-form-item>
        <a-form-item label="方法/路径" class="method">
          <a-select
              v-model:value="formState.method"
              placeholder="请选择请求方法"
          >
            <a-select-option value="GET">GET</a-select-option>
            <a-select-option value="POST">POST</a-select-option>
            <a-select-option value="PATCH">PATCH</a-select-option>
            <a-select-option value="PUT">PUT</a-select-option>
            <a-select-option value="DELETE">DELETE</a-select-option>
          </a-select>
          <a-input v-model:value="formState.path" placeholder="请输入路径"/>
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
        <a-tab-pane key="4" tab="前置脚本">TODO</a-tab-pane>
        <a-tab-pane key="5" tab="后置脚本">TODO</a-tab-pane>
      </a-tabs>
      <a-tabs>
        <a-tab-pane key="1" tab="响应体">
          <res-body></res-body>
        </a-tab-pane>
        <a-tab-pane key="2" tab="响应头">
          <res-header></res-header>
        </a-tab-pane>
        <a-tab-pane key="3" tab="断言">TODO</a-tab-pane>
        <a-tab-pane key="4" tab="提取">TODO</a-tab-pane>
        <a-tab-pane key="5" tab="请求内容">
          <req-content></req-content>
        </a-tab-pane>
      </a-tabs>
    </a-card>
  </div>
</template>

<script setup>
import {computed, onMounted, ref, watch} from "vue";
import ApiParams from "@/components/apis/ApiParams.vue";
import ApiHeaders from "@/components/apis/ApiHeaders.vue";
import ApiBody from "@/components/apis/ApiBody.vue";
import ResBody from "@/components/apis/ResBody.vue";
import ResHeader from "@/components/apis/ResHeader.vue";
import ReqContent from "@/components/apis/reqContent.vue";
import {addApiApi, apiSendApi} from "@/apis/api";
import {message} from "ant-design-vue";
import {listApi} from "@/apis/env";
import {useApiRequestStore, useApiResponseStore} from "@/stores/api";

const apiRequest = useApiRequestStore();
const formState = ref({});
watch(
    () => apiRequest.reqApi,
    () => {
      if(typeof(apiRequest.reqApi)==='object'){
        formState.value = apiRequest.reqApi;
      }else{
        formState.value = {}
      }

    },
    {immediate: true} // immediate选项可以开启首次赋值监听
);
const title = computed(() => {
  let t = ""
  if (typeof(apiRequest.reqApi)!=='object') {
    t = "新增接口"
    if (apiRequest.reqApiCategory !== "") {
      t += "(分类ID：" + apiRequest.reqApiCategory + ")"
    }
  } else {
    t = apiRequest.reqApi.name;
  }
  return t;
})


const saveApi = () => {
  if (apiRequest.reqApiCategory !== "") {
    formState.value.category = apiRequest.reqApiCategory;
  }
  // 获取请求参数
  if (apiRequest.reqParams.length !== 0) {
    formState.value.params = JSON.stringify(apiRequest.reqParams);
  }
  // 获取请求头
  if (apiRequest.reqHeaders.length !== 0) {
    formState.value.headers = JSON.stringify(apiRequest.reqHeaders);
  }
  formState.value.body_type = apiRequest.reqBodyType;
  // 获取请求体
  switch (apiRequest.reqBodyType) {
    case "JSON":
      formState.value.body = apiRequest.reqJsonBody;
      break;
    case "FORM":
      formState.value.body = JSON.stringify(apiRequest.reqFormBody);
      break;
    default:
      break;
  }
  addApiApi(formState.value).then(() => {
    message.success("保存成功");
  });
};
const envs = ref([]);
onMounted(() => {
  listApi().then((res) => {
    envs.value = res.results;
  });
});
const enviroment = ref("");
const apiResponse = useApiResponseStore();
const sendApi = () => {
  // 获取请求参数
  formState.value.params = JSON.stringify(apiRequest.reqParams);
  // 获取请求头
  formState.value.headers = JSON.stringify(apiRequest.reqHeaders);
  formState.value.body_type = apiRequest.reqBodyType;
  // 获取请求体
  switch (apiRequest.reqBodyType) {
    case "JSON":
      formState.value.body = apiRequest.reqJsonBody;
      break;
    case "FORM":
      formState.value.body = JSON.stringify(apiRequest.reqFormBody);
      break;
    default:
      break;
  }
  // 测试环境
  if (enviroment.value) {
    formState.value.env = enviroment.value;
  }
  apiSendApi(formState.value).then((res) => {
    apiResponse.updateResponse(res);
  });
};
</script>

<style lang="scss">
.api-content {
  width: 100%;
  height: 100%;

  .ant-card {
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
