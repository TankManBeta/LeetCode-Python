# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2022/2/20 12:00
"""
"""
有两种特殊字符：
    第一种字符可以用一个比特 0 来表示
    第二种字符可以用两个比特(10 或 11)来表示、
给定一个以 0 结尾的二进制数组 bits ，如果最后一个字符必须是一位字符，则返回 true 。

输入: bits = [1, 0, 0]
输出: true
解释: 唯一的编码方式是一个两比特字符和一个一比特字符。所以最后一个字符是一比特字符。

输入: bits = [1, 1, 1, 0]
输出: false
解释: 唯一的编码方式是两比特字符和两比特字符。所以最后一个字符不是一比特字符。
"""
"""
思路：遇到1跳过下一个字符，遇到0跳过本字符，看看是否落到最后。
"""


class Solution(object):
    @staticmethod
    def is_one_bit_character(bits):
        """
        :type bits: List[int]
        :rtype: bool
        """
        i, n = 0, len(bits)
        while i < n - 1:
            i += bits[i] + 1
        return i == n - 1
