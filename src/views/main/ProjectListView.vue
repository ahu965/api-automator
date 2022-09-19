<template>
  <div class="project-list">
    <div class="project_filter">
      <a-form layout="inline" :model="projectParams">
        <a-form-item label="项目名称">
          <a-input v-model:value="projectParams.name" placeholder="项目名称">
          </a-input>
        </a-form-item>
        <a-form-item>
          <a-button type="primary" html-type="submit" @click="query"
            >查询
          </a-button>
        </a-form-item>
      </a-form>
    </div>
    <a-table :columns="columns" :data-source="data" :pagination="pagination">
      <template #name="{ text }">
        <a>{{ text }}</a>
      </template>
      <template #creator="{ text }">
        <span>{{ text.username }}</span>
      </template>
      <template #action>
        <span>
          <!--          <a-divider type="vertical" />-->
          <a>删除</a>
          <!--          <a-divider type="vertical" />-->
          <!--          <a class="ant-dropdown-link">-->
          <!--            More actions-->
          <!--            <down-outlined />-->
          <!--          </a>-->
        </span>
      </template>
    </a-table>
  </div>
</template>

<script setup>
import { computed, onMounted, ref } from "vue";
import { listApi } from "../../apis/project";

const columns = [
  {
    title: "ID",
    dataIndex: "id",
    key: "id",
  },
  {
    dataIndex: "name",
    key: "name",
    title: "名称",
    slots: { customRender: "name" },
  },
  {
    title: "描述",
    dataIndex: "desc",
    key: "desc",
  },
  {
    title: "创建人",
    key: "created_by",
    dataIndex: "created_by",
    slots: { customRender: "creator" },
  },
  {
    title: "创建时间",
    key: "created_at",
    dataIndex: "created_at",
  },
  {
    title: "操作",
    key: "action",
    slots: { customRender: "action" },
  },
];

const data = ref([]);

const projectParams = ref({});

const total = ref(0);
const current = ref(1);
// 列表分页
const pagination = computed(() => ({
  total: total.value,
  current: current.value,
  pageSize: 10,
  showTotal: (total) => `总共 ${total} 项`,
  onChange: (page, pageSize) => onPageChange(page, pageSize), //点击页码事件
  defaultPageSize: 10,
}));

// 列表当前页更改
const onPageChange = (page) => {
  console.log(page);
  current.value = page;
  listProject(projectParams.value.name, current.value);
};

const listProject = (name) => {
  console.log("xxx");
  listApi(name, current.value).then((res) => {
    data.value = res.results;
    total.value = res.count;
    // console.log(total.value)
  });
};

const query = () => {
  listProject(projectParams.value.name);
};

onMounted(() => {
  listProject("");
});
</script>

<style lang="scss" scoped>
.project-list {
  .project_filter {
    padding-bottom: 24px;
  }
}
</style>
