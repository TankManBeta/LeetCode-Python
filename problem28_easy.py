# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2021/12/3 11:43
"""
"""
给你两个字符串 haystack 和 needle ，请你在 haystack 字符串中找出 needle 字符串出现的第一个位置（下标从 0 开始）。
如果不存在，则返回  -1 。

说明：
当 needle 是空字符串时，我们应当返回什么值呢？这是一个在面试中很好的问题。
对于本题而言，当 needle 是空字符串时我们应当返回 0 。这与 C 语言的 strstr() 以及 Java 的 indexOf() 定义相符。

输入：haystack = "hello", needle = "ll"
输出：2

输入：haystack = "aaaaa", needle = "bba"
输出：-1

输入：haystack = "", needle = ""
输出：0
"""
"""
思路：
从头遍历haystack，每次取needle_len个出来比较，相等就返回，不相等就继续
"""


class Solution(object):
    @staticmethod
    def str_str(haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        hay_len = len(haystack)
        needle_len = len(needle)
        if needle_len == 0:
            return 0
        if needle_len > hay_len:
            return -1
        index = -1
        for i in range(0, hay_len):
            if i + needle_len > hay_len:
                break
            if haystack[i:i+needle_len] == needle:
                index = i
                break
            else:
                continue
        return index
