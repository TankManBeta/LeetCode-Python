# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2023/4/5 14:17
"""
from cmath import inf
from itertools import accumulate
from typing import List

"""
有 N 堆石头排成一排，第 i 堆中有 stones[i] 块石头。
每次移动（move）需要将连续的 K 堆石头合并为一堆，而这个移动的成本为这 K 堆石头的总数。
找出把所有石头合并成一堆的最低成本。如果不可能，返回 -1 。 

示例 1：
输入：stones = [3,2,4,1], K = 2
输出：20
解释：
从 [3, 2, 4, 1] 开始。
合并 [3, 2]，成本为 5，剩下 [5, 4, 1]。
合并 [4, 1]，成本为 5，剩下 [5, 5]。
合并 [5, 5]，成本为 10，剩下 [10]。
总成本 20，这是可能的最小值。

示例 2：
输入：stones = [3,2,4,1], K = 3
输出：-1
解释：任何合并操作后，都会剩下 2 堆，我们无法再进行合并。所以这项任务是不可能完成的。.

示例 3：
输入：stones = [3,5,1,2,6], K = 3
输出：25
解释：
从 [3, 5, 1, 2, 6] 开始。
合并 [5, 1, 2]，成本为 8，剩下 [3, 8, 6]。
合并 [3, 8, 6]，成本为 17，剩下 [17]。
总成本 25，这是可能的最小值。
"""
"""
思路：定义 f[i][j][k] 表示将区间 [i,j] 中的石头合并成 k 堆的最小成本。初始时 f[i][i][1]=0，其他位置的值均为 ∞。注意到 k 的
取值范围为 [1,K]，因此我们需要枚举 k 的值。对于 f[i][j][k]，我们可以枚举 i≤h<j，将区间 [i,j] 拆分成两个区间 [i,h] 和 [h+1,j]，
然后将 [i,h] 中的石头合并成 1 堆，将 [h+1,j] 中的石头合并成 k−1 堆，最后将这两堆石头合并成一堆，这样就可以将区间 [i,j] 中的
石头合并成 k 堆。因此，我们可以得到状态转移方程：f[i][j][k]= min_{i≤h<j} (f[i][h][1]+f[h+1][j][k−1])。
我们将区间 [i,j] 的 K 堆石头合并成一堆，因此 f[i][j][1]=f[i][j][K]+∑_{t=i}^{j}stones[t]（先分成k堆，再将k堆合成一堆），
其中 stones[t] 表示区间 [i,j] 中石头的总数。最后答案即为 f[1][n][1]。
"""


class Solution:
    @staticmethod
    def mergeStones(stones: List[int], K: int) -> int:
        n = len(stones)
        if (n - 1) % (K - 1):
            return -1
        s = list(accumulate(stones, initial=0))
        f = [[[inf] * (K + 1) for _ in range(n + 1)] for _ in range(n + 1)]
        for i in range(1, n + 1):
            f[i][i][1] = 0
        for l in range(2, n + 1):
            for i in range(1, n - l + 2):
                j = i + l - 1
                for k in range(1, K + 1):
                    for h in range(i, j):
                        f[i][j][k] = min(f[i][j][k], f[i][h][1] + f[h + 1][j][k - 1])
                f[i][j][1] = f[i][j][K] + s[j] - s[i - 1]
        return f[1][n][1]