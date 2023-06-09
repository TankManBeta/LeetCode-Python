# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2023/6/9 10:44
"""
"""
输入一个矩阵，按照从外向里以顺时针的顺序依次打印出每一个数字。 

示例 1：
输入：matrix = [[1,2,3],[4,5,6],[7,8,9]]
输出：[1,2,3,6,9,8,7,4,5]

示例 2：
输入：matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
输出：[1,2,3,4,8,12,11,10,9,5,6,7]
"""
"""
思路：先从左到右打印第一行，然后从上到下打印最后一列，再从右到左打印最后一行，最后从下到上打印第一列，循环做即可。
"""


class Solution:
    @staticmethod
    def spiralOrder(matrix: [[int]]) -> [int]:
        if not matrix:
            return []
        l, r, t, b, res = 0, len(matrix[0]) - 1, 0, len(matrix) - 1, []
        while True:
            for i in range(l, r + 1):
                res.append(matrix[t][i])
            t += 1
            if t > b:
                break
            for i in range(t, b + 1):
                res.append(matrix[i][r])
            r -= 1
            if l > r:
                break
            for i in range(r, l - 1, -1):
                res.append(matrix[b][i])
            b -= 1
            if t > b:
                break
            for i in range(b, t - 1, -1):
                res.append(matrix[i][l])
            l += 1
            if l > r:
                break
        return res
