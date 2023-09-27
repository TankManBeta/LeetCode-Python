# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2023/9/13 10:49
"""
from typing import List

"""
骑士在一张 n x n 的棋盘上巡视。在有效的巡视方案中，骑士会从棋盘的 左上角 出发，并且访问棋盘上的每个格子 恰好一次 。
给你一个 n x n 的整数矩阵 grid ，由范围 [0, n * n - 1] 内的不同整数组成，其中 grid[row][col] 表示单元格 (row, col) 是骑士访问的第 
grid[row][col] 个单元格。骑士的行动是从下标 0 开始的。
如果 grid 表示了骑士的有效巡视方案，返回 true；否则返回 false。
注意，骑士行动时可以垂直移动两个格子且水平移动一个格子，或水平移动两个格子且垂直移动一个格子。下图展示了骑士从某个格子出发可能的八种行动路线。 

示例 1：
输入：grid = [[0,11,16,5,20],[17,4,19,10,15],[12,1,8,21,6],[3,18,23,14,9],[24,13,2,7,22]]
输出：true
解释：grid 如上图所示，可以证明这是一个有效的巡视方案。

示例 2：
输入：grid = [[0,3,6],[5,8,1],[2,7,4]]
输出：false
解释：grid 如上图所示，考虑到骑士第 7 次行动后的位置，第 8 次行动是无效的。
"""
"""
思路：直接模拟即可
"""


class Solution:
    @staticmethod
    def checkValidGrid(grid: List[List[int]]) -> bool:
        m, n = len(grid), len(grid[0])
        dirs = [(-1, -2), (-2, -1), (-2, 1), (-1, 2), (1, -2), (2, -1), (2, 1), (1, 2)]
        if grid[0][0] != 0:
            return False
        x, y = 0, 0
        depth = 0
        while True:
            flag = False
            for xx, yy in dirs:
                nx, ny = x + xx, y + yy
                if 0 <= nx <= m - 1 and 0 <= ny <= n - 1:
                    if grid[nx][ny] == depth + 1:
                        x, y = nx, ny
                        flag = True
                        depth += 1
            if not flag:
                return False
            if depth == m * n - 1:
                return True