# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2022/11/30 12:00
"""
"""
给定一种规律 pattern 和一个字符串 s ，判断 s 是否遵循相同的规律。
这里的 遵循 指完全匹配，例如， pattern 里的每个字母和字符串 s 中的每个非空单词之间存在着双向连接的对应规律。

示例1:
输入: pattern = "abba", s = "dog cat cat dog"
输出: true

示例 2:
输入:pattern = "abba", s = "dog cat cat fish"
输出: false

示例 3:
输入: pattern = "aaaa", s = "dog cat cat dog"
输出: false
"""
"""
思路：因为是双向匹配，所以使用双向哈希即可。
"""


class Solution:
    @staticmethod
    def wordPattern(pattern: str, s: str) -> bool:
        word2ch = dict()
        ch2word = dict()
        words = s.split()
        if len(pattern) != len(words):
            return False

        for ch, word in zip(pattern, words):
            if (word in word2ch and word2ch[word] != ch) or (ch in ch2word and ch2word[ch] != word):
                return False
            word2ch[word] = ch
            ch2word[ch] = word

        return True
