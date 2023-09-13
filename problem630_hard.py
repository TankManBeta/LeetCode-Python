# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2023/9/11 21:31
"""
from heapq import heappush, heappop
from typing import List

"""
这里有 n 门不同的在线课程，按从 1 到 n 编号。给你一个数组 courses ，其中 courses[i] = [durationi, lastDayi] 表示第 i 门课将会 持续 
上 durationi 天课，并且必须在不晚于 lastDayi 的时候完成。
你的学期从第 1 天开始。且不能同时修读两门及两门以上的课程。
返回你最多可以修读的课程数目。 

示例 1：
输入：courses = [[100, 200], [200, 1300], [1000, 1250], [2000, 3200]]
输出：3
解释：
这里一共有 4 门课程，但是你最多可以修 3 门：
首先，修第 1 门课，耗费 100 天，在第 100 天完成，在第 101 天开始下门课。
第二，修第 3 门课，耗费 1000 天，在第 1100 天完成，在第 1101 天开始下门课程。
第三，修第 2 门课，耗时 200 天，在第 1300 天完成。
第 4 门课现在不能修，因为将会在第 3300 天完成它，这已经超出了关闭日期。

示例 2：
输入：courses = [[1,2]]
输出：1

示例 3：
输入：courses = [[3,2],[4,3]]
输出：0
"""
"""
思路：按照课程的结束时间进行升序排序，每次选择结束时间最早的课程进行上课。如果已选择的课程的总时间 s 超过了当前课程的结束时间 last，那么我们
就将此前选择的课程中耗时最长的课程去掉，直到能够满足当前课程的结束时间为止。这里我们使用一个优先队列（大根堆） pq 来维护当前已经选择的课程的
耗时，每次我们都从优先队列中取出耗时最长的课程进行去除。最后，优先队列中的元素个数即为我们能够选择的课程数目。
"""


class Solution:
    @staticmethod
    def scheduleCourse(courses: List[List[int]]) -> int:
        courses.sort(key=lambda x: x[1])
        pq = []
        s = 0
        for duration, last in courses:
            heappush(pq, -duration)
            s += duration
            while s > last:
                s += heappop(pq)
        return len(pq)
