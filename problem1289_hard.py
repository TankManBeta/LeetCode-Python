# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2023/8/10 20:19
"""
from typing import List

"""
给你一个 n x n 整数矩阵 grid ，请你返回 非零偏移下降路径 数字和的最小值。
非零偏移下降路径 定义为：从 grid 数组中的每一行选择一个数字，且按顺序选出来的数字中，相邻数字不在原数组的同一列。 

示例 1：
输入：grid = [[1,2,3],[4,5,6],[7,8,9]]
输出：13
解释：
所有非零偏移下降路径包括：
[1,5,9], [1,5,7], [1,6,7], [1,6,8],
[2,4,8], [2,4,9], [2,6,7], [2,6,8],
[3,4,8], [3,4,9], [3,5,7], [3,5,9]
下降路径中数字和最小的是 [1,5,7] ，所以答案是 13 。

示例 2：
输入：grid = [[7]]
输出：7
"""
"""
思路：我们定义 f[i][j] 表示前 i 行，且最后一个数字在第 j 列的最小数字和。那么状态转移方程为：f[i][j]=min⁡k≠jf[i−1][k]+grid[i−1][j]
其中 kkk 表示第 i−1 行的数字在第 k 列，第 i 行第 j 列的数字为 grid[i−1] 。最后答案为 f[n] 中的最小值。
"""


class Solution:
    @staticmethod
    def minFallingPathSum(grid: List[List[int]]) -> int:
        n = len(grid)
        f = [[0] * n for _ in range(n + 1)]
        for i, row in enumerate(grid, 1):
            for j, v in enumerate(row):
                x = min((f[i - 1][k] for k in range(n) if k != j), default=0)
                f[i][j] = v + x
        return min(f[n])
