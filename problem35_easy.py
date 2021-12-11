# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2021/12/7 13:09
"""
"""
给定一个排序数组和一个目标值，在数组中找到目标值，并返回其索引。如果目标值不存在于数组中，返回它将会被按顺序插入的位置。
请必须使用时间复杂度为 O(log n) 的算法。

输入: nums = [1,3,5,6], target = 5
输出: 2

输入: nums = [1,3,5,6], target = 2
输出: 1

输入: nums = [1,3,5,6], target = 7
输出: 4

输入: nums = [1,3,5,6], target = 0
输出: 0

输入: nums = [1], target = 0
输出: 0
"""
"""
思路：二分查找，如果mid的值正好等于target，返回mid；如果mid值小于target，left变为mid+1；否则right变为mid-1，最后返回left
"""


class Solution(object):
    @staticmethod
    def search_insert(nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left = 0
        right = len(nums)-1
        while left <= right:
            mid = (left+right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return left
