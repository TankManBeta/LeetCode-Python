# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2021/12/7 12:04
"""
"""
给你一个大小为 m x n 的整数矩阵 grid ，表示一个网格。另给你三个整数 row、col 和 color 。网格中的每个值表示该位置处的网格块的颜色。
当两个网格块的颜色相同，而且在四个方向中任意一个方向上相邻时，它们属于同一 连通分量 。
连通分量的边界 是指连通分量中的所有与不在分量中的网格块相邻（四个方向上）的所有网格块，或者在网格的边界上（第一行/列或最后一行/列）的所有网格块。
请你使用指定颜色 color 为所有包含网格块 grid[row][col] 的 连通分量的边界 进行着色，并返回最终的网格 grid 。

输入：grid = [[1,1],[1,2]], row = 0, col = 0, color = 3
输出：[[3,3],[3,2]]

输入：grid = [[1,2,2],[2,3,2]], row = 0, col = 1, color = 3
输出：[[1,3,3],[2,3,3]]

输入：grid = [[1,1,1],[1,1,1],[1,1,1]], row = 1, col = 1, color = 2
输出：[[2,2,2],[2,1,2],[2,2,2]]
"""
"""
思路：直接dfs，判断是否为边界即可
"""


class Solution(object):
    def color_border(self, grid, row, col, color):
        """
        :type grid: List[List[int]]
        :type row: int
        :type col: int
        :type color: int
        :rtype: List[List[int]]
        """
        m, n = len(grid), len(grid[0])
        visited = [[False] * n for _ in range(m)]
        borders = []
        original_color = grid[row][col]
        visited[row][col] = True
        self.dfs(grid, row, col, visited, borders, original_color)
        for x, y in borders:
            grid[x][y] = color
        return grid

    def dfs(self, grid, x, y, visited, borders, original_color):
        is_border = False
        m, n = len(grid), len(grid[0])
        direction = ((-1, 0), (1, 0), (0, -1), (0, 1))
        for dx, dy in direction:
            nx, ny = x + dx, y + dy
            if not (0 <= nx < m and 0 <= ny < n and grid[nx][ny] == original_color):
                is_border = True
            elif not visited[nx][ny]:
                visited[nx][ny] = True
                self.dfs(grid, nx, ny, visited, borders, original_color)
        if is_border:
            borders.append((x, y))
