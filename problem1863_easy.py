# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2022/11/3 12:36
"""
from typing import List

"""
一个数组的 异或总和 定义为数组中所有元素按位 XOR 的结果；如果数组为 空 ，则异或总和为 0 。
例如，数组 [2,5,6] 的 异或总和 为 2 XOR 5 XOR 6 = 1 。
给你一个数组 nums ，请你求出 nums 中每个 子集 的 异或总和 ，计算并返回这些值相加之 和 。
注意：在本题中，元素 相同 的不同子集应 多次 计数。
数组 a 是数组 b 的一个 子集 的前提条件是：从 b 删除几个（也可能不删除）元素能够得到 a 。

示例 1：
输入：nums = [1,3]
输出：6
解释：[1,3] 共有 4 个子集：
- 空子集的异或总和是 0 。
- [1] 的异或总和为 1 。
- [3] 的异或总和为 3 。
- [1,3] 的异或总和为 1 XOR 3 = 2 。
0 + 1 + 3 + 2 = 6

示例 2：
输入：nums = [5,1,6]
输出：28
解释：[5,1,6] 共有 8 个子集：
- 空子集的异或总和是 0 。
- [5] 的异或总和为 5 。
- [1] 的异或总和为 1 。
- [6] 的异或总和为 6 。
- [5,1] 的异或总和为 5 XOR 1 = 4 。
- [5,6] 的异或总和为 5 XOR 6 = 3 。
- [1,6] 的异或总和为 1 XOR 6 = 7 。
- [5,1,6] 的异或总和为 5 XOR 1 XOR 6 = 2 。
0 + 5 + 1 + 6 + 4 + 3 + 7 + 2 = 28

示例 3：
输入：nums = [3,4,5,6,7,8]
输出：480
解释：每个子集的全部异或总和值之和为 480 。
"""
"""
思路：
（1）对于有n个元素的集合，子集个数有2**n个，可以映射到0-2**n-1上，每个位上的1就表示当前数字是否被选上，然后判断每一个位是否被
选上，如果选上就和结果异或，否则继续
（2）dfs，当前元素有选和不选两种操作
"""


class Solution:
    @staticmethod
    def subsetXORSum(nums: List[int]) -> int:
        # size = len(nums)
        # result = 0
        # for i in range(1 << size):
        #     res = 0
        #     for j in range(size):
        #         if i & (1 << j):
        #             res ^= nums[j]
        #     result += res
        # return result

        res = 0
        n = len(nums)

        def dfs(val, idx):
            nonlocal res
            if idx == n:
                # 终止递归
                res += val
                return
            # 考虑选择当前数字
            dfs(val ^ nums[idx], idx + 1)
            # 考虑不选择当前数字
            dfs(val, idx + 1)

        dfs(0, 0)
        return res
