# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2023/2/22 10:38
"""
from typing import List

"""
爱丽丝和鲍勃继续他们的石子游戏。许多堆石子 排成一行，每堆都有正整数颗石子 piles[i]。游戏以谁手中的石子最多来决出胜负。
爱丽丝和鲍勃轮流进行，爱丽丝先开始。最初，M = 1。
在每个玩家的回合中，该玩家可以拿走剩下的 前 X 堆的所有石子，其中 1 <= X <= 2M。然后，令 M = max(M, X)。
游戏一直持续到所有石子都被拿走。
假设爱丽丝和鲍勃都发挥出最佳水平，返回爱丽丝可以得到的最大数量的石头。

示例 1：
输入：piles = [2,7,9,4,4]
输出：10
解释：如果一开始Alice取了一堆，Bob取了两堆，然后Alice再取两堆。爱丽丝可以得到2 + 4 + 4 = 10堆。如果Alice一开始拿走了两堆，
那么Bob可以拿走剩下的三堆。在这种情况下，Alice得到2 + 7 = 9堆。返回10，因为它更大。

示例 2:
输入：piles = [1,2,3,4,5,100]
输出：104
"""
"""
思路：
（1）前缀和 + 记忆化搜索。首先我们定义一个前缀和数组，然后定义dfs(i,m)，当前的位置是i，当前能取到的最大范围为m，即M=m。如果
i+2m>=n，说明我们能把剩下的全都取完，则返回s[n]-s[i]；否则能够拿到的最大石子数为 s[n]−s[i]−dfs(i+x,max(m,x))。也即是说，
当前轮的人能够拿到的石子数为当前剩下的所有石子数减去下一轮对手能够拿到的石子数。
（2）动态规划。dfs 改成 f 数组；递归改成循环（每个参数都对应一层循环）；递归边界改成 f 数组的初始值。由于本题的边界比较复杂，
直接在递推中计算。
"""


class Solution:
    @staticmethod
    def stoneGameII(piles: List[int]) -> int:
        # n = len(piles)
        # s = list(accumulate(piles, initial=0))
        # @cache
        # def dfs(i, m):
        #     if m * 2 >= n - i:
        #         return s[n] - s[i]
        #     return max(s[n] - s[i] - dfs(i + x, max(m, x)) for x in range(1, m << 1 | 1))
        # return dfs(0, 1)

        s, n = 0, len(piles)
        f = [[0] * (n + 1) for _ in range(n)]
        for i in range(n - 1, -1, -1):
            s += piles[i]
            for m in range(1, i // 2 + 2):
                if i + m * 2 >= n:
                    f[i][m] = s
                else:
                    f[i][m] = s - min(f[i + x][max(m, x)] for x in range(1, m * 2 + 1))
        return f[0][1]
