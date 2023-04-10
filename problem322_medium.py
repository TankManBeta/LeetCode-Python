# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2023/4/9 15:11
"""
from math import inf
from typing import List

"""
给你一个整数数组 coins ，表示不同面额的硬币；以及一个整数 amount ，表示总金额。
计算并返回可以凑成总金额所需的 最少的硬币个数 。如果没有任何一种硬币组合能组成总金额，返回 -1 。
你可以认为每种硬币的数量是无限的。 

示例 1：
输入：coins = [1, 2, 5], amount = 11
输出：3 
解释：11 = 5 + 5 + 1

示例 2：
输入：coins = [2], amount = 3
输出：-1

示例 3：
输入：coins = [1], amount = 0
输出：0
"""
"""
思路：
（1）dfs，肯定超时
（2）记忆化搜索
（3）dp，如果我当前枚举的数量c<我当前使用的硬币代表的面值x，说明使用当前面值的硬币肯定不能表示当前枚举的数量；如果我当前枚举的
数量c≥我当前使用的硬币代表的面值x，说明当前面值的硬币可以用来表示部分当前枚举的数量，此时可以选择用或者不用x，即f[i + 1][c] = 
min(f[i][c], f[i + 1][c - x] + 1)。
"""


class Solution:
    @staticmethod
    def coinChange(coins: List[int], amount: int) -> int:
        # @cache
        # def dfs(i, c):
        #     if i < 0:
        #         return 0 if c == 0 else inf
        #     if c < coins[i]:
        #         return dfs(i - 1, c)
        #     return min(dfs(i - 1, c), dfs(i, c - coins[i]) + 1)
        # ans = dfs(len(coins) - 1, amount)
        # return ans if ans < inf else -1

        n = len(coins)
        f = [[inf] * (amount + 1) for _ in range(n + 1)]
        f[0][0] = 0
        for i, x in enumerate(coins):
            for c in range(amount + 1):
                if c < x:
                    f[i + 1][c] = f[i][c]
                else:
                    f[i + 1][c] = min(f[i][c], f[i + 1][c - x] + 1)
        ans = f[n][amount]
        return ans if ans < inf else -1
