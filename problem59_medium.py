# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2022/1/19 15:59
"""
"""
给你一个正整数 n ，生成一个包含 1 到 n2 所有元素，且元素按顺时针顺序螺旋排列的 n x n 正方形矩阵 matrix 。

输入：n = 3
输出：[[1,2,3],[8,9,4],[7,6,5]]

输入：n = 1
输出：[[1]]
"""
"""
思路：先左->右，然后上->下，然后右->左，然后下->上
"""


class Solution(object):
    @staticmethod
    def generate_matrix(n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        matrix = [[0 for _ in range(n)] for _ in range(n)]
        end = n*n
        num = 1
        start_row, start_col = 0, 0
        end_row, end_col = n-1, n-1
        while num <= end:
            for i in range(start_col, end_col+1):
                matrix[start_row][i] = num
                num += 1
            start_row += 1
            for i in range(start_row, end_row+1):
                matrix[i][end_col] = num
                num += 1
            end_col -= 1
            for i in range(end_col, start_col-1, -1):
                matrix[end_row][i] = num
                num += 1
            end_row -= 1
            for i in range(end_row, start_row-1, -1):
                matrix[i][start_col] = num
                num += 1
            start_col += 1
        return matrix
