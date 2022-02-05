# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2022/2/5 16:38
"""
"""
给定两个整数 n 和 k，返回范围 [1, n] 中所有可能的 k 个数的组合。
你可以按 任何顺序 返回答案。

输入：n = 4, k = 2
输出：
[
  [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4],
]

输入：n = 1, k = 1
输出：[[1]]
"""
"""
思路：dfs+剪枝，搜索起点的上界 + 接下来要选择的元素个数 - 1 = n
"""


class Solution(object):
    @staticmethod
    def combine(n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        combination = list()
        combinations = list()

        def dfs(x, depth):
            if depth == k:
                combinations.append(combination[:])
                return
            for i in range(x, n-k+depth+2):
                combination.append(i)
                dfs(i+1, depth+1)
                combination.pop()
        dfs(1, 0)
        return combinations
