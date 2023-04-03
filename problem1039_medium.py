# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2023/4/2 12:58
"""
from typing import List

"""
你有一个凸的 n 边形，其每个顶点都有一个整数值。给定一个整数数组 values ，其中 values[i] 是第 i 个顶点的值（即 顺时针顺序 ）。
假设将多边形 剖分 为 n - 2 个三角形。对于每个三角形，该三角形的值是顶点标记的乘积，三角剖分的分数是进行三角剖分后所有 n - 2 
个三角形的值之和。
返回 多边形进行三角剖分后可以得到的最低分 。

示例 1：
输入：values = [1,2,3]
输出：6
解释：多边形已经三角化，唯一三角形的分数为 6。

示例 2：
输入：values = [3,7,4,5]
输出：144
解释：有两种三角剖分，可能得分分别为：3*7*5 + 4*5*7 = 245，或 3*4*5 + 3*4*7 = 144。最低分数为 144。

示例 3：
输入：values = [1,3,1,4,1,5]
输出：13
解释：最低分数三角剖分的得分情况为 1*1*3 + 1*1*4 + 1*1*5 + 1*1*1 = 13。
"""
"""
思路：
（1）记忆化搜索。如果 i+1=j，说明多边形只有两个顶点，无法进行三角剖分，返回 0。否则，我们枚举 i 和 j 之间的一个顶点 k，即 
i<k<j，将多边形的顶点 i 到 j 进行三角剖分，可以分为两个子问题：将多边形的顶点 i 到 k 进行三角剖分，以及将多边形的顶点 k 到 j 
进行三角剖分。这两个子问题的最低分数分别为 dfs(i,k) 和 dfs(k,j)，而顶点 i, j 和 k 构成的三角形的分数为 values[i]×values[k]×
values[j]。那么，此次三角剖分的最低分数为 dfs(i,k)+dfs(k,j)+values[i]×values[k]×values[j]，我们取所有可能的最小值，即为 
dfs(i,j) 的值。
（2）动态规划。我们枚举 i 和 j 之间的一个顶点 k，即 i<k<j，将多边形的顶点 i 到 j 进行三角剖分，可以分为两个子问题：将多边形的
顶点 i 到 k 进行三角剖分，以及将多边形的顶点 k 到 j 进行三角剖分。这两个子问题的最低分数分别为 f[i][k] 和 f[k][j]，而顶点 i, 
j 和 k 构成的三角形的分数为 values[i]×values[k]×values[j]。那么，此次三角剖分的最低分数为 f[i][k]+f[k][j]+values[i]×values[k]
×values[j]，我们取所有可能的最小值，即为 f[i][j] 的值。
"""


class Solution:
    @staticmethod
    def minScoreTriangulation(values: List[int]) -> int:
        # @cache
        # def dfs(i: int, j: int) -> int:
        #     if i + 1 == j:
        #         return 0
        #     return min(dfs(i, k) + dfs(k, j) + values[i] * values[k] * values[j] for k in range(i + 1, j))
        # return dfs(0, len(values) - 1)

        n = len(values)
        f = [[0] * n for _ in range(n)]
        for i in range(n - 3, -1, -1):
            for j in range(i + 2, n):
                f[i][j] = min(f[i][k] + f[k][j] + values[i] * values[k] * values[j] for k in range(i + 1, j))
        return f[0][-1]
