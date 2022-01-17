# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2022/1/11 17:00
"""
"""
给你一个 m 行 n 列的矩阵 matrix ，请按照 顺时针螺旋顺序 ，返回矩阵中的所有元素。

输入：matrix = [[1,2,3],[4,5,6],[7,8,9]]
输出：[1,2,3,6,9,8,7,4,5]

输入：matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
输出：[1,2,3,4,8,12,11,10,9,5,6,7]
"""
"""
思路：直接遍历即可，注意边界条件
"""


class Solution(object):
    @staticmethod
    def spiral_order(matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        row, col, count = 0, 0, 0
        start_row = 0
        start_col = 0
        row_len = len(matrix)
        col_len = len(matrix[0])
        matrix_len = len(matrix) * len(matrix[0])
        res = []
        while count != matrix_len:
            if row == start_row:
                if col != col_len - 1:
                    res.append(matrix[row][col])
                    count += 1
                    col += 1
                else:
                    res.append(matrix[row][col])
                    count += 1
                    row += 1
                continue
            if col == col_len - 1:
                if row != row_len - 1:
                    res.append(matrix[row][col])
                    count += 1
                    row += 1
                else:
                    res.append(matrix[row][col])
                    count += 1
                    col -= 1
                continue
            if row == row_len - 1:
                if col != start_col:
                    res.append(matrix[row][col])
                    count += 1
                    col -= 1
                else:
                    res.append(matrix[row][col])
                    count += 1
                    row -= 1
                continue
            if col == start_col:
                if row != start_row:
                    res.append(matrix[row][col])
                    count += 1
                    row -= 1
                    if row == start_row:
                        start_row += 1
                        start_col += 1
                        row_len -= 1
                        col_len -= 1
                        row = start_row
                        col = start_col
                continue
        return res
