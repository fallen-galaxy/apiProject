from tool.get_log import GetLog
from tool.read_yaml import read_yaml

log = GetLog.get_logger()

"""配置公共变量"""

host = "http://ttapi.research.itcast.cn"
headers = {"Content-Type": "application/json"}

data_article = read_yaml('mp_article.yaml')
article_id = None
title = data_article[0][0]
content = data_article[0][1]
channel_id = data_article[0][2]
channel = data_article[0][3]
