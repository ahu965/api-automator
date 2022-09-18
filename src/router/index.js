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
          path: "nav1",
          name: "nav 1",
          icon: "icon-modular",
          component: import("../views/AboutView.vue"),
        },
        {
          path: "nav2",
          name: "nav 2",
          icon: "icon-gongjuguanli1",
          component: import("../views/AboutView.vue"),
        },
        {
          path: "nav3",
          name: "nav 3",
          icon: "icon-setting",
          component: import("../views/AboutView.vue"),
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
