# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2023/3/15 9:51
"""
from typing import List

"""
n 座城市和一些连接这些城市的道路 roads 共同组成一个基础设施网络。每个 roads[i] = [ai, bi] 都表示在城市 ai 和 bi 之间有一条双向道路。
两座不同城市构成的 城市对 的 网络秩 定义为：与这两座城市 直接 相连的道路总数。如果存在一条道路直接连接这两座城市，则这条道路只计算 一次 。
整个基础设施网络的 最大网络秩 是所有不同城市对中的 最大网络秩 。
给你整数 n 和数组 roads，返回整个基础设施网络的 最大网络秩 。

示例 1：
输入：n = 4, roads = [[0,1],[0,3],[1,2],[1,3]]
输出：4
解释：城市 0 和 1 的网络秩是 4，因为共有 4 条道路与城市 0 或 1 相连。位于 0 和 1 之间的道路只计算一次。

示例 2：
输入：n = 5, roads = [[0,1],[0,3],[1,2],[1,3],[2,3],[2,4]]
输出：5
解释：共有 5 条道路与城市 1 或 2 相连。

示例 3：
输入：n = 8, roads = [[0,1],[1,2],[2,3],[2,4],[5,6],[5,7]]
输出：5
解释：2 和 5 的网络秩为 5，注意并非所有的城市都需要连接起来。
"""
"""
思路：直接模拟即可。一开始想的是用哈希表统计以每个城市为起点的城市的数目，然后遍历，把他们加起来并且减去重复的边，时间有点长。
其实可以用存的时候直接记录，一维数组 cnt 记录每个城市的度，用二维数组 g 记录每对城市之间是否有道路相连。
"""


class Solution:
    @staticmethod
    def maximalNetworkRank(n: int, roads: List[List[int]]) -> int:
        # count = defaultdict(list)
        # for road in roads:
        #     count[road[0]].append(road[1])
        #     count[road[1]].append(road[0])
        # ans = 0
        # for i in range(n):
        #     for j in range(i+1, n):
        #         ans = max(len(count[i])+len(count[j])-int(i in count[j]), ans)
        # return ans

        ans = 0
        cnt = [0] * n
        g = [[0 for _ in range(n)] for _ in range(n)]
        for a, b in roads:
            cnt[a] += 1
            cnt[b] += 1
            g[a][b] = g[b][a] = 1
        for i in range(n):
            for j in range(i + 1, n):
                ans = max(ans, cnt[i] + cnt[j] - g[i][j])
        return ans
