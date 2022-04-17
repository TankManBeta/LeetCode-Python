# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2022/4/16 14:11
"""
from collections import Counter

"""
给定两个字符串 s 和 t ，编写一个函数来判断 t 是否是 s 的字母异位词。
注意：若 s 和 t 中每个字符出现的次数都相同，则称 s 和 t 互为字母异位词。

输入: s = "anagram", t = "nagaram"
输出: true

输入: s = "rat", t = "car"
输出: false
"""
"""
思路：
（1）直接排序，然后看两个是否相等
（2）统计字母出现次数
"""


class Solution(object):
    @staticmethod
    def isAnagram(s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        # return sorted(s) == sorted(t)
        return Counter(s) == Counter(t)
