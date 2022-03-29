# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2022/3/29 9:52
"""
import collections

"""
你这个学期必须选修 numCourses 门课程，记为 0 到 numCourses - 1 。
在选修某些课程之前需要一些先修课程。 先修课程按数组prerequisites给出，其中prerequisites[i]=[ai,bi]，
表示如果要学习课程 ai 则 必须 先学习课程  bi 。
例如，先修课程对 [0, 1] 表示：想要学习课程 0 ，你需要先完成课程 1 。
请你判断是否可能完成所有课程的学习？如果可以，返回 true ；否则，返回 false 。

输入：numCourses = 2, prerequisites = [[1,0]]
输出：true
解释：总共有 2 门课程。学习课程 1 之前，你需要完成课程 0 。这是可能的。

输入：numCourses = 2, prerequisites = [[1,0],[0,1]]
输出：false
解释：总共有 2 门课程。学习课程 1 之前，你需要先完成​课程 0 ；并且学习课程 0 之前，你还应先完成课程 1 。这是不可能的。
"""
"""
思路：
（1）dfs，对于每一个点，我们定义三种状态，已搜索，搜索中，未搜索，对于dfs的每一个点，先去看他邻居节点的状态，如果邻居的状态是
未搜索，则对邻居进行dfs；如果邻居的状态也是未搜索，说明这个状态是非法的
（2）bfs，每次将入度为0的点加入队列，弹出时将它指向的另一个节点的入度减一，最后看入队的节点数和n是否相等
"""


class Solution(object):
    @staticmethod
    def canFinish(numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        # edges = collections.defaultdict(list)
        # visited = [0] * numCourses
        # result = list()
        # valid = True
        # for info in prerequisites:
        #     edges[info[1]].append(info[0])

        # def dfs(u):
        #     nonlocal valid
        #     visited[u] = 1
        #     for v in edges[u]:
        #         if visited[v] == 0:
        #             dfs(v)
        #             if not valid:
        #                 return
        #         elif visited[v] == 1:
        #             valid = False
        #             return
        #     visited[u] = 2
        #     result.append(u)

        # for i in range(numCourses):
        #     if valid and not visited[i]:
        #         dfs(i)
        # return valid

        edges = collections.defaultdict(list)
        indeg = [0] * numCourses
        for pre in prerequisites:
            edges[pre[1]].append(pre[0])
            indeg[pre[0]] += 1
        q = collections.deque([u for u in range(numCourses) if indeg[u] == 0])
        visited = 0
        while q:
            visited += 1
            u = q.popleft()
            for v in edges[u]:
                indeg[v] -= 1
                if indeg[v] == 0:
                    q.append(v)
        return visited == numCourses
