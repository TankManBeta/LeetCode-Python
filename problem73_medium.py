# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2022/2/1 8:30
"""
"""
给定一个 m x n 的矩阵，如果一个元素为 0 ，则将其所在行和列的所有元素都设为 0 。请使用原地算法。

输入：matrix = [[1,1,1],[1,0,1],[1,1,1]]
输出：[[1,0,1],[0,0,0],[1,0,1]]

输入：matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
输出：[[0,0,0,0],[0,4,5,0],[0,3,1,0]]
"""
"""
思路：
（1）额外两个列表，将存在0的行或列存进列表，然后遍历变0即可
（2）将第一行第一列作为（1）中的列表，然后注意第一行第一列是否有0要单独处理
"""


class Solution(object):
    @staticmethod
    def set_zeroes(matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        # rows = []
        # cols = []
        # m = len(matrix)
        # n = len(matrix[0])

        # for i in range(m):
        #     for j in range(n):
        #         if matrix[i][j] == 0:
        #             if i not in rows:
        #                 rows.append(i)
        #             if j not in cols:
        #                 cols.append(j)

        # for i in range(m):
        #     for j in range(n):
        #         if i in rows or j in cols:
        #             matrix[i][j] = 0

        m = len(matrix)
        n = len(matrix[0])
        flag_row = False
        flag_col = False
        for i in range(m):
            if matrix[i][0] == 0:
                flag_col = True
                break

        for j in range(n):
            if matrix[0][j] == 0:
                flag_row = True
                break

        for i in range(0, m):
            for j in range(0, n):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0

        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0

        if flag_row:
            for j in range(n):
                matrix[0][j] = 0

        if flag_col:
            for i in range(m):
                matrix[i][0] = 0
