# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2023/2/22 20:07
"""
from collections import Counter

"""
给你一个字符串 s ，请你去除字符串中重复的字母，使得每个字母只出现一次。需保证 返回结果的字典序最小（要求不能打乱其他字符的相对位置）。

示例 1：
输入：s = "bcabc"
输出："abc"

示例 2：
输入：s = "cbacdcbc"
输出："acdb"
"""
"""
思路：我们从前向后扫描原字符串。每扫描到一个位置，我们就尽可能地处理所有的「关键字符」（s[i]>s[i+1]）。假定在扫描位置 s[i−1] 
之前的所有「关键字符」都已经被去除完毕，在扫描字符 s[i] 时，新出现的「关键字符」只可能出现在 s[i] 或者其后面的位置。我们还遗漏
了一个要求：原字符串 s 中的每个字符都需要出现在新字符串中，且只能出现一次。为了让新字符串满足该要求，之前讨论的算法需要进行以下
两点的更改。
在考虑字符 s[i] 时，如果它已经存在于栈中，则不能加入字符 s[i]。为此，需要记录每个字符是否出现在栈中。
在弹出栈顶字符时，如果字符串在后面的位置上再也没有这一字符，则不能弹出栈顶字符。为此，需要记录每个字符的剩余数量，当这个值为 0 
时，就不能弹出栈顶字符了。
"""


class Solution:
    @staticmethod
    def removeDuplicateLetters(s) -> str:
        stack = []
        seen = set()
        remain_counter = Counter(s)

        for c in s:
            if c not in seen:
                while stack and c < stack[-1] and  remain_counter[stack[-1]] > 0:
                    seen.discard(stack.pop())
                seen.add(c)
                stack.append(c)
            remain_counter[c] -= 1
        return ''.join(stack)
