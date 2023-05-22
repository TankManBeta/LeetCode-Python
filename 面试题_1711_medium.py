# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2023/2/1 20:30
"""
from typing import List

"""
有个内含单词的超大文本文件，给定任意两个不同的单词，找出在这个文件中这两个单词的最短距离(相隔单词数)。如果寻找过程在这个文件中
会重复多次，而每次寻找的单词不同，你能对此优化吗?

示例：
输入：words = ["I","am","a","student","from","a","university","in","a","city"], word1 = "a", word2 = "student"
输出：1
"""
"""
思路：从左到右遍历数组 words，当遍历到 word1 时，如果已经遍历的单词中存在 word2，为了计算最短距离，应该取最后一个已经遍历到的 
word2 所在的下标，计算和当前下标的距离。同理，当遍历到 word2 时，应该取最后一个已经遍历到的 word1 所在的下标，计算和当前下标的
距离。
"""


class Solution:
    @staticmethod
    def findClosest(words: List[str], word1: str, word2: str) -> int:
        ans = len(words)
        index1, index2 = -1, -1
        for i, word in enumerate(words):
            if word == word1:
                index1 = i
            elif word == word2:
                index2 = i
            if index1 >= 0 and index2 >= 0:
                ans = min(ans, abs(index1 - index2))
        return ans
