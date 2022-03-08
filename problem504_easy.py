# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2022/3/7 10:14
"""
"""
给定一个整数 num，将其转化为 7 进制，并以字符串形式输出。

输入: num = 100
输出: "202"

输入: num = -7
输出: "-10"
"""
"""
思路：每次模7即可，负数先当做正数处理，然后在前面添加负号即可
"""


class Solution(object):
    @staticmethod
    def convert_to_base_7(num):
        """
        :type num: int
        :rtype: str
        """
        if num == 0:
            return str(0)
        is_negative = False
        if num < 0:
            is_negative = True
        num = abs(num)
        res = []
        while num:
            remainder = num % 7
            num = num // 7
            res.insert(0, str(remainder))
        res_str = ''.join(res)
        return res_str if not is_negative else '-' + res_str
