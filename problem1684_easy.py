# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2022/11/8 10:27
"""
from typing import List

"""
给你一个由不同字符组成的字符串 allowed 和一个字符串数组 words 。
如果一个字符串的每一个字符都在 allowed 中，就称这个字符串是 一致字符串 。
请你返回 words 数组中 一致字符串 的数目。

示例 1：
输入：allowed = "ab", words = ["ad","bd","aaab","baa","badab"]
输出：2
解释：字符串 "aaab" 和 "baa" 都是一致字符串，因为它们只包含字符 'a' 和 'b' 。

示例 2：
输入：allowed = "abc", words = ["a","b","c","ab","ac","bc","abc"]
输出：7
解释：所有字符串都是一致的。

示例 3：
输入：allowed = "cad", words = ["cc","acd","b","ba","bac","bad","ac","d"]
输出：4
解释：字符串 "cc"，"acd"，"ac" 和 "d" 是一致字符串。
"""
"""
思路：将字符串变成集合，然后看补集是不是空集
"""


class Solution:
    @staticmethod
    def countConsistentStrings(allowed: str, words: List[str]) -> int:
        # count = 0
        # a = set(allowed)
        # for word in words:
        #     b = set(word)
        #     if not b-a:
        #         count += 1
        # return count

        count = 0
        a = set(allowed)
        for word in words:
            b = set(word)
            if a >= b:
                count += 1
        return count
