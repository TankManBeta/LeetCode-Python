# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2022/11/27 19:29
"""
from typing import List

"""
给你一个数组 nums 。nums 的源数组中，所有元素与 nums 相同，但按非递减顺序排列。
如果 nums 能够由源数组轮转若干位置（包括 0 个位置）得到，则返回 true ；否则，返回 false 。
源数组中可能存在 重复项 。
注意：我们称数组 A 在轮转 x 个位置后得到长度相同的数组 B ，当它们满足 A[i] == B[(i+x) % A.length] ，其中 % 为取余运算。

示例 1：
输入：nums = [3,4,5,1,2]
输出：true
解释：[1,2,3,4,5] 为有序的源数组。
可以轮转 x = 3 个位置，使新数组从值为 3 的元素开始：[3,4,5,1,2] 。

示例 2：
输入：nums = [2,1,3,4]
输出：false
解释：源数组无法经轮转得到 nums 。

示例 3：
输入：nums = [1,2,3]
输出：true
解释：[1,2,3] 为有序的源数组。
可以轮转 x = 0 个位置（即不轮转）得到 nums 。
"""
"""
思路：首先检测数组是否非递减排序，如果满足非递减排序则直接返回 true；如果数组不满足非递减排序，则找到第一个 i 满足 nums[i]<nums[i−1]，
然后分别检测子数组 nums[0,⋯,i−1],nums[i,⋯,n−1] 是否都满足非递减排序；如果两个子数组都满足非递减排序，还需检测 nums[i,⋯,n−1] 
中的元素是否都满足小于等于 nums[0]，实际我们只需检测 nums[n−1] 是否满足小于等于 nums[0] 即可。
"""


class Solution:
    @staticmethod
    def check(nums: List[int]) -> bool:
        n = len(nums)
        x = 0
        for i in range(1, n):
            if nums[i] < nums[i - 1]:
                x = i
                break
        if x == 0:
            return True
        for i in range(x + 1, n):
            if nums[i] < nums[i - 1]:
                return False
        return nums[0] >= nums[-1]
