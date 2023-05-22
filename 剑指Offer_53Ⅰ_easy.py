# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2023/5/19 11:23
"""
from bisect import bisect_left, bisect_right
from typing import List

"""
统计一个数字在排序数组中出现的次数。

示例 1:
输入: nums = [5,7,7,8,8,10], target = 8
输出: 2

示例 2:
输入: nums = [5,7,7,8,8,10], target = 6
输出: 0
"""
"""
思路：二分查找左右两个边界，然后判断左右两个边界相等的话说明没有，否则说明存在
"""


class Solution:
    @staticmethod
    def search(nums: List[int], target: int) -> int:
        n1 = bisect_left(nums, target)
        n2 = bisect_right(nums, target)
        if n1 == n2:
            return 0
        else:
            return n2 - n1
