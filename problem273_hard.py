# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2022/11/30 11:42
"""
"""
将非负整数 num 转换为其对应的英文表示。

示例 1：
输入：num = 123
输出："One Hundred Twenty Three"

示例 2：
输入：num = 12345
输出："Twelve Thousand Three Hundred Forty Five"

示例 3：
输入：num = 1234567
输出："One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven"
"""
"""
思路：数字范围最多十位，所以就每三个一组，将这三位数表示出来，然后后面跟上对应的"Billion", "Thousand", "Hundred"即可
"""

singles = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]
teens = ["Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
tens = ["", "Ten", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
thousands = ["", "Thousand", "Million", "Billion"]


class Solution:
    @staticmethod
    def numberToWords(num: int) -> str:
        if num == 0:
            return "Zero"

        def get_num(number):
            s = ""
            if number >= 100:
                s += singles[number // 100] + " Hundred "
                number %= 100
            if number >= 20:
                s += tens[number // 10] + ' '
                number %= 10
            if 0 < number < 10:
                s += singles[number] + ' '
            elif number >= 10:
                s += teens[number - 10] + ' '
            return s

        res = ""
        division = int(1e9)
        for i in range(3, -1, -1):
            cur_num = num // division
            if cur_num:
                num -= cur_num * division
                res += get_num(cur_num) + thousands[i] + ' '
            division //= 1000

        return res.strip()
