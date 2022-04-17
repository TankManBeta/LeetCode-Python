# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2022/4/16 14:09
"""
"""
给定一个整数 n ，返回 可表示为两个 n 位整数乘积的 最大回文整数 。因为答案可能非常大，所以返回它对 1337 取余 。

输入：n = 2
输出：987
解释：99 x 91 = 9009, 9009 % 1337 = 987

输入： n = 1
输出： 9
"""
"""
思路：先构造回文数，然后看能否变成两个整数乘积即可
"""


class Solution:
    @staticmethod
    def largestPalindrome(n):
        if n == 1:
            return 9
        max_ = 10 ** n - 1
        min_ = 10 ** (n - 1)
        for i in range(max_, min_ - 1, -1):
            num, temp = i, i
            while temp:
                num = num * 10 + temp % 10
                temp //= 10
            for j in range(max_, i, -1):
                if num % j == 0:
                    return num % 1337
