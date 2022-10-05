<template>
  <div class="env-list">
    <div class="env_filter clearfix">
      <a-form layout="inline" :model="envParams" class="fl">
        <a-form-item label="环境名称">
          <a-input v-model:value="envParams.name" placeholder="环境名称">
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
        >新增环境
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
            <a @click="updateEnvPre(record)">编辑</a>
            <a-divider type="vertical" />
            <a @click="deleteEnvPre(record)">删除</a>
          </span>
        </template>
      </template>
    </a-table>
  </div>
  <a-modal
    v-model:visible="createModelVisible"
    title="新增环境"
    ok-text="确定"
    cancel-text="取消"
    @ok="addEnv"
  >
    <a-form
      :model="createParams"
      v-bind="layout"
      name="nest-messages"
      @finish="onFinish"
    >
      <a-form-item label="环境名称" :rules="[{ required: true }]">
        <a-input v-model:value="createParams.name" />
      </a-form-item>
      <a-form-item label="环境描述">
        <a-input v-model:value="createParams.desc" />
      </a-form-item>
      <a-form-item label="请求协议">
        <a-select v-model:value="createParams.protocol">
          <a-select-option value="HTTP">HTTP</a-select-option>
          <a-select-option value="HTTPS">HTTPS</a-select-option>
        </a-select>
      </a-form-item>
      <a-form-item label="域名/IP" :rules="[{ required: true }]">
        <a-input v-model:value="createParams.domain" />
      </a-form-item>
      <a-form-item label="端口">
        <a-input v-model:value="createParams.port" />
      </a-form-item>
    </a-form>
  </a-modal>
  <a-modal
    v-model:visible="deleteModalVisible"
    title="提示"
    ok-text="确认删除"
    cancel-text="取消"
    @ok="deleteEnv"
  >
    <p>{{ modalMessage }}</p>
  </a-modal>
  <a-modal
    v-model:visible="updateModelVisible"
    title="编辑环境"
    ok-text="确定"
    cancel-text="取消"
    @ok="updateEnv"
  >
    <a-form :model="updateEnvForm" v-bind="layout" name="nest-messages">
      <a-form-item label="环境名称" :rules="[{ required: true }]">
        <a-input v-model:value="updateEnvForm.name" />
      </a-form-item>
      <a-form-item label="环境描述">
        <a-input v-model:value="updateEnvForm.desc" />
      </a-form-item>
      <a-form-item label="请求协议">
        <a-select v-model:value="updateEnvForm.protocol">
          <a-select-option value="HTTP">HTTP</a-select-option>
          <a-select-option value="HTTPS">HTTPS</a-select-option>
        </a-select>
      </a-form-item>
      <a-form-item label="域名/IP" :rules="[{ required: true }]">
        <a-input v-model:value="updateEnvForm.domain" />
      </a-form-item>
      <a-form-item label="端口">
        <a-input v-model:value="updateEnvForm.port" />
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
} from "../../apis/env";
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
    title: "请求协议",
    dataIndex: "protocol",
    key: "protocol",
  },
  {
    title: "域名/IP",
    dataIndex: "domain",
    key: "domain",
  },
  {
    title: "端口",
    dataIndex: "port",
    key: "port",
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

const envParams = ref({});

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
  listEnv(envParams.value.name, current.value);
};

const listEnv = (name) => {
  listApi(name, current.value).then((res) => {
    data.value = res.results;
    total.value = res.count;
  });
};

const query = () => {
  listEnv(envParams.value.name);
};

const createModelVisible = ref(false);
const layout = {
  labelCol: { span: 6 },
  wrapperCol: { span: 16 },
};
const createParams = ref({
  protocol: "HTTP",
});
const addEnv = () => {
  createApi(createParams.value).then(() => {
    createModelVisible.value = false;
    createParams.value = {};
    listEnv("");
  });
};

const deleteModalVisible = ref(false);
const modalMessage = ref("");
const deleteId = ref(null);

const deleteEnvPre = (p) => {
  modalMessage.value = "是否确认删除【" + p.name + "】？";
  deleteModalVisible.value = true;
  deleteId.value = p.id;
};

const deleteEnv = () => {
  if (deleteId.value != null) {
    deleteApi(deleteId.value).then(() => {
      message.success("删除成功");
      listEnv("");
      deleteModalVisible.value = false;
    });
  }
};

const updateModelVisible = ref(false);
const updateEnvForm = ref({});
const updateEnvPre = (text) => {
  detailApi(text.id).then((res) => {
    console.log(res);
    updateEnvForm.value = res;
    updateModelVisible.value = true;
  });
};

const updateEnv = () => {
  if (updateEnvForm.value.id != null) {
    updateApi(updateEnvForm.value).then(() => {
      message.success("编辑成功");
      updateModelVisible.value = false;
      listEnv("");
    });
  }
};
onMounted(() => {
  listEnv("");
});
</script>

<style lang="scss" scoped>
.env-list {
  .env_filter {
    padding-bottom: 24px;
  }
}
</style>
