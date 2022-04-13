# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2022/4/12 10:06
"""
"""
给你一个整数数组 nums，返回 数组 answer ，其中 answer[i] 等于 nums 中除 nums[i] 之外其余各元素的乘积 。
题目数据 保证 数组 nums之中任意元素的全部前缀元素和后缀的乘积都在  32 位 整数范围内。
请不要使用除法，且在 O(n) 时间复杂度内完成此题。

输入: nums = [1,2,3,4]
输出: [24,12,8,6]

输入: nums = [-1,1,0,-3,3]
输出: [0,0,9,0,0]
"""
"""
思路：
（1）两个数组，left计算除当前i之外，左边所有数的乘积，right计算除当前i之外右边所有数的乘积，然后left[i]*right[i]就能计算出除
自身以外所有数的乘积
（2）只用一个ans数组，ans数组先像（1）一样计算left，然后将题目中的nums数组动态构造成right数组，
"""


class Solution(object):
    @staticmethod
    def productExceptSelf(nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # n = len(nums)
        # left = [1 for _ in range(n)]
        # right = [1 for _ in range(n)]
        # for i in range(1, n):
        #     left[i] = left[i-1]*nums[i-1]
        # for j in range(n-2,-1,-1):
        #     right[j] = right[j+1]*nums[j+1]
        # ans = []
        # for i in range(n):
        #     ans.append(left[i]*right[i])
        # return ans

        n = len(nums)
        ans = [1 for _ in range(n)]
        for i in range(1, n):
            ans[i] = ans[i-1]*nums[i-1]
        for j in range(n-2, -1, -1):
            ans[j] = ans[j]*nums[j+1]
            nums[j] = nums[j]*nums[j+1]
        return ans
