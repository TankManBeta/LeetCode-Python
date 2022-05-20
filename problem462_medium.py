# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2022/5/20 12:48
"""
"""
给你一个长度为 n 的整数数组 nums ，返回使所有数组元素相等需要的最少移动数。
在一步操作中，你可以使数组中的一个元素加 1 或者减 1 。

输入：nums = [1,2,3]
输出：2
解释：
只需要两步操作（每步操作指南使一个元素加 1 或减 1）：
[1,2,3]  =>  [2,2,3]  =>  [2,2,2]

输入：nums = [1,10,2,9]
输出：16
"""
"""
思路：先排序，再取中位数，计算将所有数字移动到中位数需要移动多少次，并累加
"""


class Solution(object):
    @staticmethod
    def minMoves2(nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        return sum(abs(num - nums[len(nums) // 2]) for num in nums)
