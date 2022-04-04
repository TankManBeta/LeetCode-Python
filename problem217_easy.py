# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2022/4/3 13:46
"""
"""
给你一个整数数组 nums 。如果任一值在数组中出现 至少两次 ，返回 true ；如果数组中每个元素互不相同，返回 false 。

输入：nums = [1,2,3,1]
输出：true

输入：nums = [1,2,3,4]
输出：false

输入：nums = [1,1,1,3,3,4,3,2,4,2]
输出：true
"""
"""
思路：直接用set，然后判断长度是否相同即可
"""


class Solution(object):
    @staticmethod
    def containsDuplicate(nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        m = len(nums)
        n = len(list(set(nums)))
        return m != n
