# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2022/2/28 10:41
"""
"""
给定一个字符串 s 和一个字符串 t ，计算在 s 的子序列中 t 出现的个数。
字符串的一个 子序列 是指，通过删除一些（也可以不删除）字符且不干扰剩余字符相对位置所组成的新字符串。
（例如，"ACE" 是 "ABCDE" 的一个子序列，而 "AEC" 不是）
题目数据保证答案符合 32 位带符号整数范围。

输入：s = "rabbbit", t = "rabbit"
输出：3

输入：s = "babgbag", t = "bag"
输出：5
"""
"""
思路：
（1）dfs超时
（2）算所有的组合，然后统计，也超时
（3）dp，s[i:]表示s从下标i到末尾的子字符串，t[j:]表示t从下标j到末尾的子字符串。边界情况：当j=n时，t[j:]为空字符串，
由于空字符串是任何字符串的子序列，因此0≤i≤m-1，dp[i][n]=1；当i=m且j<n时，s[i:]为空字符串，t[j:]为非空字符串，
由于非空字符串不是空字符串的子序列，因此对任意0≤j<n，有dp[m][j]=0。
当s[i]==t[j]时，dp[i][j]由两部分组成：
    如果s[i]和t[j]匹配，则考虑t[j+1:]作为s[i+1:]的子序列，子序列数为dp[i+1][j+1]；
    如果s[i]不和t[j]匹配，则考虑t[j:]作为s[i+1:]的子序列，子序列数为dp[i+1][j]。
    因此当s[i]=t[j]时，有dp[i][j]=dp[i+1][j+1]+dp[i+1][j]。
当s[i]!=t[j]时，此时只考虑t[j:]作为s[i+1:]的子序列，子序列数为dp[i+1][j]。因此当 s[i]!=t[j]时，有dp[i][j]=dp[i+1][j]。
"""


class Solution(object):
    @staticmethod
    def num_distinct(s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        # ans = 0
        # m = len(t)
        # for combination in combinations(s, m):
        #     if ''.join(combination) == t:
        #         ans += 1
        # return ans

        # self.ans = 0
        # m, n = len(s), len(t)
        # combination = list()

        # def dfs(index, count):
        #     if len(combination) == n:
        #         self.ans += 1
        #         return

        #     for i in range(index, m):
        #         if s[i] != t[count]:
        #             continue
        #         combination.append(s[i])
        #         dfs(i+1, count+1)
        #         combination.pop()
        # dfs(0, 0)
        # return self.ans

        m, n = len(s), len(t)
        if m < n:
            return 0
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(m + 1):
            dp[i][n] = 1
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if s[i] == t[j]:
                    dp[i][j] = dp[i + 1][j + 1] + dp[i + 1][j]
                else:
                    dp[i][j] = dp[i + 1][j]
        return dp[0][0]
