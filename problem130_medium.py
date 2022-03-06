# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2022/3/5 13:17
"""
"""
给你一个 m x n 的矩阵 board ，由若干字符 'X' 和 'O' ，找到所有被 'X' 围绕的区域，并将这些区域里所有的 'O' 用 'X' 填充。

输入：board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
输出：[["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","O","X","X"]]
解释：被围绕的区间不会存在于边界上，换句话说，任何边界上的 'O' 都不会被填充为 'X'。 
任何不在边界上，或不与边界上的 'O' 相连的 'O' 最终都会被填充为 'X'。如果两个元素在水平或垂直方向相邻，则称它们是“相连”的。

输入：board = [["X"]]
输出：[["X"]]
"""
"""
思路：从外面一圈中找到O，然后dfs，能到达的且为O的地方全部变成A，然后遍历整个board，把A变成O，O变成X即可
"""


class Solution(object):
    @staticmethod
    def solve(board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        if not board:
            return []
        m, n = len(board), len(board[0])
        bound_o = []
        for i in {0, m - 1}:
            for j in range(n):
                if board[i][j] == 'O' and (i, j) not in bound_o:
                    bound_o.append((i, j))
        for j in {0, n - 1}:
            for i in range(m):
                if board[i][j] == 'O' and (i, j) not in bound_o:
                    bound_o.append((i, j))

        def dfs(row, col):
            if not 0 <= row < m or not 0 <= col < n or board[row][col] != 'O':
                return
            board[row][col] = 'A'
            dfs(row + 1, col)
            dfs(row - 1, col)
            dfs(row, col + 1)
            dfs(row, col - 1)

        for i, j in bound_o:
            dfs(i, j)

        for i in range(m):
            for j in range(n):
                if board[i][j] == 'A':
                    board[i][j] = 'O'
                elif board[i][j] == 'O':
                    board[i][j] = 'X'
