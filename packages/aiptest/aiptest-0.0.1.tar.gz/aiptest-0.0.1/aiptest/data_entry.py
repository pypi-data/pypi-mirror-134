"""
@version: V0.5.1
"""
# 数据读取
import os
import pandas as pd
import yaml


def read_excel(file_path: str) -> list:
    cases_list = []
    df = pd.read_excel(file_path, engine='openpyxl', dtype='str', keep_default_na='').replace('\n', regex=True)
    # axis=1 按照列的方式作为字段 axis=0 按照行的方式作为字段
    # 遍历 dataframe 每一行数据，并且将每一行数据变成字典
    df.apply(lambda x: cases_list.append(x.to_dict()), axis=1)
    return cases_list


def read_json(file_path: str) -> dict:
    pass


def read_yaml(file_path) -> dict:
    """
    单个yaml文件读取，结果返回成字典格式
    :param file_path: （必须），文件路径，比如：D:xx/cc/config.yaml
    :return: {'a':'123','b':'234'}
    """
    return yaml.safe_load(open(file_path, 'r', encoding='utf-8'))
