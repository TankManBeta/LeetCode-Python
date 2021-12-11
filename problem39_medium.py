# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2021/12/9 10:53
"""
"""
给定一个无重复元素的正整数数组 candidates 和一个正整数 target ，找出 candidates 中所有可以使数字和为目标数 target 的唯一组合。
candidates 中的数字可以无限制重复被选取。如果至少一个所选数字数量不同，则两种组合是唯一的。 
对于给定的输入，保证和为 target 的唯一组合数少于 150 个。

输入: candidates = [2,3,6,7], target = 7
输出: [[7],[2,2,3]]

输入: candidates = [2,3,5], target = 8
输出: [[2,2,2,2],[2,3,3],[3,5]]

输入: candidates = [2], target = 1
输出: []

输入: candidates = [1], target = 1
输出: [[1]]

输入: candidates = [1], target = 2
输出: [[1,1]]
"""
"""
思路：数组升序排列（解决重复），直接dfs，结果大于等于target就返回继续找下一个，注意返回时现场的还原
"""


class Solution(object):
    @staticmethod
    def combination_sum(candidates, target):
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
                # 大坑
                combinations.append(combination[:])
            if total > target:
                return
            for i in range(start, len_candidates):
                if total+candidates[i] > target:
                    return
                total += candidates[i]
                combination.append(candidates[i])
                dfs(total, i)
                total -= candidates[i]
                combination.pop()
        candidates = sorted(candidates)
        dfs(0, 0)
        return combinations
