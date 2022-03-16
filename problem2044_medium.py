# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2022/3/15 11:03
"""
"""
给你一个整数数组 nums ，请你找出 nums 子集 按位或 可能得到的 最大值 ，并返回按位或能得到最大值的 不同非空子集的数目 。
如果数组a可以由数组b删除一些元素（或不删除）得到，则认为数组a是数组b的一个 子集 。如果选中的元素下标位置不一样，则认为两个子集不同 。
对数组 a 执行 按位或 ，结果等于 a[0] OR a[1] OR ... OR a[a.length - 1]（下标从 0 开始）。

输入：nums = [3,1]
输出：2
解释：子集按位或能得到的最大值是 3 。有 2 个子集按位或可以得到 3 ：
- [3]
- [3,1]

输入：nums = [2,2,2]
输出：7
解释：[2,2,2] 的所有非空子集的按位或都可以得到 2 。总共有 23 - 1 = 7 个子集。

输入：nums = [3,2,1,5]
输出：6
解释：子集按位或可能的最大值是 7 。有 6 个子集按位或可以得到 7 ：
- [3,5]
- [3,1,5]
- [3,2,5]
- [3,2,1,5]
- [2,5]
- [2,1,5]
"""
"""
思路：直接dfs，有用当前数字或和不用当前数字或两种操作
"""


class Solution(object):
    def __init__(self):
        self.ans = 0
        self.max_val = 0

    def count_max_or_subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        self.n = len(nums)
        for i in range(self.n):
            self.max_val |= nums[i]

        def dfs(index, val):
            if index == self.n:
                if val == self.max_val:
                    self.ans += 1
                return
            dfs(index + 1, val)
            dfs(index + 1, val | nums[index])

        dfs(0, 0)
        return self.ans
