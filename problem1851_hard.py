# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2023/7/18 23:46
"""
from heapq import heappush, heappop
from typing import List

"""
给你一个二维整数数组 intervals ，其中 intervals[i] = [lefti, righti] 表示第 i 个区间开始于 lefti 、结束于 righti（包含两侧取值，
闭区间）。区间的 长度 定义为区间中包含的整数数目，更正式地表达是 righti - lefti + 1 。
再给你一个整数数组 queries 。第 j 个查询的答案是满足 lefti <= queries[j] <= righti 的 长度最小区间 i 的长度 。
如果不存在这样的区间，那么答案是 -1 。
以数组形式返回对应查询的所有答案。 

示例 1：
输入：intervals = [[1,4],[2,4],[3,6],[4,4]], queries = [2,3,4,5]
输出：[3,3,1,4]
解释：查询处理如下：
- Query = 2 ：区间 [2,4] 是包含 2 的最小区间，答案为 4 - 2 + 1 = 3 。
- Query = 3 ：区间 [2,4] 是包含 3 的最小区间，答案为 4 - 2 + 1 = 3 。
- Query = 4 ：区间 [4,4] 是包含 4 的最小区间，答案为 4 - 4 + 1 = 1 。
- Query = 5 ：区间 [3,6] 是包含 5 的最小区间，答案为 6 - 3 + 1 = 4 。

示例 2：
输入：intervals = [[2,3],[2,5],[1,8],[20,25]], queries = [2,19,5,22]
输出：[2,-1,4,6]
解释：查询处理如下：
- Query = 2 ：区间 [2,3] 是包含 2 的最小区间，答案为 3 - 2 + 1 = 2 。
- Query = 19：不存在包含 19 的区间，答案为 -1 。
- Query = 5 ：区间 [2,5] 是包含 5 的最小区间，答案为 5 - 2 + 1 = 4 。
- Query = 22：区间 [20,25] 是包含 22 的最小区间，答案为 25 - 20 + 1 = 6 。
"""
"""
思路：我们注意到，题目中查询的顺序并不会影响答案，并且涉及到的区间也不会发生变化，因此，我们考虑将所有的查询按照从小到大的顺序
进行排序，同时将所有的区间按照左端点从小到大的顺序进行排序。我们使用一个优先队列（小根堆） pq 来维护当前所有的区间，队列的每个
元素是一个二元组 (v,r)，表示一个区间长度为 v，右端点为 r 的区间。初始时，优先队列为空。另外，我们定义一个指针 i，指向当前遍历
到的区间，初始时 i=0。我们按照从小到大的顺序依次遍历每个查询 (x,j)，并进行如下操作：如果指针 i 尚未遍历完所有的区间，并且当前
遍历到的区间 [a,b] 的左端点小于等于 x，那么我们将该区间加入优先队列中，并将指针 i 后移一位，循环此过程；如果优先队列不为空，
并且堆顶元素的区间右端点小于 x，那么我们将堆顶元素弹出，循环此过程；此时，如果优先队列不为空，那么堆顶元素就是包含 x 的最小区间。
我们将其长度 v 加入答案数组 ans 中。在上述过程结束后，我们返回答案数组 ans 即可。
"""


class Solution:
    @staticmethod
    def minInterval(intervals: List[List[int]], queries: List[int]) -> List[int]:
        n, m = len(intervals), len(queries)
        intervals.sort()
        queries = sorted((x, i) for i, x in enumerate(queries))
        ans = [-1] * m
        pq = []
        i = 0
        for x, j in queries:
            while i < n and intervals[i][0] <= x:
                a, b = intervals[i]
                heappush(pq, (b - a + 1, b))
                i += 1
            while pq and pq[0][1] < x:
                heappop(pq)
            if pq:
                ans[j] = pq[0][0]
        return ans
