# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2022/3/7 10:55
"""
"""
给你一个字符串 s，请你将 s 分割成一些子串，使每个子串都是回文。
返回符合要求的 最少分割次数 。

输入：s = "aab"
输出：1
解释：只需一次分割就可将 s 分割成 ["aa","b"] 这样两个回文子串。

输入：s = "a"
输出：0

输入：s = "ab"
输出：1
"""
"""
思路：双dp，第一次dp中dp[i][j]表示i到j是否是回文串，只有一个字符或者 s[i-1] == s[j-1] 且 j-i == 1(仅有两个字符) || 
dp[i+1][j-1]() 才是回文；第二次dp记录最小切割次数，如果已经是回文串则切割次数为0，否则找到一个左端点j，使j到i是回文，
那么有f[i] = f[j-1]+1，每次取小即可
"""


class Solution(object):
    @staticmethod
    def min_cut(s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        is_pal = [[False for _ in range(n+1)] for _ in range(n+1)]
        for right in range(1, n+1):
            for left in range(right, 0, -1):
                if left == right:
                    is_pal[left][right] = True
                else:
                    if s[left-1] == s[right-1]:
                        if right == left+1 or is_pal[left+1][right-1]:
                            is_pal[left][right] = True
        dp = [0 for _ in range(n+1)]
        for i in range(1, n+1):
            if is_pal[1][i]:
                dp[i] = 0
            else:
                dp[i] = i-1
                for j in range(1, i+1):
                    if is_pal[j][i]:
                        dp[i] = min(dp[i], dp[j-1]+1)
        return dp[-1]
