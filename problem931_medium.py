# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2023/7/13 21:55
"""
from typing import List

"""
给你一个 n x n 的 方形 整数数组 matrix ，请你找出并返回通过 matrix 的下降路径 的 最小和 。
下降路径 可以从第一行中的任何元素开始，并从每一行中选择一个元素。在下一行选择的元素和当前行所选元素最多相隔一列（即位于正下方
或者沿对角线向左或者向右的第一个元素）。具体来说，位置 (row, col) 的下一个元素应当是 (row + 1, col - 1)、(row + 1, col) 或者 
(row + 1, col + 1) 。 

示例 1：
输入：matrix = [[2,1,3],[6,5,4],[7,8,9]]
输出：13
解释：如图所示，为和最小的两条下降路径

示例 2：
输入：matrix = [[-19,57],[-40,-5]]
输出：-59
解释：如图所示，为和最小的下降路径
"""
"""
思路：我们定义 f[i][j] 表示从第一行开始下降，到达第 i 行第 j 列的最小路径和。那么我们可以得到这样的动态规划转移方程：
f[i][j]=matrix[i][j]+min(f[i−1][j−1],f[i−1][j],f[i−1][j+1])最终的答案即为 f[n−1][j]。我们注意到，状态 f[i][j] 只与上一行
的状态有关，因此我们可以使用滚动数组的方式，去掉第一维的状态，将空间复杂度优化到 O(n)。
"""


class Solution:
    @staticmethod
    def minFallingPathSum(matrix: List[List[int]]) -> int:
        n = len(matrix)
        f = [0] * n
        for row in matrix:
            g = [0] * n
            for j, x in enumerate(row):
                l, r = max(0, j - 1), min(n, j + 2)
                g[j] = min(f[l:r]) + x
            f = g
        return min(f)
