<template>
  <div class="api-sider">
    <div class="top-search">
      <a-popover trigger="hover">
        <template #content>
          <a-button type="link">新增分类</a-button>
          <a-button type="link">新增接口</a-button>
        </template>
        <a-icon
          class="iconfont icon-jia"
          style="color: #6b6b6b; cursor: pointer"
        />
      </a-popover>
      <a-input
        v-model:value="keywords"
        placeholder="输入名称或者路径查询"
        style="width: 250px; margin: 5px"
      />
    </div>
    <a-tree
      v-model:expandedKeys="expandedKeys"
      v-model:selectedKeys="selectedKeys"
      show-line
      show-icon
      :tree-data="treeData"
    >
      <template #switcherIcon="{ switcherCls }">
        <down-outlined :class="switcherCls" />
      </template>
      <template #icon="{ method }">
        <template v-if="method === 'GET'">
          <span class="api-method" style="color: #0bbb52">{{ method }}</span>
        </template>
        <template v-if="method === 'POST'">
          <span class="api-method" style="color: #fcb100">{{ method }}</span>
        </template>
        <template v-if="method === 'PUT'">
          <span class="api-method" style="color: #0978e7">{{ method }}</span>
        </template>
        <template v-if="method === 'PATCH'">
          <span class="api-method" style="color: #07c0e9">{{ method }}</span>
        </template>
        <template v-if="method === 'DELETE'">
          <span class="api-method" style="color: #e71f12">{{ method }}</span>
        </template>
      </template>
      <template #title="{ title, method, type }">
        <div
          :style="[
            method == null ? 'width: 100%' : 'width: calc(100% - 48px);', // 计算属性，即宽度为减去某个固定值后的100%宽度
          ]"
          style="display: inline-block"
        >
          <span>{{ title }}</span>
          <a-popover trigger="hover" v-if="type == 'collection'">
            <template #content>
              <a-button type="link">编辑</a-button>
              <a-button type="link">新增分类</a-button>
              <a-button type="link">新增接口</a-button>
              <a-button type="link" danger>删除</a-button>
            </template>
            <a-icon
              class="iconfont icon-gengduo fr"
              style="color: #6b6b6b; cursor: pointer; padding-right: 10px"
            />
          </a-popover>
          <a-popover trigger="hover" v-if="type == 'api'">
            <template #content>
              <a-button type="link">新增用例</a-button>
              <a-button type="link" danger>删除</a-button>
            </template>
            <a-icon
              class="iconfont icon-gengduo fr"
              style="color: #6b6b6b; cursor: pointer; padding-right: 10px"
            />
          </a-popover>
        </div>
      </template>
    </a-tree>
  </div>
</template>

<script setup>
import { DownOutlined } from "@ant-design/icons-vue";
import { ref } from "vue";

const expandedKeys = ref(["0-0-0"]);
const selectedKeys = ref([]);
const treeData = [
  {
    title: "分类一",
    key: "0-0",
    type: "collection",
    children: [
      {
        title: "parent 1-0",
        key: "0-0-0",
        method: "PATCH",
        type: "api",
        children: [
          {
            title: "leaf",
            key: "0-0-0-0",
            type: "case",
          },
          {
            title: "leaf",
            key: "0-0-0-1",
          },
          {
            title: "leaf",
            key: "0-0-0-2",
          },
        ],
      },
      {
        title: "parent 1-1",
        key: "0-0-1",
        method: "PUT",
        type: "api",
        children: [
          {
            title: "leaf",
            key: "0-0-1-0",
          },
        ],
      },
      {
        title: "parent 1-2",
        key: "0-0-2",
        method: "GET",
        type: "api",
        children: [
          {
            title: "leaf",
            key: "0-0-2-0",
          },
          {
            title: "leaf",
            key: "0-0-2-1",
          },
        ],
      },
      {
        title: "parent 1-3",
        key: "0-0-2",
        method: "POST",
        type: "api",
        children: [
          {
            title: "leaf",
            key: "0-0-2-0",
          },
          {
            title: "leaf",
            key: "0-0-2-1",
          },
        ],
      },
      {
        title: "parent 1-4",
        key: "0-0-2",
        method: "DELETE",
        type: "api",
        children: [
          {
            title: "leaf",
            key: "0-0-2-0",
          },
          {
            title: "leaf",
            key: "0-0-2-1",
          },
        ],
      },
    ],
  },
  {
    title: "分类二",
    key: "0-1",
    type: "collection",
  },
];
</script>

<style lang="scss">
.api-sider {
  .top-search {
  }

  .api-method {
    padding-right: 10px;
    font-size: 12px; // 浏览器限制，小于12px不生效
  }

  .ant-tree {
    .ant-tree-treenode {
      width: 100%;

      .ant-tree-node-content-wrapper {
        width: 100%;

        .ant-tree-title {
          //display: inline-block;
          //width: 100%;
        }
      }
    }

    .ant-tree-node-content-wrapper {
      //width: 250px;
      .ant-tree-iconEle {
        width: 48px;
      }
    }
  }
}
</style>
