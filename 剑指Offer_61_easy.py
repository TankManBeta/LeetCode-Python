# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2023/5/31 9:36
"""
from typing import List

"""
从若干副扑克牌中随机抽 5 张牌，判断是不是一个顺子，即这5张牌是不是连续的。2～10为数字本身，A为1，J为11，Q为12，K为13，
而大、小王为 0 ，可以看成任意数字。A 不能视为 14。

示例 1:
输入: [1,2,3,4,5]
输出: True

示例 2:
输入: [0,0,1,2,5]
输出: True
"""
"""
思路：
（1）排序+遍历，注意判重
（2）直接遍历，注意判重，最大值-最小值<5则构成顺子
"""


class Solution:
    @staticmethod
    def isStraight(nums: List[int]) -> bool:
        # nums = sorted(nums)
        # zeros = 0
        # n = len(nums)
        # for i in range(n):
        #     if nums[i] == 0:
        #         zeros += 1
        #     else:
        #         if i+1 < n:
        #             if nums[i+1] == nums[i]:
        #                 return False
        #             zeros -= nums[i+1] - nums[i] -1
        # return True if zeros >= 0 else False

        repeat = set()
        ma, mi = 0, 14
        for num in nums:
            if num == 0:
                continue  # 跳过大小王
            ma = max(ma, num)  # 最大牌
            mi = min(mi, num)  # 最小牌
            if num in repeat:
                return False  # 若有重复，提前返回 false
            repeat.add(num)  # 添加牌至 Set
        return ma - mi < 5  # 最大牌 - 最小牌 < 5 则可构成顺子
