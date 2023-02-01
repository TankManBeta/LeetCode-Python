# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2023/2/1 17:38
"""
from typing import List

"""
给定一个数组 nums ，将其划分为两个连续子数组 left 和 right， 使得：
    left 中的每个元素都小于或等于 right 中的每个元素。
    left 和 right 都是非空的。
    left 的长度要尽可能小。
在完成这样的分组后返回 left 的 长度 。
用例可以保证存在这样的划分方法。

示例 1：
输入：nums = [5,0,3,8,6]
输出：3
解释：left = [5,0,3]，right = [8,6]

示例 2：
输入：nums = [1,1,1,0,6,12]
输出：4
解释：left = [1,1,1,0]，right = [6,12]
"""
"""
思路：假设我们预先规定了一个 left 的划分，其最大值为 maxLeft，划分位置为 leftPos，表示 nums[0,leftPos] 都属于 left。如果 
leftPos 右侧所有元素都大于等于它，那么该划分方案是合法的。
但如果我们找到 nums[i]，其中 i>leftPos，并且 nums[i]<maxLeft，那么意味着 leftPos 作为划分位置是非法的，需要更新 leftPos=i，
以及 maxLeft=max(nums[i])(0-i中最大值)。
"""


class Solution:
    @staticmethod
    def partitionDisjoint(nums: List[int]) -> int:
        left_max = nums[0]
        cur_max = nums[0]
        pos = 0
        for i in range(1, len(nums)):
            cur_max = max(nums[i], cur_max)
            if nums[i] < left_max:
                pos = i
                left_max = cur_max
        return pos + 1
