import time

import requests

import api


class ApiApp:

    def __init__(self):
        api.log.info("正在初始化url")
        self.url_login = api.host + '/app/v1_0/authorizations'
        self.url_article = api.host + '/app/v1_0/articles'

    def api_app_login(self, mobile, code):
        api.log.info("正在调用登录接口")
        data = {"mobile": mobile, "code": code}
        return requests.post(url=self.url_login, json=data, headers=api.headers)

    def api_app_article(self):
        api.log.info("正在调用查看文章接口")
        data = {"channel_id": api.channel_id, "timestamp": int(time.time()), "with_top": 1}
        requests.get(url=self.url_article, params=data, headers=api.headers)
