# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2022/3/6 13:11
"""
"""
给你一个字符串 s，请你将 s 分割成一些子串，使每个子串都是 回文串 。返回 s 所有可能的分割方案。
回文串 是正着读和反着读都一样的字符串。

输入：s = "aab"
输出：[["a","a","b"],["aa","b"]]

输入：s = "a"
输出：[["a"]]
"""
"""
思路：dfs即可，从端点开始，看到s[start:i]是否是回文串，然后从i开始继续下一层
"""


class Solution(object):
    @staticmethod
    def partition(s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        res = []
        n = len(s)
        combination = []
        combinations = []

        def is_palindrome(string):
            return string == string[::-1]

        def dfs(start, end):
            if start == end - 1:
                combinations.append(combination[:])
                return
            for i in range(start + 1, end):
                if is_palindrome(s[start:i]):
                    combination.append(s[start:i])
                    dfs(i, end)
                    combination.pop()

        dfs(0, n + 1)
        return combinations
