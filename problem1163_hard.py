# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2023/4/24 11:08
"""
"""
给你一个字符串 s ，找出它的所有子串并按字典序排列，返回排在最后的那个子串。 

示例 1：
输入：s = "abab"
输出："bab"
解释：我们可以找出 7 个子串 ["a", "ab", "aba", "abab", "b", "ba", "bab"]。按字典序排在最后的子串是 "bab"。

示例 2：
输入：s = "leetcode"
输出："tcode"
"""
"""
思路：
（1）最大字符串一定以最大字符开头，并且一定到结尾（长的更大）
（2）使用双指针i和j，i指向的是当前找到字典序最大的字符，j指向的是当前要进行比较的字符。使用一个位移指针k，来比较i和j构成的子串
[i,..,i + k]和[j,...,j + k]的顺序。
    s[i + k] == s[j + k]，当前比较字符相同，k后移一位，比较下一位。
    s[i + k] < s[j + k]，说明子串[i,..,i + k]的字典序小于子串[j,...,j + k]，并且[i,..,i + k]中任意的字符构成的后缀都是小于
    子串[j,...,j + k]构成的后缀。因为在后缀中一定存在s[i + k] < s[j + k]。因此[i,..,i + k]部分不会存在目标子串，直接跳过处理，
    更新i = i + k + 1。同时如果更新后的i >= j，那么说明j也是包含在[i,..,i + k]中的，j更新为当前i的下一位查找新的子串。
    s[i + k] > s[j + k]，说明子串[i,..,i + k]的字典序大于子串[j,...,j + k]，并且[i,..,i + k]中任意的字符构成的后缀都是大于
    子串[j,...,j + k]构成的后缀。因此[j,..,j + k]部分不会存在目标子串，直接跳过处理，更新j = j + k + 1。由于j始终是在i之后的，
    因此j的更新仍然保证j在i之后。
"""


class Solution:
    @staticmethod
    def lastSubstring(s: str) -> str:
        # ch = max(s)
        # res = ''
        # for i in range(len(s)):
        #     if s[i] == ch:
        #        t = s[i:]
        #        if t > res:
        #            res = t
        # return res

        i, j, k = 0, 1, 0
        while j + k < len(s):
            if s[i + k] == s[j + k]:
                k += 1
            elif s[i + k] < s[j + k]:
                i += k + 1
                k = 0
                if i >= j:
                    j = i + 1
            else:
                j += k + 1
                k = 0
        return s[i:]
