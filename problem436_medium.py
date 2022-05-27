# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2022/5/20 13:09
"""
from bisect import bisect_left

"""
给你一个区间数组 intervals ，其中 intervals[i] = [starti, endi] ，且每个 starti 都 不同 。
区间 i 的 右侧区间 可以记作区间 j ，并满足 startj >= endi ，且 startj 最小化 。
返回一个由每个区间 i 的 右侧区间 的最小起始位置组成的数组。如果某个区间 i 不存在对应的 右侧区间 ，则下标 i 处的值设为 -1 。

输入：intervals = [[1,2]]
输出：[-1]
解释：集合中只有一个区间，所以输出-1。

输入：intervals = [[3,4],[2,3],[1,2]]
输出：[-1,0,1]
解释：对于 [3,4] ，没有满足条件的“右侧”区间。
对于 [2,3] ，区间[3,4]具有最小的“右”起点;
对于 [1,2] ，区间[2,3]具有最小的“右”起点。

输入：intervals = [[1,4],[2,3],[3,4]]
输出：[-1,2,-1]
解释：对于区间 [1,4] 和 [3,4] ，没有满足条件的“右侧”区间。
对于 [2,3] ，区间 [3,4] 有最小的“右”起点。
"""
"""
思路：首先我们可以对区间 intervals 的起始位置进行排序，并将每个起始位置intervals[i][0]对应的索引i存储在数组startIntervals中，
然后枚举每个区间 i 的右端点 intervals[i][1]，利用二分查找来找到大于等于intervals[i][1] 的最小值 val 即可，此时区间 i 对应的
右侧区间即为右端点 val 对应的索引。
"""


class Solution(object):
    @staticmethod
    def findRightInterval(intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[int]
        """
        for i, interval in enumerate(intervals):
            interval.append(i)
        intervals.sort()

        n = len(intervals)
        ans = [-1] * n
        for _, end, id in intervals:
            i = bisect_left(intervals, [end])
            if i < n:
                ans[id] = intervals[i][2]
        return ans
