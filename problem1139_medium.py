# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2022/4/26 11:33
"""
"""
给你一个由若干 0 和 1 组成的二维网格 grid，请你找出边界全部由 1 组成的最大 正方形 子网格，并返回该子网格中的元素数量。
如果不存在，则返回 0。

输入：grid = [[1,1,1],[1,0,1],[1,1,1]]
输出：9

输入：grid = [[1,1,0,0]]
输出：1
"""
"""
思路：width和height数组分别记录以当前点为右下角的连续1的长度，然后取两者当中的最小值，就能获取到下边和右边两条边的边长，然后
继续判断左边和上边取当中的最小值
"""


class Solution(object):
    @staticmethod
    def largest1BorderedSquare(grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m = len(grid)
        n = len(grid[0])
        ans = 0
        width = [[0 for _ in range(n)] for _ in range(m)]
        height = [[0 for _ in range(n)] for _ in range(m)]

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    continue
                width[i][j] = 1 if j == 0 else width[i][j - 1] + 1
                height[i][j] = 1 if i == 0 else height[i - 1][j] + 1
                min_len = min(width[i][j], height[i][j])
                for k in range(min_len):
                    if width[i - k][j] >= k + 1 and height[i][j - k] >= k + 1:
                        ans = max(ans, k + 1)

        return ans * ans
