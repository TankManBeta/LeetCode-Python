# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2023/3/27 11:18
"""
"""
给定两个字符串 text1 和 text2，返回这两个字符串的最长 公共子序列 的长度。如果不存在 公共子序列 ，返回 0 。
一个字符串的 子序列 是指这样一个新的字符串：它是由原字符串在不改变字符的相对顺序的情况下删除某些字符（也可以不删除任何字符）后组成的新字符串。
例如，"ace" 是 "abcde" 的子序列，但 "aec" 不是 "abcde" 的子序列。
两个字符串的 公共子序列 是这两个字符串所共同拥有的子序列。

示例 1：
输入：text1 = "abcde", text2 = "ace" 
输出：3  
解释：最长公共子序列是 "ace" ，它的长度为 3 。

示例 2：
输入：text1 = "abc", text2 = "abc"
输出：3
解释：最长公共子序列是 "abc" ，它的长度为 3 。

示例 3：
输入：text1 = "abc", text2 = "def"
输出：0
解释：两个字符串没有公共子序列，返回 0 。
"""
"""
思路：动态规划，涉及到两个字符串的比较，通常我们的做法都是设置两个指针进行遍历操作；而两个指针当前走到哪以及当前已经记录的公共
子序列长度，我们可以采取一个二维dp记录。若当前i，j指向的字符相同，则一定在LCS中，指针i，j同时移动，即有：dp[i][j] = dp[i-1][j-1]+1;
若当前i，j指向的字符不相同，则i，j指向的字符至少有一个不在LCS中，获取前面子问题的最大解：dp[i][j] = max(dp[i-1][j],dp[i][j-1])
"""


class Solution:
    @staticmethod
    def longestCommonSubsequence(text1: str, text2: str) -> int:
        m, n = len(text1), len(text2)
        dp = [[0 for _ in range(n+1)] for _ in range(m+1)]
        for i in range(1, m+1):
            for j in range(1, n+1):
                if text1[i - 1] == text2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        return dp[m][n]
