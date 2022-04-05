# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2022/4/4 22:05
"""
"""
在一个由 '0' 和 '1' 组成的二维矩阵内，找到只包含 '1' 的最大正方形，并返回其面积。

输入：matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]] 
输出：4

输入：matrix = [["0","1"],["1","0"]] 
输出：1

输入：matrix = [["0"]] 
输出：0
"""
"""
思路：
（1）暴力，对于每一个board[i][j]等于1，看对角线以及新加的行和列是否全为1，然后更新maxSide
（2）动态规划，dp[i][j]是左上，上边，左边的最小值+1，然后更新即可
"""


class Solution(object):
    @staticmethod
    def maximalSquare(matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        # if len(matrix) == 0 or len(matrix[0]) == 0:
        #     return 0
        #
        # maxSide = 0
        # rows, columns = len(matrix), len(matrix[0])
        # for i in range(rows):
        #     for j in range(columns):
        #         if matrix[i][j] == '1':
        #             # 遇到一个 1 作为正方形的左上角
        #             maxSide = max(maxSide, 1)
        #             # 计算可能的最大正方形边长
        #             currentMaxSide = min(rows - i, columns - j)
        #             for k in range(1, currentMaxSide):
        #                 # 判断新增的一行一列是否均为 1
        #                 flag = True
        #                 if matrix[i + k][j + k] == '0':
        #                     break
        #                 for m in range(k):
        #                     if matrix[i + k][j + m] == '0' or matrix[i + m][j + k] == '0':
        #                         flag = False
        #                         break
        #                 if flag:
        #                     maxSide = max(maxSide, k + 1)
        #                 else:
        #                     break
        #
        # maxSquare = maxSide * maxSide
        # return maxSquare

        if len(matrix) == 0 or len(matrix[0]) == 0:
            return 0

        maxSide = 0
        rows, columns = len(matrix), len(matrix[0])
        dp = [[0] * columns for _ in range(rows)]
        for i in range(rows):
            for j in range(columns):
                if matrix[i][j] == '1':
                    if i == 0 or j == 0:
                        dp[i][j] = 1
                    else:
                        dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1
                    maxSide = max(maxSide, dp[i][j])

        maxSquare = maxSide * maxSide
        return maxSquare
