# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2023/5/20 13:37
"""
from typing import List

"""
在一个 n * m 的二维数组中，每一行都按照从左到右 非递减 的顺序排序，每一列都按照从上到下 非递减 的顺序排序。请完成一个高效的函数，
输入这样的一个二维数组和一个整数，判断数组中是否含有该整数。

示例:
现有矩阵 matrix 如下：
[
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]
给定 target = 5，返回 true。
给定 target = 20，返回 false。
"""
"""
思路：
（1）对每一行进行二分
（2）从右上角开始，当前数比target小就i+1，否则j-1，看是否有数的值等于target
"""


class Solution:
    @staticmethod
    def findNumberIn2DArray(matrix: List[List[int]], target: int) -> bool:
        # for row in matrix:
        #     idx = bisect.bisect_left(row, target)
        #     if idx < len(row) and row[idx] == target:
        #         return True
        # return False

        if len(matrix) == 0 or len(matrix[0]) == 0:
            return False
        m, n = len(matrix), len(matrix[0])
        x, y = 0, n - 1
        while x < m and y >= 0:
            if matrix[x][y] == target:
                return True
            if matrix[x][y] > target:
                y -= 1
            else:
                x += 1
        return False
