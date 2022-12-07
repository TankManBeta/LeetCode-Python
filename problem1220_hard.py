# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2022/12/6 17:18
"""
"""
给你一个整数 n，请你帮忙统计一下我们可以按下述规则形成多少个长度为 n 的字符串：
字符串中的每个字符都应当是小写元音字母（'a', 'e', 'i', 'o', 'u'）
    每个元音 'a' 后面都只能跟着 'e'
    每个元音 'e' 后面只能跟着 'a' 或者是 'i'
    每个元音 'i' 后面 不能 再跟着另一个 'i'
    每个元音 'o' 后面只能跟着 'i' 或者是 'u'
    每个元音 'u' 后面只能跟着 'a'
由于答案可能会很大，所以请你返回 模 10^9 + 7 之后的结果。

示例 1：
输入：n = 1
输出：5
解释：所有可能的字符串分别是："a", "e", "i" , "o" 和 "u"。

示例 2：
输入：n = 2
输出：10
解释：所有可能的字符串分别是："ae", "ea", "ei", "ia", "ie", "io", "iu", "oi", "ou" 和 "ua"。

示例 3：
输入：n = 5
输出：68
"""
"""
思路：
（1）dp，反过来想，下一个是a的话，他的前面只能是e、i和u，依次类推。递归方程就可以得到
（2）矩阵快速幂，f(n)=M×f(n-1)=M^{n-1}×f(1)
"""

# import numpy as np


class Solution:
    @staticmethod
    def countVowelPermutation(n: int) -> int:
        dp = [1, 1, 1, 1, 1]
        m = 10**9 + 7
        for _ in range(n-1):
            dp = [(dp[1]+dp[2]+dp[4])%m, (dp[0]+dp[2])%m, (dp[1]+dp[3])%m, dp[2]%m, (dp[2]+dp[3])%m]
        return sum(dp)%m

        # factor = np.mat([(0, 1, 0, 0, 0), (1, 0, 1, 0, 0), (1, 1, 0, 1, 1), (0, 0, 1, 0, 1), (1, 0, 0, 0, 0)],
        #                 np.dtype('O'))
        # res = np.mat([(1, 1, 1, 1, 1)], np.dtype('O'))
        # n -= 1
        # while n > 0:
        #     if n % 2 == 1:
        #         res = res * factor % 1000000007
        #     factor = factor * factor % 1000000007
        #     n = n // 2
        # return res.sum() % 1000000007
