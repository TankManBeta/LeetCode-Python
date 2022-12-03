# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2022/12/2 11:15
"""
from typing import List

"""
给定一个包含 n + 1 个整数的数组 nums ，其数字都在 [1, n] 范围内（包括 1 和 n），可知至少存在一个重复的整数。
假设 nums 只有 一个重复的整数 ，返回 这个重复的数 。
你设计的解决方案必须 不修改 数组 nums 且只用常量级 O(1) 的额外空间。

示例 1：
输入：nums = [1,3,4,2,2]
输出：2

示例 2：
输入：nums = [3,1,3,4,2]
输出：3
"""
"""
思路：
（1）用数组变为集合，集合和数组之间的差就是重复m次的数的和，但是不满足题设条件
（2）二分查找，如果cnt[mid]<=mid，则说明前面正好不重复或者前面有的数字被后面的给顶替掉，那么left=mid+1，否则说明前面有重复的
"""


class Solution:
    @staticmethod
    def findDuplicate(nums: List[int]) -> int:
        # new_nums = list(set(nums))
        # a = len(nums)
        # b = len(new_nums)
        # return (sum(nums) - sum(new_nums)) // (a-b)

        n = len(nums)
        left, right = 0, n-1
        ans = -1
        while left <= right:
            mid = (left+right) >> 1
            cnt = 0
            for i in range(n):
                cnt += nums[i] <= mid
            if cnt <= mid:
                left = mid + 1
            else:
                right = mid - 1
                ans = mid
        return ans
