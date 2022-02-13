# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2022/2/12 11:44
"""
"""
给你一个大小为 m x n 的二进制矩阵 grid ，其中 0 表示一个海洋单元格、1 表示一个陆地单元格。
一次 移动 是指从一个陆地单元格走到另一个相邻（上、下、左、右）的陆地单元格或跨过 grid 的边界。
返回网格中 无法 在任意次数的移动中离开网格边界的陆地单元格的数量。

输入：grid = [[0,0,0,0],[1,0,1,0],[0,1,1,0],[0,0,0,0]]
输出：3
解释：有三个 1 被 0 包围。一个 1 没有被包围，因为它在边界上。

输入：grid = [[0,1,1,0],[0,0,1,0],[0,0,1,0],[0,0,0,0]]
输出：0
解释：所有 1 都在边界上或可以到达边界。
"""
"""
思路：dfs，对边缘的陆地进行dfs，dfs完成后剩余的未被访问过的陆地数量就是飞地数量
"""


class Solution(object):
    def __init__(self):
        self.ans = 0

    def num_enclaves(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m = len(grid)
        n = len(grid[0])
        visited = [[0 for _ in range(n)] for _ in range(m)]

        def dfs(r, c):
            if r < 0 or r >= m or c < 0 or c >= n or not grid[r][c] or visited[r][c]:
                return
            visited[r][c] = 1
            for new_i, new_j in ((r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)):
                dfs(new_i, new_j)

        for i in range(m):
            dfs(i, 0)
            dfs(i, n - 1)
        for j in range(1, n - 1):
            dfs(0, j)
            dfs(m - 1, j)

        for row in range(1, m):
            for col in range(1, n):
                if grid[row][col] and not visited[row][col]:
                    self.ans += 1
        return self.ans
