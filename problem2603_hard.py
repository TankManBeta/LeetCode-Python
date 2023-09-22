# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2023/9/21 15:49
"""
from collections import deque, defaultdict
from typing import List

"""
给你一个 n 个节点的无向无根树，节点编号从 0 到 n - 1 。给你整数 n 和一个长度为 n - 1 的二维整数数组 edges ，其中 edges[i] = [ai, bi] 
表示树中节点 ai 和 bi 之间有一条边。再给你一个长度为 n 的数组 coins ，其中 coins[i] 可能为 0 也可能为 1 ，1 表示节点 i 处有一个金币。
一开始，你需要选择树中任意一个节点出发。你可以执行下述操作任意次：
收集距离当前节点距离为 2 以内的所有金币，或者
移动到树中一个相邻节点。
你需要收集树中所有的金币，并且回到出发节点，请你返回最少经过的边数。
如果你多次经过一条边，每一次经过都会给答案加一。 

示例 1：
输入：coins = [1,0,0,0,0,1], edges = [[0,1],[1,2],[2,3],[3,4],[4,5]]
输出：2
解释：从节点 2 出发，收集节点 0 处的金币，移动到节点 3 ，收集节点 5 处的金币，然后移动回节点 2 。

示例 2：
输入：coins = [0,0,0,1,1,0,0,1], edges = [[0,1],[0,2],[1,3],[1,4],[2,5],[5,6],[5,7]]
输出：2
解释：从节点 0 出发，收集节点 4 和 3 处的金币，移动到节点 2 处，收集节点 7 处的金币，移动回节点 0 。
"""
"""
思路：拓扑排序。我们先将 edges 中的边转换成邻接表 g，其中 g[i] 表示节点 i 的所有邻接节点，用集合表示。接下来我们遍历所有节点，找到 coins[i]=0
且 g[i] 中只有一个节点的节点（也即是金币为 0 的叶子节点），将其加入队列 q 中。然后我们不断地从队列中取出节点，将其从邻接表中删除，然后判断其
邻接节点是否满足 coins[j]=0 且 g[j] 中只有一个节点的条件，如果满足则将其加入队列 q 中。循环，直至队列为空。经过上述操作后，我们得到了一棵
新的树，且树的叶子节点都是金币为 1 的节点。然后，我们再删除剩下的两层叶子节点，最终得到的是一棵所有节点都需要被访问的节点，我们只需要统计其边数，
乘上 2，即为答案。
"""


class Solution:
    @staticmethod
    def collectTheCoins(coins: List[int], edges: List[List[int]]) -> int:
        g = defaultdict(set)
        for a, b in edges:
            g[a].add(b)
            g[b].add(a)
        n = len(coins)
        q = deque(i for i in range(n) if len(g[i]) == 1 and coins[i] == 0)
        while q:
            i = q.popleft()
            for j in g[i]:
                g[j].remove(i)
                if coins[j] == 0 and len(g[j]) == 1:
                    q.append(j)
            g[i].clear()
        for k in range(2):
            q = [i for i in range(n) if len(g[i]) == 1]
            for i in q:
                for j in g[i]:
                    g[j].remove(i)
                g[i].clear()
        return sum(len(g[a]) > 0 and len(g[b]) > 0 for a, b in edges) * 2
