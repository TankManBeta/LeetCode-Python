# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2023/3/25 16:48
"""
from bisect import bisect_left
from typing import List

"""
给你一个整数数组 arr ，请你删除一个子数组（可以为空），使得 arr 中剩下的元素是 非递减 的。
一个子数组指的是原数组中连续的一个子序列。
请你返回满足题目要求的最短子数组的长度。

示例 1：
输入：arr = [1,2,3,10,4,2,3,5]
输出：3
解释：我们需要删除的最短子数组是 [10,4,2] ，长度为 3 。剩余元素形成非递减数组 [1,2,3,3,5] 。
另一个正确的解为删除子数组 [3,10,4] 。

示例 2：
输入：arr = [5,4,3,2,1]
输出：4
解释：由于数组是严格递减的，我们只能保留一个元素。所以我们需要删除长度为 4 的子数组，要么删除 [5,4,3,2]，要么删除 [4,3,2,1]。

示例 3：
输入：arr = [1,2,3]
输出：0
解释：数组已经是非递减的了，我们不需要删除任何元素。

示例 4：
输入：arr = [1]
输出：0
"""
"""
思路：首先找出最长非递减前缀和最长非递减后缀，如果 i≥j，说明数组本身就是非递减的，返回 0。否则，我们可以选择删除右侧后缀，
也可以选择删除左侧前缀，因此初始时答案为 min(n−i−1,j)。接下来，我们枚举左侧前缀的最右端点 l，对于每个 l，我们可以通过二分查找，
在 nums[j..n−1] 中找到第一个大于等于 nums[l] 的位置，记为 r，此时我们可以删除 nums[l+1..r−1]，并且更新答案 ans=min(ans,r−l−1)。
继续枚举 l，最终得到答案。
"""


class Solution:
    @staticmethod
    def findLengthOfShortestSubarray(arr: List[int]) -> int:
        n = len(arr)
        i, j = 0, n - 1
        while i + 1 < n and arr[i] <= arr[i + 1]:
            i += 1
        while j - 1 >= 0 and arr[j - 1] <= arr[j]:
            j -= 1
        if i >= j:
            return 0
        ans = min(n-i-1, j)
        for l in range(i+1):
            r = bisect_left(arr, arr[l], lo=j)
            ans = min(ans, r - l - 1)
        return ans
