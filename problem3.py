# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2021/10/28 10:33
"""
"""
给定一个字符串s，请你找出其中不含有重复字符的最长子串的长度。

输入: s = "abcabcbb"
输出: 3 
解释: 因为无重复字符的最长子串是"abc"，所以其长度为3。

输入: s = "bbbbb"
输出: 1
解释: 因为无重复字符的最长子串是"b"，所以其长度为1。

输入: s = "pwwkew"
输出: 3
解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。请注意，你的答案必须是子串的长度，"pwke" 是一个子序列，不是子串。

输入: s = ""
输出: 0
"""
"""
思路：
max_len为返回的长度。建一个列表，循环整个字符串，如果列表中不存在当前字符，直接将当前字符放入列表中，比较max_len和列表长度，
选择更新与否。如果列表中存在当前字符，则定位在列表中的位置，先将当前字符加入列表，再从刚刚定位到的位置的下一个开始切片。
"""


class Solution(object):
    @staticmethod
    def length_of_longest_substring(s):
        """
        :type s: str
        :rtype: int
        """
        max_len = 0
        substr_list = []
        for index, value in enumerate(s):
            if s[index] in substr_list:
                i = substr_list.index(s[index])
                substr_list.append(s[index])
                substr_list = substr_list[i+1:]
            else:
                substr_list.append(s[index])
                if len(substr_list) > max_len:
                    max_len = len(substr_list)
        return max_len
