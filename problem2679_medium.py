# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2023/7/4 19:16
"""
from typing import List

"""
给你一个下标从 0 开始的二维整数数组 nums 。一开始你的分数为 0 。你需要执行以下操作直到矩阵变为空：
    矩阵中每一行选取最大的一个数，并删除它。如果一行中有多个最大的数，选择任意一个并删除。
    在步骤 1 删除的所有数字中找到最大的一个数字，将它添加到你的 分数 中。
请你返回最后的 分数 。 

示例 1：
输入：nums = [[7,2,1],[6,4,2],[6,5,3],[3,2,1]]
输出：15
解释：第一步操作中，我们删除 7 ，6 ，6 和 3 ，将分数增加 7 。下一步操作中，删除 2 ，4 ，5 和 2 ，将分数增加 5 。最后删除 1 ，
2 ，3 和 1 ，将分数增加 3 。所以总得分为 7 + 5 + 3 = 15 。

示例 2：
输入：nums = [[1]]
输出：1
解释：我们删除 1 并将分数增加 1 ，所以返回 1 。
"""
"""
思路：排序，然后找每一列的最大值。
"""


class Solution:
    @staticmethod
    def matrixSum(nums: List[List[int]]) -> int:
        res = 0
        m = len(nums)
        n = len(nums[0])
        for i in range(m):
            nums[i].sort()
        for j in range(n):
            max_val = 0
            for i in range(m):
                max_val = max(max_val, nums[i][j])
            res += max_val
        return res
