# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2023/6/13 21:00
"""
from collections import Counter
from typing import List

"""
给你一个下标从 0 开始的正整数数组 nums 。请你找出并统计满足下述条件的三元组 (i, j, k) 的数目：
    0 <= i < j < k < nums.length
    nums[i]、nums[j] 和 nums[k] 两两不同 。
        换句话说：nums[i] != nums[j]、nums[i] != nums[k] 且 nums[j] != nums[k] 。
返回满足上述条件三元组的数目。 

示例 1：
输入：nums = [4,4,2,4,3]
输出：3
解释：下面列出的三元组均满足题目条件：
- (0, 2, 4) 因为 4 != 2 != 3
- (1, 2, 4) 因为 4 != 2 != 3
- (2, 3, 4) 因为 2 != 4 != 3
共计 3 个三元组，返回 3 。
注意 (2, 0, 4) 不是有效的三元组，因为 2 > 0 。

示例 2：
输入：nums = [1,1,1,1,1]
输出：0
解释：不存在满足条件的三元组，所以返回 0 。
"""
"""
思路：
（1）暴力，三重循环
（2）哈希表，使用哈希表 cnt 来统计数组 nums 中每个元素的数量。然后遍历哈希表 cnt，枚举中间元素的个数 b，左侧元素个数记为 a，
那么右侧元素个数有 c=n−a−b，此时符合条件的三元组数量为 a×b×c，累加到答案中。接着更新 a=a+b，继续枚举中间元素的个数 b。
"""


class Solution:
    @staticmethod
    def unequalTriplets(nums: List[int]) -> int:
        # n = len(nums)
        # ans = 0
        # for i in range(n-2):
        #     for j in range(i+1, n-1):
        #         for k in range(j+1, n):
        #             if nums[i] != nums[j] and nums[j] != nums[k] and nums[k] != nums[i]:
        #                 ans += 1
        # return ans

        cnt = Counter(nums)
        n = len(nums)
        ans = a = 0
        for b in cnt.values():
            c = n - a - b
            ans += a * b * c
            a += b
        return ans
