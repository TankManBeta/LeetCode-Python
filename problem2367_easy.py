# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2023/3/31 11:21
"""
from typing import List

"""
给你一个下标从 0 开始、严格递增 的整数数组 nums 和一个正整数 diff 。如果满足下述全部条件，则三元组 (i, j, k) 就是一个 算术三元组 ：
    i < j < k ，
    nums[j] - nums[i] == diff 且
    nums[k] - nums[j] == diff
返回不同 算术三元组 的数目。

示例 1：
输入：nums = [0,1,4,6,7,10], diff = 3
输出：2
解释：
(1, 2, 4) 是算术三元组：7 - 4 == 3 且 4 - 1 == 3 。
(2, 4, 5) 是算术三元组：10 - 7 == 3 且 7 - 4 == 3 。

示例 2：
输入：nums = [4,5,6,7,8,9], diff = 2
输出：2
解释：
(0, 2, 4) 是算术三元组：8 - 6 == 2 且 6 - 4 == 2 。
(1, 3, 5) 是算术三元组：9 - 7 == 2 且 7 - 5 == 2 。
"""
"""
思路：
（1）直接暴力
（2）哈希表，判断 x+diff, x+diff+diff 是否也在 vis 中
"""


class Solution:
    @staticmethod
    def arithmeticTriplets(nums: List[int], diff: int) -> int:
        # n = len(nums)
        # ans = 0
        # for i in range(n):
        #     for j in range(i+1, n):
        #         if nums[j]-nums[i] == diff:
        #             k = j + 1
        #             while k < n:
        #                 if nums[k] - nums[j] == diff:
        #                     ans += 1
        #                     break
        #                 elif nums[k] - nums[j] < diff:
        #                     k += 1
        #                 else:
        #                     break
        # return ans

        vis = set(nums)
        return sum(x + diff in vis and x + diff * 2 in vis for x in nums)
