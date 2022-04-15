# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2022/4/14 10:06
"""
"""
给你一个整数 n ，请你找出并返回第 n 个 丑数 。
丑数 就是只包含质因数 2、3 和/或 5 的正整数。

输入：n = 10
输出：12
解释：[1, 2, 3, 4, 5, 6, 8, 9, 10, 12] 是由前 10 个丑数组成的序列

输入：n = 1
输出：1
解释：1 通常被视为丑数
"""
"""
思路：
（1）小根堆，每次都把当前数字×2，×3，×5的放入堆中，同时使用集合去重
（2）动态规划，初始三个指针全都指向位置1，然后每一轮迭代都用当前指针指向位置的数去乘对应的数，然后比较当前选出来的和三个指针算出来
的是否相等，相等指针就++
"""


class Solution(object):
    @staticmethod
    def nthUglyNumber(n):
        """
        :type n: int
        :rtype: int
        """
        # factors = [2, 3, 5]
        # seen = {1}
        # heap = [1]
        # for i in range(n - 1):
        #     curr = heapq.heappop(heap)
        #     for factor in factors:
        #         nxt = curr * factor
        #         if nxt not in seen:
        #             seen.add(nxt)
        #             heapq.heappush(heap, nxt)
        # return heapq.heappop(heap)

        dp = [0] * (n + 1)
        dp[1] = 1
        p2 = p3 = p5 = 1
        for i in range(2, n + 1):
            num2, num3, num5 = dp[p2] * 2, dp[p3] * 3, dp[p5] * 5
            dp[i] = min(num2, num3, num5)
            if dp[i] == num2:
                p2 += 1
            if dp[i] == num3:
                p3 += 1
            if dp[i] == num5:
                p5 += 1
        return dp[n]
