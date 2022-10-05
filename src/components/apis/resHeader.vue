<template>
  <div class="res-header">
    <a-table :dataSource="dataSource" :columns="columns" :pagination="false"/>
  </div>
</template>

<script setup>
import {computed, ref} from "vue";
import {useApiResponseStore} from "../../stores/api";

const apiResponse = useApiResponseStore();
const dataSource = computed(()=>{
  let resHeaders = apiResponse.resHeaders;
  const res = [];
  if(typeof(resHeaders)==='object'){
    for (const key in resHeaders) {
      let body={}
      body["key"]=key;
      body["value"]=resHeaders[key];
      res.push(body)
    }
  }
  return res;
})

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
