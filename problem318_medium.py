# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2023/2/23 11:11
"""
from collections import defaultdict
from itertools import product
from typing import List

"""
给你一个字符串数组 words ，找出并返回 length(words[i]) * length(words[j]) 的最大值，并且这两个单词不含有公共字母。
如果不存在这样的两个单词，返回 0 。

示例 1：
输入：words = ["abcw","baz","foo","bar","xtfn","abcdef"]
输出：16 
解释：这两个单词为 "abcw", "xtfn"。

示例 2：
输入：words = ["a","ab","abc","d","cd","bcd","abcd"]
输出：4 
解释：这两个单词为 "ab", "cd"。

示例 3：
输入：words = ["a","aa","aaa","aaaa"]
输出：0 
解释：不存在这样的两个单词。
"""
"""
思路：
（1）暴力，遍历字符串数组 words 中的每一对单词，判断这一对单词是否有公共字母，如果没有公共字母，则用这一对单词的长度乘积更新
最大单词长度乘积。
（2）位运算优化暴力，由于单词只包含小写字母，共有 26 个小写字母，因此可以使用位掩码的最低 26 位分别表示每个字母是否在这个单词中
出现。然后用一个哈希表记录有相同掩码的单词的最长长度，然后看两个与起来是否是0来计算最大长度。
"""


class Solution:
    @staticmethod
    def maxProduct(words: List[str]) -> int:
        # tmp = [list(set(word)) for word in words]
        # n = len(words)
        # ans = 0
        # for i in range(n):
        #     for j in range(i+1, n):
        #         flag = True
        #         for letter in tmp[i]:
        #             if letter in tmp[j]:
        #                 flag = False
        #                 break
        #         if flag:
        #             ans = max(ans, len(words[i])*len(words[j]))
        # return ans

        cnt = defaultdict(int)
        for word in words:
            mask = 0
            for letter in word:
                mask |= 1 << (ord(letter) - ord('a'))
            cnt[mask] = max(cnt[mask], len(word))
        return max((cnt[x] * cnt[y] for x, y in product(cnt, repeat=2) if x & y == 0), default=0)
