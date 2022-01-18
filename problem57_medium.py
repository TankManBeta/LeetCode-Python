# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2022/1/18 13:34
"""
"""
给你一个 无重叠的 ，按照区间起始端点排序的区间列表。
在列表中插入一个新的区间，你需要确保列表中的区间仍然有序且不重叠（如果有必要的话，可以合并区间）。

输入：intervals = [[1,3],[6,9]], newInterval = [2,5]
输出：[[1,5],[6,9]]

输入：intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
输出：[[1,2],[3,10],[12,16]]
解释：这是因为新的区间 [4,8] 与 [3,5],[6,7],[8,10] 重叠。

输入：intervals = [], newInterval = [5,7]
输出：[[5,7]]

输入：intervals = [[1,5]], newInterval = [2,3]
输出：[[1,5]]

输入：intervals = [[1,5]], newInterval = [2,7]
输出：[[1,7]]
"""
"""
思路：判断新区间的左右两端分别在哪个区间，然后合并区间即可
"""


class Solution(object):
    @staticmethod
    def insert(intervals, new_interval):
        """
        :type intervals: List[List[int]]
        :type new_interval: List[int]
        :rtype: List[List[int]]
        """
        if not intervals:
            intervals.append(new_interval)
            return intervals
        if new_interval[0] > intervals[-1][1]:
            intervals.append(new_interval)
            return intervals
        if new_interval[0] == intervals[-1][1]:
            intervals[-1][1] = new_interval[-1]
            return intervals
        if new_interval[1] < intervals[0][0]:
            intervals.insert(0, new_interval)
            return intervals
        if new_interval[1] == intervals[0][0]:
            intervals[0][0] = new_interval[0]
            return intervals

        len_intervals = len(intervals)
        left, right = 0, len_intervals-1
        i = 0
        while i < len_intervals:
            if intervals[i][0] <= new_interval[0] <= intervals[i][1]:
                left = i
            if intervals[i-1][1] < new_interval[0] < intervals[i][0]:
                left = i
            if intervals[i][0] <= new_interval[1] <= intervals[i][1]:
                right = i
            if intervals[i-1][1] < new_interval[1] < intervals[i][0]:
                right = i-1
            i += 1

        intervals[left: right+1] = ([min(intervals[left][0], new_interval[0]),
                                     max(new_interval[1], intervals[right][1])],)
        return intervals
