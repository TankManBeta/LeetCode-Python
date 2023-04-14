# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2023/4/13 10:25
"""
from collections import defaultdict
from typing import List

"""
给你一个整数数组 nums ，返回出现最频繁的偶数元素。
如果存在多个满足条件的元素，只需要返回 最小 的一个。如果不存在这样的元素，返回 -1 。 

示例 1：
输入：nums = [0,1,2,2,4,4,1]
输出：2
解释：
数组中的偶数元素为 0、2 和 4 ，在这些元素中，2 和 4 出现次数最多。
返回最小的那个，即返回 2 。

示例 2：
输入：nums = [4,4,4,9,2,4]
输出：4
解释：4 是出现最频繁的偶数元素。

示例 3：
输入：nums = [29,47,21,41,13,37,25,7]
输出：-1
解释：不存在偶数元素。
"""
"""
思路：哈希表计数即可。
"""


class Solution:
    @staticmethod
    def mostFrequentEven(nums: List[int]) -> int:
        counter = defaultdict(int)
        max_count = 0
        ans = 10 ** 5 + 1
        for num in nums:
            if num % 2 == 0:
                counter[num] += 1
                max_count = max(max_count, counter[num])
        for key, value in counter.items():
            if value == max_count:
                ans = min(key, ans)
        return ans if ans != 10 ** 5 + 1 else -1
