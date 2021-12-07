# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2021/12/7 13:08
"""
"""
给定一个按照升序排列的整数数组 nums，和一个目标值 target。找出给定目标值在数组中的开始位置和结束位置。
如果数组中不存在目标值 target，返回 [-1, -1]。
进阶：
你可以设计并实现时间复杂度为 O(log n) 的算法解决此问题吗？

输入：nums = [5,7,7,8,8,10], target = 8
输出：[3,4]

输入：nums = [5,7,7,8,8,10], target = 6
输出：[-1,-1]

输入：nums = [], target = 0
输出：[-1,-1]
"""
"""
思路：二分查找，分别找第一个target和第一个target+1，注意结束和判断条件条件
"""


class Solution(object):
    @staticmethod
    def search_range(nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        def search_left(new_nums, new_target):
            n = len(new_nums) - 1
            left = 0
            right = n
            while left <= right:
                mid = (left+right) // 2
                if new_nums[mid] >= new_target:
                    right = mid-1
                else:
                    left = mid+1
            return left

        a = search_left(nums, target)
        b = search_left(nums, target+1)
        if a == len(nums) or nums[a] != target:
            return [-1, -1]
        else:
            return [a, b-1]
