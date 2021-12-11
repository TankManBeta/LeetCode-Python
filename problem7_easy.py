# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2021/10/29 10:11
"""
"""
给你一个 32 位的有符号整数x，返回将x中的数字部分反转后的结果。
如果反转后整数超过32位的有符号整数的范围[−2**31, 2**31−1]，就返回0。
假设环境不允许存储64位整数（有符号或无符号）。

输入：x = 123
输出：321

输入：x = -123
输出：-321

输入：x = 120
输出：21

输入：x = 0
输出：0
"""
"""
思路：用一个字符串存反转后的数，然后再转成整数，每次把余数加入字符串，被除数除以10，直到被除数为0。
"""


class Solution(object):
    @staticmethod
    def reverse(x):
        """
        :type x: int
        :rtype: int
        """
        INT_MAX = 2**31-1
        INT_MIN = -2**31
        dividend = x if x > 0 else -x
        remainder_str = ""
        if dividend == 0:
            return dividend
        while dividend != 0:
            remainder = dividend % 10
            remainder_str += str(remainder)
            dividend = dividend / 10
        final_num = int(remainder_str) if x > 0 else -int(remainder_str)
        if INT_MIN <= final_num <= INT_MAX:
            return final_num
        else:
            return 0
