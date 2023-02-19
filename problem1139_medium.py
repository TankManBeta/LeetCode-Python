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
思路：
（1）width和height数组分别记录以当前点为右下角的连续1的长度，然后取两者当中的最小值，就是万一能构成的正方形的边长，此时正方形
的右边和下边都可以确定下来，然后在考虑左下角和右上角是否满足连续k个1即可。
（2）我们可以使用前缀和的方法预处理出每个位置向下和向右的连续 1 的个数，记为 down[i][j] 和 right[i][j]。然后我们枚举正方形的
边长 k，从最大的边长开始枚举，然后枚举正方形的左上角位置 (i,j)，如果满足条件，即可返回 k**2 。
"""


class Solution(object):
    @staticmethod
    def largest1BorderedSquare(grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        # m = len(grid)
        # n = len(grid[0])
        # ans = 0
        # width = [[0 for _ in range(n)] for _ in range(m)]
        # height = [[0 for _ in range(n)] for _ in range(m)]
        # for i in range(m):
        #     for j in range(n):
        #         if grid[i][j] == 0:
        #             continue
        #         width[i][j] = 1 if j == 0 else width[i][j - 1] + 1
        #         height[i][j] = 1 if i == 0 else height[i - 1][j] + 1
        #         min_len = min(width[i][j], height[i][j])
        #         for k in range(min_len):
        #             if width[i - k][j] >= k + 1 and height[i][j - k] >= k + 1:
        #                 ans = max(ans, k + 1)
        # return ans * ans

        m, n = len(grid), len(grid[0])
        down = [[0] * n for _ in range(m)]
        right = [[0] * n for _ in range(m)]
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if grid[i][j]:
                    down[i][j] = down[i + 1][j] + 1 if i + 1 < m else 1
                    right[i][j] = right[i][j + 1] + 1 if j + 1 < n else 1
        for k in range(min(m, n), 0, -1):
            for i in range(m - k + 1):
                for j in range(n - k + 1):
                    if down[i][j] >= k and right[i][j] >= k and down[i][j + k - 1] >= k and right[i + k - 1][j] >= k:
                        return k * k
        return 0
