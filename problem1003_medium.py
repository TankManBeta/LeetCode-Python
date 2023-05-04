# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2023/5/3 20:11
"""
"""
给你一个字符串 s ，请你判断它是否 有效 。
字符串 s 有效 需要满足：假设开始有一个空字符串 t = "" ，你可以执行 任意次 下述操作将 t 转换为 s ：
将字符串 "abc" 插入到 t 中的任意位置。形式上，t 变为 tleft + "abc" + tright，其中 t == tleft + tright 。注意，tleft 和 tright 可能为 空 。
如果字符串 s 有效，则返回 true；否则，返回 false。 

示例 1：
输入：s = "aabcbc"
输出：true
解释：
"" -> "abc" -> "aabcbc"
因此，"aabcbc" 有效。

示例 2：
输入：s = "abcabcababcc"
输出：true
解释：
"" -> "abc" -> "abcabc" -> "abcabcabc" -> "abcabcababcc"
因此，"abcabcababcc" 有效。

示例 3：
输入：s = "abccba"
输出：false
解释：执行操作无法得到 "abccba" 。
"""
"""
思路：栈。首先s的长度肯定是3的倍数，如果不是的话肯定为False；使用栈，每次取最后三个，如果组成的字符串是"abc"就弹出，最后看栈
是否为空即可。
"""


class Solution:
    @staticmethod
    def isValid(s: str) -> bool:
        n = len(s)
        if n % 3 != 0:
            return False
        stack = []
        for c in s:
            stack.append(c)
            if ''.join(stack[-3:]) == 'abc':
                stack[-3:] = []
        return not stack
