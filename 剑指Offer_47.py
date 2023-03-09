# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2023/3/8 10:02
"""
from typing import List

"""
在一个 m*n 的棋盘的每一格都放有一个礼物，每个礼物都有一定的价值（价值大于 0）。你可以从棋盘的左上角开始拿格子里的礼物，
并每次向右或者向下移动一格、直到到达棋盘的右下角。给定一个棋盘及其上面的礼物的价值，请计算你最多能拿到多少价值的礼物？

示例 1:
输入: 
[
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
输出: 12
解释: 路径 1→3→5→2→1 可以拿到最多价值的礼物
"""
"""
思路：dp，定义 f[i][j] 为从棋盘左上角走到 (i−1,j−1) 的礼物最大累计价值，那么 f[i][j] 的值由 f[i−1][j] 和 f[i][j−1] 决定，
即从上方格子和左方格子走过来的两个方案中选择一个价值较大的方案。因此我们可以写出动态规划转移方程：f[i][j]=max(f[i−1][j],
f[i][j−1])+grid[i−1][j−1]，答案为 f[m][n]。
"""


class Solution:
    @staticmethod
    def maxValue(grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        dp = [[0 for _ in range(n)] for _ in range(m)]
        dp[0][0] = grid[0][0]
        for i in range(1, m):
            dp[i][0] = dp[i - 1][0] + grid[i][0]
        for j in range(1, n):
            dp[0][j] = dp[0][j - 1] + grid[0][j]
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1]) + grid[i][j]
        return dp[m - 1][n - 1]
