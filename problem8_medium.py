# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2021/10/29 10:22
"""
"""
请你来实现一个 myAtoi(string s) 函数，使其能将字符串转换成一个 32 位有符号整数（类似 C/C++ 中的 atoi 函数）。
函数 myAtoi(string s) 的算法如下：
读入字符串并丢弃无用的前导空格
检查下一个字符（假设还未到字符末尾）为正还是负号，读取该字符（如果有）。确定最终结果是负数还是正数。如果两者都不存在，则假定结果为正。
读入下一个字符，直到到达下一个非数字字符或到达输入的结尾。字符串的其余部分将被忽略。
将前面步骤读入的这些数字转换为整数（即，"123"->123， "0032"->32）。如果没有读入数字，则整数为 0 。必要时更改符号（从步骤2开始）。
如果整数数超过32位有符号整数范围 [−2**31,2**31−1]，需要截断这个整数，使其保持在这个范围内。
具体来说，小于−231的整数应该被固定为−2**31，大于2**31−1的整数应该被固定为 231 − 1 。
返回整数作为最终结果。
注意：
本题中的空白字符只包括空格字符 ' ' 。
除前导空格或数字后的其余字符串外，请勿忽略 任何其他字符。
"""
"""
思路：
先去除前面的空格，然后判断第一个是加号、减号、数字或是其他字符，然后遍历字符串，直到遇到除数字外的其他字符或遍历完成结束。
"""


class Solution(object):
    @staticmethod
    def my_atoi(s):
        """
        :type s: str
        :rtype: int
        """
        int_min = -2147483648
        int_max = 2147483647
        s = s.lstrip()
        if s == "":
            return 0
        is_neg = 0
        result_num = 0
        if s[0] == '+':
            is_neg = 0
            s = s[1:]
        elif s[0] == '-':
            is_neg = 1
            s = s[1:]
        for char in s:
            if '0' <= char <= '9':
                result_num = result_num * 10 + int(char) - int('0')
            else:
                break
        if is_neg == 0:
            return result_num if result_num <= int_max else int_max
        if is_neg == 1:
            return -result_num if -result_num >= int_min else int_min
