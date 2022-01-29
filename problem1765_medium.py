# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2022/1/29 14:36
"""
"""
给你一个大小为 m x n 的整数矩阵 isWater ，它代表了一个由 陆地 和 水域 单元格组成的地图。
如果 isWater[i][j] == 0 ，格子 (i, j) 是一个 陆地 格子。
如果 isWater[i][j] == 1 ，格子 (i, j) 是一个 水域 格子。
你需要按照如下规则给每个单元格安排高度：
每个格子的高度都必须是非负的。
如果一个格子是是 水域 ，那么它的高度必须为 0 。
任意相邻的格子高度差 至多 为 1 。当两个格子在正东、南、西、北方向上相互紧挨着，就称它们为相邻的格子。（也就是说它们有一条公共边）
找到一种安排高度的方案，使得矩阵中的最高高度值 最大 。
请你返回一个大小为 m x n 的整数矩阵 height ，其中 height[i][j] 是格子 (i, j) 的高度。如果有多种解法，请返回 任意一个 。

输入：isWater = [[0,1],[0,0]]
输出：[[1,0],[2,1]]
解释：上图展示了给各个格子安排的高度。
蓝色格子是水域格，绿色格子是陆地格。

输入：isWater = [[0,0,1],[1,0,0],[0,0,0]]
输出：[[1,1,0],[0,1,1],[1,2,2]]
解释：所有安排方案中，最高可行高度为 2 。
任意安排方案中，只要最高高度为 2 且符合上述规则的，都为可行方案。
"""
"""
思路：
1.第一眼没想到bfs，想到的是dp，结果应该是min(dp[i-1][j],dp[i][j-1],dp[i+1][j],dp[i][j+1])+1，但是没过，看了题解发现可以用
双向dp，因为每一个陆地的最近距离只有可能由左方，上方，或右方，下方转化而来，因此，由于我们的遍历顺序有两种，可能由左上到右下，
也有可能从右下到左上，遍历两遍，才能找到全局的最小距离。
2.多源bfs，这个应该一开始就想到的，注意如果不使用双端队列会超时
"""


class Solution(object):
    @staticmethod
    def highest_peak(is_water):
        """
        :type is_water: List[List[int]]
        :rtype: List[List[int]]
        """
        # 双向dp
        # m = len(is_water)
        # n = len(is_water[0])
        # res = [[m*n for _ in range(n)] for _ in range(m)]
        # for i in range(m):
        #     for j in range(n):
        #         if is_water[i][j] == 1:
        #             res[i][j] = 0
        # for i in range(m):
        #     for j in range(n):
        #         if is_water[i][j] == 1:
        #             continue
        #         else:
        #             if i > 0:
        #                 res[i][j] = min(res[i-1][j]+1, res[i][j])
        #             if j > 0:
        #                 res[i][j] = min(res[i][j-1]+1, res[i][j])
        # for i in range(m-1, -1, -1):
        #     for j in range(n-1, -1, -1):
        #         if is_water[i][j] == 1:
        #             continue
        #         else:
        #             if i < m-1:
        #                 res[i][j] = min(res[i+1][j]+1, res[i][j])
        #             if j < n-1:
        #                 res[i][j] = min(res[i][j+1]+1, res[i][j])
        # return res

        # 多源bfs
        m = len(is_water)
        n = len(is_water[0])
        res = [[m * n for _ in range(n)] for _ in range(m)]
        import collections
        que = collections.deque()
        for i in range(m):
            for j in range(n):
                if is_water[i][j] == 1:
                    res[i][j] = 0
                    que.append((i, j))
                else:
                    res[i][j] = -1
        while que:
            i, j = que.popleft()
            for x, y in ((i, j + 1), (i, j - 1), (i - 1, j), (i + 1, j)):
                if 0 <= x < m and 0 <= y < n and res[x][y] == -1:
                    res[x][y] = res[i][j] + 1
                    que.append((x, y))
        return res
