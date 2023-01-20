# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2023/1/19 19:40
"""
"""
给定一个字符串 s，返回 s 中不同的非空「回文子序列」个数 。
通过从 s 中删除 0 个或多个字符来获得子序列。
如果一个字符序列与它反转后的字符序列一致，那么它是「回文字符序列」。
如果有某个 i , 满足 ai != bi ，则两个序列 a1, a2, ... 和 b1, b2, ... 不同。
注意：
结果可能很大，你需要对 109 + 7 取模 。

示例 1：
输入：s = 'bccb'
输出：6
解释：6 个不同的非空回文子字符序列分别为：'b', 'c', 'bb', 'cc', 'bcb', 'bccb'。
注意：'bcb' 虽然出现两次但仅计数一次。

示例 2：
输入：s = 'abcdabcdabcdabcdabcdabcdabcdabcddcbadcbadcbadcbadcbadcbadcbadcba'
输出：104860361
解释：共有 3104860382 个不同的非空回文子序列，104860361 对 109 + 7 取模后的值。
"""
"""
思路：动态规划（使用三维数组）。
显然每一个「回文序列」都满足开头和结尾的字符相同。那么我们设给定字符串为 s，长度为 n，状态 dp(x,i,j) 表示在字符串区间 s[i:j] 
中以字符 x 为开头和结尾的不同「回文序列」总数，其中 s[i:j] 表示字符串 s 从下标 i 到下标 j 的子串（包含下标 i 和下标 j）。
那么最终我们需要求的答案就转化为了 (∑_{i=0}^{C}dp(xi,0,n−1))mod1000000007，其中 xi∈S，S 为题目给定的的字符集合，C 为该字符
集合的大小。
我们思考如何求解各个状态：
当 s[i]=x 且 s[j]=x 时，那么对于 s[i+1:j−1] 中的任意一个「回文序列」在头尾加上字符 x 都会生成一个新的以字符 x 为开头结尾的
「回文序列」，并加上 xx 和 x 两个单独的「回文序列」。下式中，由于 xk不同的「回文序列」一定互不相同，因此可以直接累加，无需考虑
去重。dp(x,i,j)=2+∑_{k=0}^{C}dp(xk,i+1,j−1)
当 s[i]=x 且 s[j]≠x 时，那么 dp(x,i,j) 等价于 dp(x,i,j−1)。dp(x,i,j)=dp(x,i,j−1)
当 s[i]≠x 且 s[j]=x 时，那么 dp(x,i,j) 等价于 dp(x,i+1,j)。dp(x,i,j)=dp(x,i+1,j)
当 s[i]≠x 且 s[j]≠x 时，那么 dp(x,i,j) 等价于 dp(x,i+1,j−1)。dp(x,i,j)=dp(x,i+1,j−1)
"""


class Solution:
    @staticmethod
    def countPalindromicSubsequences(s: str) -> int:
        MOD = 10 ** 9 + 7
        n = len(s)
        dp = [[[0] * n for _ in range(n)] for _ in range(4)]
        for i, c in enumerate(s):
            dp[ord(c) - ord('a')][i][i] = 1

        for sz in range(2, n + 1):
            for j in range(sz - 1, n):
                i = j - sz + 1
                for k, c in enumerate("abcd"):
                    if s[i] == c and s[j] == c:
                        dp[k][i][j] = (2 + sum(d[i + 1][j - 1] for d in dp)) % MOD
                    elif s[i] == c:
                        dp[k][i][j] = dp[k][i][j - 1]
                    elif s[j] == c:
                        dp[k][i][j] = dp[k][i + 1][j]
                    else:
                        dp[k][i][j] = dp[k][i + 1][j - 1]
        return sum(d[0][n - 1] for d in dp) % MOD
