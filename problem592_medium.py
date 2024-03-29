# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2023/1/17 15:36
"""
from math import gcd

"""
给定一个表示分数加减运算的字符串 expression ，你需要返回一个字符串形式的计算结果。 
这个结果应该是不可约分的分数，即最简分数。 如果最终结果是一个整数，例如 2，你需要将它转换成分数形式，其分母为 1。
所以在上述例子中, 2 应该被转换为 2/1。

示例 1:
输入: expression = "-1/2+1/2"
输出: "0/1"

示例 2:
输入: expression = "-1/2+1/2+1/3"
输出: "1/3"

示例 3:
输入: expression = "1/3-1/2"
输出: "-1/6"
"""
"""
思路：对于两个分数 y1/x1 和 y2/x2 ，它们相加的结果为：(x1×y2+x2×y1)/y1×y2。初始分数的分子为 x=0，分母为 y=1。我们不断从字符串
中获取下一个分数，它的分子为 x1，分母为 y1，将它加到初始分数上，有：x=x×y1+x1×y；y=y×y1。最后如果x=0，说明结果为零，直接返回 
"0/1"；否则计算分子分母的最大公约数，返回约简后分数的字符串表示。
"""


class Solution:
    @staticmethod
    def fractionAddition(expression: str) -> str:
        denominator, numerator = 0, 1  # 分子，分母
        i, n = 0, len(expression)
        while i < n:
            # 读取分子
            denominator1, sign = 0, 1
            if expression[i] == '-' or expression[i] == '+':
                if expression[i] == '-':
                    sign = -1
                i += 1
            while i < n and expression[i].isdigit():
                denominator1 = denominator1 * 10 + int(expression[i])
                i += 1
            denominator1 = sign * denominator1
            i += 1

            # 读取分母
            numerator1 = 0
            while i < n and expression[i].isdigit():
                numerator1 = numerator1 * 10 + int(expression[i])
                i += 1

            denominator = denominator * numerator1 + denominator1 * numerator
            numerator *= numerator1
        if denominator == 0:
            return "0/1"
        g = gcd(abs(denominator), numerator)
        return f"{denominator // g}/{numerator // g}"
