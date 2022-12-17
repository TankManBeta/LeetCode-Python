# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2022/12/17 14:54
"""
from typing import List

"""
给你一个整数数组 nums ，找到其中最长严格递增子序列的长度。
子序列 是由数组派生而来的序列，删除（或不删除）数组中的元素而不改变其余元素的顺序。例如，[3,6,2,7] 是数组 [0,3,1,6,2,2,7] 的子序列。

示例 1：
输入：nums = [10,9,2,5,3,7,101,18]
输出：4
解释：最长递增子序列是 [2,3,7,101]，因此长度为 4 。

示例 2：
输入：nums = [0,1,0,3,2,3]
输出：4

示例 3：
输入：nums = [7,7,7,7,7,7,7]
输出：1
"""
"""
思路：
（1）枚举子集，如果升序就往临时的子集中存放，然后根据子集的长度更新最后的ans，超时
（2）dp，dp[i]=max(dp[j])+1；如果dp[i]>dp[j]并且0≤j＜i
（3）二分查找，新建数组 cell，用于保存最长上升子序列。对原序列进行遍历，将每位元素二分插入 cell 中。如果 cell 中元素都比它小，
将它插到最后；否则，用它覆盖掉比它大的元素中最小的那个。总之，思想就是让 cell 中存储比较小的元素。这样，cell 未必是真实的最长
上升子序列，但长度是对的。（这样的方式使得之后的容纳能力变强了，有利于后面元素的添加）
"""


class Solution:
    @staticmethod
    def lengthOfLIS(nums: List[int]) -> int:
        # n = len(nums)
        # ans = 0
        # for i in range(1<<n):
        #     temp_nums1 = []
        #     for j in range(n):
        #         if (1<<j) & i:
        #             if len(temp_nums1) > 0:
        #                 if nums[j] > temp_nums1[-1]:
        #                     temp_nums1.append(nums[j])
        #             else:
        #                 temp_nums1.append(nums[j])
        #     ans = max(ans, len(temp_nums1))
        # return ans

        # if not nums:
        #     return 0
        # dp = []
        # for i in range(len(nums)):
        #     dp.append(1)
        #     for j in range(i):
        #         if nums[i] > nums[j]:
        #             dp[i] = max(dp[i], dp[j] + 1)
        # return max(dp)

        d = []
        for n in nums:
            if not d or n > d[-1]:
                d.append(n)
            else:
                l, r = 0, len(d) - 1
                loc = r
                while l <= r:
                    mid = (l + r) // 2
                    if d[mid] >= n:
                        loc = mid
                        r = mid - 1
                    else:
                        l = mid + 1
                d[loc] = n
        return len(d)
