import request from "@/utils/request";

export function listApi(name, page) {
  return request({
    url: "main/envs/",
    method: "get",
    params: { name, page },
  });
}

export function createApi(data) {
  return request({
    url: "main/envs/",
    method: "post",
    data,
  });
}

export function deleteApi(id) {
  return request({
    url: "main/envs/" + id,
    method: "delete",
  });
}

export function detailApi(id) {
  return request({
    url: "main/envs/" + id,
    method: "get",
  });
}

export function updateApi(data) {
  return request({
    url: "main/envs/" + data.id + "/",
    method: "put",
    data,
  });
}
