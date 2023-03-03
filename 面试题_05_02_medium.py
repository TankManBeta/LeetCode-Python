# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2023/3/2 9:26
"""
"""
二进制数转字符串。给定一个介于0和1之间的实数（如0.72），类型为double，打印它的二进制表达式。如果该数字无法精确地用32位以内的
二进制表示，则打印“ERROR”。

示例1:
 输入：0.625
 输出："0.101"

示例2:
 输入：0.1
 输出："ERROR"
 提示：0.1无法被二进制准确表示
"""
"""
思路：任何进制表示的小数，乘上进制等价于小数点往右移一位。十进制小数转二进制小数的方法是：小数部分乘以 2，取整数部分作为二进制
小数的下一位，小数部分作为下一次乘法的被乘数，直到小数部分为 0 或者二进制小数的长度超过 32 位。
"""


class Solution:
    @staticmethod
    def printBin(num: float) -> str:
        ans = '0.'
        while len(ans) < 32 and num:
            num *= 2
            x = int(num)
            ans += str(x)
            num -= x
        return 'ERROR' if num else ans
