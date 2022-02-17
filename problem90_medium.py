# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2022/2/16 0:45
"""
"""
给你一个整数数组 nums ，其中可能包含重复元素，请你返回该数组所有可能的子集（幂集）。
解集 不能 包含重复的子集。返回的解集中，子集可以按 任意顺序 排列。

输入：nums = [1,2,2]
输出：[[],[1],[1,2],[1,2,2],[2],[2,2]]

输入：nums = [0]
输出：[[],[0]]
"""
"""
思路：
（1）直接在添加结果时排序，看是否已经存在
（2）要保证不重复，那么在每一层展开的时候需要保证后一个节点不等于前一个节点，不然必定重复。
"""


class Solution(object):
    @staticmethod
    def subsets_with_dup(nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # combination = list()
        # combinations = list()
        # count = len(nums)
        #
        # def dfs(k):
        #     temp = sorted(combination)
        #     if temp not in combinations:
        #         combinations.append(temp[:])
        #     for i in range(k, count):
        #         combination.append(nums[i])
        #         dfs(i+1)
        #         combination.pop()
        # dfs(0)
        # return combinations

        path = []
        res = []

        def recur(num, path):
            res.append(list(path))
            if len(num) == 0:
                return
            for i in range(len(num)):
                if i > 0 and num[i] == num[i-1]:
                    continue
                path.append(num[i])
                recur(num[i+1:], path)
                path.pop()
        nums.sort()
        recur(nums, path)
        return res
