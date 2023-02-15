# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2023/2/14 11:35
"""
"""
给定一个整数，写一个函数来判断它是否是 3 的幂次方。如果是，返回 true ；否则，返回 false 。
整数 n 是 3 的幂次方需满足：存在整数 x 使得 n == 3x 

示例 1：
输入：n = 27
输出：true

示例 2：
输入：n = 0
输出：false

示例 3：
输入：n = 9
输出：true

示例 4：
输入：n = 45
输出：false
"""
"""
思路：
（1）递归看是否是3的倍数
（2）看一个数是否是范围内3的最大幂的因数
"""


class Solution:
    @staticmethod
    def isPowerOfThree(n: int) -> bool:
        # while n and n % 3 == 0:
        #     n //= 3
        # return n == 1

        return n > 0 and 1162261467 % n == 0
