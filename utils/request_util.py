import json
from typing import Dict

from django.contrib.contenttypes.models import ContentType
from django.http import HttpResponse
from requests import request, Response

from main.models import Api, Env


def request_by_api(env: Env, api: Dict) -> Response:
    return request_by_domain(domain=env.domain,
                             protocol=env.protocol,
                             port=env.port,
                             path=api["path"],
                             params=api["params"],
                             body=api["body"],
                             body_type=api["body_type"],
                             headers=api["headers"],
                             method=api["method"]
                             )


def request_by_domain(
        domain: str,
        port: str,
        path: str,
        params: str,
        body: str,
        headers: str,
        protocol: str = "HTTP",
        body_type: str = "NONE",
        method: str = "GET") -> Response:
    url = f"{protocol.lower()}://{domain}"
    if port:
        url += f":{port}"
    url += path
    req_params = {}
    if len(params) > 0:
        for param in params:
            req_params[param['param_key']] = param['value']
    req_headers = {}
    if len(headers) > 0:
        for header in headers:
            req_headers[header['param_key']] = header['value']
    if method == "GET":
        return request(method, url, headers=req_headers, params=req_params)
    else:
        if body_type == "JSON":
            return request(method=method, url=url, params=params, headers=headers, json=body)
        else:
            return request(method=method, url=url, params=params, headers=headers, data=body)


def request_by_url():
    pass


def response_handler(resp:Response):
    # 进行请求封装
    result = {
        "body": resp.content,
        "headers": resp.headers,
        "content": f"""
        {resp.request.method} {resp.request.url} {resp.status_code}\n
        {resp.request.headers} \n
        {resp.request.body} \n
        {resp.raw}
        """
    }
    return result
