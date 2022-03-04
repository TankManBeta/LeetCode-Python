# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2022/3/3 9:48
"""
"""
给定一个非负整数 num，反复将各个位上的数字相加，直到结果为一位数。返回这个结果。

输入: num = 38
输出: 2 
解释: 各位相加的过程为：
38 --> 3 + 8 --> 11
11 --> 1 + 1 --> 2
由于 2 是一位数，所以返回 2。

输入: num = 0
输出: 0
"""
"""
思路：num和num%9同余
"""


class Solution(object):
    @staticmethod
    def add_digits(num):
        """
        :type num: int
        :rtype: int
        """
        return (num - 1) % 9 + 1 if num else 0
