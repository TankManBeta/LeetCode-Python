# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2022/11/16 11:21
"""
from typing import List

"""
给你一个长度为 n 的整数数组 nums ，表示由范围 [0, n - 1] 内所有整数组成的一个排列。
全局倒置 的数目等于满足下述条件不同下标对 (i, j) 的数目：
    0 <= i < j < n
    nums[i] > nums[j]
局部倒置 的数目等于满足下述条件的下标 i 的数目：
    0 <= i < n - 1
    nums[i] > nums[i + 1]
当数组 nums 中 全局倒置 的数量等于 局部倒置 的数量时，返回 true ；否则，返回 false 。

示例 1：
输入：nums = [1,0,2]
输出：true
解释：有 1 个全局倒置，和 1 个局部倒置。

示例 2：
输入：nums = [1,2,0]
输出：false
解释：有 2 个全局倒置，和 1 个局部倒置。
"""
"""
思路：
（1）局部倒置一定是全局倒置，只要找到非局部倒置的全局倒置即可，也就是看非相邻数字是否满足递增，可以利用前缀最大值来判断，因此，
我们枚举每个数 nums[i]，其中 2≤i≤n−1，维护前缀数组 nums[0,..i-2] 中的最大值，记为 mx。如果存在 mx 大于 nums[i]，
说明全局倒置的数量大于局部倒置的数量，返回 false 即可。
（2）利用偏移量，可以通过nums[i]-i计算出i位置的元素与有序后的位置之间的差值：
【差值等于0】表示元素i所在的位置就是排序后的位置。
【差值等于1】表示元素1所在的位置向前1位或向后1位。
【其他情况】表示元素所在位置偏差大于1位，也就是出现了全局倒置并且非局部倒置的情况。
"""


class Solution:
    @staticmethod
    def isIdealPermutation(nums: List[int]) -> bool:
        # max_val = nums[0]
        # n = len(nums)
        # for i in range(2, n):
        #     if nums[i] < max_val:
        #         return False
        #     max_val = max(nums[i-1], max_val)
        # return True

        n = len(nums)
        for i in range(n):
            if abs(nums[i]-i) > 1:
                return False
        return True
