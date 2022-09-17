import { createApp } from "vue";
import { createPinia } from "pinia";

import App from "./App.vue";
import router from "./router";

import Antd from "ant-design-vue";
import "ant-design-vue/dist/antd.css";

import axios from "axios";

const app = createApp(App);

app.use(createPinia());
app.use(router);
app.use(Antd);

app.provide("$axios", axios);

app.mount("#app");
