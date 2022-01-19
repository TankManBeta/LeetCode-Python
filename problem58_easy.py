# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2022/1/19 13:54
"""
"""
给你一个字符串 s，由若干单词组成，单词前后用一些空格字符隔开。返回字符串中最后一个单词的长度。
单词 是指仅由字母组成、不包含任何空格字符的最大子字符串。

输入：s = "Hello World"
输出：5

输入：s = "   fly me   to   the moon  "
输出：4

输入：s = "luffy is still joyboy"
输出：6
"""
"""
思路：直接去除头尾空格，然后split，返回最后一个单词长度即可
"""


class Solution(object):
    @staticmethod
    def length_of_last_word(s):
        """
        :type s: str
        :rtype: int
        """
        s1 = s.strip()
        s2 = s1.split()
        return len(s2[-1])
