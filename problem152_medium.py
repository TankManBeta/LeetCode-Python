# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2022/3/16 10:59
"""
"""
给你一个整数数组 nums ，请你找出数组中乘积最大的非空连续子数组（该子数组中至少包含一个数字），并返回该子数组所对应的乘积。
测试用例的答案是一个 32-位 整数。
子数组 是数组的连续子序列。

输入: nums = [2,3,-2,4]
输出: 6
解释: 子数组 [2,3] 有最大乘积 6。

输入: nums = [-2,0,-1]
输出: 0
解释: 结果不能为 2, 因为 [-2,-1] 不是子数组。
"""
"""
思路：
（1）dp，因为其中有负数，所以维护两个dp数组，一个记录最大值，一个记录最小值，max_nums[i]=max(max_nums[i-1]*nums[i], min_nums
[i-1]*nums[i], nums[i])，最小值同理
（2）因为有负数，我们可以考虑负数个数的奇偶，如果有偶数个负数，那么全部乘起来的值肯定是最大的；如果有奇数个负数，那么去掉左边的
负数或者右边的负数的乘积是最大的，最大值肯定出现在遍历过程中，如果有0就把前面的累积乘积变为1
"""


class Solution(object):
    @staticmethod
    def max_product(nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # min_nums = nums[:]
        # max_nums = nums[:]
        # n = len(nums)
        # for i in range(1, n):
        #     max_nums[i] = max(max_nums[i-1]*nums[i], min_nums[i-1]*nums[i], nums[i])
        #     min_nums[i] = min(max_nums[i-1]*nums[i], min_nums[i-1]*nums[i], nums[i])
        # ans = max_nums[0]
        # for i in range(1, n):
        #     ans = max(ans, max_nums[i])
        # return ans

        reversed_nums = nums[::-1]
        n = len(nums)
        for i in range(1, n):
            nums[i] *= nums[i-1] or 1
            reversed_nums[i] *= reversed_nums[i-1] or 1
        return max(nums+reversed_nums)
