# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2022/11/23 11:46
"""
from typing import List

"""
给你一个正整数数组 nums ，请你从中删除一个含有 若干不同元素 的子数组。删除子数组的 得分 就是子数组各元素之 和 。
返回 只删除一个 子数组可获得的 最大得分 。
如果数组 b 是数组 a 的一个连续子序列，即如果它等于 a[l],a[l+1],...,a[r] ，那么它就是 a 的一个子数组。

示例 1：
输入：nums = [4,2,4,5,6]
输出：17
解释：最优子数组是 [2,4,5,6]

示例 2：
输入：nums = [5,2,1,2,5,2,1,2,5]
输出：8
解释：最优子数组是 [5,2,1] 或 [1,2,5]
"""
"""
思路：滑动窗口，如果当前数字在窗口中没出现过，就加入到窗口中，求和并和已有最大值比较，同时更新访问数组；如果当前数字已经访问过，
就l++，直到找到它出现的位置，在此基础之上l++，就能剔除它第一次出现的位置。
"""


class Solution:
    @staticmethod
    def maximumUniqueSubArray(nums: List[int]) -> int:
        exist = [False] * 10001
        n = len(nums)
        l = 0
        temp = 0
        res = 0
        for r in range(n):
            if exist[nums[r]]:
                while nums[l] != nums[r]:
                    temp -= nums[l]
                    exist[nums[l]] = False
                    l += 1
                l += 1
            else:
                temp += nums[r]
                exist[nums[r]] = True
                res = max(temp, res)
        return res
