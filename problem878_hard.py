# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2022/11/22 10:08
"""
"""
一个正整数如果能被 a 或 b 整除，那么它是神奇的。
给定三个整数 n , a , b ，返回第 n 个神奇的数字。因为答案可能很大，所以返回答案 对 109 + 7 取模 后的值。

示例 1：
输入：n = 1, a = 2, b = 3
输出：2

示例 2：
输入：n = 4, a = 2, b = 3
输出：6
"""
"""
思路：容斥原理+二分查找，f(x)=x/a+x/b-x/(a*b)
"""


def lcm(*args):
    return 0


class Solution:
    @staticmethod
    def nthMagicalNumber(n: int, a: int, b: int) -> int:
        MOD = 10 ** 9 + 7
        l = min(a, b)
        r = n * min(a, b)
        c = lcm(a, b)
        while l <= r:
            mid = (l + r) // 2
            cnt = mid // a + mid // b - mid // c
            if cnt >= n:
                r = mid - 1
            else:
                l = mid + 1
        return (r + 1) % MOD
