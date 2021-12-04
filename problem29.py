# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2021/12/4 14:41
"""
"""
给定两个整数，被除数 dividend 和除数 divisor。将两数相除，要求不使用乘法、除法和 mod 运算符。
返回被除数 dividend 除以除数 divisor 得到的商。
整数除法的结果应当截去（truncate）其小数部分，例如：truncate(8.345) = 8 以及 truncate(-2.7335) = -2

输入: dividend = 10, divisor = 3
输出: 3
解释: 10/3 = truncate(3.33333..) = truncate(3) = 3

输入: dividend = 7, divisor = -3
输出: -2
解释: 7/-3 = truncate(-2.33333..) = -2
"""
"""
思路：
（1）一开始想法是直接每次减被除数，提交超时
（2）看完题解之后想到可以每次将被除数×2，对应结果也×2，大大减少时间
"""


INT_MIN = 0 - 2 ** 31
INT_MAX = 2 ** 31 - 1


class Solution(object):
    @staticmethod
    def divide(dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        if dividend == 0:
            return 0
        if dividend == INT_MIN and divisor == -1:
            return INT_MAX
        num_a, num_b = abs(dividend), abs(divisor)

        def positive_divide(a, b):
            if a < b:
                return 0
            else:
                new_b = b
                count = 1
                while a > new_b << 1:
                    new_b = new_b << 1
                    count = count << 1
                return count + positive_divide(a - new_b, b)

        res = positive_divide(num_a, num_b)
        if (dividend > 0 and divisor > 0) or (dividend < 0 and divisor < 0):
            return res
        else:
            return 0 - res
