# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2023/8/11 9:26
"""
from typing import List

"""
给你一个正方形矩阵 mat，请你返回矩阵对角线元素的和。
请你返回在矩阵主对角线上的元素和副对角线上且不在主对角线上元素的和。 

示例  1：
输入：mat = [[1,2,3],
            [4,5,6],
            [7,8,9]]
输出：25
解释：对角线的和为：1 + 5 + 9 + 3 + 7 = 25
请注意，元素 mat[1][1] = 5 只会被计算一次。

示例  2：
输入：mat = [[1,1,1,1],
            [1,1,1,1],
            [1,1,1,1],
            [1,1,1,1]]
输出：8

示例 3：
输入：mat = [[5]]
输出：5
"""
"""
思路：直接遍历即可
"""


class Solution:
    @staticmethod
    def diagonalSum(mat: List[List[int]]) -> int:
        n = len(mat)
        ans = 0
        for i in range(n):
            ans += mat[i][i]
            index_i, index_j = i, n - 1 - i
            if index_i != index_j:
                ans += mat[index_i][index_j]
        return ans
