# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2021/10/28 15:47
"""
"""
给你一个字符串s，找到s中最长的回文子串。

输入：s = "babad"
输出："bab"
解释："aba" 同样是符合题意的答案

输入：s = "cbbd"
输出："bb

输入：s = "a"
输出："a"

输入：s = "ac"
输出："a"
"""
"""
思路：
根据回文串的特性，选取中间一个为中心点或者中心两个为中心点，向两边扩散即可
"""


class Solution(object):
    @staticmethod
    def longest_palindrome(s):
        """
        :type s: str
        :rtype: str
        """
        result_str = ""
        str_length = len(s)
        for i in range(0, str_length):
            left, right = i, i
            while left >= 0 and right < str_length:
                if s[left] != s[right]:
                    break
                else:
                    if len(result_str) < (right + 1 - left):
                        result_str = s[left: right + 1]
                    left -= 1
                    right += 1
        if str_length >= 2:
            for i in range(0, str_length):
                left, right = i, i + 1
                while left >= 0 and right < str_length:
                    if s[left] != s[right]:
                        break
                    else:
                        if len(result_str) < (right + 1 - left):
                            result_str = s[left: right + 1]
                        left -= 1
                        right += 1
        return result_str
