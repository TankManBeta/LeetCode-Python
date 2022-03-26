# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2022/3/25 12:37
"""
"""
给你一个由 '1'（陆地）和 '0'（水）组成的的二维网格，请你计算网格中岛屿的数量。
岛屿总是被水包围，并且每座岛屿只能由水平方向和/或竖直方向上相邻的陆地连接形成。
此外，你可以假设该网格的四条边均被水包围。

输入：grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
输出：1

输入：grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
输出：3
"""
"""
思路：
（1）dfs或者bfs，统计dfs或者bfs的次数即可
（2）并查集
"""


class UnionFind:
    def __init__(self, grid):
        m, n = len(grid), len(grid[0])
        self.count = 0
        self.parent = [-1] * (m * n)
        self.rank = [0] * (m * n)
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    self.parent[i * n + j] = i * n + j
                    self.count += 1

    # 找i的父节点parent[i]，理论上parent[i]应该是i本身，如果不是则说明他被合并过过，需要找parent[i]的父节点作为i的父节点
    def find(self, i):
        if self.parent[i] != i:
            self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    # 合并
    def union(self, x, y):
        # 两个父节点相同说明已经在同一个连通分量
        rootx = self.find(x)
        rooty = self.find(y)
        if rootx != rooty:
            # 按照秩进行排序，简单的往复杂上并
            if self.rank[rootx] < self.rank[rooty]:
                rootx, rooty = rooty, rootx
            self.parent[rooty] = rootx
            if self.rank[rootx] == self.rank[rooty]:
                self.rank[rootx] += 1
            self.count -= 1

    # 返回连通分量的个数
    def getCount(self):
        return self.count


class Solution(object):
    @staticmethod
    def numIslands(grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        # m = len(grid)
        # n = len(grid[0])
        # ans = 0
        # for i in range(m):
        #     for j in range(n):
        #         if grid[i][j] == '1':
        #             grid[i][j] = '0'
        #             queue = [(i, j)]
        #             while queue:
        #                 r, c = queue.pop(0)
        #                 for new_r, new_c in [(r-1, c), (r+1, c), (r, c-1), (r, c+1)]:
        #                     if 0<=new_r<m and 0<=new_c<n and grid[new_r][new_c] == '1':
        #                         queue.append((new_r, new_c))
        #                         grid[new_r][new_c] = '0'
        #             ans += 1
        # return ans

        nr = len(grid)
        if nr == 0:
            return 0
        nc = len(grid[0])
        uf = UnionFind(grid)
        for r in range(nr):
            for c in range(nc):
                if grid[r][c] == "1":
                    grid[r][c] = "0"
                    for x, y in [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]:
                        if 0 <= x < nr and 0 <= y < nc and grid[x][y] == "1":
                            uf.union(r * nc + c, x * nc + y)
        return uf.getCount()
