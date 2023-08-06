"""
@author: Del
@contact: delfung@163.com
@time  : 2020/2/29
@file  : Flogger.py
@desc  :
0.1 添加两种logger流
"""
import logging
from logging.handlers import TimedRotatingFileHandler
import pathlib


class Logger(object):
    def __init__(self, file_path=r'./'):
        self.logger = logging.getLogger('log')  # 创建logger 参数为空返回root
        self.logger.setLevel(logging.DEBUG)
        self.FORMATTER = logging.Formatter(fmt="[%(asctime)s %(levelname)s] %(message)s",
                                           datefmt="%Y-%m-%d %X")  # 输出格式
        info = rf'{file_path}/log/log.log'
        self._mkdir(info)
        self.FileHandler = TimedRotatingFileHandler(info, when='midnight', encoding='utf-8')  # 创建Handler
        self.FileHandler.setFormatter(self.FORMATTER)  # 设置输出格式

    def _set_handler(self):
        self.logger.addHandler(self.FileHandler)

    def _remove_handler(self):
        self.logger.removeHandler(self.FileHandler)

    @staticmethod
    def _mkdir(file_name):
        parent_path = pathlib.Path(file_name).parent
        if not parent_path.is_dir():
            parent_path.mkdir(parents=True, exist_ok=True)
        if not pathlib.Path(file_name).is_file():
            fd = open(file_name, mode='w', encoding='utf-8')
            fd.close()

    def debug(self, log_msg):
        self._set_handler()
        self.logger.debug(log_msg)
        self._remove_handler()

    def info(self, log_msg):
        self._set_handler()
        self.logger.info(log_msg)
        self._remove_handler()

    def warning(self, log_msg):
        self._set_handler()
        self.logger.warning(log_msg)
        self._remove_handler()

    def error(self, log_msg):
        self._set_handler()
        self.logger.error(log_msg)
        self._remove_handler()

    def critical(self, log_msg):
        self._set_handler()
        self.logger.critical(log_msg)
        self._remove_handler()
