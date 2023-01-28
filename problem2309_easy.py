# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2023/1/27 20:08
"""
"""
给你一个由英文字母组成的字符串 s ，请你找出并返回 s 中的 最好 英文字母。返回的字母必须为大写形式。如果不存在满足条件的字母，则返回一个空字符串。
最好 英文字母的大写和小写形式必须 都 在 s 中出现。
英文字母 b 比另一个英文字母 a 更好 的前提是：英文字母表中，b 在 a 之 后 出现。

示例 1：
输入：s = "lEeTcOdE"
输出："E"
解释：
字母 'E' 是唯一一个大写和小写形式都出现的字母。

示例 2：
输入：s = "arRAzFif"
输出："R"
解释：
字母 'R' 是大写和小写形式都出现的最好英文字母。
注意 'A' 和 'F' 的大写和小写形式也都出现了，但是 'R' 比 'F' 和 'A' 更好。

示例 3：
输入：s = "AbCdEfGhIjK"
输出：""
解释：
不存在大写和小写形式都出现的字母。
"""
"""
思路：遍历set过后的字符串，然后mark一下大小写是否出现过，然后要是大小写都出现过就返回
"""


class Solution:
    @staticmethod
    def greatestLetter(s: str) -> str:
        s = list(set(s))
        lower = [0] * 26
        upper = [0] * 26
        for letter in s:
            if 'a' <= letter <= 'z':
                index = ord(letter) - ord('a')
                lower[index] = 1
            else:
                index = ord(letter) - ord('A')
                upper[index] = 1
        for i in range(25, -1, -1):
            if lower[i] == 1 and upper[i] == 1:
                return chr(ord('A') + i)
        return ''
