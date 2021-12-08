# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2021/12/8 17:30
"""
"""
编写一个程序，通过填充空格来解决数独问题。
数独的解法需 遵循如下规则：
数字 1-9 在每一行只能出现一次。
数字 1-9 在每一列只能出现一次。
数字 1-9 在每一个以粗实线分隔的 3x3 宫内只能出现一次。（请参考示例图）
数独部分空格内已填入了数字，空白格用 '.' 表示。

输入：[["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],
       [".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],
       ["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],
       [".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],
       [".",".",".",".","8",".",".","7","9"]]
输出：[["5","3","4","6","7","8","9","1","2"],["6","7","2","1","9","5","3","4","8"],
       ["1","9","8","3","4","2","5","6","7"],["8","5","9","7","6","1","4","2","3"],
       ["4","2","6","8","5","3","7","9","1"],["7","1","3","9","2","4","8","5","6"],
       ["9","6","1","5","3","7","2","8","4"],["2","8","7","4","1","9","6","3","5"],
       ["3","4","5","2","8","6","1","7","9"]]
"""
"""
思路：dfs，如果i=9，说明有解，如果当前是空格，就需要填充，从1-9开始尝试，然后返回时需要重新还原现场。
"""


class Solution(object):
    @staticmethod
    def solve_sudoku(board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        row = [[False] * 9 for _ in range(9)]
        column = [[False] * 9 for _ in range(9)]
        square = [[False] * 9 for _ in range(9)]
        for i in range(0, 9):
            for j in range(0, 9):
                if board[i][j] != '.':
                    digit = int(board[i][j])-1
                    row[i][digit] = column[j][digit] = square[3*(i//3) + j//3][digit] = True

        def dfs(i, j):
            if j == 9:
                i += 1
                j = 0
            if i == 9:
                return True
            if board[i][j] == '.':
                for num in range(9):
                    if row[i][num] == column[j][num] == square[3*(i//3) + j//3][num] is False:
                        row[i][num] = column[j][num] = square[3*(i//3) + j//3][num] = True
                        board[i][j] = str(num + 1)
                        if dfs(i, j+1):
                            return True
                        row[i][num] = column[j][num] = square[3*(i//3) + j//3][num] = False
                        board[i][j] = '.'
            else:
                return dfs(i, j+1)
            return False
        dfs(0, 0)
        return board
