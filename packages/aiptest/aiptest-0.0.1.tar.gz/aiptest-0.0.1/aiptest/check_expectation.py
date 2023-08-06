"""
@author: del
@file: rule_verification.py
@time: 2020/3/111:55
@IDE: PyCharm
@version: V0.5.1
"""
import pytest


def _eq(actual_value, expect_value):
    pytest.assume(actual_value == expect_value,
                  f'期望值：{str(type(expect_value))[8:-2]}({expect_value})  不等于  实际值：{str(type(actual_value))[8:-2]}({actual_value})  ')


def _neq(actual_value, expect_value):
    pytest.assume(actual_value != expect_value,
                  f'期望值：{str(type(expect_value))[8:-2]} ({expect_value}) 等于 实际值：{str(type(actual_value))[8:-2]}({actual_value})  ')


def _gt(actual_value, expect_value):
    pytest.assume(actual_value > expect_value,
                  f'期望值：{str(type(expect_value))[8:-2]} ({expect_value}) 小于等于 实际值：{str(type(actual_value))[8:-2]}({actual_value})  ')


def _gte(actual_value, expect_value):
    pytest.assume(actual_value >= expect_value,
                  f'期望值：{str(type(expect_value))[8:-2]}({expect_value}) 小于 实际值：{str(type(actual_value))[8:-2]}({actual_value}) ')


def _lt(actual_value, expect_value):
    pytest.assume(actual_value < expect_value,
                  f'期望值：{str(type(expect_value))[8:-2]}({expect_value}) 大于等于 实际值：{str(type(actual_value))[8:-2]}({actual_value}) ')


def _lte(actual_value, expect_value):
    pytest.assume(actual_value <= expect_value,
                  f'期望值：{str(type(expect_value))[8:-2]}({expect_value}) 大于 实际值：{str(type(actual_value))[8:-2]}({actual_value}) ')


rule = {
    "==": _eq,
    "!=": _neq,
    ">": _gt,
    ">=": _gte,
    "<": _lt,
    "<=": _lte,
}


# 注册函数
# e.g. registe_check_expectation({"not_in":func_name})
def registe_check_expectation(rule_dict):
    if isinstance(rule_dict, dict) and rule_dict is not None:
        rule.update(rule_dict)
