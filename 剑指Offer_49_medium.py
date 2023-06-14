# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2023/6/13 19:55
"""
"""
我们把只包含质因子 2、3 和 5 的数称作丑数（Ugly Number）。求按从小到大的顺序的第 n 个丑数。

示例:
输入: n = 10
输出: 12
解释: 1, 2, 3, 4, 5, 6, 8, 9, 10, 12 是前 10 个丑数。
"""
"""
思路：设动态规划列表 dp ，dp[i] 代表第 i+1 个丑数；当索引 a,b,c 满足以下条件时， dp[i] 为三种情况的最小值；每轮计算 dp[i] 后，
需要更新索引 a,b,c 的值，使其始终满足方程条件。实现方法：分别独立判断 dp[i] 和 dp[a]×2 , dp[b]×3 , dp[c]×5 的大小关系，
若相等则将对应索引 a , b , c 加 1 ；dp[i]=min(dp[a]×2,dp[b]×3,dp[c]×5)
"""


class Solution:
    @staticmethod
    def nthUglyNumber(n: int) -> int:
        dp, a, b, c = [1] * n, 0, 0, 0
        for i in range(1, n):
            n2, n3, n5 = dp[a] * 2, dp[b] * 3, dp[c] * 5
            dp[i] = min(n2, n3, n5)
            if dp[i] == n2: a += 1
            if dp[i] == n3: b += 1
            if dp[i] == n5: c += 1
        return dp[-1]
