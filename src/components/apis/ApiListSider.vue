<template>
  <div class="api-sider">
    <div class="top-search">
      <a-popover trigger="hover">
        <template #content>
          <a-button type="link" @click="showCategoryModal">新增分类</a-button>
          <a-button type="link" @click="addApi(null)">新增接口</a-button>
        </template>
        <span
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
        :load-data="loadData"
        @select="selectRow"
    >
      <template #switcherIcon="{ switcherCls }">
        <down-outlined :class="switcherCls"/>
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
      <template #title="{ name, type, id }">
        <div
            :style="[
            type === 'collection' ? 'width: 100%' : 'width: calc(100% - 48px);', // 计算属性，即宽度为减去某个固定值后的100%宽度
          ]"
            style="display: inline-block"
        >
          <span>{{ name }}</span>
          <a-popover trigger="hover" v-if="type === 'collection'">
            <template #content>
              <a-button type="link">编辑</a-button>
              <a-button type="link" @click="showCategoryModal(id)"
              >新增分类
              </a-button>
              <a-button type="link" @click="addApi(id)"
              >新增接口
              </a-button>
              <a-button type="link" danger>删除</a-button>
            </template>
            <span
                class="iconfont icon-gengduo fr"
                style="color: #6b6b6b; cursor: pointer; padding-right: 10px"
            />
          </a-popover>
          <a-popover trigger="hover" v-if="type === 'api'">
            <template #content>
              <a-button type="link">新增用例</a-button>
              <a-button type="link" danger>删除</a-button>
            </template>
            <span
                class="iconfont icon-gengduo fr"
                style="color: #6b6b6b; cursor: pointer; padding-right: 10px"
            />
          </a-popover>
        </div>
      </template>
    </a-tree>
  </div>
  <a-modal
      v-model:visible="categoryVisible"
      :title="categoryModalTitle"
      :ok-text="'确定'"
      :cancel-text="'取消'"
      @ok="postCategory"
  >
    <a-form :model="categoryForm" name="nest-messages">
      <a-form-item label="分类名称" :rules="[{ required: true }]">
        <a-input v-model:value="categoryForm.name"/>
      </a-form-item>
    </a-form>
  </a-modal>
</template>

<script setup>
import {DownOutlined} from "@ant-design/icons-vue";
import {onMounted, ref} from "vue";
import {
  addCategoryApi,
  detailApiApi,
  listCategoryApiApi,
} from "../../apis/api";
import {useApiRequestStore} from "@/stores/api";

const emits = defineEmits(["showDefault"]);

const expandedKeys = ref(["0-0-0"]);
const selectedKeys = ref([]);
const treeData = ref([]);
const categoryVisible = ref(false);
const categoryModalTitle = ref("");
const categoryForm = ref({
  id: "",
  name: "",
  parent_category: null,
});
const keywords = ref("");

const showCategoryModal = (id) => {
  if (id != null) {
    categoryModalTitle.value = "新增子分类";
    categoryForm.value.parent_category = id;
  } else {
    categoryModalTitle.value = "新增分类";
  }
  categoryVisible.value = true;
};
const postCategory = () => {
  if (categoryForm.value.id === "") {
    let body = {
      name: categoryForm.value.name,
    };
    if (categoryForm.value.parent_category != null) {
      body["parent_category"] = categoryForm.value.parent_category;
    }
    addCategoryApi(body).then(() => {
      categoryVisible.value = false;
      queryCategories(-1);
    });
  }
};
const loadData = (treeNode) => {
  return new Promise((resolve) => {
    if (treeNode.dataRef.children) {
      resolve();
      return;
    }
    if (treeNode.dataRef.type === "collection") {
      listCategoryApiApi(treeNode.dataRef.id).then((res) => {
        treeNode.dataRef.children = res;
        treeData.value = [...treeData.value];
        resolve();
      });
    } else {
      // TODO:接口需要查询用例
      resolve();
    }
  });
};

const queryCategories = (parent_category) => {
  listCategoryApiApi(parent_category).then((res) => {
    treeData.value = res;
  });
};

onMounted(() => {
  queryCategories();
});

const apiRequest = useApiRequestStore();

// 点击树节点
const selectRow = (key, row) => {
  if (row.node.type === "api") {
    detailApiApi(row.node.id).then((res) => {
      emits("showDefault", false);
      apiRequest.updateRequest(res);
    });
  }else{
    emits("showDefault", true);
  }
};

// 新增接口
const addApi = (id)=>{
  emits("showDefault", false);
  apiRequest.resetData();
  if(id!==null){
    apiRequest.reqApiCategory = id;
  }
}
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
