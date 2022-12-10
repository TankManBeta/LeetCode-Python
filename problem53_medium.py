# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2021/12/23 15:42
"""
"""
给你一个整数数组 nums ，请你找出一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。
子数组 是数组中的一个连续部分。

输入：nums = [-2,1,-3,4,-1,2,1,-5,4]
输出：6
解释：连续子数组 [4,-1,2,1] 的和最大，为6。

输入：nums = [1]
输出：1

输入：nums = [5,4,-1,7,8]
输出：23
"""
"""
思路：动态规划，如果前面的和已经小于0，那就没有保留的必要了，如果dp[i-1]<0，dp[i]=nums[i]，否则dp[i]=dp[i-1]+nums[i]
"""


class Solution(object):
    @staticmethod
    def max_sub_array(nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        len_nums = len(nums)
        dp = [0]*len_nums
        for i in range(len_nums):
            if dp[i-1] < 0:
                dp[i] = nums[i]
            else:
                dp[i] = dp[i-1] + nums[i]
        return max(dp)
