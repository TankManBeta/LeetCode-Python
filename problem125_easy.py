# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2022/3/3 10:15
"""
"""
给定一个字符串，验证它是否是回文串，只考虑字母和数字字符，可以忽略字母的大小写。
说明：本题中，我们将空字符串定义为有效的回文串。

输入: "A man, a plan, a canal: Panama"
输出: true
解释："amanaplanacanalpanama" 是回文串

输入: "race a car"
输出: false
解释："raceacar" 不是回文串
"""
"""
思路：全变成小写，然后只考虑字母和数字
"""


class Solution(object):
    @staticmethod
    def is_palindrome(s):
        """
        :type s: str
        :rtype: bool
        """
        res = []
        s = s.lower()
        for char in s:
            if 'a' <= char <= 'z' or '0' <= char <= '9':
                res.append(char)
        new_s = ''.join(res)
        return new_s == new_s[::-1]
