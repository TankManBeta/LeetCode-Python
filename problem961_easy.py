# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2023/2/5 22:23
"""
from typing import List

"""
给你一个整数数组 nums ，该数组具有以下属性：
    nums.length == 2 * n.
    nums 包含 n + 1 个 不同的 元素
    nums 中恰有一个元素重复 n 次
找出并返回重复了 n 次的那个元素。

示例 1：
输入：nums = [1,2,3,3]
输出：3

示例 2：
输入：nums = [2,1,2,5,3,2]
输出：2

示例 3：
输入：nums = [5,1,5,2,5,3,5,4]
输出：5
"""
"""
思路：找到第一个出现两次的直接返回即可
"""


class Solution:
    @staticmethod
    def repeatedNTimes(nums: List[int]) -> int:
        found = set()

        for num in nums:
            if num in found:
                return num
            found.add(num)

        # 不可能的情况
        return -1
