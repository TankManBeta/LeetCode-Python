# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2023/3/12 14:44
"""
from collections import defaultdict
from typing import List

"""
给你 n 个城市，编号为从 1 到 n 。同时给你一个大小为 n-1 的数组 edges ，其中 edges[i] = [ui, vi] 表示城市 ui 和 vi 之间有一条
双向边。题目保证任意城市之间只有唯一的一条路径。换句话说，所有城市形成了一棵 树 。
一棵 子树 是城市的一个子集，且子集中任意城市之间可以通过子集中的其他城市和边到达。两个子树被认为不一样的条件是至少有一个城市在
其中一棵子树中存在，但在另一棵子树中不存在。
对于 d 从 1 到 n-1 ，请你找到城市间 最大距离 恰好为 d 的所有子树数目。
请你返回一个大小为 n-1 的数组，其中第 d 个元素（下标从 1 开始）是城市间 最大距离 恰好等于 d 的子树数目。
请注意，两个城市间距离定义为它们之间需要经过的边的数目。 

示例 1：
输入：n = 4, edges = [[1,2],[2,3],[2,4]]
输出：[3,4,0]
解释：
子树 {1,2}, {2,3} 和 {2,4} 最大距离都是 1 。
子树 {1,2,3}, {1,2,4}, {2,3,4} 和 {1,2,3,4} 最大距离都为 2 。
不存在城市间最大距离为 3 的子树。

示例 2：
输入：n = 2, edges = [[1,2]]
输出：[1]

示例 3：
输入：n = 3, edges = [[1,2],[2,3]]
输出：[2,1]
"""
"""
思路：枚举子集。首先先建邻接表；接下来，我们在 [1,..2^n−1] 的范围内枚举子树 mask，对于每个子树：如果 mask 的二进制表示中只有
一个二进制位为 1，即 mask∈[1,2,4,8,⋯,2^n−1]，则跳过该 mask，因为这些 mask 表示的子树只有一个节点，不符合题意；否则，我们找到 
mask 的二进制表示中最高位的二进制位为 1 的位置，记为 cur。然后从节点 cur 出发，通过深度优先搜索或者广度优先搜索，找到树直径的
一个端点 nxt，然后我们再从节点 nxt 出发，同样通过深度优先搜索或者广度优先搜索，过程中记录下最大距离 mx。当走到最深的节点时，
即可得知树的直径。此时我们更新答案数组 ans，将 ans[mx−1] 的值加 1。注意，这里是 mx−1，因为题目中的最大距离是从 1 开始计数的。
最后，枚举完所有的子树，返回答案数组 ans 即可。
"""


class Solution:
    @staticmethod
    def countSubgraphsForEachDiameter(n: int, edges: List[List[int]]) -> List[int]:
        def dfs(u: int, d: int = 0):
            nonlocal mx, nxt, msk
            # 更新最长距离及端点
            if mx < d:
                mx, nxt = d, u
            # 当前位置访问过就取反
            msk ^= 1 << u
            # 移动到u的邻接点
            for v in g[u]:
                if msk >> v & 1:
                    dfs(v, d + 1)

        g = defaultdict(list)
        for u, v in edges:
            u, v = u - 1, v - 1
            g[u].append(v)
            g[v].append(u)
        ans = [0] * (n - 1)
        nxt = mx = 0
        for mask in range(1, 1 << n):
            # 树中只有一个节点
            if mask & (mask - 1) == 0:
                continue
            msk, mx = mask, 0
            # 获取最高位
            cur = msk.bit_length() - 1
            # 从当前最高位开始找到树直径的一个端点
            dfs(cur)
            # 当前需要判断的mask中每一个节点都属于这个树
            if msk == 0:
                msk, mx = mask, 0
                # 从找到的端点开始找另一个端点
                dfs(nxt)
                ans[mx - 1] += 1
        return ans
