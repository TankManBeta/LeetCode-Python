# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2022/1/25 12:40
"""
"""
一个机器人位于一个 m x n 网格的左上角 （起始点在下图中标记为 “Start” ）。
机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为 “Finish”）。
现在考虑网格中有障碍物。那么从左上角到右下角将会有多少条不同的路径？
网格中的障碍物和空位置分别用 1 和 0 来表示。

输入：obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]]
输出：2
解释：3x3 网格的正中间有一个障碍物。
从左上角到右下角一共有 2 条不同的路径：
1. 向右 -> 向右 -> 向下 -> 向下
2. 向下 -> 向下 -> 向右 -> 向右

输入：obstacleGrid = [[0,1],[0,0]]
输出：1
"""
"""
思路：首先初始化全部为0， 然后初始化第一行和第一列为1（因为第一行第一列只能由一个方向到，并且有一个为obstacle为1，
后面的不需要再置1了），后面的f(i,j)就由f(i-1,j)和f(i,j-1)决定，并且如果当前位置的obstacle为1的话,f(i,j)直接置0
"""


class Solution(object):
    @staticmethod
    def unique_paths_with_obstacles(obstacle_grid):
        """
        :type obstacle_grid: List[List[int]]
        :rtype: int
        """
        m = len(obstacle_grid)
        n = len(obstacle_grid[0])
        ans = [[0 for _ in range(n)] for _ in range(m)]

        for i in range(m):
            if obstacle_grid[i][0] == 0:
                ans[i][0] = 1
            else:
                break

        for j in range(n):
            if obstacle_grid[0][j] == 0:
                ans[0][j] = 1
            else:
                break

        for i in range(1, m):
            for j in range(1, n):
                if obstacle_grid[i][j] == 0:
                    ans[i][j] = ans[i-1][j] + ans[i][j-1]
                else:
                    ans[i][j] = 0
        return ans[m-1][n-1]
