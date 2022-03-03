# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2022/3/2 11:17
"""
"""
给定一个数组 prices ，它的第 i 个元素 prices[i] 表示一支给定股票第 i 天的价格。
你只能选择 某一天 买入这只股票，并选择在 未来的某一个不同的日子 卖出该股票。设计一个算法来计算你所能获取的最大利润。
返回你可以从这笔交易中获取的最大利润。如果你不能获取任何利润，返回 0 。

输入：[7,1,5,3,6,4]
输出：5

输入：prices = [7,6,4,3,1]
输出：0
"""
"""
思路：最大利润出现在右边的减去左边最小的，所以在遍历过程中找左边最小的即可
"""


class Solution(object):
    @staticmethod
    def max_profit(prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        n = len(prices)
        min_index = 0
        max_profit = 0
        for i in range(1, n):
            if prices[i] < prices[min_index]:
                min_index = i
            if (prices[i]-prices[min_index]) > max_profit:
                max_profit = prices[i]-prices[min_index]
        return max_profit
