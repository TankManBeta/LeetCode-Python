# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2022/2/6 0:23
"""
"""
给你一个整数数组 nums ，数组中的元素 互不相同 。返回该数组所有可能的子集（幂集）。
解集 不能 包含重复的子集。你可以按 任意顺序 返回解集。

输入：nums = [1,2,3]
输出：[[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]

输入：nums = [0]
输出：[[],[0]]
"""
"""
思路：
（1）dp，初始化dp=[[]]，对nums中每一个数字，在前一个状态的基础之上加上新的num
（2）dfs，树的每一个节点即可
"""


class Solution(object):
    @staticmethod
    def subsets(nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # dp = [[]]
        # len_nums = len(nums)
        # for num in nums:
        #     temp_len = len(dp)
        #     for j in range(0, temp_len):
        #         dp.append(dp[j]+[num])
        # return dp

        combination = list()
        combinations = list()
        count = len(nums)

        def dfs(k):
            combinations.append(combination[:])
            for i in range(k, count):
                combination.append(nums[i])
                dfs(i+1)
                combination.pop()
        dfs(0)
        return combinations
