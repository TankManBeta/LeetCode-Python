# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2023/3/1 9:09
"""
from typing import List

"""
给你一个大小为 n x n 的整数矩阵 grid 。
生成一个大小为 (n - 2) x (n - 2) 的整数矩阵  maxLocal ，并满足：
    maxLocal[i][j] 等于 grid 中以 i + 1 行和 j + 1 列为中心的 3 x 3 矩阵中的 最大值 。
    换句话说，我们希望找出 grid 中每个 3 x 3 矩阵中的最大值。
返回生成的矩阵。 

示例 1：
输入：grid = [[9,9,8,1],[5,6,2,6],[8,2,6,4],[6,2,2,2]]
输出：[[9,9],[8,6]]
解释：原矩阵和生成的矩阵如上图所示。
注意，生成的矩阵中，每个值都对应 grid 中一个相接的 3 x 3 矩阵的最大值。

示例 2：
输入：grid = [[1,1,1,1,1],[1,1,1,1,1],[1,1,2,1,1],[1,1,1,1,1],[1,1,1,1,1]]
输出：[[2,2,2],[2,2,2],[2,2,2]]
解释：注意，2 包含在 grid 中每个 3 x 3 的矩阵中。
"""
"""
思路：我们可以枚举每个 3×3 的矩阵，求出每个 3×3 的矩阵中的最大值，然后将这些最大值放入答案矩阵中。
"""


class Solution:
    @staticmethod
    def largestLocal(grid: List[List[int]]) -> List[List[int]]:
        # n = len(grid)
        # ans = [[0]*(n-2) for _ in range(n-2)]
        # def get_max(center_i, center_j):
        #     max_val = grid[center_i][center_j]
        #     for dir_x, dir_y in [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]:
        #         new_x = center_i + dir_x
        #         new_y = center_j + dir_y
        #         if 0 <= new_x < n and 0 <= new_y < n:
        #             max_val = max(max_val, grid[new_x][new_y])
        #     return max_val
        # for i in range(1, n-1):
        #     for j in range(1, n-1):
        #         ans[i-1][j-1] = get_max(i, j)
        # return ans

        n = len(grid)
        ans = [[0] * (n - 2) for _ in range(n - 2)]
        for i in range(n - 2):
            for j in range(n - 2):
                ans[i][j] = max(grid[x][y] for x in range(i, i + 3) for y in range(j, j + 3))
        return ans
