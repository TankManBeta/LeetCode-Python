# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2023/3/10 11:10
"""
from typing import List

"""
给你一个正整数数组 nums，请你移除 最短 子数组（可以为 空），使得剩余元素的 和 能被 p 整除。 不允许 将整个数组都移除。
请你返回你需要移除的最短子数组的长度，如果无法满足题目要求，返回 -1 。
子数组 定义为原数组中连续的一组元素。

示例 1：
输入：nums = [3,1,4,2], p = 6
输出：1
解释：nums 中元素和为 10，不能被 p 整除。我们可以移除子数组 [4] ，剩余元素的和为 6 。

示例 2：
输入：nums = [6,3,5,2], p = 9
输出：2
解释：我们无法移除任何一个元素使得和被 9 整除，最优方案是移除子数组 [5,2] ，剩余元素为 [6,3]，和为 9 。

示例 3：
输入：nums = [1,2,3], p = 3
输出：0
解释：和恰好为 6 ，已经能被 3 整除了。所以我们不需要移除任何元素。

示例  4：
输入：nums = [1,2,3], p = 7
输出：-1
解释：没有任何方案使得移除子数组后剩余元素的和被 7 整除。

示例 5：
输入：nums = [1000000000,1000000000,1000000000], p = 3
输出：0
"""
"""
思路：
（1）直接暴力，枚举子区间，看删完之后能否整除。
（2）前缀和+哈希表。首先判断一下是否本来就能整除，可以整除就返回0，否则先记下取模的结果k；用哈希表记录每个前缀和模 p 的值最后
一次出现的位置。对于当前位置的前缀和模p的结果cur，我们想要找到比他先出现的前缀和模p的结果target，看使得（cur-target）==k，
所以看cur-k是否在哈希表中，在的话更新结果。原理是因为我们删除的子数组要是和原来数组和同余的话，删完之后就不再有余数了（把余数
也删了）。
"""


class Solution:
    @staticmethod
    def minSubarray(nums: List[int], p: int) -> int:
        # n = len(nums)
        # ans = n
        # total = sum(nums)
        # if total % p == 0:
        #     return 0
        # for i in range(n):
        #     tmp = 0
        #     for j in range(i, n):
        #         tmp += nums[j]
        #         if (total-tmp) % p == 0:
        #             ans = min(j-i+1, ans)
        #             break
        # return -1 if ans == n else ans

        total = sum(nums)
        k = total % p
        if k == 0:
            return 0
        n = len(nums)
        ans = n
        s = 0
        index = {0: -1}
        for i, num in enumerate(nums):
            s += num
            index[s % p] = i
            if (s - k) % p in index:
                ans = min(i - index[(s - k) % p], ans)
        return -1 if ans == n else ans
