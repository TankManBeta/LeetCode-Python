# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2023/6/9 11:22
"""
from typing import List

"""
给你一个 n 个节点的 无向带权连通 图，节点编号为 0 到 n - 1 ，再给你一个整数数组 edges ，其中 edges[i] = [ai, bi, wi] 表示节点 
ai 和 bi 之间有一条边权为 wi 的边。
部分边的边权为 -1（wi = -1），其他边的边权都为 正 数（wi > 0）。
你需要将所有边权为 -1 的边都修改为范围 [1, 2 * 109] 中的 正整数 ，使得从节点 source 到节点 destination 的 最短距离 为整数 target 。
如果有 多种 修改方案可以使 source 和 destination 之间的最短距离等于 target ，你可以返回任意一种方案。
如果存在使 source 到 destination 最短距离为 target 的方案，请你按任意顺序返回包含所有边的数组（包括未修改边权的边）。
如果不存在这样的方案，请你返回一个 空数组 。
注意：你不能修改一开始边权为正数的边。 

示例 1：
输入：n = 5, edges = [[4,1,-1],[2,0,-1],[0,3,-1],[4,3,-1]], source = 0, destination = 1, target = 5
输出：[[4,1,1],[2,0,1],[0,3,3],[4,3,1]]
解释：上图展示了一个满足题意的修改方案，从 0 到 1 的最短距离为 5 。

示例 2：
输入：n = 3, edges = [[0,1,-1],[0,2,5]], source = 0, destination = 2, target = 6
输出：[]
解释：上图是一开始的图。没有办法通过修改边权为 -1 的边，使得 0 到 2 的最短距离等于 6 ，所以返回一个空数组。

示例 3：
输入：n = 4, edges = [[1,0,4],[1,2,3],[2,3,5],[0,3,-1]], source = 0, destination = 2, target = 6
输出：[[1,0,4],[1,2,3],[2,3,5],[0,3,1]]
解释：上图展示了一个满足题意的修改方案，从 0 到 2 的最短距离为 6 。
"""
"""
思路：我们先不考虑边权为 −1 的边，使用 Dijkstra 算法求出从 source 到 destination 的最短距离 d。
如果 d<target，说明存在一条完全由正权边组成的最短路径，此时无论我们如何修改边权为 −1 的边，都无法使得 source 到 destination 
的最短距离等于 target，因此不存在满足题意的修改方案，返回一个空数组即可。
如果 d=target，说明存在一条完全由正权边组成的、长度为 target 的最短路径，此时我们可以将所有边权为 −1 的边修改为最大值 2×10**9 即可。
如果 d>target，我们可以尝试往图中加入一条边权为 −1 的边，将边权设置为 1，然后再次使用 Dijkstra 算法求出从 source 到 destination 的最短距离 d。
    如果最短距离 d≤target，说明加入这条边后，可以使得最短路变短，而且最短路也一定经过这条边，那么我们只需要将这条边的边权改为 
    target−d+1，就可以使得最短路等于 target。然后我们将其余的边权为 −1 的边修改为最大值 2×10**9即可。
    如果最短距离 d>target，说明加入这条边后，最短路不会变短，那么我们贪心地将这条边的边权保持为 −1，然后继续尝试加入其余的边权为 −1 的边。
"""


class Solution:
    @staticmethod
    def modifiedGraphEdges(
            n: int, edges: List[List[int]], source: int, destination: int, target: int
    ) -> List[List[int]]:
        def dijkstra(edges: List[List[int]]) -> int:
            g = [[inf] * n for _ in range(n)]
            for a, b, w in edges:
                if w == -1:
                    continue
                g[a][b] = g[b][a] = w
            dist = [inf] * n
            dist[source] = 0
            vis = [False] * n
            for _ in range(n):
                k = -1
                for j in range(n):
                    if not vis[j] and (k == -1 or dist[k] > dist[j]):
                        k = j
                vis[k] = True
                for j in range(n):
                    dist[j] = min(dist[j], dist[k] + g[k][j])
            return dist[destination]

        inf = 2 * 10**9
        d = dijkstra(edges)
        if d < target:
            return []
        ok = d == target
        for e in edges:
            if e[2] > 0:
                continue
            if ok:
                e[2] = inf
                continue
            e[2] = 1
            d = dijkstra(edges)
            if d <= target:
                ok = True
                e[2] += target - d
        return edges if ok else []
