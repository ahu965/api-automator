<template>
  <div class="table-form">
    <a-table
      :row-selection="rowSelection"
      :columns="columns"
      :data-source="data"
      :pagination="false"
    >
      <template #bodyCell="{ column, record, index }">
        <template v-if="column.key !== 'action'">
          <a-input v-model:value="record[column.key]"></a-input>
        </template>
        <template v-if="column.key === 'action'">
          <span>
            <a-icon
              class="iconfont icon-jia"
              style="color: #6b6b6b; cursor: pointer; margin-right: 10px"
              @click="addParam"
            />
            <a-icon
              class="iconfont icon-jianhao"
              style="color: #e71f12; cursor: pointer"
              @click="deleteParam(index)"
            />
          </span>
        </template>
      </template>
    </a-table>
  </div>
</template>

<script setup>
import { computed, onMounted, ref, unref } from "vue";

const props = defineProps({
  // 表头
  columns: {
    type: Array,
    default: () => {
      return [
        {
          title: "key",
          dataIndex: "key",
          key: "key",
        },
        {
          title: "value",
          dataIndex: "value",
          key: "value",
        },
        {
          title: "描述",
          dataIndex: "desc",
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
        key: "",
        value: "",
        desc: "",
      };
    },
  },
});
const data = ref([]);
onMounted(() => {
  data.value = props.initData;
});

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
  data.value.push(props.dataStruct);
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
