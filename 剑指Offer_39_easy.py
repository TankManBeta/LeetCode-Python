# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2023/6/7 11:48
"""
from typing import List

"""
数组中有一个数字出现的次数超过数组长度的一半，请找出这个数字。
你可以假设数组是非空的，并且给定的数组总是存在多数元素。

示例 1:
输入: [1, 2, 3, 2, 2, 2, 5, 4, 2]
输出: 2
"""
"""
思路：
（1）统计个数，超过一半的就是要找的元素
（2）排序，中间的哪个就是要找的元素
（3）摩尔投票法，若记 众数 的票数为 +1 ，非众数 的票数为 −1 ，则一定有所有数字的 票数和 >0
"""


class Solution:
    @staticmethod
    def majorityElement(nums: List[int]) -> int:
        # cnt = defaultdict(int)
        # n = len(nums)
        # for num in nums:
        #     cnt[num] += 1
        #     if cnt[num] >= n // 2 + 1:
        #         return num

        # nums.sort()
        # return nums[len(nums) // 2]

        votes = 0
        for num in nums:
            if votes == 0:
                x = num
            votes += 1 if num == x else -1
        return x
