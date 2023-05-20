# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2023/5/19 11:07
"""
from typing import List

"""
找出数组中重复的数字。
在一个长度为 n 的数组 nums 里的所有数字都在 0～n-1 的范围内。数组中某些数字是重复的，但不知道有几个数字重复了，也不知道每个数字
重复了几次。请找出数组中任意一个重复的数字。

示例 1：
输入：
[2, 3, 1, 0, 2, 5, 3]
输出：2 或 3 
"""
"""
思路：
（1）哈希表或者集合记录是否有重复的出现
（2）每次都将自己放到自己该放的位置上，如果遍历有重复的说明就是多出来的数字
"""


class Solution:
    @staticmethod
    def findRepeatNumber(nums: List[int]) -> int:
        # cnt = defaultdict(int)
        # for num in nums:
        #     if cnt[num] == 1:
        #         return num
        #     else:
        #         cnt[num] += 1
        #
        # cnt = set()
        # for num in nums:
        #     if num in cnt:
        #         return num
        #     else:
        #         cnt.add(num)

        i = 0
        while i < len(nums):
            if nums[i] == i:
                i += 1
                continue
            if nums[nums[i]] == nums[i]:
                return nums[i]
            nums[nums[i]], nums[i] = nums[i], nums[nums[i]]
