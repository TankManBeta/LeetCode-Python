# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2023/6/22 22:42
"""
from typing import List

"""
你有一个用于表示一片土地的整数矩阵land，该矩阵中每个点的值代表对应地点的海拔高度。若值为0则表示水域。由垂直、水平或对角连接的
水域为池塘。池塘的大小是指相连接的水域的个数。编写一个方法来计算矩阵中所有池塘的大小，返回值需要从小到大排序。

示例：
输入：
[
  [0,2,1,0],
  [0,1,0,1],
  [1,1,0,1],
  [0,1,0,1]
]
输出： [1,2,4]
"""
"""
思路：dfs，我们可以遍历整数矩阵 land 中的每个点 (i,j)，如果该点的值为 0，则从该点开始进行深度优先搜索，直到搜索到的点的值不为 
0，则停止搜索，此时搜索到的点的个数即为池塘的大小，将其加入答案数组中。注意：在进行深度优先搜索时，为了避免重复搜索，我们将搜索
到的点的值置为 1。最后，我们对答案数组进行排序，即可得到最终答案。
"""


class Solution:
    @staticmethod
    def pondSizes(land: List[List[int]]) -> List[int]:
        def dfs(i: int, j: int) -> int:
            res = 1
            land[i][j] = 1
            for x in range(i - 1, i + 2):
                for y in range(j - 1, j + 2):
                    if 0 <= x < m and 0 <= y < n and land[x][y] == 0:
                        res += dfs(x, y)
            return res

        m, n = len(land), len(land[0])
        return sorted(dfs(i, j) for i in range(m) for j in range(n) if land[i][j] == 0)
