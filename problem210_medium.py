# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2022/3/29 10:03
"""
import collections

"""
现在你总共有 numCourses 门课需要选，记为 0 到 numCourses - 1。给你一个数组 prerequisites ，其中 prerequisites[i] = [ai,bi]，
表示在选修课程 ai 前 必须 先选修 bi 。
例如，想要学习课程 0 ，你需要先完成课程 1 ，我们用一个匹配来表示：[0,1] 。
返回你为了学完所有课程所安排的学习顺序。可能会有多个正确的顺序，你只要返回任意一种就可以了。
如果不可能完成所有课程，返回一个空数组。

输入：numCourses = 2, prerequisites = [[1,0]]
输出：[0,1]
解释：总共有 2 门课程。要学习课程 1，你需要先完成课程 0。因此，正确的课程顺序为 [0,1] 。

输入：numCourses = 2, prerequisites = [[1,0]]
输出：[0,1]
解释：总共有 2 门课程。要学习课程 1，你需要先完成课程 0。因此，正确的课程顺序为 [0,1] 。

输入：numCourses = 4, prerequisites = [[1,0],[2,0],[3,1],[3,2]]
输出：[0,2,1,3]
解释：总共有 4 门课程。要学习课程 3，你应该先完成课程 1 和课程 2。并且课程 1 和课程 2 都应该排在课程 0 之后。
因此，一个正确的课程顺序是 [0,1,2,3] 。另一个正确的排序是 [0,2,1,3] 。

输入：numCourses = 1, prerequisites = []
输出：[0]
"""
"""
思路：和207一样，只需要加个数组记录结果即可
"""


class Solution(object):
    @staticmethod
    def findOrder(numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        edges = collections.defaultdict(list)
        indeg = [0] * numCourses
        res = []
        for pre in prerequisites:
            edges[pre[1]].append(pre[0])
            indeg[pre[0]] += 1
        q = collections.deque([u for u in range(numCourses) if indeg[u] == 0])
        visited = 0
        while q:
            u = q.popleft()
            res.append(u)
            for v in edges[u]:
                indeg[v] -= 1
                if indeg[v] == 0:
                    q.append(v)
        return res if len(res) == numCourses else []