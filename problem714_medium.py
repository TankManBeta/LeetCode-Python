# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2023/10/6 9:38
"""
from typing import List

"""
给定一个整数数组 prices，其中 prices[i]表示第 i 天的股票价格 ；整数 fee 代表了交易股票的手续费用。
你可以无限次地完成交易，但是你每笔交易都需要付手续费。如果你已经购买了一个股票，在卖出它之前你就不能再继续购买股票了。
返回获得利润的最大值。
注意：这里的一笔交易指买入持有并卖出股票的整个过程，每笔交易你只需要为支付一次手续费。 

示例 1：
输入：prices = [1, 3, 2, 8, 4, 9], fee = 2
输出：8
解释：能够达到的最大利润:  
在此处买入 prices[0] = 1
在此处卖出 prices[3] = 8
在此处买入 prices[4] = 4
在此处卖出 prices[5] = 9
总利润: ((8 - 1) - 2) + ((9 - 4) - 2) = 8

示例 2：
输入：prices = [1,3,7,5,10,3], fee = 3
输出：6
"""
"""
思路：我们定义 f[i][j] 表示到第 i 天，且状态为 j 时，能够获得的最大利润。其中 j 的取值为 0,1，分别表示当前不持有股票和持有股票。初始时 
f[0][0]=0, f[0][1]=−prices[0]。当 i≥1 时，如果当前不持有股票，那么 f[i][0] 可以由 f[i−1][0] 和 f[i−1][1]+prices[i]−fee转移得到，
即 f[i][0]=max(f[i−1][0],f[i−1][1]+prices[i]−fee)；如果当前持有股票，那么 f[i][1] 可以由 f[i−1][1] 和 f[i−1][0]−prices[i] 转移
得到，即 f[i][1]=max(f[i−1][1],f[i−1][0]−prices[i])。最终答案为 f[n−1][0]。
"""


class Solution:
    @staticmethod
    def maxProfit(prices: List[int], fee: int) -> int:
        n = len(prices)
        f = [[0] * 2 for _ in range(n)]
        f[0][1] = -prices[0]
        for i in range(1, n):
            f[i][0] = max(f[i - 1][0], f[i - 1][1] + prices[i] - fee)
            f[i][1] = max(f[i - 1][1], f[i - 1][0] - prices[i])
        return f[n - 1][0]
