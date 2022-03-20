# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2022/3/19 12:40
"""
"""
给定两个整数，分别表示分数的分子 numerator 和分母 denominator，以 字符串形式返回小数 。
如果小数部分为循环小数，则将循环的部分括在括号内。
如果存在多个答案，只需返回 任意一个 。
对于所有给定的输入，保证 答案字符串的长度小于 104 。

输入：numerator = 1, denominator = 2
输出："0.5"

输入：numerator = 2, denominator = 1
输出："2"

输入：numerator = 2, denominator = 3
输出："0.(6)"

输入：numerator = 4, denominator = 333
输出："0.(012)"

输入：numerator = 1, denominator = 5
输出："0.2"
"""
"""
思路：先看正负号，然后先算整数部分；再算小数部分，组合数学中学过两个整数相除的结果要么除尽要么就是循环的，终止条件就是这个就行，
用一个indexMap记录每个数字在余数中的位置，如果再次出现就说明有循环节
"""


class Solution(object):
    @staticmethod
    def fractionToDecimal(numerator, denominator):
        """
        :type numerator: int
        :type denominator: int
        :rtype: str
        """
        if numerator % denominator == 0:
            return str(numerator // denominator)

        s = []
        if (numerator < 0) != (denominator < 0):
            s.append('-')

        numerator = abs(numerator)
        denominator = abs(denominator)
        integerPart = numerator // denominator
        s.append(str(integerPart))
        s.append('.')

        indexMap = {}
        remainder = numerator % denominator
        while remainder and remainder not in indexMap:
            indexMap[remainder] = len(s)
            remainder *= 10
            s.append(str(remainder // denominator))
            remainder %= denominator
        if remainder:
            insertIndex = indexMap[remainder]
            s.insert(insertIndex, '(')
            s.append(')')

        return ''.join(s)
