<template>
  <div class="api">
    <a-layout>
      <a-layout-sider>
        <api-list-sider
          @showDefault="showApiContent"
          @detail="detail"
        ></api-list-sider>
      </a-layout-sider>
      <a-layout-content>
        <div v-if="show">请新增或者编辑已经存在的接口</div>
        <api-list-content
          v-if="!show"
          :category_id="category_id"
          :initData="apiDetail"
        ></api-list-content>
      </a-layout-content>
    </a-layout>
  </div>
</template>

<script setup>
import ApiListSider from "@/components/apis/ApiListSider.vue";
import ApiListContent from "@/components/apis/ApiListContent.vue";
import { ref } from "vue";

const show = ref(true);
const category_id = ref("");
const apiDetail = ref({});

const showApiContent = (id, defaultShow) => {
  show.value = defaultShow;
  category_id.value = id;
};
const detail = (value) => {
  apiDetail.value = value;
};
</script>

<style lang="scss">
.api {
  height: 100%;

  .ant-layout {
    height: 100%;
  }

  .ant-layout-sider {
    color: #fff;
    background: #ffffff;
    flex: 0 0 280px !important;
    max-width: 280px !important;
    overflow-y: auto;
  }

  .ant-layout-content {
    padding: 0px !important;
    width: 100%;
    height: 100%;
    background-color: #ffffff;
  }

  //[data-theme='dark']  .ant-layout-sider {
  //  background: #3499ec;
  //}
  // .ant-layout-content {
  //  min-height: 120px;
  //  color: #fff;
  //  line-height: 120px;
  //  background: rgba(16, 142, 233, 1);
  //}
  //[data-theme='dark']  .ant-layout-content {
  //  background: #107bcb;
  //}
  // > .code-box-demo > .ant-layout + .ant-layout {
  //  margin-top: 48px;
  //}
}
</style>
<script>
export default {
  components: {},
};
</script>
