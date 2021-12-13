# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2021/12/13 10:34
"""
"""
在二维数组grid中，grid[i][j]代表位于某处的建筑物的高度。 我们被允许增加任何数量（不同建筑物的数量可能不同）的建筑物的高度。 
高度 0 也被认为是建筑物。
最后，从新数组的所有四个方向（即顶部，底部，左侧和右侧）观看的“天际线”必须与原始数组的天际线相同。 
城市的天际线是从远处观看时，由所有建筑物形成的矩形的外部轮廓。 请看下面的例子。
建筑物高度可以增加的最大总和是多少？

例子：
输入： grid = [[3,0,8,4],[2,4,5,7],[9,2,6,3],[0,3,1,0]]
输出： 35
解释： 
The grid is:
[ [3, 0, 8, 4], 
  [2, 4, 5, 7],
  [9, 2, 6, 3],
  [0, 3, 1, 0] ]

从数组竖直方向（即顶部，底部）看“天际线”是：[9, 4, 8, 7]
从水平水平方向（即左侧，右侧）看“天际线”是：[8, 7, 9, 3]

在不影响天际线的情况下对建筑物进行增高后，新数组如下：
gridNew = [ [8, 4, 8, 7],
            [7, 4, 7, 7],
            [9, 4, 8, 7],
            [3, 3, 3, 3] ]
"""
"""
思路：找每行每列最高的就是能加高的最大高度，如果grid[i][j]小于行列最低的，就加高到行列最低的并进行计数，否则继续
"""


class Solution(object):
    @staticmethod
    def max_increase_keeping_skyline(grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        row_len = len(grid)
        col_len = len(grid[0])
        row_max = [0]*row_len
        col_max = [0]*row_len
        for i in range(0, row_len):
            for j in range(0, col_len):
                if grid[i][j] > row_max[i]:
                    row_max[i] = grid[i][j]
                if grid[i][j] > col_max[j]:
                    col_max[j] = grid[i][j]
        count = 0
        for i in range(0, row_len):
            for j in range(0, col_len):
                min_height = min(row_max[i], col_max[j])
                if grid[i][j] < min_height:
                    count += min_height - grid[i][j]
                    grid[i][j] = min_height
        return count
