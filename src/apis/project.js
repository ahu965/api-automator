import request from "@/utils/request";

export function listApi(name, page) {
  return request({
    url: "main/projects/",
    method: "get",
    params: { name, page },
  });
}

export function createApi(data) {
  return request({
    url: "main/projects/",
    method: "post",
    data,
  });
}

export function deleteApi(id) {
  return request({
    url: "main/projects/" + id,
    method: "delete",
  });
}
