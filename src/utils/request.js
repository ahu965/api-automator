import axios from "axios";
import router from "../router";

// create an axios instance
const service = axios.create({
  baseURL: "http://127.0.0.1:8000/", // url = base url + request url
  timeout: 60000, // request timeout
});

// response interceptor
service.interceptors.response.use(
  (response) => {
    if (response.status === 200) {
      return response.data;
    }
  },
  (error) => {
    let response = error.response;
    let currentPath = router.currentRoute.value.path;
    switch (response.status) {
      case 400:
        console.log(response);
        break;
      case 401:
        // 判断当前页面
        if (currentPath === "/login") {
          console.error("用户名或密码错误");
        } else {
          console.error("TOKEN过期，请重新登录");
          router.push("/login");
        }
        break;
    }
    return Promise.reject(error);
  }
);

export default service;
