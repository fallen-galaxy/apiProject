import pytest

import api
import case
from api.api_mp import ApiMp
from tool.read_yaml import read_yaml
from tool.tool import Tool


class TestMp:

    def setup_class(self):
        self.mp = ApiMp()

    @pytest.mark.parametrize("mobile,code", read_yaml('mp_login.yaml'))
    def test_01_mp_login(self, mobile, code):
        resp = self.mp.api_mp_login(mobile, code)
        print(resp.text)
        try:
            Tool.common_token(resp)
            Tool.common_assert(resp)
        except Exception as e:
            case.log.error("断言出错：{}".format(e))
            raise

    def test_02_mp_article(self, title=api.title, content=api.content, channel_id=api.channel_id):
        resp = self.mp.api_mp_article(title, content, channel_id)
        api.article_id = resp.json().get('data').get('id')
        try:
            Tool.common_assert(resp)
        except Exception as e:
            case.log.error("断言出错：{}".format(e))
            raise
