# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2023/1/16 20:17
"""
"""
一个句子是由一些单词与它们之间的单个空格组成，且句子的开头和结尾没有多余空格。比方说，"Hello World" ，"HELLO" ，"hello world 
hello world" 都是句子。每个单词都 只 包含大写和小写英文字母。如果两个句子 sentence1 和 sentence2 ，可以通过往其中一个句子插入
一个任意的句子（可以是空句子）而得到另一个句子，那么我们称这两个句子是 相似的 。比方说，sentence1 = "Hello my name is Jane" 
且 sentence2 = "Hello Jane" ，我们可以往 sentence2 中 "Hello" 和 "Jane" 之间插入 "my name is" 得到 sentence1 。
给你两个句子 sentence1 和 sentence2 ，如果 sentence1 和 sentence2 是相似的，请你返回 true ，否则返回 false 。

示例 1：
输入：sentence1 = "My name is Haley", sentence2 = "My Haley"
输出：true
解释：可以往 sentence2 中 "My" 和 "Haley" 之间插入 "name is" ，得到 sentence1 。

示例 2：
输入：sentence1 = "of", sentence2 = "A lot of words"
输出：false
解释：没法往这两个句子中的一个句子只插入一个句子就得到另一个句子。

示例 3：
输入：sentence1 = "Eating right now", sentence2 = "Eating"
输出：true
解释：可以往 sentence2 的结尾插入 "right now" 得到 sentence1 。

示例 4：
输入：sentence1 = "Luky", sentence2 = "Lucccky"
输出：false
"""
"""
思路：
（1）从头到尾消消乐，把前面和后面相同的都消掉即可，看剩下的是否为空
（2）i 表示两个字符串数组从左开始，最多有 i 个字符串相同。j 表示剩下的字符串数组从右开始，最多有 j 个字符串相同。如果 i+j 正好
是某个字符串数组的长度，那么原字符串就是相似的。
"""


class Solution:
    @staticmethod
    def areSentencesSimilar(sentence1: str, sentence2: str) -> bool:
        # split1 = sentence1.split(' ')
        # split2 = sentence2.split(' ')
        # while split1 and split2:
        #     if split1[0] == split2[0]:
        #         split1.pop(0)
        #         split2.pop(0)
        #     elif split1[-1] == split2[-1]:
        #         split1.pop()
        #         split2.pop()
        #     else:
        #         return False
        # return True

        words1 = sentence1.split()
        words2 = sentence2.split()
        i, j = 0, 0
        while i < len(words1) and i < len(words2) and words1[i] == words2[i]:
            i += 1
        while j < len(words1) - i and j < len(words2) - i and words1[-j - 1] == words2[-j - 1]:
            j += 1
        return i + j == min(len(words1), len(words2))
