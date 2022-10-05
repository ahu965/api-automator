<template>
  <div class="project-list">
    <div class="project_filter clearfix">
      <a-form layout="inline" :model="projectParams" class="fl">
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

      <a-button
        type="primary"
        html-type="submit"
        @click="createModelVisible = true"
        class="fr"
        >新增项目
      </a-button>
    </div>
    <a-table :columns="columns" :data-source="data" :pagination="pagination">
      <template #bodyCell="{column,record}">
        <template v-if="column.key==='name'">
          <a>{{ record.name }}</a>
        </template>
        <template v-if="column.key==='creator'">
          <span>{{ record == null ? "" : record.username }}</span>
        </template>
        <template v-if="column.key==='action'">
          <span>
            <a @click="updateProjectPre(record)">编辑</a>
            <a-divider type="vertical" />
            <a @click="deleteProjectPre(record)">删除</a>
          </span>
        </template>
      </template>
    </a-table>
  </div>
  <a-modal
    v-model:visible="createModelVisible"
    title="新增项目"
    ok-text="确定"
    cancel-text="取消"
    @ok="addProject"
  >
    <a-form
      :model="createParams"
      v-bind="layout"
      name="nest-messages"
      @finish="onFinish"
    >
      <a-form-item label="项目名称" :rules="[{ required: true }]">
        <a-input v-model:value="createParams.name" />
      </a-form-item>
      <a-form-item label="项目描述">
        <a-input v-model:value="createParams.desc" />
      </a-form-item>
    </a-form>
  </a-modal>
  <a-modal
    v-model:visible="deleteModalVisible"
    title="提示"
    ok-text="确认删除"
    cancel-text="取消"
    @ok="deleteProject"
  >
    <p>{{ modalMessage }}</p>
  </a-modal>
  <a-modal
    v-model:visible="updateModelVisible"
    title="编辑项目"
    ok-text="确定"
    cancel-text="取消"
    @ok="updateProject"
  >
    <a-form :model="updateProjectForm" v-bind="layout" name="nest-messages">
      <a-form-item label="项目名称" :rules="[{ required: true }]">
        <a-input v-model:value="updateProjectForm.name" />
      </a-form-item>
      <a-form-item label="项目描述">
        <a-input v-model:value="updateProjectForm.desc" />
      </a-form-item>
    </a-form>
  </a-modal>
</template>

<script setup>
import { computed, onMounted, ref } from "vue";
import {
  createApi,
  deleteApi,
  detailApi,
  listApi,
  updateApi,
} from "../../apis/project";
import { message } from "ant-design-vue";

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
  },
  {
    title: "创建时间",
    key: "created_at",
    dataIndex: "created_at",
  },
  {
    title: "操作",
    key: "action",
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
  listApi(name, current.value).then((res) => {
    data.value = res.results;
    total.value = res.count;
  });
};

const query = () => {
  listProject(projectParams.value.name);
};

const createModelVisible = ref(false);
const layout = {
  labelCol: { span: 6 },
  wrapperCol: { span: 16 },
};
const createParams = ref({});
const addProject = () => {
  createApi(createParams.value).then(() => {
    createModelVisible.value = false;
    createParams.value = {};
    listProject("");
  });
};

const deleteModalVisible = ref(false);
const modalMessage = ref("");
const deleteId = ref(null);

const deleteProjectPre = (p) => {
  modalMessage.value = "是否确认删除【" + p.name + "】？";
  deleteModalVisible.value = true;
  deleteId.value = p.id;
};

const deleteProject = () => {
  if (deleteId.value != null) {
    deleteApi(deleteId.value).then(() => {
      message.success("删除成功");
      listProject("");
      deleteModalVisible.value = false;
    });
  }
};

const updateModelVisible = ref(false);
const updateProjectForm = ref({});
const updateProjectPre = (text) => {
  detailApi(text.id).then((res) => {
    console.log(res);
    updateProjectForm.value = res;
    updateModelVisible.value = true;
  });
};

const updateProject = () => {
  if (updateProjectForm.value.id != null) {
    updateApi(updateProjectForm.value).then(() => {
      message.success("编辑成功");
      updateModelVisible.value = false;
      listProject("");
    });
  }
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
