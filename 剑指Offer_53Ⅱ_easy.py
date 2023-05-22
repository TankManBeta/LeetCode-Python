# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2023/5/19 11:32
"""
from typing import List

"""
一个长度为n-1的递增排序数组中的所有数字都是唯一的，并且每个数字都在范围0～n-1之内。在范围0～n-1内的n个数字中有且只有一个数字
不在该数组中，请找出这个数字。

示例 1:
输入: [0,1,3]
输出: 2

示例 2:
输入: [0,1,2,3,4,5,6,7,9]
输出: 8
"""
"""
思路：
（1）直接遍历，如果nums[i]!=i，说明这个是错的；如果遍历完成后还没返回结果，则返回n
（2）二分，对于nums[i]!=i来说，他左边的数组肯定是符合规则的，他右边的肯定是因为自己缺失了才造成的，所以可以使用二分。
"""


class Solution:
    @staticmethod
    def missingNumber(nums: List[int]) -> int:
        # for i, num in enumerate(nums):
        #     if i != num:
        #         return i
        # return len(nums)

        i, j = 0, len(nums) - 1
        while i <= j:
            m = (i + j) // 2
            if nums[m] == m:
                i = m + 1
            else:
                j = m - 1
        return i
