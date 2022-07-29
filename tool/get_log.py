import logging.handlers
import os

from config import BASE_PATH


class GetLog:

    # 日志器变量
    __logger = None

    # 获取日志器
    @classmethod
    def get_logger(cls):
        # 使用同一个日志器
        if cls.__logger is None:
            # 获取日志器
            cls.__logger = logging.getLogger()
            # 设置日志级别
            cls.__logger.setLevel(logging.INFO)
            # 指定日志文件
            log_path = BASE_PATH + os.sep + "log" + os.sep + "operation.log"
            # 获取处理器
            th = logging.handlers.TimedRotatingFileHandler(filename=log_path,
                                                           when="midnight",
                                                           interval=1,
                                                           backupCount=3,
                                                           encoding="utf-8")
            # 指定日志格式
            fmt = "%(asctime)s %(levelname)s [%(filename)s(%(funcName)s:%(lineno)d)] - %(message)s"
            # 获取格式器
            fm = logging.Formatter(fmt)
            # 格式器添加到处理器
            th.setFormatter(fm)
            # 处理器添加到日志器
            cls.__logger.addHandler(th)
        # 返回日志器
        return cls.__logger
