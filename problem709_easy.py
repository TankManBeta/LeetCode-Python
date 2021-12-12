# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2021/12/12 13:02
"""
"""
给你一个字符串 s ，将该字符串中的大写字母转换成相同的小写字母，返回新的字符串。

输入：s = "Hello"
输出："hello"

输入：s = "here"
输出："here"

输入：s = "LOVELY"
输出："lovely"
"""
"""
思路：
（1）遍历改大小
（2）调用函数
"""


class Solution(object):
    @staticmethod
    def to_lower_case(s):
        """
        :type s: str
        :rtype: str
        """
        res_list = []
        for i in s:
            if 'A' <= i <= 'Z':
                temp = chr(ord(i)+32)
                res_list.append(temp)
            else:
                res_list.append(i)
        res_str = "".join(res_list)
        return res_str
