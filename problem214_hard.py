# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2022/4/6 9:53
"""
"""
给定一个字符串 s，你可以通过在字符串前面添加字符将其转换为回文串。找到并返回可以用这种方式转换的最短回文串。

输入：s = "aacecaaa"
输出："aaacecaaa"

输入：s = "abcd"
输出："dcbabcd"
"""
"""
思路：
（1）字符串哈希，我们要在s前面添加s'使得新串成为回文串，s'长度肯定小于s，因为我们必然可以将s从第一个字符开始倒序，然后放入s的开
头，我们将s微分两个部分，一个部分记为s1，已经是回文串，剩下的s2，经过倒序之后放到前面。
（2）KMP算法求最长公共前缀，计算KMP算法所需要的next数组，数组每一位为target字符串中对应的位置前（包括此字符，但后缀不包括
target首个字符）子字符串中，公共前后缀的长度e.g. target = abaakkabak next = 0011001230
"""


class Solution(object):
    @staticmethod
    def shortestPalindrome(s):
        """
        :type s: str
        :rtype: str
        """
        # n = len(s)
        # base, mod = 131, 10**9 + 7
        # left = right = 0
        # mul = 1
        # best = -1
        # for i in range(n):
        #     left = (left * base + ord(s[i])) % mod
        #     right = (right + mul * ord(s[i])) % mod
        #     if left == right:
        #         best = i
        #     mul = mul * base % mod
        # add = ("" if best == n - 1 else s[best+1:])
        # return add[::-1] + s

        n = len(s)
        fail = [-1] * n
        for i in range(1, n):
            j = fail[i - 1]
            while j != -1 and s[j + 1] != s[i]:
                j = fail[j]
            if s[j + 1] == s[i]:
                fail[i] = j + 1
        best = -1
        for i in range(n - 1, -1, -1):
            while best != -1 and s[best + 1] != s[i]:
                best = fail[best]
            if s[best + 1] == s[i]:
                best += 1
        add = ("" if best == n - 1 else s[best+1:])
        return add[::-1] + s
