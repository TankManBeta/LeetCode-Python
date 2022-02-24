# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2022/2/23 14:50
"""
"""
给你一个字符串 s ，根据下述规则反转字符串：
    所有非英文字母保留在原有位置。
    所有英文字母（小写或大写）位置反转。
返回反转后的 s 。

输入：s = "ab-cd"
输出："dc-ba"

输入：s = "a-bC-dEf-ghIj"
输出："j-Ih-gfE-dCba"

输入：s = "Test1ng-Leet=code-Q!"
输出："Qedo1ct-eeLg=ntse-T!"
"""
"""
思路：左边找一个字母右边找一个字母，交换即可
"""


class Solution(object):
    @staticmethod
    def reverse_only_letters(s):
        """
        :type s: str
        :rtype: str
        """
        m = len(s)
        i, j = 0, m-1
        s = list(s)
        while i < j:
            if 33 <= ord(s[i]) <= 64 or 91 <= ord(s[i]) <= 96:
                i += 1
                continue
            if 33 <= ord(s[j]) <= 64 or 91 <= ord(s[j]) <= 96:
                j -= 1
                continue
            s[i], s[j] = s[j], s[i]
            i += 1
            j -= 1
        return ''.join(s)
