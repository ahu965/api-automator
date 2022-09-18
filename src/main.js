import { createApp } from "vue";
import { createPinia } from "pinia";

import App from "./App.vue";
import router from "./router";

import Antd from "ant-design-vue";
import "ant-design-vue/dist/antd.css";

// 引入阿里云字体图标css
import "./assets/icons/iconfont/iconfont.css";

const app = createApp(App);

app.use(createPinia());
app.use(router);
app.use(Antd);

app.mount("#app");
