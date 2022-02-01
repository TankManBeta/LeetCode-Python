# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2022/1/31 16:55
"""
"""
给你两个单词 word1 和 word2， 请返回将 word1 转换成 word2 所使用的最少操作数  。
你可以对一个单词进行如下三种操作：
    插入一个字符
    删除一个字符
    替换一个字符

输入：word1 = "horse", word2 = "ros"
输出：3
解释：
horse -> rorse (将 'h' 替换为 'r')
rorse -> rose (删除 'r')
rose -> ros (删除 'e')

输入：word1 = "intention", word2 = "execution"
输出：5
解释：
intention -> inention (删除 't')
inention -> enention (将 'i' 替换为 'e')
enention -> exention (将 'n' 替换为 'x')
exention -> exection (将 'n' 替换为 'c')
exection -> execution (插入 'u')
"""
"""
思路：用dp，dp[i][j]表示word1的前i个变成word2的前j个所用的最少步数，考虑到字符串为空的情况，加入了''，初始化的时候第一行为
空字符串变成word2，即增加操作，第一列为word1变成空串的情况，即删除操作。dp[i][j]=min(dp[i-1][j-1],dp[i-1][j],dp[i][j-1])+1，
如果word1[i-1]==word2[j-1]，说明当前字符相同，所以只需操作前面的字符即可，即dp[i][j]=dp[i-1][j-1]
"""


class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        m = len(word1)
        n = len(word2)

        if m * n == 0:
            return m + n

        dp = [[0 for _ in range(n+1)] for _ in range(m+1)]

        for i in range(0, m+1):
            dp[i][0] = i

        for j in range(0, n+1):
            dp[0][j] = j

        for i in range(1, m+1):
            for j in range(1, n+1):
                dp[i][j] = min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1]) + 1
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1]

        return dp[m][n]