# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2023/6/5 10:38
"""
"""
写一个函数，求两个整数之和，要求在函数体内不得使用 “+”、“-”、“*”、“/” 四则运算符号。

示例:
输入: a = 1, b = 1
输出: 2
"""
"""
思路：无进位和 n 与进位 c 的计算公式如下；n=a⊕b（非进位和：异或运算）c=a&b<<1（进位：与运算）。（和 s ）=（非进位和 n ）+
（进位 c ）。即可将 s=a+b 转化为：s=a+b⇒s=n+c。循环求 n 和 c ，直至进位 c=0 ；此时 s=n ，返回 n 即可。
"""


class Solution:
    @staticmethod
    def add(a: int, b: int) -> int:
        x = 0xffffffff
        a, b = a & x, b & x
        while b != 0:
            a, b = (a ^ b), (a & b) << 1 & x
        return a if a <= 0x7fffffff else ~(a ^ x)
