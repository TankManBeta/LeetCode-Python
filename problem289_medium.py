# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2022/12/3 17:00
"""
from typing import List

"""
根据 百度百科 ， 生命游戏 ，简称为 生命 ，是英国数学家约翰·何顿·康威在 1970 年发明的细胞自动机。
给定一个包含 m × n 个格子的面板，每一个格子都可以看成是一个细胞。每个细胞都具有一个初始状态： 1 即为 活细胞 （live），
或 0 即为 死细胞 （dead）。每个细胞与其八个相邻位置（水平，垂直，对角线）的细胞都遵循以下四条生存定律：
如果活细胞周围八个位置的活细胞数少于两个，则该位置活细胞死亡；
如果活细胞周围八个位置有两个或三个活细胞，则该位置活细胞仍然存活；
如果活细胞周围八个位置有超过三个活细胞，则该位置活细胞死亡；
如果死细胞周围正好有三个活细胞，则该位置死细胞复活；
下一个状态是通过将上述规则同时应用于当前状态下的每个细胞所形成的，其中细胞的出生和死亡是同时发生的。给你 m x n 网格面板 board 的当前状态，返回下一个状态。

示例 1：
输入：board = [[0,1,0],[0,0,1],[1,1,1],[0,0,0]]
输出：[[0,0,0],[1,0,1],[0,1,1],[0,1,0]]

示例 2：
输入：board = [[1,1],[1,0]]
输出：[[1,1],[1,1]]
"""
"""
思路：
（1）统计每个细胞周围的活细胞数目，然后再根据股则修改即可。需要m*n个额外空间计数
（2）采用新的规则，既直到转换之后的状态，又能知道转变之前的状态
"""


class Solution:
    @staticmethod
    def gameOfLife(board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # m = len(board)
        # n = len(board[0])
        # dirs = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

        # def get_count(board):
        #     count = [[0 for _ in range(n)] for _ in range(m)]
        #     for i in range(m):
        #         for j in range(n):
        #             for dir_x, dir_y in dirs:
        #                 new_x = i + dir_x
        #                 new_y = j + dir_y
        #                 if new_x < 0 or new_x >=m or new_y < 0 or new_y >=n:
        #                     continue
        #                 if board[new_x][new_y]:
        #                     count[i][j] += 1
        #     return count

        # my_count = get_count(board)

        # for i in range(m):
        #     for j in range(n):
        #         if my_count[i][j] == 3:
        #             board[i][j] = 1
        #         elif my_count[i][j]<2 or my_count[i][j] >3:
        #             board[i][j] = 0
        # return board

        neighbors = [(1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1)]

        rows = len(board)
        cols = len(board[0])

        # 遍历面板每一个格子里的细胞
        for row in range(rows):
            for col in range(cols):

                # 对于每一个细胞统计其八个相邻位置里的活细胞数量
                live_neighbors = 0
                for neighbor in neighbors:

                    # 相邻位置的坐标
                    r = (row + neighbor[0])
                    c = (col + neighbor[1])

                    # 查看相邻的细胞是否是活细胞
                    if (rows > r >= 0) and (cols > c >= 0) and abs(board[r][c]) == 1:
                        live_neighbors += 1

                # 规则 1 或规则 3
                if board[row][col] == 1 and (live_neighbors < 2 or live_neighbors > 3):
                    # -1 代表这个细胞过去是活的现在死了
                    board[row][col] = -1
                # 规则 4
                if board[row][col] == 0 and live_neighbors == 3:
                    # 2 代表这个细胞过去是死的现在活了
                    board[row][col] = 2

        # 遍历 board 得到一次更新后的状态
        for row in range(rows):
            for col in range(cols):
                if board[row][col] > 0:
                    board[row][col] = 1
                else:
                    board[row][col] = 0
