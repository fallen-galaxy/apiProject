import api
import requests


class ApiMis:

    def __init__(self):
        api.log.info("正在初始化url")
        self.url_login = api.host + '/mis/v1_0/authorizations'
        self.url_search = api.host + '/mis/v1_0/articles'
        self.url_audit = api.host + '/mis/v1_0/articles'

    def api_mis_login(self, account, password):
        api.log.info("正在调用登录接口")
        data = {"account": account, "password": password}
        return requests.post(url=self.url_login, json=data, headers=api.headers)

    def api_mis_search(self):
        api.log.info("正在调用查询文章接口")
        data = {"title": api.title, "channel": api.channel}
        return requests.get(url=self.url_search, params=data, headers=api.headers)

    def api_mis_audit(self):
        api.log.info("正在调用审核文章接口")
        data = {"article_ids": [api.article_id], "status": 2}
        return requests.put(url=self.url_audit, json=data, headers=api.headers)