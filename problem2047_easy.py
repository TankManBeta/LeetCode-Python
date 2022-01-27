# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2022/1/27 10:50
"""
"""
句子仅由小写字母（'a' 到 'z'）、数字（'0' 到 '9'）、连字符（'-'）、标点符号（'!'、'.' 和 ','）以及空格（' '）组成。
每个句子可以根据空格分解成 一个或者多个 token ，这些 token 之间由一个或者多个空格 ' ' 分隔。
如果一个 token 同时满足下述条件，则认为这个 token 是一个有效单词：
仅由小写字母、连字符和/或标点（不含数字）。
至多一个 连字符 '-' 。如果存在，连字符两侧应当都存在小写字母（"a-b" 是一个有效单词，但 "-ab" 和 "ab-" 不是有效单词）。
至多一个 标点符号。如果存在，标点符号应当位于 token 的 末尾 。
这里给出几个有效单词的例子："a-b."、"afad"、"ba-c"、"a!" 和 "!" 。
给你一个字符串 sentence ，请你找出并返回 sentence 中 有效单词的数目 。

输入：sentence = "cat and  dog"
输出：3
解释：句子中的有效单词是 "cat"、"and" 和 "dog"

输入：sentence = "!this  1-s b8d!"
输出：0
解释：句子中没有有效单词
"!this" 不是有效单词，因为它以一个标点开头
"1-s" 和 "b8d" 也不是有效单词，因为它们都包含数字

输入：sentence = "alice and  bob are playing stone-game10"
输出：5
解释：句子中的有效单词是 "alice"、"and"、"bob"、"are" 和 "playing"
"stone-game10" 不是有效单词，因为它含有数字

输入：sentence = "he bought 2 pencils, 3 erasers, and 1  pencil-sharpener."
输出：6
解释：句子中的有效单词是 "he"、"bought"、"pencils,"、"erasers,"、"and" 和 "pencil-sharpener."
"""
"""
思路：先split，然后看是否有数字，然后看连字符，count>1不合法，然后看位置，-1对应了count为0的情况，然后判断左右两个是否合法，
最后判断最后一位
"""


class Solution(object):
    @staticmethod
    def count_valid_words(sentence):
        """
        :type sentence: str
        :rtype: int
        """
        def is_valid(word):
            flag = 1
            # deal with number
            for i in [str(j) for j in range(0,10)]:
                if i in word:
                    flag = 0
                    return flag
            # deal with -
            count = word.count('-')
            if count > 1:
                flag = 0
                return flag
            index = word.find('-')
            if index == 0 or index == len(word)-1:
                flag = 0
                return flag
            elif index == -1:
                pass
            else:
                if word[index-1] < 'a' or word[index-1] > 'z' or word[index+1] < 'a' or word[index+1] > 'z':
                    flag = 0
                    return flag
            # deal with others
            for i in ['!', '.', ',']:
                if i in word[0:-1]:
                    flag = 0
                    return flag
            return flag

        words = sentence.split()
        ans = 0
        for item in words:
            ans += is_valid(item)
        return ans
