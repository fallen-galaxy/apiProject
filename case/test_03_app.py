import pytest

import case
from api.api_app import ApiApp
from tool.read_yaml import read_yaml
from tool.tool import Tool


class TestApp:

    def setup_class(self):
        self.app = ApiApp()

    @pytest.mark.parametrize("mobile,code", read_yaml('mp_login.yaml'))
    def test_01_app_login(self, mobile, code):
        resp = self.app.api_app_login(mobile, code)
        Tool.common_token(resp)
        try:
            Tool.common_assert(resp)
        except Exception as e:
            case.log.error("断言出错：{}".format(e))
            raise

    def test_02_app_article(self):
        resp = self.app.api_app_article()
        try:
            Tool.common_assert(response=resp, status_code=200)
        except Exception as e:
            case.log.error("断言出错：{}".format(e))
            raise
