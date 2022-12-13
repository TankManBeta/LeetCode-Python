# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2022/12/12 10:07
"""
from typing import List

"""
给你一个大小为 m x n 的矩阵 mat ，请以对角线遍历的顺序，用一个数组返回这个矩阵中的所有元素。

示例 1：
输入：mat = [[1,2,3],[4,5,6],[7,8,9]]
输出：[1,2,4,7,5,3,6,8,9]

示例 2：
输入：mat = [[1,2],[3,4]]
输出：[1,2,3,4]
"""
"""
思路：一共有(m+n-1)条对角线，如果是奇数对角线的话就规定方向为向右上，否则规定方向为向左下，对于右上来说，x--，y++；对于左下来说，
x++，y--
"""


class Solution:
    @staticmethod
    def findDiagonalOrder(mat: List[List[int]]) -> List[int]:
        ans = []
        m, n = len(mat), len(mat[0])
        for i in range(m + n - 1):
            if i % 2:
                x = 0 if i < n else i - n + 1
                y = i if i < n else n - 1
                while x < m and y >= 0:
                    ans.append(mat[x][y])
                    x += 1
                    y -= 1
            else:
                x = i if i < m else m - 1
                y = 0 if i < m else i - m + 1
                while x >= 0 and y < n:
                    ans.append(mat[x][y])
                    x -= 1
                    y += 1
        return ans
