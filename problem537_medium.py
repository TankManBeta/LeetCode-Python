# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2022/2/25 10:28
"""
"""
复数 可以用字符串表示，遵循 "实部+虚部i" 的形式，并满足下述条件：
    实部 是一个整数，取值范围是 [-100, 100]
    虚部 也是一个整数，取值范围是 [-100, 100]
    i2 == -1
给你两个字符串表示的复数 num1 和 num2 ，请你遵循复数表示形式，返回表示它们乘积的字符串。

输入：num1 = "1+1i", num2 = "1+1i"
输出："0+2i"
解释：(1 + i) * (1 + i) = 1 + i2 + 2 * i = 2i ，你需要将它转换为 0+2i 的形式。

输入：num1 = "1+-1i", num2 = "1+-1i"
输出："0+-2i"
解释：(1 - i) * (1 - i) = 1 + i2 - 2 * i = -2i ，你需要将它转换为 0+-2i 的形式。 
"""
"""
思路：一开始一维可能没有输入的标准形式，后面细看题目才发现右标准的输入形式，直接获取实部虚部进行计算即可
"""


class Solution(object):
    @staticmethod
    def complex_number_multiply(num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        # import re
        # pattern = "[+i]"
        # num1_split = re.split(pattern, num1[:-1])
        # num2_split = re.split(pattern, num2)
        # real = int(num1_split[0])*int(num2_split[0])-int(num1_split[1])*int(num2_split[1])
        # complex = int(num1_split[0])*int(num2_split[1])+int(num1_split[1])*int(num2_split[0])
        # return str(real) + '+' + str(complex) + 'i'

        num1_split = num1[:-1].split('+')
        num2_split = num2[:-1].split('+')
        real_part = int(num1_split[0])*int(num2_split[0])-int(num1_split[1])*int(num2_split[1])
        complex_part = int(num1_split[0]) * int(num2_split[1]) + int(num1_split[1]) * int(num2_split[0])
        return str(real_part) + '+' + str(complex_part) + 'i'
