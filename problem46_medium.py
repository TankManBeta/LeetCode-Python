# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2021/12/13 9:58
"""
"""
给定一个不含重复数字的数组 nums ，返回其 所有可能的全排列 。你可以按任意顺序返回答案。

输入：nums = [1,2,3]
输出：[[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

输入：nums = [0,1]
输出：[[0,1],[1,0]]

输入：nums = [1]
输出：[[1]]
"""
"""
思路：dfs，如果在combination里就continue，注意回复上一步的状态即可
"""


class Solution(object):
    @staticmethod
    def permute(nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        combination = list()
        combinations = list()
        nums_len = len(nums)

        def dfs(count):
            if count == nums_len:
                combinations.append(combination[:])
            for num in nums:
                if num in combination:
                    continue
                combination.append(num)
                dfs(count+1)
                combination.pop()
        dfs(0)
        return combinations
