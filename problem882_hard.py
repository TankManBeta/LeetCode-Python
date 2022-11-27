# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2022/11/26 15:51
"""
from heapq import heappop, heappush
from math import inf
from typing import Tuple, List

"""
给你一个无向图（原始图），图中有 n 个节点，编号从 0 到 n - 1 。你决定将图中的每条边 细分 为一条节点链，每条边之间的新节点数各不相同。
图用由边组成的二维数组 edges 表示，其中 edges[i] = [ui, vi, cnti] 表示原始图中节点 ui 和 vi 之间存在一条边，cnti 是将边 细分 后的新节点总数。
注意，cnti == 0 表示边不可细分。
要 细分 边 [ui, vi] ，需要将其替换为 (cnti + 1) 条新边，和 cnti 个新节点。
新节点为 x1, x2, ..., xcnti ，新边为 [ui, x1], [x1, x2], [x2, x3], ..., [xcnti+1, xcnti], [xcnti, vi] 。
现在得到一个 新的细分图 ，请你计算从节点 0 出发，可以到达多少个节点？如果节点间距离是 maxMoves 或更少，则视为 可以到达 。
给你原始图和 maxMoves ，返回 新的细分图中从节点 0 出发 可到达的节点数 。

输入：edges = [[0,1,10],[0,2,1],[1,2,2]], maxMoves = 6, n = 3
输出：13
解释：边的细分情况如上图所示。
可以到达的节点已经用黄色标注出来。

示例 2：
输入：edges = [[0,1,4],[1,2,6],[0,2,8],[1,3,1]], maxMoves = 10, n = 4
输出：23

示例 3：
输入：edges = [[1,2,4],[1,4,5],[1,3,1],[2,3,4],[3,4,5]], maxMoves = 17, n = 5
输出：1
解释：节点 0 与图的其余部分没有连通，所以只有节点 0 可以到达。
"""
"""
思路：先建图，边的距离设为cnti+1。先用Dijkstra算法求出源点到各个点之间的距离s，只要s<maxMoves，说明肯定可以到达，在此基础之上
对于一条边的两个顶点而言，两个顶点之间新节点能到达的个数为在到达顶点之后还能走的步数之和与cnti的较小值
"""


class Solution:
    def reachableNodes(self, edges: List[List[int]], maxMoves: int, n: int) -> int:
        g = [[] for _ in range(n)]
        for u, v, cnt in edges:
            g[u].append((v, cnt + 1))
            g[v].append((u, cnt + 1))

        dist = self.dijkstra(g, 0)  # 从 0 出发的最短路

        ans = sum(d <= maxMoves for d in dist)  # 可以在 maxMoves 步内到达的点的个数
        for u, v, cnt in edges:
            a = max(maxMoves - dist[u], 0)
            b = max(maxMoves - dist[v], 0)
            ans += min(a + b, cnt)  # 这条边上可以到达的节点数
        return ans

    def dijkstra(self, g: List[List[Tuple[int]]], start: int) -> List[int]:
        dist = [inf]*len(g)
        dist[start] = 0
        h = [(0, start)]
        while h:
            d, x = heappop(h)
            if d > dist[x]:
                continue
            for y, edge in g[x]:
                new_dist = edge + dist[x]
                if new_dist < dist[y]:
                    dist[y] = new_dist
                    heappush(h, (new_dist, y))
        return dist
