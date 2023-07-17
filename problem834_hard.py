# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2023/7/16 23:29
"""
from collections import defaultdict
from typing import List

"""
给定一个无向、连通的树。树中有 n 个标记为 0...n-1 的节点以及 n-1 条边 。
给定整数 n 和数组 edges ， edges[i] = [ai, bi]表示树中的节点 ai 和 bi 之间有一条边。
返回长度为 n 的数组 answer ，其中 answer[i] 是树中第 i 个节点与所有其他节点之间的距离之和。 

示例 1:
输入: n = 6, edges = [[0,1],[0,2],[2,3],[2,4],[2,5]]
输出: [8,12,6,10,10,10]
解释: 树如图所示。
我们可以计算出 dist(0,1) + dist(0,2) + dist(0,3) + dist(0,4) + dist(0,5) 
也就是 1 + 1 + 2 + 2 + 2 = 8。 因此，answer[0] = 8，以此类推。

示例 2:
输入: n = 1, edges = []
输出: [0]

示例 3:
输入: n = 2, edges = [[1,0]]
输出: [1,1]
"""
"""
思路：树形dp。我们先跑一遍 DFS，计算出每个节点的子树大小，记录在数组 size 中，并且统计出节点 0 到其他节点的距离之和，记录在 
ans[0] 中。接下来，我们再跑一遍 DFS，枚举每个点作为根节点时，其他节点到根节点的距离之和。假设当前节点 i 的答案为 t，当我们从
节点 i 转移到节点 j 时，距离之和变为 t−size[j]+n−size[j]，即距离节点 j 及其子树节点的距离之和减少 size[j]，而距离其它节点的
距离之和增加 n−size[j]。
"""


class Solution:
    @staticmethod
    def sumOfDistancesInTree(n: int, edges: List[List[int]]) -> List[int]:
        def dfs1(i: int, fa: int, d: int):
            ans[0] += d
            size[i] = 1
            for j in g[i]:
                if j != fa:
                    dfs1(j, i, d + 1)
                    size[i] += size[j]

        def dfs2(i: int, fa: int, t: int):
            ans[i] = t
            for j in g[i]:
                if j != fa:
                    dfs2(j, i, t - size[j] + n - size[j])

        g = defaultdict(list)
        for a, b in edges:
            g[a].append(b)
            g[b].append(a)

        ans = [0] * n
        size = [0] * n
        dfs1(0, -1, 0)
        dfs2(0, -1, ans[0])
        return ans
