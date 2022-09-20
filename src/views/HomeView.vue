<template>
  <a-layout class="home">
    <a-layout-sider v-model:collapsed="collapsed" :trigger="null" collapsible>
      <div v-if="!collapsed" class="logo_big" />
      <div v-if="collapsed" class="logo_small" />
      <a-menu v-model:selectedKeys="selectedKeys" theme="dark" mode="inline">
        <a-menu-item v-for="(item, index) in menus" :key="index">
          <template #icon>
            <a-icon
              class="iconfont"
              :class="item.icon"
              style="margin-right: 10px"
            ></a-icon>
          </template>
          <span>
            <router-link :to="item.path" class="link">{{
              item.name
            }}</router-link>
          </span>
        </a-menu-item>
      </a-menu>
    </a-layout-sider>
    <a-layout>
      <a-layout-header style="background: #fff; padding: 0">
        <menu-unfold-outlined
          v-if="collapsed"
          class="trigger"
          @click="collapsed = !collapsed"
        />
        <menu-fold-outlined
          v-else
          class="trigger"
          @click="collapsed = !collapsed"
        />
      </a-layout-header>
      <a-layout-content
        :style="{
          margin: '24px 16px',
          padding: '24px',
          background: '#fff',
          minHeight: '280px',
        }"
      >
        <RouterView />
      </a-layout-content>
    </a-layout>
  </a-layout>
</template>

<script setup>
import { MenuUnfoldOutlined, MenuFoldOutlined } from "@ant-design/icons-vue";
import { onMounted, ref } from "vue";
import router from "../router";

let selectedKeys = ref(["1"]);
let collapsed = ref(false);
let menus = ref([]);

onMounted(() => {
  let routes = router.getRoutes().filter((item) => item.name === "home");
  menus.value = routes[0].children;
  console.log(routes);
});
</script>
<style lang="scss">
.home {
  height: 100%;

  .logo_big {
    width: 200px;
    height: 60px;
    background-image: url("/public/images/logo_big.png");
    background-size: 200px 60px;
  }

  .logo_small {
    width: 80px;
    height: 60px;
    background-image: url("/public/images/logo_small.png");
    background-size: 80px 60px;
  }

  .trigger {
    font-size: 18px;
    line-height: 64px;
    padding: 0 24px;
    cursor: pointer;
    transition: color 0.3s;
  }

  .ant-menu-item a,
  .ant-menu-item a:hover {
    color: #a4adb5;
  }

  .ant-menu-item-selected a,
  .ant-menu-item-selected a:hover {
    color: #eeeeee;
  }

  .ant-layout-content {
    overflow-y: auto;
  }
}

//#components-layout-demo-custom-trigger .trigger:hover {
//  color: #1890ff;
//}
//
//#components-layout-demo-custom-trigger .logo {
//  height: 32px;
//  background: rgba(255, 255, 255, 0.3);
//  margin: 16px;
//}
//
//.site-layout .site-layout-background {
//  background: #fff;
//}
</style>
