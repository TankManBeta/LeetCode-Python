# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2023/3/27 9:59
"""
"""
给你两个字符串 s 和 t ，请你找出 s 中的非空子串的数目，这些子串满足替换 一个不同字符 以后，是 t 串的子串。换言之，
请你找到 s 和 t 串中 恰好 只有一个字符不同的子字符串对的数目。
比方说， "computer" and "computation" 只有一个字符不同： 'e'/'a' ，所以这一对子字符串会给答案加 1 。
请你返回满足上述条件的不同子字符串对数目。
一个 子字符串 是一个字符串中连续的字符。 

示例 1：
输入：s = "aba", t = "baba"
输出：6
解释：以下为只相差 1 个字符的 s 和 t 串的子字符串对：
("aba", "baba")
("aba", "baba")
("aba", "baba")
("aba", "baba")
("aba", "baba")
("aba", "baba")
加粗部分分别表示 s 和 t 串选出来的子字符串。

示例 2：
输入：s = "ab", t = "bb"
输出：3
解释：以下为只相差 1 个字符的 s 和 t 串的子字符串对：
("ab", "bb")
("ab", "bb")
("ab", "bb")
加粗部分分别表示 s 和 t 串选出来的子字符串。

示例 3：
输入：s = "a", t = "a"
输出：0

示例 4：
输入：s = "abe", t = "bbc"
输出：10
"""
"""
思路：
（1）枚举两个子串的左端点和长度，如果diff==1，则ans++；如果diff>1，则说明不止一个字符不相同，则break循环，枚举下一个端点。
（2）动态规划，可以预处理出以每个位置 (i,j) 结尾的最长相同后缀的长度，以及以每个位置 (i,j) 开头的最长相同前缀的长度，分别记录
在数组 f 和 g 中。接下来，我们枚举字符串 s 和 t 中不同的那个字符位置 (i,j)，那么以该位置为中心的满足条件的子串对数目为 
(f[i][j]+1)×(g[i+1][j+1]+1)，累加到答案中即可。
"""


class Solution:
    @staticmethod
    def countSubstrings(s: str, t: str) -> int:
        # m, n = len(s), len(t)
        # ans = 0
        # for i in range(m):
        #     for j in range(n):
        #         k = 0
        #         diff = 0
        #         while i + k < m and j+k < n:
        #             if s[i+k] != t[j+k]:
        #                 diff += 1
        #             if diff == 1:
        #                 ans += 1
        #             if diff > 1:
        #                 break
        #             k += 1
        # return ans

        ans = 0
        m, n = len(s), len(t)
        l, r = [[0 for _ in range(n + 1)] for _ in range(m + 1)], [[0 for _ in range(n + 1)] for _ in range(m + 1)]
        for i, a in enumerate(s, 1):
            for j, b in enumerate(t, 1):
                if a == b:
                    l[i][j] = l[i - 1][j - 1] + 1
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if s[i] == t[j]:
                    r[i][j] = r[i + 1][j + 1] + 1
                else:
                    ans += (l[i][j] + 1) * (r[i + 1][j + 1] + 1)
        return ans
