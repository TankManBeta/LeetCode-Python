# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2022/3/30 11:05
"""
import bisect

"""
给定一个含有 n 个正整数的数组和一个正整数 target 。
找出该数组中满足其和 ≥ target 的长度最小的 连续子数组 [numsl, numsl+1, ..., numsr-1, numsr] ，并返回其长度。
如果不存在符合条件的子数组，返回 0 。

输入：target = 7, nums = [2,3,1,2,4,3]
输出：2
解释：子数组 [4,3] 是该条件下的长度最小的子数组。

输入：target = 4, nums = [1,4,4]
输出：1

输入：target = 11, nums = [1,1,1,1,1,1,1,1]
输出：0
"""
"""
思路：
（1）O(n)滑动窗口即可
（2）前缀和+二分，sums数组计算前缀和，然后对于sums中每一个前缀和，将它加上target，记为s，然后再sums中找到第一个大于s的位置，这
个位置和i的差值之间所有数的和一定大于等于target
"""


class Solution(object):
    @staticmethod
    def minSubArrayLen(target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        # if not nums:
        #     return 0
        # n = len(nums)
        # ans = n + 1
        # start, end = 0, 0
        # total = 0
        # while end < n:
        #     total += nums[end]
        #     while total >= target:
        #         ans = min(ans, end - start + 1)
        #         total -= nums[start]
        #         start += 1
        #     end += 1
        # return 0 if ans == n + 1 else ans

        if not nums:
            return 0
        n = len(nums)
        ans = n + 1
        sums = [0]
        for i in range(n):
            sums.append(sums[-1] + nums[i])
        for i in range(1, n + 1):
            s = target + sums[i - 1]
            bound = bisect.bisect_left(sums, s)
            if bound != len(sums):
                ans = min(ans, bound - (i - 1))
        return 0 if ans == n + 1 else ans
