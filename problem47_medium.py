# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2021/12/13 17:54
"""
"""
给定一个可包含重复数字的序列 nums ，按任意顺序 返回所有不重复的全排列。

输入：nums = [1,1,2]
输出：
[[1,1,2],[1,2,1],[2,1,1]]
 
输入：nums = [1,2,3]
输出：[[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
"""
"""
思路：同46，额外增加一个visited数组，同时判断是否已经存在即可
"""


class Solution(object):
    @staticmethod
    def permute_unique(nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        combination = list()
        combinations = list()
        nums_len = len(nums)
        visited = [False] * nums_len

        def dfs(count):
            if count == nums_len:
                if combination not in combinations:
                    combinations.append(combination[:])
            for i in range(0, nums_len):
                if not visited[i]:
                    combination.append(nums[i])
                    visited[i] = True
                    dfs(count + 1)
                    combination.pop()
                    visited[i] = False

        dfs(0)
        return combinations
