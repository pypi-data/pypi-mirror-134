import re
import ast
import importlib
import types
import os
import inspect

# compile 方法正则表达 至于用不用可行选择
# 解析 ${func_name(args1,args2,...,**kwargs)}
_func_compile = re.compile(r'\${([\w_]+)\(([$\w.\-/_ =,]*)\)}$')


def ab(q, w=1):
    return q + w


func = {"ab": ab}


# 标志模式${func(args1,args2,...,**kwages)}
def _parse_function(content):
    # 匹配函数正则
    matched = _func_compile.match(content)
    func_meta = {
        "func_name": matched.group(1),
        "args": [],
        "kwargs": {}
    }
    # 去除字符串中的所有空格
    args_str = matched.group(2).replace(" ", "")
    if args_str == "":
        return func_meta
    # 遍历args_str.split结果,这是一个list.
    for arg in re.split(',', args_str):
        if "=" in arg:
            # 如果是arg中存在= 判定为缺省参数中
            key, value = re.split('=', arg)
            func_meta["kwargs"][key] = ast.literal_eval(arg)
        else:
            func_meta["args"].append(ast.literal_eval(arg))

    return func_meta


# e.g. ${func_name(1,2,3,...)}
def run_func(func_name):
    # 解析函数字符串
    func_info_dict = _parse_function(func_name)
    # 提取function name信息
    f_name = func_info_dict["func_name"]
    if f_name in func.keys():
        if inspect.getfullargspec(func[f_name]).varkw:
            return func[f_name](*func_info_dict["args"], **func_info_dict["kwargs"])
        return func[f_name](*func_info_dict["args"])
    else:
        raise NameError(f"不存在 {f_name}方法")


def registe_function(func_dict):
    if isinstance(func_dict, dict) and func_dict is not None:
        func.update(func_dict)
# if __name__ == '__main__':
#     print(run_func("${ab(1)}"))
#     # a(*[1, 3], **{"ss": 1})
