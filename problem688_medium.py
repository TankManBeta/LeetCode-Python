# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2022/2/17 13:08
"""
"""
在一个 n x n 的国际象棋棋盘上，一个骑士从单元格 (row, column) 开始，并尝试进行 k 次移动。
行和列是 从 0 开始 的，所以左上单元格是 (0,0) ，右下单元格是 (n - 1, n - 1) 。
象棋骑士有8种可能的走法，如下图所示。每次移动在基本方向上是两个单元格，然后在正交方向上是一个单元格。
每次骑士要移动时，它都会随机从8种可能的移动中选择一种(即使棋子会离开棋盘)，然后移动到那里。
骑士继续移动，直到它走了 k 步或离开了棋盘。
返回 骑士在棋盘停止移动后仍留在棋盘上的概率 。

输入: n = 3, k = 2, row = 0, column = 0
输出: 0.0625
解释: 有两步(到(1,2)，(2,1))可以让骑士留在棋盘上。
在每一个位置上，也有两种移动可以让骑士留在棋盘上。
骑士留在棋盘上的总概率是0.0625。

输入: n = 1, k = 0, row = 0, column = 0
输出: 1.00000
"""
"""
思路：
（1）直接dfs，超时
（2）dp，每一次的dp[i][j]是从上一次的位置过来的
"""


class Solution(object):
    @staticmethod
    def knight_probability(n, k, row, column):
        """
        :type n: int
        :type k: int
        :type row: int
        :type column: int
        :rtype: float
        """
        # self.count = 8**k
        # self.ans = 0
        # def dfs(steps, r, c):
        #     if steps == k:
        #         if 0<=r<n and 0<=c<n:
        #             self.ans += 1
        #         return
        #     else:
        #         if r<0 or r>=n or c<0 or c>=n:
        #             return
        #     for new_r, new_c in((r-1,c-2),(r-2,c-1),(r-2,c+1),(r-1,c+2),(r+1,c-2),(r+2,c-1),(r+2,c+1),(r+1,c+2)):
        #         dfs(steps+1, new_r, new_c)
        # dfs(0,row,column)
        # return float(self.ans)/self.count

        dp = [[0 for _ in range(n)] for _ in range(n)]
        dp[row][column] = 1
        directions = [(1, 2), (1, -2), (2, 1), (2, -1), (-2, 1), (-2, -1), (-1, 2), (-1, -2)]
        for _ in range(k):
            new_dp = [[0 for _ in range(n)] for _ in range(n)]
            for i in range(n):
                for j in range(n):
                    for d in directions:
                        x, y = i + d[0], j + d[1]
                        if x < 0 or x >= n or y < 0 or y >= n:
                            continue
                        new_dp[i][j] += dp[x][y]
            dp = new_dp
        return sum(map(sum, dp)) / float(8 ** k)
