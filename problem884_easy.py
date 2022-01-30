# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2022/1/30 14:25
"""
"""
句子 是一串由空格分隔的单词。每个 单词 仅由小写字母组成。
如果某个单词在其中一个句子中恰好出现一次，在另一个句子中却 没有出现 ，那么这个单词就是 不常见的 。
给你两个 句子 s1 和 s2 ，返回所有 不常用单词 的列表。返回列表中单词可以按 任意顺序 组织。

输入：s1 = "this apple is sweet", s2 = "this apple is sour"
输出：["sweet","sour"]

输入：s1 = "apple apple", s2 = "banana"
输出：["banana"]
"""
"""
思路：判断s1里每个单词是否在s1只出现一次并且在s2中没有出现，就是不常见单词
"""


class Solution(object):
    @staticmethod
    def uncommon_from_sentences(s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: List[str]
        """
        words1 = s1.split(' ')
        words2 = s2.split(' ')
        res = []
        for word in words1:
            if word not in words2 and words1.count(word) == 1:
                res.append(word)

        for word in words2:
            if word not in words1 and words2.count(word) == 1:
                res.append(word)

        return res
