# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2022/3/1 11:34
"""
"""
给定一个三角形 triangle ，找出自顶向下的最小路径和。
每一步只能移动到下一行中相邻的结点上。相邻的结点 在这里指的是下标与上一层结点下标相同或者等于上一层结点下标+1的两个结点。
也就是说，如果正位于当前行的下标 i ，那么下一步可以移动到下一行的下标 i 或 i + 1 。

输入：triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]
输出：11

输入：triangle = [[-10]]
输出：-10
"""
"""
思路：
（1）dfs，超时
（2）dp，dp[i][j]是指从头到(i,j)位置需要的最小距离，dp[i][j] = min(dp[i-1][j-1], dp[i-1][j]) + triangle[i][j]
（3）优化，使用两个长度为n的数组，然后就映射即可，O(2n)=O(n)
（3）继续优化，使用一个数组，从后往前计算，这样前面的还是上一轮为值，O(n)
"""


class Solution(object):
    @staticmethod
    def minimum_total(triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        # n = len(triangle)
        # dp = [[0]*n for _ in range(n)]
        # dp[0][0] = triangle[0][0]
        # for i in range(1, n):
        #     dp[i][0] = dp[i-1][0] + triangle[i][0]
        #     for j in range(1, i):
        #         dp[i][j] = min(dp[i-1][j-1], dp[i-1][j]) + triangle[i][j]
        #     dp[i][i] = dp[i-1][i-1] + triangle[i][i]
        # return min(dp[n-1])

        # n = len(triangle)
        # dp = [[0]*n for _ in range(2)]
        # dp[0][0] = triangle[0][0]
        # for i in range(1, n):
        #     cur, pre = i%2, 1-i%2
        #     dp[cur][0] = dp[pre][0] + triangle[i][0]
        #     for j in range(1, i):
        #         dp[cur][j] = min(dp[pre][j-1], dp[pre][j]) + triangle[i][j]
        #     dp[cur][i] = dp[pre][i-1] + triangle[i][i]
        # return min(dp[(n-1)%2])

        n = len(triangle)
        dp = [0] * n
        dp[0] = triangle[0][0]
        for i in range(1, n):
            dp[i] = dp[i - 1] + triangle[i][i]
            for j in range(i - 1, 0, -1):
                dp[j] = min(dp[j - 1], dp[j]) + triangle[i][j]
            dp[0] += triangle[i][0]
        return min(dp)
