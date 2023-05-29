# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2023/5/28 0:36
"""
from typing import List

"""
输入一个整数数组，实现一个函数来调整该数组中数字的顺序，使得所有奇数在数组的前半部分，所有偶数在数组的后半部分。

示例：
输入：nums = [1,2,3,4]
输出：[1,3,2,4] 
注：[3,1,2,4] 也是正确的答案之一。
"""
"""
思路：从前往后找偶数，从后往前找奇数，然后交换即可
"""


class Solution:
    @staticmethod
    def exchange(nums: List[int]) -> List[int]:
        i = 0
        j = len(nums) - 1
        while i < j:
            while i < j and nums[i] % 2 != 0:
                i += 1
            while i < j and nums[j] % 2 == 0:
                j -= 1
            nums[i], nums[j] = nums[j], nums[i]
        return nums
