# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2023/1/8 0:08
"""
from typing import List

"""
给你一个字符串数组 words 和一个字符串 pref 。
返回 words 中以 pref 作为 前缀 的字符串的数目。
字符串 s 的 前缀 就是  s 的任一前导连续字符串。

示例 1：
输入：words = ["pay","attention","practice","attend"], pref = "at"
输出：2
解释：以 "at" 作为前缀的字符串有两个，分别是："attention" 和 "attend" 。

示例 2：
输入：words = ["leetcode","win","loops","success"], pref = "code"
输出：0
解释：不存在以 "code" 作为前缀的字符串。
"""
"""
思路：直接模拟即可
"""


class Solution:
    @staticmethod
    def prefixCount(words: List[str], pref: str) -> int:
        n = len(pref)
        ans = 0
        for word in words:
            if len(word) >= n:
                if word.startswith(pref):
                    ans += 1
        return ans
