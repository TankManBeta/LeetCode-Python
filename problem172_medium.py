# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2022/3/21 9:56
"""
"""
给定一个整数 n ，返回 n! 结果中尾随零的数量。
提示 n! = n * (n - 1) * (n - 2) * ... * 3 * 2 * 1

输入：n = 3
输出：0
解释：3! = 6 ，不含尾随 0

输入：n = 5
输出：1
解释：5! = 120 ，有一个尾随 0

输入：n = 0
输出：0
"""
"""
思路：计算因子5的个数即可
"""


class Solution(object):
    @staticmethod
    def trailingZeroes(n):
        """
        :type n: int
        :rtype: int
        """
        res = 0
        while n != 0:
            n //= 5
            res += n
        return res
