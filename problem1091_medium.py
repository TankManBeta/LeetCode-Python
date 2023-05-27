# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2023/5/26 11:06
"""
from typing import List

"""
给你一个 n x n 的二进制矩阵 grid 中，返回矩阵中最短 畅通路径 的长度。如果不存在这样的路径，返回 -1 。
二进制矩阵中的 畅通路径 是一条从 左上角 单元格（即，(0, 0)）到 右下角 单元格（即，(n - 1, n - 1)）的路径，该路径同时满足下述要求：
    路径途经的所有单元格都的值都是 0 。
    路径中所有相邻的单元格应当在 8 个方向之一 上连通（即，相邻两单元之间彼此不同且共享一条边或者一个角）。
畅通路径的长度 是该路径途经的单元格总数。

示例 1：
输入：grid = [[0,1],[1,0]]

输出：2
示例 2：
输入：grid = [[0,0,0],[1,1,0],[1,1,0]]
输出：4

示例 3：
输入：grid = [[1,0,0],[1,1,0],[1,1,0]]
输出：-1
"""
"""
思路：
（1）bfs，用一个同样大的visited数组记录是否访问过，然后每层枚举8个方向的即可。结果超时。
（2）可以不用visited数组，直接在grid上修改，结果不超时。
"""


class Solution:
    @staticmethod
    def shortestPathBinaryMatrix(grid: List[List[int]]) -> int:
        # if grid[0][0] != 0 or grid[-1][-1] != 0:
        #     return -1
        # n = len(grid)
        # visited = [[False for _ in range(n)] for _ in range(n)]
        # visited[0][0] = True
        # ans = 1
        # queue = [(0, 0)]
        # dirs = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]
        # while queue:
        #     for _ in range(len(queue)):
        #         tmp = queue.pop(0)
        #         if tmp[0] == n-1 and tmp[1] == n-1:
        #             return ans
        #         visited[tmp[0]][tmp[1]] = True
        #         for dir_x, dir_y in dirs:
        #             new_x, new_y = dir_x+tmp[0], dir_y+tmp[1]
        #             if 0 <= new_x <= n-1 and 0 <= new_y <= n-1 and not visited[new_x][new_y] and grid[new_x][new_y] == 0:
        #                 queue.append((new_x, new_y))
        #     ans += 1
        # return -1

        if grid[0][0] != 0 or grid[-1][-1] != 0:
            return -1
        n = len(grid)
        grid[0][0] = 1
        ans = 1
        queue = [(0, 0)]
        dirs = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
        while queue:
            for _ in range(len(queue)):
                i, j = queue.pop(0)
                if i == j == n - 1:
                    return ans
                for dir_x, dir_y in dirs:
                    x, y = dir_x + i, dir_y + j
                    if 0 <= x <= n - 1 and 0 <= y <= n - 1 and grid[x][y] == 0:
                        queue.append((x, y))
                        grid[x][y] = 1
            ans += 1
        return -1
