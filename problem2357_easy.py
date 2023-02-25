# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2023/2/24 11:17
"""
from typing import List

"""
给你一个非负整数数组 nums 。在一步操作中，你必须：
    选出一个正整数 x ，x 需要小于或等于 nums 中 最小 的 非零 元素。
    nums 中的每个正整数都减去 x。
返回使 nums 中所有元素都等于 0 需要的 最少 操作数。

示例 1：
输入：nums = [1,5,0,3,5]
输出：3
解释：
第一步操作：选出 x = 1 ，之后 nums = [0,4,0,2,4] 。
第二步操作：选出 x = 2 ，之后 nums = [0,2,0,0,2] 。
第三步操作：选出 x = 2 ，之后 nums = [0,0,0,0,0] 。

示例 2：
输入：nums = [0]
输出：0
解释：nums 中的每个元素都已经是 0 ，所以不需要执行任何操作。
"""
"""
思路：
（1）排序+模拟。先排序。然后每次取最小的非0元素，所有数减去这个值即可
（2）统计不同的非0元素个数即可，因为每次总是能使最小的非0值变为0
"""


class Solution:
    @staticmethod
    def minimumOperations(nums: List[int]) -> int:
        # ans = 0
        # n = len(nums)
        # nums.sort()
        # for i in range(n):
        #     if nums[i] == 0:
        #         continue
        #     else:
        #         tmp = nums[i]
        #         for j in range(i, n):
        #             nums[j] -= tmp
        #         ans += 1
        # return ans

        return len({x for x in nums if x})
