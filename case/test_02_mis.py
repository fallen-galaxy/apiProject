import pytest
import case
from api.api_mis import ApiMis
from tool.read_yaml import read_yaml
from tool.tool import Tool


class TestMis:

    def setup_class(self):
        self.mis = ApiMis()

    @pytest.mark.parametrize("account,password", read_yaml('mis_login.yaml'))
    def test_01_mis_login(self, account, password):
        resp = self.mis.api_mis_login(account, password)
        Tool.common_token(resp)
        try:
            Tool.common_assert(resp)
        except Exception as e:
            case.log.error("断言出错：{}".format(e))
            raise

    def test_02_mis_search(self):
        resp = self.mis.api_mis_search()
        try:
            Tool.common_assert(response=resp, status_code=200)
        except Exception as e:
            case.log.error("断言出错：{}".format(e))
            raise

    def test_03_mis_audit(self):
        resp = self.mis.api_mis_audit()
        try:
            Tool.common_assert(resp)
        except Exception as e:
            case.log.error("断言出错：{}".format(e))
            raise

