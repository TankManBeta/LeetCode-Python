# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2023/5/10 11:30
"""
import bisect
from typing import List

"""
给你一个整数数组 nums 以及两个整数 lower 和 upper 。求数组中，值位于范围 [lower, upper] （包含 lower 和 upper）之内的 区间和的个数 。
区间和 S(i, j) 表示在 nums 中，位置从 i 到 j 的元素之和，包含 i 和 j (i ≤ j)。

示例 1：
输入：nums = [-2,5,-1], lower = -2, upper = 2
输出：3
解释：存在三个区间：[0,0]、[2,2] 和 [0,2] ，对应的区间和分别是：-2 、-1 、2 。

示例 2：
输入：nums = [0], lower = 0, upper = 0
输出：1
"""
"""
思路：
（1）直接前缀和暴力，60/67超时。
（2）使用前缀数组pre，然后每个前缀和pre[i]二分查找前面i−1个和的pre[i]−lower和pre[i]−upper的位置得出区间和的数量，然后把pre[i]二分插入到数组中保持数组有序
"""


class Solution:
    @staticmethod
    def countRangeSum(nums: List[int], lower: int, upper: int) -> int:
        # n = len(nums)
        # pre = [0]
        # for i in range(n):
        #     pre.append(nums[i]+pre[-1])
        # option = []
        # for i in range(n):
        #     for j in range(i+1, n+1):
        #         range_sum = pre[j] - pre[i]
        #         if lower <= range_sum <= upper:
        #             option.append(range_sum)
        # return len(option)

        res, pre, now = 0, [0], 0
        for n in nums:
            now += n
            res += bisect.bisect_right(pre, now - lower) - bisect.bisect_left(pre, now - upper)
            bisect.insort(pre, now)
        return res
