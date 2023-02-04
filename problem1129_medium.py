# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2023/2/2 7:49
"""
from typing import List

"""
在一个有向图中，节点分别标记为 0, 1, ..., n-1。图中每条边为红色或者蓝色，且存在自环或平行边。
red_edges 中的每一个 [i, j] 对表示从节点 i 到节点 j 的红色有向边。类似地，blue_edges 中的每一个 [i, j] 对表示从节点 i 到节点 j 的蓝色有向边。
返回长度为 n 的数组 answer，其中 answer[X] 是从节点 0 到节点 X 的红色边和蓝色边交替出现的最短路径的长度。如果不存在这样的路径，那么 answer[x] = -1。

示例 1：
输入：n = 3, red_edges = [[0,1],[1,2]], blue_edges = []
输出：[0,1,-1]

示例 2：
输入：n = 3, red_edges = [[0,1]], blue_edges = [[2,1]]
输出：[0,1,-1]

示例 3：
输入：n = 3, red_edges = [[1,0]], blue_edges = [[2,1]]
输出：[0,-1,-1]

示例 4：
输入：n = 3, red_edges = [[0,1]], blue_edges = [[1,2]]
输出：[0,1,2]

示例 5：
输入：n = 3, red_edges = [[0,1],[0,2]], blue_edges = [[1,0]]
输出：[0,1,1]
"""
"""
思路：如果存在从节点 0 到节点 x 的类型 0 的颜色交替路径，并且从节点 x 到节点 y 的有向边为蓝色，那么该路径加上该有向边组成了从节点 
0 到节点 y 的类型 1 的颜色交替路径。类似地，如果存在从节点 0 到节点 x 的类型 1 的颜色交替路径，并且从节点 x 到节点 y 的有向边为红色，
那么该路径加上该有向边组成了从节点 0 到节点 y 的类型 0 的颜色交替路径。
使用广度优先搜索获取从节点 0 到某一节点的两种类型的颜色交替最短路径的长度，广度优先搜索的队列元素由节点编号和节点路径类型组成，
初始时节点 0 到节点 0 的两种类型的颜色交替最短路径的长度都是 0，将两个初始值入队。对于某一个队列元素，节点编号为 x，节点路径类型
为 t，那么根据类型 t 选择颜色为 1−t 的相邻有向边，如果有向边的终点节点 y 对应类型 1−t 没有被访问过，那么更新节点 y 的类型 1−t 
的颜色交替最短路径的长度为节点 x 的类型 t 的颜色交替最短路径的长度加 1，并且将它入队。
从节点 0 到某一节点的颜色交替最短路径的长度为两种类型的颜色交替最短路径长度的最小值。
"""


class Solution:
    @staticmethod
    def shortestAlternatingPaths(n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        g = [[] for _ in range(n)]
        for x, y in redEdges:
            g[x].append((y, 0))
        for x, y in blueEdges:
            g[x].append((y, 1))

        dis = [-1] * n
        vis = {(0, 0), (0, 1)}
        q = [(0, 0), (0, 1)]
        level = 0
        while q:
            tmp = q
            q = []
            for x, color in tmp:
                if dis[x] == -1:
                    dis[x] = level
                for p in g[x]:
                    if p[1] != color and p not in vis:
                        vis.add(p)
                        q.append(p)
            level += 1
        return dis
