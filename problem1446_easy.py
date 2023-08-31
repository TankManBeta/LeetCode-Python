# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2023/8/25 16:29
"""
"""
给你一个字符串 s ，字符串的「能量」定义为：只包含一种字符的最长非空子字符串的长度。
请你返回字符串 s 的 能量。 

示例 1：
输入：s = "leetcode"
输出：2
解释：子字符串 "ee" 长度为 2 ，只包含字符 'e' 。

示例 2：
输入：s = "abbcccddddeeeeedcba"
输出：5
解释：子字符串 "eeeee" 长度为 5 ，只包含字符 'e' 。
"""
"""
思路：双指针即可
"""


class Solution:
    @staticmethod
    def maxPower(s: str) -> int:
        ans = 0
        n = len(s)
        i, j = 0, 0
        while i < n:
            while j < n and s[i] == s[j]:
                j += 1
            ans = max(ans, j - i)
            i = j
        return ans
