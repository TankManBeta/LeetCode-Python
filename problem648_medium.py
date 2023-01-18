# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2023/1/17 17:24
"""
from typing import List

"""
在英语中，我们有一个叫做词根(root)的概念，可以词根后面添加其他一些词组成另一个较长的单词——我们称这个词为继承词(successor)。例如，
词根an，跟随着单词other(其他)，可以形成新的单词another(另一个)。现在，给定一个由许多词根组成的词典 dictionary 和一个用空格分隔
单词形成的句子 sentence。你需要将句子中的所有继承词用词根替换掉。如果继承词有许多可以形成它的词根，则用最短的词根替换它。
你需要输出替换之后的句子。

示例 1：
输入：dictionary = ["cat","bat","rat"], sentence = "the cattle was rattled by the battery"
输出："the cat was rat by the bat"

示例 2：
输入：dictionary = ["a","b","c"], sentence = "aadsfasf absbs bbab cadsfafs"
输出："a a b c"
"""
"""
思路：首先将 dictionary 中所有词根放入哈希集合中，然后对于 sentence 中的每个单词，由短至长遍历它所有的前缀，如果这个前缀出现在
哈希集合中，则我们找到了当前单词的最短词根，将这个词根替换原来的单词。最后返回重新拼接的句子。
"""


class Solution:
    @staticmethod
    def replaceWords(dictionary: List[str], sentence: str) -> str:
        dictionarySet = set(dictionary)
        words = sentence.split(' ')
        for i, word in enumerate(words):
            for j in range(1, len(words) + 1):
                if word[:j] in dictionarySet:
                    words[i] = word[:j]
                    break
        return ' '.join(words)
