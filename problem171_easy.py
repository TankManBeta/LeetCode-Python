# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2022/3/20 13:10
"""
"""
给你一个字符串 columnTitle ，表示 Excel 表格中的列名称。返回 该列名称对应的列序号 。

输入: columnTitle = "A"
输出: 1

输入: columnTitle = "AB"
输出: 28

输入: columnTitle = "ZY"
输出: 701
"""
"""
思路：转化成26进制即可
"""


class Solution(object):
    @staticmethod
    def titleToNumber(columnTitle):
        """
        :type columnTitle: str
        :rtype: int
        """
        res = 0
        n = len(columnTitle)
        for i in range(n):
            res += (ord(columnTitle[i]) - 64)*26**(n-1-i)
        return res
