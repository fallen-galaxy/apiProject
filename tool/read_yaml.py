import os

import yaml
import tool

from config import BASE_PATH


def read_yaml(filename):
    file_path = BASE_PATH + os.sep + "data" + os.sep + filename
    tuple_in_list = []
    tool.log.info("正在读取文件：{}".format(filename))
    with open(file_path, "rt", encoding="utf-8") as f:
        # 获取字典
        content = yaml.safe_load(f)
        tool.log.info("查看文件内容：{}".format(content))
        for datas in content.values():
            print(datas)
            tuple_in_list.append((tuple(datas.values())))
    tool.log.info("查看元组列表：{}".format(tuple_in_list))
    return tuple_in_list
