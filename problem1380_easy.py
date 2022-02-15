# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2022/2/15 12:48
"""
"""
给你一个 m * n 的矩阵，矩阵中的数字 各不相同 。请你按 任意 顺序返回矩阵中的所有幸运数。
幸运数是指矩阵中满足同时下列两个条件的元素：
    在同一行的所有元素中最小
    在同一列的所有元素中最大

输入：matrix = [[3,7,8],[9,11,13],[15,16,17]]
输出：[15]
解释：15 是唯一的幸运数，因为它是其所在行中的最小值，也是所在列中的最大值。

输入：matrix = [[1,10,4,2],[9,3,8,7],[15,16,17,12]]
输出：[12]
解释：12 是唯一的幸运数，因为它是其所在行中的最小值，也是所在列中的最大值。

输入：matrix = [[7,8],[1,2]]
输出：[7]
"""
"""
思路：首先遍历一遍，记录每一行的最小和每一列的最大，然后判断每一行的最小是否是每一列的最大即可
"""


class Solution(object):
    @staticmethod
    def lucky_numbers(matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        m = len(matrix)
        n = len(matrix[0])
        row = [0 for _ in range(m)]
        col = [0 for _ in range(n)]
        res = []
        for i in range(m):
            for j in range(n):
                if matrix[i][j] < matrix[i][row[i]]:
                    row[i] = j
                if matrix[i][j] > matrix[col[j]][j]:
                    col[j] = i
        for index in range(m):
            if col[row[index]] == index:
                res.append(matrix[index][row[index]])
        return res
