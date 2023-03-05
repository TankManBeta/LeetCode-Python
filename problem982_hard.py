# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2023/3/4 10:07
"""
from collections import Counter
from typing import List

"""
给你一个整数数组 nums ，返回其中 按位与三元组 的数目。
按位与三元组 是由下标 (i, j, k) 组成的三元组，并满足下述全部条件：
    0 <= i < nums.length
    0 <= j < nums.length
    0 <= k < nums.length
nums[i] & nums[j] & nums[k] == 0 ，其中 & 表示按位与运算符。
 
示例 1：
输入：nums = [2,1,3]
输出：12
解释：可以选出如下 i, j, k 三元组：
(i=0, j=0, k=1) : 2 & 2 & 1
(i=0, j=1, k=0) : 2 & 1 & 2
(i=0, j=1, k=1) : 2 & 1 & 1
(i=0, j=1, k=2) : 2 & 1 & 3
(i=0, j=2, k=1) : 2 & 3 & 1
(i=1, j=0, k=0) : 1 & 2 & 2
(i=1, j=0, k=1) : 1 & 2 & 1
(i=1, j=0, k=2) : 1 & 2 & 3
(i=1, j=1, k=0) : 1 & 1 & 2
(i=1, j=2, k=0) : 1 & 3 & 2
(i=2, j=0, k=1) : 3 & 2 & 1
(i=2, j=1, k=0) : 3 & 1 & 2

示例 2：
输入：nums = [0,0,0]
输出：27
"""
"""
思路：
（1）三重循环超时
（2）二重循环，先记录x&y的值，然后遍历这些值再做一次&的操作。
"""


class Solution:
    @staticmethod
    def countTriplets(nums: List[int]) -> int:
        cnt = Counter((x & y) for x in nums for y in nums)
        ans = 0
        for x in nums:
            for mask, freq in cnt.items():
                if (x & mask) == 0:
                    ans += freq
        return ans
