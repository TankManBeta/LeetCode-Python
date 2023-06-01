# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2023/5/31 10:57
"""
import functools
from typing import List

"""
输入一个非负整数数组，把数组里所有数字拼接起来排成一个数，打印能拼接出的所有数字中最小的一个。 

示例 1:
输入: [10,2]
输出: "102"

示例 2:
输入: [3,30,34,5,9]
输出: "3033459"
"""
"""
思路：使用自定义排序规则，如果x和y拼接的结果>y和x拼接的结果，则说明在这个排序规则之下x>y。例如x=3，y=30，330＞303，说明x＞y
"""


class Solution:
    @staticmethod
    def minNumber(nums: List[int]) -> str:
        def sort_rule(x, y):
            a, b = x + y, y + x
            if a > b:
                return 1
            elif a < b:
                return -1
            else:
                return 0

        strs = [str(num) for num in nums]
        strs.sort(key=functools.cmp_to_key(sort_rule))
        return ''.join(strs)
