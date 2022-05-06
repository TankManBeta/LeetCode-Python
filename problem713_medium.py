# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2022/5/5 10:00
"""
"""
给你一个整数数组 nums 和一个整数 k ，请你返回子数组内所有元素的乘积严格小于 k 的连续子数组的数目。

输入：nums = [10,5,2,6], k = 100
输出：8
解释：8 个乘积小于 100 的子数组分别为：[10]、[5]、[2],、[6]、[10,5]、[5,2]、[2,6]、[5,2,6]。
需要注意的是 [10,5,2] 并不是乘积小于 100 的子数组。

输入：nums = [1,2,3], k = 0
输出：0
"""
"""
思路：枚举子数组的右端点 j，并且左端点从 i = 0 开始，用 prod 记录子数组 [i, j] 的元素乘积。每枚举一个右端点 j，如果当前子数组元素乘积 
prod 大于等于 k，那么我们右移左端点 i 直到满足当前子数组元素乘积小于 k 或者i > j，那么元素乘积小于 k 的子数组数目为 j - i + 1。
返回所有数目之和。
"""


class Solution(object):
    @staticmethod
    def numSubarrayProductLessThanK(nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        ans, prod, i = 0, 1, 0
        for j, num in enumerate(nums):
            prod *= num
            while i <= j and prod >= k:
                prod //= nums[i]
                i += 1
            ans += j - i + 1
        return ans
