# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2022/12/3 16:33
"""
"""
给你一个混合字符串 s ，请你返回 s 中 第二大 的数字，如果不存在第二大的数字，请你返回 -1 。
混合字符串 由小写英文字母和数字组成。

示例 1：
输入：s = "dfa12321afd"
输出：2
解释：出现在 s 中的数字包括 [1, 2, 3] 。第二大的数字是 2 。

示例 2：
输入：s = "abc1111"
输出：-1
解释：出现在 s 中的数字只包含 [1] 。没有第二大的数字。
"""
"""
思路：如果num比最大的大，它就是最大的，最大的就变成第二大的；如果num比第二大的大，那它就是第二大的。
"""


class Solution:
    @staticmethod
    def secondHighest(s: str) -> int:
        first = second = -1
        for c in s:
            if c.isdigit():
                num = int(c)
                if num > first:
                    second = first
                    first = num
                elif second < num < first:
                    second = num
        return second
