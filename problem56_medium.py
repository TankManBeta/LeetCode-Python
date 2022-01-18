# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2022/1/17 17:09
"""
"""
以数组 intervals 表示若干个区间的集合，其中单个区间为 intervals[i] = [start, end]。
请你合并所有重叠的区间，并返回一个不重叠的区间数组，该数组需恰好覆盖输入中的所有区间。

输入：intervals = [[1,3],[2,6],[8,10],[15,18]]
输出：[[1,6],[8,10],[15,18]]
解释：区间 [1,3] 和 [2,6] 重叠, 将它们合并为 [1,6].

输入：intervals = [[1,4],[4,5]]
输出：[[1,5]]
解释：区间 [1,4] 和 [4,5] 可被视为重叠区间。
"""
"""
思路：
先排序，然后直接比较前一个的尾和后一个的头并合并
"""


class Solution(object):
    @staticmethod
    def merge(intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        sorted_intervals = sorted(intervals)
        i = 0
        while i < len(sorted_intervals) - 1:
            if sorted_intervals[i][1] >= sorted_intervals[i + 1][0]:
                sorted_intervals[i:i + 2] = (
                [sorted_intervals[i][0], max(sorted_intervals[i][1], sorted_intervals[i + 1][1])],)
            else:
                i += 1
        return sorted_intervals
