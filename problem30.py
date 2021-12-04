# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2021/12/4 16:46
"""
"""
给定一个字符串 s 和一些 长度相同 的单词 words 。找出 s 中恰好可以由 words 中所有单词串联形成的子串的起始位置。
注意子串要与 words 中的单词完全匹配，中间不能有其他字符 ，但不需要考虑 words 中单词串联的顺序。

输入：s = "barfoothefoobarman", words = ["foo","bar"]
输出：[0,9]
解释：
从索引 0 和 9 开始的子串分别是 "barfoo" 和 "foobar" 。
输出的顺序不重要, [9,0] 也是有效答案。

输入：s = "wordgoodgoodgoodbestword", words = ["word","good","best","word"]
输出：[]

输入：s = "barfoofoobarthefoobarman", words = ["bar","foo","the"]
输出：[6,9,12]
"""
"""
思路：
（1）全排列words，构成单词串联成的所有可能集合，然后在s中匹配，会超时
（2）看完评论，每次取k=len(words)*len(words[0])个，然后每len(words[0])个进行切片，构成候选列表，
然后比对words和候选列表里的单词是否相同，相同就把start加入结果集合，否则就start++，end++
"""


class Solution(object):
    @staticmethod
    def find_sub_string(s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        len_words = len(words)
        len_word = len(words[0])
        len_window = len(words) * len(words[0])
        len_s = len(s)
        start = 0
        end = len_window - 1
        res_list = []
        while end < len_s:
            option_list = [s[start + len_word * i: start + len_word * (i+1)] for i in range(0, len_words)]
            flag = 1
            for item in words:
                if item not in option_list:
                    flag = 0
                    break
                else:
                    option_list.remove(item)
            if flag == 1:
                res_list.append(start)
            start += 1
            end += 1
        return res_list
