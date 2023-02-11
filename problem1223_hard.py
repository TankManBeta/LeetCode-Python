# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2023/2/10 0:27
"""
from typing import List

"""
有一个骰子模拟器会每次投掷的时候生成一个 1 到 6 的随机数。
不过我们在使用它时有个约束，就是使得投掷骰子时，连续 掷出数字 i 的次数不能超过 rollMax[i]（i 从 1 开始编号）。
现在，给你一个整数数组 rollMax 和一个整数 n，请你来计算掷 n 次骰子可得到的不同点数序列的数量。
假如两个序列中至少存在一个元素不同，就认为这两个序列是不同的。由于答案可能很大，所以请返回 模 10^9 + 7 之后的结果。

示例 1：
输入：n = 2, rollMax = [1,1,2,2,2,3]
输出：34
解释：我们掷 2 次骰子，如果没有约束的话，共有 6 * 6 = 36 种可能的组合。但是根据 rollMax 数组，数字 1 和 2 最多连续出现一次，
所以不会出现序列 (1,1) 和 (2,2)。因此，最终答案是 36-2 = 34。

示例 2：
输入：n = 2, rollMax = [1,1,1,1,1,1]
输出：30

示例 3：
输入：n = 3, rollMax = [1,1,1,2,2,3]
输出：181
"""
"""
思路：
（1）dfs，index是第几次掷骰子，pre是上一次的点数，count是出现已经连续出现过几次。每次掷骰子的时候看一下当前点数cur和上一次点数
pre是否相同，相同的话就把count++，否则count置为1。如果count<rollMax[cur-1]，说明可以继续进行下一次投掷，否则说明当前情况不可
继续。
（2）dp，对于任意的dp[i][j][1]，由于其结尾是 j，则可以由任意前面的某个状态dp[i-1][p][q] 转移而来，但是注意此时p不能为 j，
因为这样就连续了。对于任意的dp[i][j][k],其中k != 1 && k <= rollMax[j-1]，则状态转移为dp[i][j][k] = dp[i-1][j][k-1]，
即通过掷k-1并且最后是k-1个连续的j的序列再加一个j得到dp[i][j][k]
"""

MOD = 10 ** 9 + 7


class Solution:
    @staticmethod
    def dieSimulator(n: int, rollMax: List[int]) -> int:
        # @lru_cache(None)
        # def dfs(index: int, pre: int, count: int) -> int:
        #     if index == n:
        #         return 1

        #     res = 0
        #     for cur in range(1, 7):
        #         nextCount = 1 if cur != pre else count + 1
        #         if nextCount <= rollMax[cur - 1]:
        #             res += dfs(index + 1, cur, nextCount)
        #             res %= MOD
        #     return res

        # res = 0
        # for start in range(1, 7):
        #     res += dfs(1, start, 1)
        #     res %= MOD
        # return res

        dp = [[[0 for _ in range(16)] for _ in range(7)] for _ in range(n + 1)]
        for i in range(1, 7):
            dp[1][i][1] = 1
        for i in range(2, n + 1):
            for j in range(1, 7):
                for k in range(1, min(rollMax[j - 1], i) + 1):
                    if k == 1:
                        for p in range(1, 7):
                            if p == j:
                                continue
                            for q in range(1, min(rollMax[p - 1], i - 1) + 1):
                                dp[i][j][k] = (dp[i][j][k] + dp[i - 1][p][q]) % MOD
                    else:
                        dp[i][j][k] = (dp[i][j][k] + dp[i - 1][j][k - 1]) % MOD
        ans = 0
        for i in range(1, 7):
            for j in range(1, rollMax[i - 1] + 1):
                ans = (ans + dp[n][i][j]) % MOD
        return ans
