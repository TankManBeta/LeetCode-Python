# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2023/1/20 19:43
"""
from typing import List

"""
设计一个包含一些单词的特殊词典，并能够通过前缀和后缀来检索单词。
实现 WordFilter 类：
    WordFilter(string[] words) 使用词典中的单词 words 初始化对象。
    f(string pref, string suff) 返回词典中具有前缀 prefix 和后缀 suff 的单词的下标。如果存在不止一个满足要求的下标，返回其中 
    最大的下标 。如果不存在这样的单词，返回 -1 。

示例：
输入
["WordFilter", "f"]
[[["apple"]], ["a", "e"]]
输出
[null, 0]
解释
WordFilter wordFilter = new WordFilter(["apple"]);
wordFilter.f("a", "e"); // 返回 0 ，因为下标为 0 的单词：前缀 prefix = "a" 且 后缀 suff = "e" 。
"""
"""
思路：预先计算出每个单词的前缀后缀组合可能性，用特殊符号连接，作为键，对应的最大下标作为值保存入哈希表。检索时，同样用特殊符号
连接前后缀，在哈希表中进行搜索。
"""


class WordFilter:

    def __init__(self, words: List[str]):
        self.d = {}
        for i, word in enumerate(words):
            m = len(word)
            for prefixLength in range(1, m + 1):
                for suffixLength in range(1, m + 1):
                    self.d[word[:prefixLength] + '#' + word[-suffixLength:]] = i

    def f(self, prefix: str, suffix: str) -> int:
        return self.d.get(prefix + '#' + suffix, -1)

# Your WordFilter object will be instantiated and called as such:
# obj = WordFilter(words)
# param_1 = obj.f(prefix,suffix)
