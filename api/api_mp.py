import api
import requests


class ApiMp:

    def __init__(self):
        api.log.info("正在初始化url")
        self.url_login = api.host + '/mp/v1_0/authorizations'
        self.url_article = api.host + '/mp/v1_0/articles'

    def api_mp_login(self, mobile, code):
        api.log.info("正在调用登录接口")
        data = {"mobile": mobile, "code": code}
        return requests.post(url=self.url_login, json=data, headers=api.headers)

    def api_mp_article(self, title, content, channel_id):
        api.log.info("正在调用发布文章接口")
        data = {"title": title, "content": content, "channel_id": channel_id, "cover": {"type": 0, "images": []}}
        return requests.post(url=self.url_article, json=data, headers=api.headers)
