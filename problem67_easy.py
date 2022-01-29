# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2022/1/28 11:32
"""
"""
给你两个二进制字符串，返回它们的和（用二进制表示）。
输入为 非空 字符串且只包含数字 1 和 0。

输入: a = "11", b = "1"
输出: "100"

输入: a = "1010", b = "1011"
输出: "10101"
"""
"""
思路：首先把两个串变成同样长度（前面添0），设置一个进位（默认为'0'），从最后一位开始，统计a[i]，b[i]，carry中'1'的个数，
如果count为0就是当前位结果为0但不进位，为1就是当前位结果为1但不进位，同理。最后统计结束后再看进位，如果为1说明要多添1位，
否则不需要。
"""


class Solution(object):
    @staticmethod
    def add_binary(a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        len_a = len(a)
        len_b = len(b)
        len_s = max(len_a, len_b)
        a = (len_s-len_a)*'0' + a
        b = (len_s - len_b)*'0' + b
        res = []
        carry = '0'
        for i in range(len_s-1, -1, -1):
            options = [carry, a[i], b[i]]
            count = options.count('1')
            if count == 0:
                carry = '0'
                res.insert(0, '0')
            elif count == 1:
                carry = '0'
                res.insert(0, '1')
            elif count == 2:
                carry = '1'
                res.insert(0, '0')
            else:
                carry = '1'
                res.insert(0, '1')
        res_str = ''.join(res)
        res_str = '1'+res_str if carry == '1' else res_str
        return res_str
