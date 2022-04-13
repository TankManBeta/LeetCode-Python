# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2022/4/12 11:01
"""
"""
丑数 就是只包含质因数 2、3 和 5 的正整数。
给你一个整数 n ，请你判断 n 是否为 丑数 。如果是，返回 true ；否则，返回 false 。

输入：n = 6
输出：true
解释：6 = 2 × 3

输入：n = 1
输出：true
解释：1 没有质因数，因此它的全部质因数是 {2, 3, 5} 的空集。习惯上将其视作第一个丑数。

输入：n = 14
输出：false
解释：14 不是丑数，因为它包含了另外一个质因数 7 。
"""
"""
思路：对于每一个因子，用num将这个因子除干净，然后再处理下一个因子
"""


class Solution(object):
    @staticmethod
    def isUgly(n):
        """
        :type n: int
        :rtype: bool
        """
        if n <= 0:
            return False
        factors = [2, 3, 5]
        for factor in factors:
            while n % factor == 0:
                n //= factor
        return n == 1
