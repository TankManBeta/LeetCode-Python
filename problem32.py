# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2021/12/4 21:06
"""
"""
给你一个只包含 '(' 和 ')' 的字符串，找出最长有效（格式正确且连续）括号子串的长度。

输入：s = "(()"
输出：2
解释：最长有效括号子串是 "()"

输入：s = ")()())"
输出：4
解释：最长有效括号子串是 "()()"

输入：s = ""
输出：0
"""
"""
思路：看完题解才懂，从左至右，如果是'('就left++，否则right++，当left==right时，计算当前最长有效的，当右括号数量多于左括号时，
全部left和right全部变为0，但这会漏掉左括号一直比右括号多的情况，只需从右向左重新遍历一次。
"""


class Solution(object):
    @staticmethod
    def longest_valid_parentheses(s):
        """
        :type s: str
        :rtype: int
        """
        n, left, right, maxlength = len(s), 0, 0, 0
        for i in range(n):
            if s[i] == '(':
                left += 1
            else:
                right += 1
            if left == right:
                maxlength = max(maxlength, 2 * right)
            elif right > left:
                left = right = 0
        left = right = 0
        for i in range(n-1, -1, -1):
            if s[i] == '(':
                left += 1
            else:
                right += 1
            if left == right:
                maxlength = max(maxlength, 2 * left)
            elif left > right:
                left = right = 0

        return maxlength
