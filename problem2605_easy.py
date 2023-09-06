# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2023/9/5 18:41
"""
from typing import List

"""
给你两个只包含 1 到 9 之间数字的数组 nums1 和 nums2 ，每个数组中的元素 互不相同 ，请你返回 最小 的数字，两个数组都 至少 包含这个数字的某个数位。

示例 1：
输入：nums1 = [4,1,3], nums2 = [5,7]
输出：15
解释：数字 15 的数位 1 在 nums1 中出现，数位 5 在 nums2 中出现。15 是我们能得到的最小数字。

示例 2：
输入：nums1 = [3,5,2,6], nums2 = [3,1,7]
输出：3
解释：数字 3 的数位 3 在两个数组中都出现了。
"""
"""
思路：如果两个列表有交集，返回交集中的最小值；否则排序，返回两个列表中的最小值，然后构成一个最小的数
"""


class Solution:
    @staticmethod
    def minNumber(nums1: List[int], nums2: List[int]) -> int:
        set1 = set(nums1)
        set2 = set(nums2)
        intersection = set1 & set2
        if intersection:
            return min(intersection)
        else:
            nums1 = sorted(nums1)
            nums2 = sorted(nums2)
            min_val = min(nums1[0], nums2[0])
            max_val = max(nums1[0], nums2[0])
            return min_val * 10 + max_val
