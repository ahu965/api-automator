import { createRouter, createWebHistory } from "vue-router";
import HomeView from "../views/HomeView.vue";

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: "/",
      name: "home",
      component: HomeView,
      children: [
        {
          path: "main/projects",
          name: "项目管理",
          icon: "icon-modular",
          component: () => import("../views/main/ProjectListView.vue"),
        },
        {
          path: "main/apis",
          name: "接口管理",
          icon: "icon-gongjuguanli1",
          component: () => import("../views/main/apis/ApiListView.vue"),
        },
        {
          path: "main/envs",
          name: "环境管理",
          icon: "icon-setting",
          component: () => import("../views/main/EnvListView.vue"),
        },
      ],
    },
    {
      path: "/about",
      name: "about",
      // route level code-splitting
      // this generates a separate chunk (About.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: () => import("../views/AboutView.vue"),
    },
    {
      path: "/login",
      name: "login",
      component: () => import("../views/LoginView.vue"),
    },
  ],
});

export default router;
