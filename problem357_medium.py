# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2022/4/11 10:07
"""
"""
给你一个整数 n ，统计并返回各位数字都不同的数字 x 的个数，其中 0 <= x < 10^n 。

输入：n = 2
输出：91
解释：答案应为除去 11、22、33、44、55、66、77、88、99 外，在 0 ≤ x < 100 范围内的所有数字。

输入：n = 0
输出：1
"""
"""
思路：一位数，两位数，n位数的结果累加起来即可。
"""


class Solution(object):
    @staticmethod
    def countNumbersWithUniqueDigits(n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 1
        if n == 1:
            return 10
        res = 10
        option = 9
        for i in range(1, n):
            option = option*(10-i)
            res += option
        return res
