# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2021/12/21 15:58
"""
"""
实现 pow(x, n) ，即计算 x 的 n 次幂函数（即，x^n）。

输入：x = 2.00000, n = 10
输出：1024.00000

输入：x = 2.10000, n = 3
输出：9.26100

输入：x = 2.00000, n = -2
输出：0.25000
"""
"""
思路：每次求floor(N/2)次方,如果当前次方是奇数则返回的时候要多乘x
"""


class Solution(object):
    @staticmethod
    def my_pow(x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """

        def quick_mul(degree):
            if degree == 0:
                return 1.0
            y = quick_mul(degree // 2)
            return y * y if degree % 2 == 0 else y * y * x

        return quick_mul(n) if n >= 0 else 1.0 / quick_mul(-n)
