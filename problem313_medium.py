# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2023/2/15 22:17
"""
from math import inf
from typing import List

"""
超级丑数 是一个正整数，并满足其所有质因数都出现在质数数组 primes 中。
给你一个整数 n 和一个整数数组 primes ，返回第 n 个 超级丑数 。
题目数据保证第 n 个 超级丑数 在 32-bit 带符号整数范围内。

示例 1：
输入：n = 12, primes = [2,7,13,19]
输出：32 
解释：给定长度为 4 的质数数组 primes = [2,7,13,19]，前 12 个超级丑数序列为：[1,2,4,7,8,13,14,16,19,26,28,32] 。

示例 2：
输入：n = 1, primes = [2,3,5]
输出：1
解释：1 不含质因数，因此它的所有质因数都在质数数组 primes = [2,3,5] 中。
"""
"""
思路：
（1）有序列表。每次把当前最小的丑数取出来，将它与primes数组每一个数做乘积，然后将这些新的丑数继续加入有序列表中（注意去重）。
（2）动态规划。dp数组用于存储丑数，indexes数组用于记录当前的prime因子应该同第几个丑数相乘，每次我们用了第几个prime，则它对应的
应该相乘的丑数的位置就加一。例如我们用了prime=3，3的indexes本来是0，代表他应该同第一个丑数相乘，现在乘完了，indexes++，说明下
次应该和第二个丑数相乘，即indexes=2。
"""

from sortedcontainers import SortedList


class Solution:
    @staticmethod
    def nthSuperUglyNumber(n: int, primes: List[int]) -> int:
        # q = SortedList()
        # q.add(1)
        # cnt = 1
        # while cnt != n:
        #     tmp = q.pop(0)
        #     for prime in primes:
        #         if tmp*prime not in q:
        #             q.add(tmp*prime)
        #     cnt += 1
        # return q[0]

        m = len(primes)
        # dp[i] 代表第i+1个丑数
        dp = [inf] * n
        dp[0] = 1
        # indexes代表每个质因子现在应该跟哪个丑数相乘
        indexes = [0] * m
        for i in range(1, n):
            # 哪个质因子相乘的丑数将会变化
            changeIndex = 0
            for j in range(m):
                # 如果当前质因子乘它的丑数小于当前的丑数，更新当前丑数并更新变化坐标
                if primes[j] * dp[indexes[j]] < dp[i]:
                    changeIndex = j
                    dp[i] = primes[j] * dp[indexes[j]]
                # 如果相等直接变化，这样可以去重复
                elif primes[j] * dp[indexes[j]] == dp[i]:
                    indexes[j] += 1
            # 变化的坐标+1
            indexes[changeIndex] += 1
        return dp[-1]
