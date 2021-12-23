# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2021/12/23 15:31
"""
"""
n 皇后问题 研究的是如何将 n 个皇后放置在 n × n 的棋盘上，并且使皇后彼此之间不能相互攻击。
给你一个整数 n ，返回 n 皇后问题 不同的解决方案的数量。

输入：n = 4
输出：2

输入：n = 1
输出：1
"""
"""
思路：同51，只是把方案变成了方案数量
"""


class Solution(object):
    @staticmethod
    def total_n_queens(n):
        """
        :type n: int
        :rtype: int
        """
        visited_col = [False for _ in range(n)]
        visited_diag1 = [False for _ in range(2*n-1)]
        visited_diag2 = [False for _ in range(2*n-1)]
        answers = []
        chessboard = [['.']*n for _ in range(n)]

        def dfs(row):
            if row == n:
                answers.append('1')
                return
            for col in range(n):
                if not visited_col[col] and not visited_diag1[n-row+col-1] and not visited_diag2[row+col]:
                    chessboard[row][col] = 'Q'
                    visited_col[col] = True
                    visited_diag1[n - row + col - 1] = True
                    visited_diag2[row + col] = True
                    dfs(row+1)
                    chessboard[row][col] = '.'
                    visited_col[col] = False
                    visited_diag1[n - row + col - 1] = False
                    visited_diag2[row + col] = False
                else:
                    continue
        dfs(0)
        return len(answers)
