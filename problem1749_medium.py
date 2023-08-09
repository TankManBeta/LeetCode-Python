# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2023/8/8 9:37
"""
from typing import List

"""
给你一个整数数组 nums 。一个子数组 [numsl, numsl+1, ..., numsr-1, numsr] 的 和的绝对值 为 abs(numsl + numsl+1 + ... + numsr-1 + numsr) 。
请你找出 nums 中 和的绝对值 最大的任意子数组（可能为空），并返回该 最大值 。
abs(x) 定义如下：
    如果 x 是负整数，那么 abs(x) = -x 。
    如果 x 是非负整数，那么 abs(x) = x 。
 
示例 1：
输入：nums = [1,-3,2,3,-4]
输出：5
解释：子数组 [2,3] 和的绝对值最大，为 abs(2+3) = abs(5) = 5 。

示例 2：
输入：nums = [2,-5,1,-4,3,-2]
输出：8
解释：子数组 [-5,1,-4] 和的绝对值最大，为 abs(-5+1-4) = abs(-8) = 8 。
"""
"""
思路：子数组的和首先想到前缀和，然后结果应该为波峰减去波谷
"""


class Solution:
    @staticmethod
    def maxAbsoluteSum(nums: List[int]) -> int:
        pre = [0]
        for num in nums:
            pre.append(num+pre[-1])
        return max(pre) - min(pre)
