# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2022/1/19 15:56
"""
"""
给你一个整数数组 nums 和一个整数 k ，判断数组中是否存在两个 不同的索引 i 和 j ，满足 nums[i] == nums[j] 且 abs(i - j) <= k。
如果存在，返回 true ；否则，返回 false 。

输入：nums = [1,2,3,1], k = 3
输出：true

输入：nums = [1,0,1,1], k = 1
输出：true

输入：nums = [1,2,3,1,2,3], k = 2
输出：false
"""
"""
思路：直接判断每一个位置上的是否在字典的键里，如果在的话计算两个位置的差值，如果<=k则返回，否则更新这个键所在的位置位最新访问的
"""


class Solution(object):
    @staticmethod
    def contains_nearby_duplicate(nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        res_dict = {}
        for i in range(0, len(nums)):
            if nums[i] in res_dict and i-res_dict[nums[i]] <= k:
                return True
            res_dict[nums[i]] = i
        return False
