# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2023/5/18 10:28
"""
"""
请实现一个函数，把字符串 s 中的每个空格替换成"%20"。 

示例 1：
输入：s = "We are happy."
输出："We%20are%20happy."
"""
"""
思路：
（1）直接replace
（2）可以在时间复杂度为O(n)的情况下将空间复杂度变为O(1)，即扩充字符串，然后再从后往前进行填充即可。
"""


class Solution:
    @staticmethod
    def replaceSpace(s: str) -> str:
        return s.replace(' ', '%20')
