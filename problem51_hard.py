# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2021/12/23 13:55
"""
"""
n皇后问题研究的是如何将n个皇后放置在n×n的棋盘上，并且使皇后彼此之间不能相互攻击。
给你一个整数n，返回所有不同的n皇后问题 的解决方案。
每一种解法包含一个不同的 n 皇后问题 的棋子放置方案，该方案中 'Q' 和 '.' 分别代表了皇后和空位。

输入：n = 4
输出：[[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]

输入：n = 1
输出：[["Q"]]
"""
"""
思路：每次确定在一行中的位置即可，每次判断当前列和所在对角线是否能放棋子（左上右下和左下右上两条对角线）
"""


class Solution(object):
    @staticmethod
    def solve_n_queens(n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        visited_col = [False for _ in range(n)]
        visited_diag1 = [False for _ in range(2*n-1)]
        visited_diag2 = [False for _ in range(2*n-1)]
        answers = []
        chessboard = [['.']*n for _ in range(n)]

        def dfs(row):
            if row == n:
                res_list = [''.join(item) for item in chessboard]
                answers.append(res_list)
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
        return answers
