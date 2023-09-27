# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2023/8/17 16:35
"""
from linecache import cache
from typing import List

"""
给你一个 rows x cols 大小的矩形披萨和一个整数 k ，矩形包含两种字符： 'A' （表示苹果）和 '.' （表示空白格子）。你需要切披萨 
k-1 次，得到 k 块披萨并送给别人。切披萨的每一刀，先要选择是向垂直还是水平方向切，再在矩形的边界上选一个切的位置，将披萨一分为二。
如果垂直地切披萨，那么需要把左边的部分送给一个人，如果水平地切，那么需要把上面的部分送给一个人。在切完最后一刀后，需要把剩下来的
一块送给最后一个人。
请你返回确保每一块披萨包含 至少 一个苹果的切披萨方案数。由于答案可能是个很大的数字，请你返回它对 10^9 + 7 取余的结果。 

示例 1：
输入：pizza = ["A..","AAA","..."], k = 3
输出：3 
解释：上图展示了三种切披萨的方案。注意每一块披萨都至少包含一个苹果。

示例 2：
输入：pizza = ["A..","AA.","..."], k = 3
输出：1

示例 3：
输入：pizza = ["A..","A..","..."], k = 1
输出：1
"""
"""
思路：我们可以使用二维前缀和来快速计算出每个子矩形中苹果的数量，定义 s[i][j] 表示矩形前 i 行，前 j 列的子矩形中苹果的数量，
那么 s[i][j] 可以由 s[i−1], s[i][j−1], s[i−1][j−1] 三个子矩形的苹果数量求得，具体的计算方法如下：
s[i][j]=s[i−1][j]+s[i][j−1]−s[i−1][j−1]+(pizza[i−1][j−1]==′A′) 其中 pizza[i−1][j−1] 表示矩形中第 i 行，第 j 列的字符，
如果是苹果，则为 1，否则为 0。
接下来，我们设计一个函数 dfs(i,j,k)，表示将矩形 (i,j,m−1,n−1) 切 k 刀，得到 k+1 块披萨的方案数，其中 (i,j) 和 (m−1,n−1) 
分别是矩形的左上角和右下角的坐标。函数 dfs(i,j,k) 的计算方法如下：
如果 k=0，表示没有可以切了，那么我们需要判断矩形中是否有苹果，如果有苹果，则返回 1，否则返回 0；
如果 k>0，我们需要枚举最后一刀的切法，如果最后一刀是水平切，那么我们需要枚举切的位置 x，其中 i<x<m，如果 
s[x][n]−s[i][n]−s[x][j]+s[i][j]>0，说明切出来的上面一块披萨中有苹果，我们累加 dfs(x,j,k−1) 的值到答案中；如果最后一刀是垂直切，
那么我们需要枚举切的位置 y，其中 j<y<n，如果 s[m][y]−s[i][y]−s[m][j]+s[i][j]>0，说明切出来的左边一块披萨中有苹果，我们累加 
dfs(i,y,k−1) 的值到答案中。最终的答案即为 dfs(0,0,k−1) 的值。为了避免重复计算，我们可以使用记忆化搜索的方法，用一个三维数组 f 
来记录 dfs(i,j,k) 的值。当我们需要计算 dfs(i,j,k) 的值时，如果 f[i][j][k] 不为 −1，说明我们之前已经计算过了，直接返回 f[i][j][k] 即可，
否则我们按照上面的方法计算 dfs(i,j,k) 的值，并将结果保存到 f[i][j][k] 中。
"""


class Solution:
    @staticmethod
    def ways(pizza: List[str], k: int) -> int:
        @cache
        def dfs(i: int, j: int, k: int) -> int:
            if k == 0:
                return int(s[m][n] - s[i][n] - s[m][j] + s[i][j] > 0)
            ans = 0
            for x in range(i + 1, m):
                if s[x][n] - s[i][n] - s[x][j] + s[i][j] > 0:
                    ans += dfs(x, j, k - 1)
            for y in range(j + 1, n):
                if s[m][y] - s[i][y] - s[m][j] + s[i][j] > 0:
                    ans += dfs(i, y, k - 1)
            return ans % mod

        mod = 10**9 + 7
        m, n = len(pizza), len(pizza[0])
        s = [[0] * (n + 1) for _ in range(m + 1)]
        for i, row in enumerate(pizza, 1):
            for j, c in enumerate(row, 1):
                s[i][j] = s[i - 1][j] + s[i][j - 1] - s[i - 1][j - 1] + int(c == 'A')
        return dfs(0, 0, k - 1)