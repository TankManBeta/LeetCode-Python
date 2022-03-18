# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2022/3/17 9:51
"""
"""
给出一个字符串数组 words 组成的一本英语词典。返回 words 中最长的一个单词，该单词是由 words 词典中其他单词逐步添加一个字母组成。
若其中有多个可行的答案，则返回答案中字典序最小的单词。若无答案，则返回空字符串。

输入：words = ["w","wo","wor","worl", "world"]
输出："world"
解释： 单词"world"可由"w", "wo", "wor", 和 "worl"逐步添加一个字母组成。

输入：words = ["a", "banana", "app", "appl", "ap", "apply", "apple"]
输出："apple"
解释："apply" 和 "apple" 都能由词典中的单词组成。但是 "apple" 的字典序小于 "apply" 
"""
"""
思路：
（1）按照长度升序，字典序降序的规则给words排序，然后依次遍历，看除最后一位之外组成的单词在不在set中，在的话就更新set和结果
（2）字典树，每一层26个节点，一个字符给一层的对应位置赋值，字母遍历结束is_end变为True
"""


class TrieNode:
    def __init__(self):
        self.is_end = False
        self.children = [None] * 26

    def insert(self, string):
        node = self
        for ch in string:
            index = ord(ch) - ord('a')
            if node.children[index] is None:
                node.children[index] = TrieNode()
            node = node.children[index]
        node.is_end = True

    def search(self, string):
        node = self
        for ch in string:
            index = ord(ch) - ord('a')
            if node.children[index] is None or not node.children[index].is_end:
                return False
            node = node.children[index]
        return True


class Solution(object):
    @staticmethod
    def longest_word(words):
        """
        :type words: List[str]
        :rtype: str
        """
        # words = sorted(words, key=lambda x:(-len(x), x), reverse=True)
        # hash_set = {""}
        # ans = ""
        # for word in words:
        #     if word[0:-1] in hash_set:
        #         ans = word
        #         hash_set.add(word)
        # return ans

        t = TrieNode()
        for word in words:
            t.insert(word)
        longest = ""
        for word in words:
            if t.search(word) and (len(word) > len(longest) or len(word) == len(longest) and word < longest):
                longest = word
        return longest
