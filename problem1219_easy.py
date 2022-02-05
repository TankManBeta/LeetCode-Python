# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2022/2/5 12:30
"""
"""
你要开发一座金矿，地质勘测学家已经探明了这座金矿中的资源分布，并用大小为 m * n 的网格 grid 进行了标注。
每个单元格中的整数就表示这一单元格中的黄金数量；如果该单元格是空的，那么就是 0。
为了使收益最大化，矿工需要按以下规则来开采黄金：
每当矿工进入一个单元，就会收集该单元格中的所有黄金。
矿工每次可以从当前位置向上下左右四个方向走。
每个单元格只能被开采（进入）一次。
不得开采（进入）黄金数目为 0 的单元格。
矿工可以从网格中 任意一个 有黄金的单元格出发或者是停止。

输入：grid = [[0,6,0],[5,8,7],[0,9,0]]
输出：24
解释：
[[0,6,0],
 [5,8,7],
 [0,9,0]]
一种收集最多黄金的路线是：9 -> 8 -> 7。

输入：grid = [[1,0,7],[2,0,6],[3,4,5],[0,3,0],[9,0,20]]
输出：28
解释：
[[1,0,7],
 [2,0,6],
 [3,4,5],
 [0,3,0],
 [9,0,20]]
一种收集最多黄金的路线是：1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7。
"""
"""
思路：所有不为0的点dfs即可
"""


class Solution(object):
    def __init__(self):
        self.ans = 0

    def get_maximum_gold(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m = len(grid)
        n = len(grid[0])

        def dfs(x, y, count):
            count += grid[x][y]
            self.ans = max(self.ans, count)
            temp = grid[x][y]
            grid[x][y] = 0
            for new_x, new_y in ((x - 1, y), (x, y - 1), (x, y + 1), (x + 1, y)):
                if 0 <= new_x <= m - 1 and 0 <= new_y <= n - 1 and grid[new_x][new_y] > 0:
                    dfs(new_x, new_y, count)
            grid[x][y] = temp

        for i in range(m):
            for j in range(n):
                if grid[i][j] != 0:
                    dfs(i, j, 0)

        return self.ans
