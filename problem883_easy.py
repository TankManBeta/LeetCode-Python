# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2022/4/26 9:55
"""
"""
在 n x n 的网格 grid 中，我们放置了一些与 x，y，z 三轴对齐的 1 x 1 x 1 立方体。
每个值 v = grid[i][j] 表示 v 个正方体叠放在单元格 (i, j) 上。
现在，我们查看这些立方体在 xy 、yz 和 zx 平面上的投影。
投影 就像影子，将 三维 形体映射到一个 二维 平面上。从顶部、前面和侧面看立方体时，我们会看到“影子”。
返回 所有三个投影的总面积 。

输入：[[1,2],[3,4]]
输出：17
解释：这里有该形体在三个轴对齐平面上的三个投影(“阴影部分”)。

输入：grid = [[2]]
输出：5

输入：[[1,0],[0,2]]
输出：8
"""
"""
思路：xy平面的投影面积等于网格上非零数值的数目；yz平面的投影面积等于网格上每一行最大数值之和；zx平面的投影面积等于网格上每一列
最大数值之和。
"""


class Solution(object):
    @staticmethod
    def projectionArea(grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m = len(grid)
        n = len(grid[0])
        xoy = 0
        yoz = 0
        xoz = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] != 0:
                    xoy += 1

        for i in range(m):
            xoz += max(grid[i])

        for j in range(n):
            max_col = grid[0][j]
            for i in range(m):
                max_col = max(grid[i][j], max_col)
            yoz += max_col

        return xoy + yoz + xoz
