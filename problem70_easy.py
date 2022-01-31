# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2022/1/30 16:24
"""
"""
假设你正在爬楼梯。需要 n 阶你才能到达楼顶。
每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？

输入：n = 2
输出：2
解释：有两种方法可以爬到楼顶。
1. 1 阶 + 1 阶
2. 2 阶

输入：n = 3
输出：3
解释：有三种方法可以爬到楼顶。
1. 1 阶 + 1 阶 + 1 阶
2. 1 阶 + 2 阶
3. 2 阶 + 1 阶
"""
"""
思路：
（1）直接dp，dp[i]=dp[i-1]+dp[i-2]
（2）组合数学中算an表达式
（3）矩阵快速幂，左乘n次[[1,1],[1,0]]
"""


class Solution(object):
    @staticmethod
    def climb_stairs(n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1 or n == 2:
            return n
        dp = [0 for _ in range(n)]
        dp[0] = 1
        dp[1] = 2
        for i in range(2, n):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[n-1]
