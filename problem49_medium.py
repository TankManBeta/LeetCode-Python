# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2021/12/20 9:39
"""
"""
给你一个字符串数组，请你将 字母异位词 组合在一起。可以按任意顺序返回结果列表。
字母异位词是由重新排列源单词的字母得到的一个新单词，所有源单词中的字母通常恰好只用一次。

输入: words = ["eat", "tea", "tan", "ate", "nat", "bat"]
输出: [["bat"],["nat","tan"],["ate","eat","tea"]]

输入: words = [""]
输出: [[""]]

输入: words = ["a"]
输出: [["a"]]
"""
"""
思路：一开始以为每个字母异位词只出现一次，想法是直接对每个单词dfs，然后在words里删掉存在的单词即可，后来发现题意理解错误。
首先对words里的word排序，把排序后的新单词作为dict的键，然后对每个单词排序，看是否在键里即可，最后返回dict.values()的列表
"""


class Solution(object):
    @staticmethod
    def group_anagrams(words):
        """
        :type words: List[str]
        :rtype: List[List[str]]
        """
        res_dict = {}
        for word in words:
            sorted_word = ''.join(sorted(word))
            temp_list = res_dict.get(sorted_word, [])
            temp_list.append(word)
            res_dict[sorted_word] = temp_list
        res_list = list(res_dict.values())
        return res_list
