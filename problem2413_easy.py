# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2023/4/21 11:00
"""
"""
给你一个正整数 n ，返回 2 和 n 的最小公倍数（正整数）。

示例 1：
输入：n = 5
输出：10
解释：5 和 2 的最小公倍数是 10 。

示例 2：
输入：n = 6
输出：6
解释：6 和 2 的最小公倍数是 6 。注意数字会是它自身的倍数。
"""
"""
思路：如果n是2的倍数就返回n，否则返回2*n
"""


class Solution:
    @staticmethod
    def smallestEvenMultiple(n: int) -> int:
        if n % 2 == 0:
            return n
        else:
            return 2 * n
