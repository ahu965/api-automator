import request from "@/utils/request";

export function loginApi(username, password) {
  return request({
    url: "login/",
    method: "post",
    data: {
      username,
      password,
    },
  });
}
