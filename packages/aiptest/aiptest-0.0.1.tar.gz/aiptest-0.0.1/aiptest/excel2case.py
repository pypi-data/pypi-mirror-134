"""
@version: V0.5.1
"""
from .function import run_func
from .api import GDWH
import re


# 标签分析并且转换
def resolve_case(case):
    output_dict = {}
    # 期望
    expected = case.pop('expected')
    # global
    global_var = case.pop('globalVar')
    if expected:
        # 将期望解析成list
        output_dict['expected'] = _case_str_tolist(expected)
    if global_var:
        output_dict['globalVar'] = _case_str_tolist(global_var)

    for k, v in case.items():
        if "$" in v:
            output_dict[k] = _parse_flag(v)
        elif v == "":
            pass
        else:
            output_dict[k] = _change_data(v)
    return output_dict


# 用于解析excel中期望值和，全局变量获取
def _case_str_tolist(data: str) -> list:
    if data:
        final_data = []
        for list_child_str in list(filter(lambda x: x, re.split(';', data))):
            item_list = re.split(',', list_child_str)
            if len(item_list) == 1:
                item_list = re.split('=', list_child_str)
            final_data.append(item_list)
            return final_data
    return ""


# 解析函数、变量标记
# e.g. ${global var},${getnum()}
def _parse_flag(flag_data: str):
    all_flag_list = re.findall(r'\$.*?}', flag_data)
    if len(all_flag_list) == len(re.findall(r'\$.*?{', flag_data)):
        for flag in all_flag_list:
            l_ = flag.find("(")
            r_ = flag.find(")")
            if l_ == -1 and r_ == -1:
                # 从全局变量中获取数据
                return flag_data.replace(flag, str(GDWH.select('GLOBALS')[flag[2:-1]]))
            elif l_ == -1 and r_ != -1 or l_ != -1 and r_ == -1:
                raise ValueError(f"数据错误！请检查数据是否正确{flag_data}")
            else:
                return run_func(flag_data)
    else:
        raise ValueError(f'参数{flag_data}中大括号标记不是成对出现的请检查case')


def _change_data(data: str) -> str or dict or list:
    try:
        if isinstance(data, str):
            if re.findall(r'^[{](.*)[}]$', data) or re.findall(r'^[[](.*)[]]$', data):  # ast str转list和dict
                # output_data = ast.literal_eval(data)
                output_data = eval(data) 
            elif '=' in data and ';' != data[-1]:
                output_data = dict(i.split('=') for i in data.split(','))  # 将a=b,c=d 转化成字典
            elif ';' == data[-1]:
                output_data = _case_str_tolist(data)
            else:
                output_data = data
            return output_data
    except SyntaxError:
        raise SyntaxError(f"解析数据{data}，时发生错误，请检查数据!")
    except ValueError:
        raise ValueError(f"解析数据{data}，时发生错误，请检查数据!")
