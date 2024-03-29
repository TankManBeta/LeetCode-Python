# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2023/5/18 10:41
"""
"""
字符串的左旋转操作是把字符串前面的若干个字符转移到字符串的尾部。请定义一个函数实现字符串左旋转操作的功能。
比如，输入字符串"abcdefg"和数字2，该函数将返回左旋转两位得到的结果"cdefgab"。 

示例 1：
输入: s = "abcdefg", k = 2
输出: "cdefgab"

示例 2：
输入: s = "lrloseumgh", k = 6
输出: "umghlrlose"
"""
"""
思路：
（1）直接切片
（2）要是不让使用切片，就用列表+join或者直接在空字符串后面加
"""


class Solution:
    @staticmethod
    def reverseLeftWords(s: str, n: int) -> str:
        # return s[n:]+s[:n]

        res = ""
        for i in range(n, len(s)):
            res += s[i]
        for i in range(n):
            res += s[i]
        return res
