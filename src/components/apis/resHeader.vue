<template>
  <div class="res-header">
    <a-table :dataSource="dataSource" :columns="columns" :pagination="false" />
  </div>
</template>

<script setup>
import { ref } from "vue";

const dataSource = ref([
  {
    key: "1",
    value: "Mike",
  },
  {
    key: "2",
    value: "John",
  },
]);

const columns = ref([
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
]);
</script>

<style lang="scss">
.res-header {
  .ant-table-cell {
    padding: 5px 5px;
  }
}
</style>
