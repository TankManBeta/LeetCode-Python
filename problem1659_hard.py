# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2023/6/24 23:02
"""
from linecache import cache

"""
给你四个整数 m、n、introvertsCount 和 extrovertsCount 。有一个 m x n 网格，和两种类型的人：内向的人和外向的人。总共有 
introvertsCount 个内向的人和 extrovertsCount 个外向的人。
请你决定网格中应当居住多少人，并为每个人分配一个网格单元。 注意，不必 让所有人都生活在网格中。
每个人的 幸福感 计算如下：
    内向的人 开始 时有 120 个幸福感，但每存在一个邻居（内向的或外向的）他都会 失去  30 个幸福感。
    外向的人 开始 时有 40 个幸福感，每存在一个邻居（内向的或外向的）他都会 得到  20 个幸福感。
邻居是指居住在一个人所在单元的上、下、左、右四个直接相邻的单元中的其他人。
网格幸福感 是每个人幸福感的 总和 。 返回 最大可能的网格幸福感 。 

示例 1：
输入：m = 2, n = 3, introvertsCount = 1, extrovertsCount = 2
输出：240
解释：假设网格坐标 (row, column) 从 1 开始编号。
将内向的人放置在单元 (1,1) ，将外向的人放置在单元 (1,3) 和 (2,3) 。
- 位于 (1,1) 的内向的人的幸福感：120（初始幸福感）- (0 * 30)（0 位邻居）= 120
- 位于 (1,3) 的外向的人的幸福感：40（初始幸福感）+ (1 * 20)（1 位邻居）= 60
- 位于 (2,3) 的外向的人的幸福感：40（初始幸福感）+ (1 * 20)（1 位邻居）= 60
网格幸福感为：120 + 60 + 60 = 240
上图展示该示例对应网格中每个人的幸福感。内向的人在浅绿色单元中，而外向的人在浅紫色单元中。

示例 2：
输入：m = 3, n = 1, introvertsCount = 2, extrovertsCount = 1
输出：260
解释：将内向的人放置在单元 (1,1) 和 (3,1) ，将外向的人放置在单元 (2,1) 。
- 位于 (1,1) 的内向的人的幸福感：120（初始幸福感）- (1 * 30)（1 位邻居）= 90
- 位于 (2,1) 的外向的人的幸福感：40（初始幸福感）+ (2 * 20)（2 位邻居）= 80
- 位于 (3,1) 的内向的人的幸福感：120（初始幸福感）- (1 * 30)（1 位邻居）= 90
网格幸福感为 90 + 80 + 90 = 260

示例 3：
输入：m = 2, n = 2, introvertsCount = 4, extrovertsCount = 0
输出：240
"""
"""
思路：我们定义一个函数 dfs(i,pre,ic,ec)，表示当前从第 i 行开始，且上一行的状态为 pre，内向的人还剩 ic 个，外向的人还剩 ec 个时，
网格的最大幸福感。那么答案就是 dfs(0,0,introvertsCount,extrovertsCount)。函数 dfs(i,pre,ic,ec) 的计算过程如下：如果 i=m，
表示已经处理完了所有的行，那么返回 0；如果 ic=0 且 ec=0，表示所有的人都已经分配完了，那么返回 0；否则，枚举当前行的状态 cur，
其中 cur∈[0,3**n)，然后计算当前行的幸福感 f[cur]，以及与上一行的状态 pre 之间对幸福感的贡献 g[pre][cur]，并递归计算 
dfs(i+1,cur,ic−ix[cur],ec−ex[cur])，最后返回 f[cur]+g[pre][cur]+dfs(i+1,cur,ic−ix[cur],ec−ex[cur]) 的最大值，即：
dfs(i,pre,ic,ec)= max{f[cur]+g[pre][cur]+dfs(i+1,cur,ic−ix[cur],ec−ex[cur])}
其中：ix[cur] 表示状态 cur 中内向的人的个数；ex[cur] 表示状态 cur 中外向的人的个数；f[cur] 表示状态 cur 中的人的初始幸福感；
g[pre][cur] 表示两个相邻状态行对幸福感的贡献。这些值都可以通过预处理得到。并且，我们可以使用记忆化搜索的方法，避免重复计算。
"""


class Solution:
    @staticmethod
    def getMaxGridHappiness(
            m: int, n: int, introvertsCount: int, extrovertsCount: int
    ) -> int:
        @cache
        def dfs(i: int, pre: int, ic: int, ec: int) -> int:
            if i == m or (ic == 0 and ec == 0):
                return 0
            ans = 0
            for cur in range(mx):
                if ix[cur] <= ic and ex[cur] <= ec:
                    a = f[cur] + g[pre][cur]
                    b = dfs(i + 1, cur, ic - ix[cur], ec - ex[cur])
                    ans = max(ans, a + b)
            return ans

        mx = pow(3, n)
        f = [0] * mx
        g = [[0] * mx for _ in range(mx)]
        h = [[0, 0, 0], [0, -60, -10], [0, -10, 40]]
        bits = [[0] * n for _ in range(mx)]
        ix = [0] * mx
        ex = [0] * mx
        for i in range(mx):
            mask = i
            for j in range(n):
                mask, x = divmod(mask, 3)
                bits[i][j] = x
                if x == 1:
                    ix[i] += 1
                    f[i] += 120
                elif x == 2:
                    ex[i] += 1
                    f[i] += 40
                if j:
                    f[i] += h[x][bits[i][j - 1]]
        for i in range(mx):
            for j in range(mx):
                for k in range(n):
                    g[i][j] += h[bits[i][k]][bits[j][k]]
        return dfs(0, 0, introvertsCount, extrovertsCount)
