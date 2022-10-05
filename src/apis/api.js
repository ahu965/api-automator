import request from "@/utils/request";

export function addCategoryApi(data) {
  return request({
    url: "main/categories/",
    method: "post",
    data,
  });
}

export function listCategoryApi(parent_category) {
  return request({
    url: "main/categories/",
    method: "get",
    params: { parent_category },
  });
}

export function addApiApi(data) {
  return request({
    url: "main/apis/",
    method: "post",
    data,
  });
}

export function listApiApi(category) {
  return request({
    url: "main/apis/",
    method: "get",
    params: { category },
  });
}

export function detailApiApi(id) {
  return request({
    url: "main/apis/" + id + "/",
    method: "get",
  });
}

export function listCategoryApiApi(category) {
  return request({
    url: "main/categorie_apis/",
    method: "get",
    params: { category },
  });
}

export function apiSendApi(data) {
  return request({
    url: "main/api_send/",
    method: "post",
    data,
  });
}
