# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2023/6/15 0:27
"""
"""
数字以0123456789101112131415…的格式序列化到一个字符序列中。在这个序列中，第5位（从下标0开始计数）是5，第13位是1，第19位是4，等等。
请写一个函数，求任意第n位对应的数字。

示例 1：
输入：n = 3
输出：3

示例 2：
输入：n = 11
输出：0
"""
"""
思路：确定 n 所在 数字 的 位数 ，记为 digit ；确定 n 所在的 数字 ，记为 num ；确定 n 是 num 中的哪一数位，并返回结果。
"""


class Solution:
    @staticmethod
    def findNthDigit(n: int) -> int:
        digit, start, count = 1, 1, 9
        while n > count:  # 1.
            n -= count
            start *= 10
            digit += 1
            count = 9 * start * digit
        num = start + (n - 1) // digit  # 2.
        return int(str(num)[(n - 1) % digit])  # 3.
