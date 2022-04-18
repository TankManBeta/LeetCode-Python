# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2022/4/17 13:50
"""
"""
给定一个段落 (paragraph) 和一个禁用单词列表 (banned)。返回出现次数最多，同时不在禁用列表中的单词。
题目保证至少有一个词不在禁用列表中，而且答案唯一。
禁用列表中的单词用小写字母表示，不含标点符号。段落中的单词不区分大小写。答案都是小写字母。

输入: 
paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
banned = ["hit"]
输出: "ball"
解释: 
"hit" 出现了3次，但它是一个禁用的单词。
"ball" 出现了2次 (同时没有其他单词出现2次)，所以它是段落里出现次数最多的，且不在禁用列表中的单词。 
注意，所有这些单词在段落里不区分大小写，标点符号需要忽略（即使是紧挨着单词也忽略， 比如 "ball,"）， 
"hit"不是最终的答案，虽然它出现次数更多，但它在禁用单词列表中。
"""
"""
思路：预处理+统计词频
"""


class Solution(object):
    @staticmethod
    def mostCommonWord(paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """
        ops = [".", ",", ";", "!", "?", "'"]
        paragraph = paragraph.lower()
        for op in ops:
            paragraph = paragraph.replace(op, ' ')
        words = paragraph.split()
        print(words)
        word_dict = {}
        ans = ""
        count = 0
        for word in words:
            if word not in banned:
                word_dict[word] = word_dict.get(word, 0) + 1
                if word_dict[word] > count:
                    ans = word
                    count = word_dict[word]
        return ans
