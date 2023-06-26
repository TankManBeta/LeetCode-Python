# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2023/6/25 10:50
"""
from typing import List

"""
给你一个整数数组 nums ，其中总是存在 唯一的 一个最大整数 。
请你找出数组中的最大元素并检查它是否 至少是数组中每个其他数字的两倍 。如果是，则返回 最大元素的下标 ，否则返回 -1 。 

示例 1：
输入：nums = [3,6,1,0]
输出：1
解释：6 是最大的整数，对于数组中的其他整数，6 至少是数组中其他元素的两倍。6 的下标是 1 ，所以返回 1 。

示例 2：
输入：nums = [1,2,3,4]
输出：-1
解释：4 没有超过 3 的两倍大，所以返回 -1 。

示例 3：
输入：nums = [1]
输出：0
解释：因为不存在其他数字，所以认为现有数字 1 至少是其他数字的两倍。
"""
"""
思路：只需要找到第一大和第二大的数字，然后比较第一大的数字是否至少是第二大的数字的两倍即可。所以我们维护max1，max2，index1分别
代指最大值，第二大值以及最大值的下标，如果当前数比最大值大，说明当前数是最大值，最大值就变成了第二大值；如果当前值比第二大值大，
就只需要更新第二大值，因为最大值没变。
"""


class Solution:
    @staticmethod
    def dominantIndex(nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        index1 = -1, -1
        max1, max2 = -1, -1
        for i, num in enumerate(nums):
            if num > max1:
                max2 = max1
                max1 = num
                index1 = i
            elif num > max2:
                max2 = num
        return index1 if max1 >= 2 * max2 else -1
