# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2023/6/13 21:26
"""
"""
请实现一个函数用来匹配包含'. '和'*'的正则表达式。模式中的字符'.'表示任意一个字符，而'*'表示它前面的字符可以出现任意次（含0次）。
在本题中，匹配是指字符串的所有字符匹配整个模式。例如，字符串"aaa"与模式"a.a"和"ab*ac*a"匹配，但与"aa.a"和"ab*a"均不匹配。

示例 1:
输入:
s = "aa"
p = "a"
输出: false
解释: "a" 无法匹配 "aa" 整个字符串。

示例 2:
输入:
s = "aa"
p = "a*"
输出: true
解释: 因为 '*' 代表可以匹配零个或多个前面的那一个元素, 在这里前面的元素就是 'a'。因此，字符串 "aa" 可被视为 'a' 重复了一次。

示例 3:
输入:
s = "ab"
p = ".*"
输出: true
解释: ".*" 表示可匹配零个或多个（'*'）任意字符（'.'）。

示例 4:
输入:
s = "aab"
p = "c*a*b"
输出: true
解释: 因为 '*' 表示零个或多个，这里 'c' 为 0 个, 'a' 被重复一次。因此可以匹配字符串 "aab"。

示例 5:
输入:
s = "mississippi"
p = "mis*is*p*."
输出: false
"""
"""
思路：动态规划，dp[0][0] = true： 代表两个空字符串能够匹配。dp[0][j] = dp[0][j - 2] 且 p[j - 1] = '*'： 首行 s 为空字符串，
因此当 p 的偶数位为 * 时才能够匹配（即让 p 的奇数位出现 0 次，保持 p 是空字符串）。因此，循环遍历字符串 p ，步长为 2（即只看偶数位）。
当 p[j - 1] = '*' 时， dp[i][j] 在当以下任一情况为 true 时等于 true ：
    dp[i][j - 2]： 即将字符组合 p[j - 2] * 看作出现 0 次时，能否匹配；
    dp[i - 1][j] 且 s[i - 1] = p[j - 2]: 即让字符 p[j - 2] 多出现 1 次时，能否匹配；
    dp[i - 1][j] 且 p[j - 2] = '.': 即让字符 '.' 多出现 1 次时，能否匹配；
当 p[j - 1] != '*' 时， dp[i][j] 在当以下任一情况为 true 时等于 true ：
    dp[i - 1][j - 1] 且 s[i - 1] = p[j - 1]： 字符串 s 的前 i-1 个字符和 p 的前 j -1个字符匹配, 且s的第i个字符等于p的第j个字符；
    dp[i - 1][j - 1] 且 p[j - 1] = '.'： 字符串 s 的前 i-1 个字符和 p 的前 j -1个字符匹配, 且p的第j个字符为'.'。
"""


class Solution:
    @staticmethod
    def isMatch(s: str, p: str) -> bool:
        m, n = len(s) + 1, len(p) + 1
        dp = [[False] * n for _ in range(m)]
        dp[0][0] = True
        for j in range(2, n, 2):
            dp[0][j] = dp[0][j - 2] and p[j - 1] == '*'
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i][j - 2] or dp[i - 1][j] and (s[i - 1] == p[j - 2] or p[j - 2] == '.') \
                           if p[j - 1] == '*' else \
                           dp[i - 1][j - 1] and (p[j - 1] == '.' or s[i - 1] == p[j - 1])
        return dp[-1][-1]
