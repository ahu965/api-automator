<template>
  <div class="table-form">
    <a-table
      :row-selection="rowSelection"
      :columns="columns"
      :data-source="data"
      :pagination="false"
    >
      <template #bodyCell="{ column, record, index }">
        <template v-if="column.key === 'param_key'">
          <a-input v-model:value="record.param_key"></a-input>
        </template>
        <template v-if="column.key === 'value'">
          <a-input v-model:value="record.value"></a-input>
        </template>
        <template v-if="column.key === 'desc'">
          <a-input v-model:value="record.desc"></a-input>
        </template>
        <template v-if="column.key === 'action'">
          <span>
            <span
              class="iconfont icon-jia"
              style="color: #6b6b6b; cursor: pointer; margin-right: 10px"
              @click="addParam"
            />
            <span
              class="iconfont icon-jianhao"
              style="color: #e71f12; cursor: pointer"
              @click="deleteParam(index)"
            />
          </span>
        </template>
      </template>
      <template #emptyText>
        <div style="padding: 30px">
          <IconEmpty />
          <a-button
            type="primary"
            style="display: block; margin: auto"
            @click="addParam"
            >新增
          </a-button>
        </div>
      </template>
    </a-table>
  </div>
</template>

<script setup>
import { computed, onMounted, ref, unref, watch } from "vue";
import IconEmpty from "./icons/IconEmpty.vue";

const props = defineProps({
  // 表头
  columns: {
    type: Array,
    default: () => {
      return [
        {
          title: "key",
          key: "param_key",
        },
        {
          title: "value",
          key: "value",
        },
        {
          title: "描述",
          key: "desc",
        },
        {
          title: "操作",
          key: "action",
        },
      ];
    },
  },
  // 表格初始化数据
  initData: {
    type: Array,
  },
  // 表格数据结构
  dataStruct: {
    type: Object,
    default: () => {
      return {
        param_key: "",
        value: "",
        desc: "",
      };
    },
  },
});
const data = ref([]);
watch(
  () => props.initData,
  () => {
    data.value = props.initData;
  },
  { immediate: true } // immediate选项可以开启首次赋值监听
);

const selectedRowKeys = ref([]);
const rowSelection = computed(() => {
  return {
    selectedRowKeys: unref(selectedRowKeys),
    onChange: onSelectChange,
    hideDefaultSelections: true,
  };
});
const onSelectChange = () => {};
const addParam = () => {
  data.value.push(JSON.parse(JSON.stringify(props.dataStruct)));
};
const deleteParam = (index) => {
  data.value.splice(index, 1);
};
</script>

<style lang="scss">
.table-form {
  .ant-table-cell {
    padding: 5px 5px;
  }
}
</style>
