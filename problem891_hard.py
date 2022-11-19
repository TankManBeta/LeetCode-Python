# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2022/11/18 11:22
"""
from typing import List

"""
一个序列的 宽度 定义为该序列中最大元素和最小元素的差值。
给你一个整数数组 nums ，返回 nums 的所有非空 子序列 的 宽度之和 。由于答案可能非常大，请返回对 10**9 + 7 取余 后的结果。
子序列 定义为从一个数组里删除一些（或者不删除）元素，但不改变剩下元素的顺序得到的数组。
例如，[3,6,2,7] 就是数组 [0,3,1,6,2,2,7] 的一个子序列。

示例 1：
输入：nums = [2,1,3]
输出：6
解释：子序列为 [1], [2], [3], [2,1], [2,3], [1,3], [2,1,3] 。
相应的宽度是 0, 0, 0, 1, 1, 2, 2 。
宽度之和是 6 。

示例 2：
输入：nums = [2]
输出：0
"""
"""
思路：先对数组排序，然后看每一个数字做了多少次大哥和多少次小弟，做大哥的次数就是前面的子集的个数，做小弟的次数就是后面的子集的
个数，然后相减乘以自身就是自己的贡献。
"""


class Solution:
    @staticmethod
    def sumSubSequenceWidths(nums: List[int]) -> int:
        MOD = 10 ** 9 + 7
        nums.sort()
        n = len(nums)
        res = [0]*n
        res[0] = 1
        for i in range(1, n):
            res[i] = 2*res[i-1] % MOD
        return sum((res[i] - res[-1 - i]) * num for i, num in enumerate(nums)) % MOD
