import os

import pytest

# 执行用例
pytest.main()
# 生成报告
os.system("allure generate temp -o report --clean")
