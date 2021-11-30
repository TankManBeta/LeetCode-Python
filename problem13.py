# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2021/11/30 20:30
"""
"""
罗马数字包含以下七种字符: I， V， X， L，C，D 和 M。

字符          数值
I             1
V             5
X             10
L             50
C             100
D             500
M             1000

例如， 罗马数字2写做II ，即为两个并列的1 。12写做XII，即为 X + II 。 27 写做  XXVII, 即为 XX + V + II 。

通常情况下，罗马数字中小的数字在大的数字的右边。但也存在特例，例如 4 不写做 IIII，而是 IV。
数字 1 在数字 5 的左边，所表示的数等于大数 5 减小数 1 得到的数值 4 。
同样地，数字 9 表示为 IX。这个特殊的规则只适用于以下六种情况：

I 可以放在 V (5) 和 X (10) 的左边，来表示 4 和 9。
X 可以放在 L (50) 和 C (100) 的左边，来表示 40 和 90。 
C 可以放在 D (500) 和 M (1000) 的左边，来表示 400 和 900。
给定一个罗马数字，将其转换成整数。

输入: s = "III"
输出: 3

输入: s = "IV"
输出: 4

输入: s = "IX"
输出: 9

输入: s = "LVIII"
输出: 58
解释: L = 50, V= 5, III = 3.

输入: s = "MCMXCIV"
输出: 1994
解释: M = 1000, CM = 900, XC = 90, IV = 4.
"""
"""
思路：
和problem12思路相似，遍历字符串，每次看开头的和已经定义的symbol-value，然后每次更新值。
"""


class Solution(object):
    @staticmethod
    def roman_to_int(s):
        """
        :type s: str
        :rtype: int
        """
        value_symbols = [
            (1000, "M"),
            (900, "CM"),
            (500, "D"),
            (400, "CD"),
            (100, "C"),
            (90, "XC"),
            (50, "L"),
            (40, "XL"),
            (10, "X"),
            (9, "IX"),
            (5, "V"),
            (4, "IV"),
            (1, "I")
    ]
        val = 0
        for value, symbol in value_symbols:
            while s.startswith(symbol):
                val += value
                s = s[len(symbol):]
        return val
