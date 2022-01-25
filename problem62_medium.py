# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2022/1/24 12:18
"""
import math
"""
一个机器人位于一个 m x n 网格的左上角 （起始点在下图中标记为 “Start” ）。
机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为 “Finish” ）。
问总共有多少条不同的路径？

输入：m = 3, n = 7
输出：28

输入：m = 3, n = 2
输出：3

输入：m = 7, n = 3
输出：28

输入：m = 3, n = 3
输出：6
"""
"""
思路：
（1）dfs超时
（2）动态规划：由于我们每一步只能从向下或者向右移动一步，因此要想走到(i,j)，如果向下走一步，那么会从(i−1,j) 走过来；
如果向右走一步，那么会从(i,j−1) 走过来。f(i,j)=f(i−1,j)+f(i,j−1)
（3）组合数学，一共走n+m-2步，从中取m-1（或n-1）步即可
"""


# class Solution(object):
#     count = 0
#
#     def uniquePaths(self, m, n):
#         """
#         :type m: int
#         :type n: int
#         :rtype: int
#         """
#
#         def dfs(row, col):
#             if row == m - 1 and col == n - 1:
#                 Solution.count += 1
#             elif row == m - 1 and col != n - 1:
#                 dfs(row, col + 1)
#             elif row != m - 1 and col == n - 1:
#                 dfs(row + 1, col)
#             else:
#                 for direction in [(1, 0), (0, 1)]:
#                     dfs(row + direction[0], col + direction[1])
#
#         dfs(0, 0)
#         return Solution.count


# class Solution(object):
#     def uniquePaths(self, m, n):
#         """
#         :type m: int
#         :type n: int
#         :rtype: int
#         """
#         # return int(math.factorial(m+n-2)/math.factorial(m-1)/math.factorial(n-1))
#         f = [[1] * n] + [[1] + [0] * (n - 1) for _ in range(m - 1)]
#
#         for i in range(1, m):
#             for j in range(1, n):
#                 f[i][j] = f[i - 1][j] + f[i][j - 1]
#         return f[m - 1][n - 1]


class Solution(object):
    @staticmethod
    def unique_paths(m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        return int(math.factorial(m+n-2)/math.factorial(m-1)/math.factorial(n-1))
