# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2022/11/22 11:45
"""
"""
给你四个整数：n 、a 、b 、c ，请你设计一个算法来找出第 n 个丑数。
丑数是可以被 a 或 b 或 c 整除的 正整数 。

示例 1：
输入：n = 3, a = 2, b = 3, c = 5
输出：4
解释：丑数序列为 2, 3, 4, 5, 6, 8, 9, 10... 其中第 3 个是 4。

示例 2：
输入：n = 4, a = 2, b = 3, c = 4
输出：6
解释：丑数序列为 2, 3, 4, 6, 8, 9, 10, 12... 其中第 4 个是 6。

示例 3：
输入：n = 5, a = 2, b = 11, c = 13
输出：10
解释：丑数序列为 2, 4, 6, 8, 10, 11, 12, 13... 其中第 5 个是 10。

示例 4：
输入：n = 1000000000, a = 2, b = 217983653, c = 336916467
输出：1999999984
"""
"""
思路：容斥原理+二分查找，和878题一个意思
"""


def lcm(*args):
    return 0


class Solution:
    @staticmethod
    def nthUglyNumber(n: int, a: int, b: int, c: int) -> int:
        l = min(a, b, c)
        r = n * min(a, b, c)
        n1 = lcm(a, b)
        n2 = lcm(a, c)
        n3 = lcm(b, c)
        n4 = lcm(a, b, c)
        while l <= r:
            mid = (l + r) // 2
            cnt = mid // a + mid // b + mid // c - mid // n1 - mid // n2 - mid // n3 + mid // n4
            if cnt >= n:
                r = mid - 1
            else:
                l = mid + 1
        return r + 1
