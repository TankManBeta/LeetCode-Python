# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2022/3/20 13:07
"""
"""
给你一个整数 columnNumber ，返回它在 Excel 表中相对应的列名称。

输入：columnNumber = 1
输出："A"

输入：columnNumber = 28
输出："AB"

输入：columnNumber = 701
输出："ZY"

输入：columnNumber = 2147483647
输出："FXSHRXW"
"""
"""
思路：转化成26进制即可，但26进制从0开始，所以每次number-1再求即可
"""


class Solution(object):
    @staticmethod
    def convertToTitle(columnNumber):
        """
        :type columnNumber: int
        :rtype: str
        """
        res = []
        while True:
            columnNumber -= 1
            m = columnNumber // 26
            n = columnNumber % 26
            res.append(n)
            if m == 0:
                break
            columnNumber = m
        for i in range(len(res)):
            res[i] = chr(65+res[i])
        return ''.join(res[::-1])
