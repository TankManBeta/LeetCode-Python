# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2023/6/30 21:23
"""
"""
句子 是由单个空格分隔的一组单词，且不含前导或尾随空格。

例如，"Hello World"、"HELLO"、"hello world hello world" 都是符合要求的句子。
单词 仅 由大写和小写英文字母组成。且大写和小写字母会视作不同字符。

如果句子满足下述全部条件，则认为它是一个 回环句 ：

单词的最后一个字符和下一个单词的第一个字符相等。
最后一个单词的最后一个字符和第一个单词的第一个字符相等。
例如，"leetcode exercises sound delightful"、"eetcode"、"leetcode eats soul" 都是回环句。然而，"Leetcode is cool"、"happy 
Leetcode"、"Leetcode" 和 "I like Leetcode" 都 不 是回环句。
给你一个字符串 sentence ，请你判断它是不是一个回环句。如果是，返回 true ；否则，返回 false 。

示例 1：
输入：sentence = "leetcode exercises sound delightful"
输出：true
解释：句子中的单词是 ["leetcode", "exercises", "sound", "delightful"] 。
- leetcode 的最后一个字符和 exercises 的第一个字符相等。
- exercises 的最后一个字符和 sound 的第一个字符相等。
- sound 的最后一个字符和 delightful 的第一个字符相等。
- delightful 的最后一个字符和 leetcode 的第一个字符相等。
这个句子是回环句。

示例 2：
输入：sentence = "eetcode"
输出：true
解释：句子中的单词是 ["eetcode"] 。
- eetcode 的最后一个字符和 eetcode 的第一个字符相等。
这个句子是回环句。

示例 3：
输入：sentence = "Leetcode is cool"
输出：false
解释：句子中的单词是 ["Leetcode", "is", "cool"] 。
- Leetcode 的最后一个字符和 is 的第一个字符 不 相等。 
这个句子 不 是回环句。
"""
"""
思路：
（1）分隔单词然后模拟
（2）直接模拟，看空格前后的单词是否一样
"""


class Solution:
    @staticmethod
    def isCircularSentence(sentence: str) -> bool:
        # words = sentence.split()
        # n = len(words)
        # if n == 1:
        #     return words[0][0] == words[0][-1]
        # for i in range(n-1):
        #     if words[i][-1] != words[i+1][0]:
        #         return False
        # return words[-1][-1] == words[0][0]

        if sentence[-1] != sentence[0]:
            return False
        for i, c in enumerate(sentence):
            if c == ' ':
                if sentence[i-1] != sentence[i+1]:
                    return False
        return True
