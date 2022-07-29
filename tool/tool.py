import api
import tool


class Tool:

    @classmethod
    def common_token(cls, response):
        tool.log.info("正在提取token")
        token = response.json().get('data').get('token')
        api.headers['Authorization'] = 'Bearer ' + token

    @classmethod
    def common_assert(cls, response, status_code=201):
        tool.log.info("正在进行断言")
        assert status_code == response.status_code
