# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2022/3/28 10:11
"""
"""
给定一个正整数，检查它的二进制表示是否总是 0、1 交替出现：换句话说，就是二进制表示中相邻两位的数字永不相同。

输入：n = 5
输出：true
解释：5 的二进制表示是：101

输入：n = 7
输出：false
解释：7 的二进制表示是：111.

输入：n = 11
输出：false
解释：11 的二进制表示是：1011.
"""
"""
思路：首先n^(n>>1)，变成全1，然后再和n+1进行与，如果全0说明是交替出现的
"""


class Solution(object):
    @staticmethod
    def hasAlternatingBits(n):
        """
        :type n: int
        :rtype: bool
        """
        a = n ^ (n >> 1)
        return a & (a+1) == 0
