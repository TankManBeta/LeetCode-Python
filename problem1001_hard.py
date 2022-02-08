# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2022/2/8 11:21
"""
"""
在大小为 n x n 的网格 grid 上，每个单元格都有一盏灯，最初灯都处于 关闭 状态。
给你一个由灯的位置组成的二维数组 lamps ，其中 lamps[i] = [rowi, coli] 表示 打开 位于 grid[rowi][coli] 的灯。
即便同一盏灯可能在 lamps 中多次列出，不会影响这盏灯处于 打开 状态。
当一盏灯处于打开状态，它将会照亮 自身所在单元格 以及同一 行 、同一 列 和两条 对角线 上的 所有其他单元格 。
另给你一个二维数组 queries ，其中 queries[j] = [rowj, colj] 。
对于第 j 个查询，如果单元格 [rowj, colj] 是被照亮的，则查询结果为 1 ，否则为 0 。
在第j次查询之后 [按照查询的顺序]，关闭位于单元格grid[rowj][colj]上及相邻8个方向上（与单元格grid[rowi][coli]共享角或边）的任何灯。
返回一个整数数组 ans 作为答案， ans[j] 应等于第 j 次查询 queries[j] 的结果，1 表示照亮，0 表示未照亮。

输入：n = 5, lamps = [[0,0],[4,4]], queries = [[1,1],[1,0]]
输出：[1,0]
解释：最初所有灯都是关闭的。在执行查询之前，打开位于 [0, 0] 和 [4, 4] 的灯。第 0 次查询检查grid[1][1]是否被照亮（蓝色方框）。
该单元格被照亮，所以 ans[0] = 1 。然后，关闭红色方框中的所有灯。

输入：n = 5, lamps = [[0,0],[4,4]], queries = [[1,1],[1,1]]
输出：[1,1]

输入：n = 5, lamps = [[0,0],[0,4]], queries = [[0,4],[0,1],[1,4]]
输出：[1,1,0]
"""
"""
思路：维护四个哈希表，分别表示行、列、对角线、反对角线（对角线用x-y，反对角线用x+y），对于lamps中每一个lamp，如果没有出现过，
points中add，row[r]，col[c]，diag[r-c]，anti_diag[r+c]全部++，查询时直接看要查询的点在四个哈希表中是否存在，然后关闭自己及
周围的八个点（如果在points中）
"""


class Solution(object):
    @staticmethod
    def grid_illumination(n, lamps, queries):
        """
        :type n: int
        :type lamps: List[List[int]]
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        points = set()
        row, col, diag, anti_diag = dict(), dict(), dict(), dict()
        for r, c in lamps:
            if (r, c) in points:
                continue
            points.add((r, c))
            row[r] = row.get(r, 0)+1
            col[c] = col.get(c, 0)+1
            diag[r-c] = diag.get(r-c, 0)+1
            anti_diag[r+c] = anti_diag.get(r+c, 0)+1

        ans = [0]*len(queries)
        for i, (r, c) in enumerate(queries):
            if row.get(r, 0) or col.get(c, 0) or diag.get(r-c, 0) or anti_diag.get(r+c, 0):
                ans[i] = 1
            for x in range(r - 1, r + 2):
                for y in range(c - 1, c + 2):
                    if x < 0 or y < 0 or x >= n or y >= n or (x, y) not in points:
                        continue
                    points.remove((x, y))
                    row[x] -= 1
                    col[y] -= 1
                    diag[x - y] -= 1
                    anti_diag[x + y] -= 1
        return ans
