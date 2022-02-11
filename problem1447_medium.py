# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2022/2/10 11:19
"""
"""
给你一个整数 n ，请你返回所有 0 到 1 之间（不包括 0 和 1）满足分母小于等于n 的最简分数 。分数可以以任意顺序返回。

输入：n = 2
输出：["1/2"]
解释："1/2" 是唯一一个分母小于等于 2 的最简分数。

输入：n = 3
输出：["1/2","1/3","2/3"]

输入：n = 4
输出：["1/2","1/3","1/4","2/3","3/4"]
解释："2/4" 不是最简分数，因为它可以化简为 "1/2" 。

输入：n = 1
输出：[]
"""
"""
思路：遍历1-n，算gcd即可
"""


class Solution(object):
    @staticmethod
    def simplified_fractions(n):
        """
        :type n: int
        :rtype: List[str]
        """

        def gcd(a, b):
            return a if b == 0 else gcd(b, a % b)

        res = []
        for i in range(2, n + 1):
            for j in range(1, i):
                if gcd(i, j) == 1:
                    res.append(str(j) + '/' + str(i))
        return res
