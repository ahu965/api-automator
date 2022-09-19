import request from "@/utils/request";

export function listApi(name, page) {
  return request({
    url: "main/projects/",
    method: "get",
    params: { name, page },
  });
}
