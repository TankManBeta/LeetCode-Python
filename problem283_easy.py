# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2022/11/16 11:38
"""
from typing import List

"""
给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序。
请注意 ，必须在不复制数组的情况下原地对数组进行操作。

示例 1:
输入: nums = [0,1,0,3,12]
输出: [1,3,12,0,0]

示例 2:
输入: nums = [0]
输出: [0]
"""
"""
思路：双指针，找到不为0的就移到左边
"""


class Solution:
    @staticmethod
    def moveZeroes(nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if not nums:
            return 0
        # 两个指针i和j
        j = 0
        for i in range(len(nums)):
            # 当前元素!=0，就把其交换到左边，等于0的交换到右边
            if nums[i]:
                nums[j],nums[i] = nums[i],nums[j]
                j += 1