# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2021/12/9 15:49
"""
"""
给定一个数组 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。
candidates 中的每个数字在每个组合中只能使用一次。
注意：解集不能包含重复的组合。 

输入: candidates = [10,1,2,7,6,1,5], target = 8,
输出:
[
[1,1,6],
[1,2,5],
[1,7],
[2,6]
]

输入: candidates = [2,5,2,1,2], target = 5,
输出:
[
[1,2,2],
[5]
]
"""
"""
思路：同上一题相似，主要是判断重复情况
"""


class Solution(object):
    @staticmethod
    def combination_sum2(candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        combination = list()
        combinations = list()
        len_candidates = len(candidates)

        def dfs(total, start):
            if total == target:
                combinations.append(combination[:])
            if total > target:
                return
            for i in range(start, len_candidates):
                if i >start and candidates[i] == candidates[i-1]:
                    continue
                if total+candidates[i] > target:
                    return
                total += candidates[i]
                combination.append(candidates[i])
                dfs(total, i+1)
                total -= candidates[i]
                combination.pop()
        candidates = sorted(candidates)
        dfs(0, 0)
        return combinations
