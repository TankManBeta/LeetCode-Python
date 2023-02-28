# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2023/2/27 21:11
"""
from typing import List

"""
给你一个整数数组 nums，每次 操作 会从中选择一个元素并 将该元素的值减少 1。
如果符合下列情况之一，则数组 A 就是 锯齿数组：
    每个偶数索引对应的元素都大于相邻的元素，即 A[0] > A[1] < A[2] > A[3] < A[4] > ...
    或者，每个奇数索引对应的元素都大于相邻的元素，即 A[0] < A[1] > A[2] < A[3] > A[4] < ...
返回将数组 nums 转换为锯齿数组所需的最小操作次数。

示例 1：
输入：nums = [1,2,3]
输出：2
解释：我们可以把 2 递减到 0，或把 3 递减到 1。

示例 2：
输入：nums = [9,6,1,6,2]
输出：4
"""
"""
思路：我们可以分别枚举偶数位和奇数位作为“比相邻元素小”的元素，然后计算需要的操作次数。取两者的最小值即可。
"""


class Solution:
    @staticmethod
    def movesToMakeZigzag(nums: List[int]) -> int:
        ans = [0, 0]
        n = len(nums)
        for i in range(2):
            for j in range(i, n, 2):
                d = 0
                if j:
                    d = max(d, nums[j] - nums[j - 1] + 1)
                if j < n - 1:
                    d = max(d, nums[j] - nums[j + 1] + 1)
                ans[i] += d
        return min(ans)
