<template>
  <div class="login-container">
    <a-form
      class="login-form"
      :model="formState"
      name="basic"
      autocomplete="off"
    >
      <div class="login-wrapper">
        <a-form-item>
          <h3 class="title">接口测试平台</h3>
        </a-form-item>
        <a-form-item
          name="username"
          :rules="[{ required: true, message: '请输入用户名！' }]"
        >
          <a-input
            placeholder="请输入用户名"
            v-model:value="formState.username"
          />
        </a-form-item>

        <a-form-item
          name="password"
          :rules="[{ required: true, message: '请输入密码!' }]"
        >
          <a-input-password
            placeholder="请输入密码"
            v-model:value="formState.password"
          />
        </a-form-item>

        <a-form-item>
          <a-button type="primary" class="btn-login" @click="login"
            >登录
          </a-button>
        </a-form-item>
      </div>
    </a-form>
  </div>
</template>

<script setup>
import { reactive } from "vue";
import { loginApi } from "../apis/user";

const formState = reactive({
  username: "",
  password: "",
});

const login = () => {
  loginApi(formState.username, formState.password).then((val) => {
    console.log(val);
  });
};
</script>

<style lang="scss">
.login-container {
  min-height: 100%;
  width: 100%;
  background-color: #2d3a4b;
  overflow: hidden;

  .login-form {
    width: 520px;
    margin-top: 10%;
    margin-left: auto;
    margin-right: auto;

    .login-wrapper {
      padding: 25px;
      border: 1px solid rgba(255, 255, 255, 0.1);
      background: rgba(0, 0, 0, 0.1);
      border-radius: 10px;
    }

    .title {
      color: #eee;
      text-align: center;
      font-size: 32px;
    }

    #basic_username {
      height: 45px;
    }

    .ant-input-password {
      height: 45px;
    }

    .btn-login {
      width: 100%;
      height: 45px;
      font-size: 18px;
    }
  }
}
</style>
