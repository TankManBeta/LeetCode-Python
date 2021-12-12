# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2021/10/29 11:24
"""
"""
给你一个字符串s和一个字符规律p，请你来实现一个支持'.'和'*'的正则表达式匹配。
'.' 匹配任意单个字符
'*' 匹配零个或多个前面的那一个元素
所谓匹配，是要涵盖 整个字符串s的，而不是部分字符串。

输入：s = "aa" p = "a"
输出：false
解释："a"无法匹配"aa"整个字符串。

输入：s = "aa" p = "a*"
输出：true
解释：因为'*'代表可以匹配零个或多个前面的那一个元素, 在这里前面的元素就是'a'。因此，字符串"aa"可被视为'a'重复了一次。

输入：s = "ab" p = ".*"
输出：true
解释：".*"表示可匹配零个或多个（'*'）任意字符（'.'）。

输入：s = "aab" p = "c*a*b"
输出：true
解释：因为'*'表示零个或多个，这里'c'为0个, 'a'被重复一次。因此可以匹配字符串"aab"。

输入：s = "mississippi" p = "mis*is*p*."
输出：false
"""
"""
思路：只知道dp
"""


class Solution(object):
    @staticmethod
    def is_match(s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        m, n = len(s), len(p)

        def matches(i, j):
            if i == 0:
                return False
            if p[j - 1] == '.':
                return True
            return s[i - 1] == p[j - 1]

        f = [[False] * (n + 1) for _ in range(m + 1)]
        f[0][0] = True
        for i in range(m + 1):
            for j in range(1, n + 1):
                if p[j - 1] == '*':
                    f[i][j] |= f[i][j - 2]
                    if matches(i, j - 1):
                        f[i][j] |= f[i - 1][j]
                else:
                    if matches(i, j):
                        f[i][j] |= f[i - 1][j - 1]
        return f[m][n]
