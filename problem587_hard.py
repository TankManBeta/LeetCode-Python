# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2022/4/25 13:05
"""
"""
在一个二维的花园中，有一些用 (x, y) 坐标表示的树。由于安装费用十分昂贵，你的任务是先用最短的绳子围起所有的树。
只有当所有的树都被绳子包围时，花园才能围好栅栏。你需要找到正好位于栅栏边界上的树的坐标。


输入: [[1,1],[2,2],[2,0],[2,4],[3,3],[4,2]]
输出: [[1,1],[2,0],[4,2],[3,3],[2,4]]

输入: [[1,2],[2,2],[4,2]]
输出: [[1,2],[2,2],[4,2]]
"""
"""
思路：题目是典型的凸包问题
（1）Jarvis算法，首先必须要从凸包上的某一点开始，比如从给定点集中最左边的点开始，例如最左的一点A1。然后选择A2点使得
所有点都在向量A1A2的左方或者右方，我们每次选择左方，需要比较所有点以A1为原点的极坐标角度。然后以 A_{2}A2为原点，重复这个步骤，
依次找到A3,A4,…,Ak。
（2）Andrew算法，先对点进行从小到大排序，然后算上凸包和下凸包，不停加减点即可
"""


class Solution(object):
    @staticmethod
    def outerTrees(trees):
        """
        :type trees: List[List[int]]
        :rtype: List[List[int]]
        """

        # def sign(p, q, r):
        #     return (p[0] - r[0])*(q[1] - r[1]) - (p[1] - r[1])*(q[0] - r[0])

        # def check_valid(points, r):
        #     points.append(r)
        #     while len(points) >= 3 and sign(*points[-3:]) < 0:
        #         points.pop(-2)
        #     return points

        # trees.sort(key = lambda p: (p[0], p[1]))
        # lower = reduce(check_valid, trees, [])
        # upper = reduce(check_valid, trees[::-1], [])
        # return lower + list(filter(lambda p: p not in lower, upper))

        # def cross(p, q, r):
        #     return (q[0] - p[0]) * (r[1] - q[1]) - (q[1] - p[1]) * (r[0] - q[0])

        # n = len(trees)
        # if n < 4:
        #     return trees

        # leftMost = 0
        # for i, tree in enumerate(trees):
        #     if tree[0] < trees[leftMost][0] or (tree[0] == trees[leftMost][0] and tree[1] < trees[leftMost][1]):
        #         leftMost = i

        # ans = []
        # vis = [False] * n
        # p = leftMost
        # while True:
        #     q = (p + 1) % n
        #     for r, tree in enumerate(trees):
        #         # // 如果 r 在 pq 的右侧，则 q = r
        #         if cross(trees[p], trees[q], tree) < 0:
        #             q = r
        #     # 是否存在点 i, 使得 p q i 在同一条直线上
        #     for i, b in enumerate(vis):
        #         if not b and i != p and i != q and cross(trees[p], trees[q], trees[i]) == 0:
        #             ans.append(trees[i])
        #             vis[i] = True
        #     if not vis[q]:
        #         ans.append(trees[q])
        #         vis[q] = True
        #     p = q
        #     if p == leftMost:
        #         break
        # return ans

        def cross(p, q, r):
            return (q[0] - p[0]) * (r[1] - q[1]) - (q[1] - p[1]) * (r[0] - q[0])

        n = len(trees)
        if n < 4:
            return trees

        trees.sort()

        hull = [0]
        used = [False] * n

        for i in range(1, n):
            while len(hull) > 1 and cross(trees[hull[-2]], trees[hull[-1]], trees[i]) < 0:
                used[hull.pop()] = False
            used[i] = True
            hull.append(i)
        m = len(hull)
        for i in range(n - 2, -1, -1):
            if not used[i]:
                while len(hull) > m and cross(trees[hull[-2]], trees[hull[-1]], trees[i]) < 0:
                    used[hull.pop()] = False
                used[i] = True
                hull.append(i)
        hull.pop()

        return [trees[i] for i in hull]
