# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2023/1/18 20:37
"""
from bisect import bisect_left
from typing import List

"""
数对 (a,b) 由整数 a 和 b 组成，其数对距离定义为 a 和 b 的绝对差值。
给你一个整数数组 nums 和一个整数 k ，数对由 nums[i] 和 nums[j] 组成且满足 0 <= i < j < nums.length 。返回 所有数对距离中 
第 k 小的数对距离。

示例 1：
输入：nums = [1,3,1], k = 1
输出：0
解释：数对和对应的距离如下：
(1,3) -> 2
(1,1) -> 0
(3,1) -> 2
距离第 1 小的数对是 (1,1) ，距离为 0 。

示例 2：
输入：nums = [1,1,1], k = 2
输出：0

示例 3：
输入：nums = [1,6,1], k = 3
输出：5
"""
"""
思路：先将数组 nums 从小到大进行排序。因为第 k 小的数对距离必然在区间 [0,max(nums)−min(nums)] 内，令 left=0，right=max(nums)
−min(nums)，我们在区间 [left,right] 上进行二分。对于当前搜索的距离 mid，计算所有距离小于等于 mid 的数对数目 cnt，如果 cnt≥k，
那么 right=mid−1，否则 left=mid+1。当 left>right 时，终止搜索，那么第 k 小的数对距离为 left。
给定距离 mid，计算所有距离小于等于 mid 的数对数目 cnt 可以使用二分查找：枚举所有数对的右端点 j，二分查找大于等于 nums[j]−mid 
的最小值的下标 i，那么右端点为 j 且距离小于等于 mid 的数对数目为 j−i，计算这些数目之和。
"""


class Solution:
    @staticmethod
    def smallestDistancePair(nums: List[int], k: int) -> int:
        def count(mid: int) -> int:
            cnt = 0
            for j, num in enumerate(nums):
                i = bisect_left(nums, num - mid, 0, j)
                cnt += j - i
            return cnt

        nums.sort()
        return bisect_left(range(nums[-1] - nums[0]), k, key=count)
