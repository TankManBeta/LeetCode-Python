# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2022/2/18 12:07
"""
"""
给你一个整数 n ，求恰由 n 个节点组成且节点值从 1 到 n 互不相同的 二叉搜索树 有多少种？返回满足题意的二叉搜索树的种数。

输入：n = 3
输出：5

输入：n = 1
输出：1
"""
"""
思路：假设 n 个节点存在二叉排序树的个数是G(n)，令f(i)为以i为根的二叉搜索树的个数，则G(n)=f(1)+f(2)+f(3)+f(4)+...+f(n)
当 i 为根节点时，其左子树节点个数为 i-1 个，右子树节点为 n-i，则f(i)=G(i−1)∗G(n−i)。综合两个公式可以得到卡特兰数公式
G(n)=G(0)∗G(n−1)+G(1)∗(n−2)+...+G(n−1)∗G(0)
"""


class Solution(object):
    @staticmethod
    def num_trees(n):
        """
        :type n: int
        :rtype: int
        """
        dp = [0 for _ in range(n + 1)]
        dp[0] = 1
        dp[1] = 1

        for i in range(2, n + 1):
            for j in range(1, i + 1):
                dp[i] += dp[j - 1] * dp[i - j]
        return dp[n]
