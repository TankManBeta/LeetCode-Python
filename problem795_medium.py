# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2022/11/24 14:54
"""
from typing import List

"""
给你一个整数数组 nums 和两个整数：left 及 right 。找出 nums 中连续、非空且其中最大元素在范围 [left, right] 内的子数组，
并返回满足条件的子数组的个数。
生成的测试用例保证结果符合 32-bit 整数范围。

示例 1：
输入：nums = [2,1,4,3], left = 2, right = 3
输出：3
解释：满足条件的三个子数组：[2], [2, 1], [3]

示例 2：
输入：nums = [2,9,2,5,6], left = 2, right = 8
输出：7
"""
"""
思路：对于每一个i以当前数字为数组的右端点，所以只需要找到合法的左端点即可。首先必须找到上一个大于right的数字所在的位置，
然后需要找到大于left的数字所在的位置，这两个之间位置的差就是合法的个数。依此类推。
"""


class Solution:
    @staticmethod
    def numSubarrayBoundedMax(nums: List[int], left: int, right: int) -> int:
        # n = len(nums)
        # count = 0
        # for i in range(n):
        #     for j in range(i+1, n+1):
        #         if left <= max(nums[i:j]) <= right:
        #             count += 1
        # return count

        # res = 0
        # last2 = last1 = -1
        # for i, x in enumerate(nums):
        #     if left <= x <= right:
        #         last1 = i
        #     elif x > right:
        #         last2 = i
        #         last1 = -1
        #     if last1 != -1:
        #         res += last1 - last2
        # return res

        ans, i0, i1 = 0, -1, -1
        for i, x in enumerate(nums):
            if x > right:
                i0 = i
            if x >= left:
                i1 = i
            ans += i1 - i0
        return ans
