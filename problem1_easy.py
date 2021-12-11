# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2021/10/27 21:36
"""
"""
给定一个整数数组nums和一个整数目标值target，请你在该数组中找出和为目标值target的那两个整数，并返回它们的数组下标。
你可以假设每种输入只会对应一个答案。但是，数组中同一个元素在答案里不能重复出现。
你可以按任意顺序返回答案。

输入：nums = [2,7,11,15], target = 9
输出：[0,1]
解释：因为 nums[0] + nums[1] == 9 ，返回 [0, 1] 。

输入：nums = [3,2,4], target = 6
输出：[1,2]

输入：nums = [3,3], target = 6
输出：[0,1]
"""
"""
思路：
（1）直接暴力
（2）直接哈希找，value变成index，index变成value
"""


class Solution(object):
    @staticmethod
    def two_sum(nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        result_dict = {}
        for index, value in enumerate(nums):
            result_dict[value] = index
        for index, value in enumerate(nums):
            j = result_dict.get(target - value)
            # 如果有两个数字相同，字典中存的位置是最新的，找结果时从头开始找，不会出现两个重复的数字找不到的问题
            if j is not None and index != j:
                return [index, j]
