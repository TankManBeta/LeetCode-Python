# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2023/2/15 21:17
"""
from typing import List

"""
给定一个整数数组prices，其中第  prices[i] 表示第 i 天的股票价格 。​
设计一个算法计算出最大利润。在满足以下约束条件下，你可以尽可能地完成更多的交易（多次买卖一支股票）:
    卖出股票后，你无法在第二天买入股票 (即冷冻期为 1 天)。
注意：你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。

示例 1:
输入: prices = [1,2,3,0,2]
输出: 3 
解释: 对应的交易状态为: [买入, 卖出, 冷冻期, 买入, 卖出]

示例 2:
输入: prices = [1]
输出: 0
"""
"""
思路：动态规划。首先我们需要找到题目存在的状态，本题的状态主要有三个：有股票，无股票且在冷冻期，无股票且不在冷冻期。这里的
「冷冻期」指的是在第 i 天结束之后的状态。我们定义f[i][0]，f[i][1]，f[i][2]分别为这三种状态，现在我们推导如何有i-1的状态转移到
i的状态。
f[i][0]：如果我们在第i步拥有股票，则可能的情况有：第i-1步我们就有股票，即f[i-1][0]；第i步我们买入的，则说明第i-1步我们没有股票，
并且i-1天结束之后不处于冷冻期，即f[i-1][2]-price[i]。所以f[i][0]=max(f[i−1][0],f[i−1][2]−prices[i])。
f[i][1]：如果我们在第i步没有股票且处在冷冻期，说明我们在第i天卖出了股票，也就是说我们第i-1步必有股票。所以f[i][1]=f[i−1][0]+prices[i]。
f[i][2]：如果我们在第i步没有股票且不在冷冻期，则可能的情况有：第i-1步我们就没有股票且不在冷冻期，即f[i][2]=f[i-1][2]；前一天
结束之后我们处在冷冻期，经过一天之后解冻了，即f[i][2]=f[i-1][1]。所以f[i][2]=max(f[i−1][1],f[i−1][2])
最后的结果就是max(f[n−1][0],f[n−1][1],f[n−1][2])
注意，如果在最后一天（第 n−1 天）结束之后，手上仍然持有股票，那么显然是没有任何意义的。因此更加精确地，最终的答案实际上是 
f[n−1][1] 和 f[n−1][2] 中的较大值，即：max(f[n−1][1],f[n−1][2])
"""


class Solution:
    @staticmethod
    def maxProfit(prices: List[int]) -> int:
        # if not prices:
        #     return 0
        # n = len(prices)
        # # f[i][0]: 手上持有股票的最大收益
        # # f[i][1]: 手上不持有股票，并且处于冷冻期中的累计最大收益
        # # f[i][2]: 手上不持有股票，并且不在冷冻期中的累计最大收益
        # f = [[-prices[0], 0, 0]] + [[0] * 3 for _ in range(n - 1)]
        # for i in range(1, n):
        #     f[i][0] = max(f[i - 1][0], f[i - 1][2] - prices[i])
        #     f[i][1] = f[i - 1][0] + prices[i]
        #     f[i][2] = max(f[i - 1][1], f[i - 1][2])
        # return max(f[n - 1][1], f[n - 1][2])

        if not prices:
            return 0
        n = len(prices)
        f0, f1, f2 = -prices[0], 0, 0
        for i in range(1, n):
            new_f0 = max(f0, f2 - prices[i])
            new_f1 = f0 + prices[i]
            new_f2 = max(f1, f2)
            f0, f1, f2 = new_f0, new_f1, new_f2
        return max(f1, f2)
