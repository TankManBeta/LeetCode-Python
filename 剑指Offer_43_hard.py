# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2023/6/15 20:14
"""
"""

"""
"""
输入一个整数 n ，求1～n这n个整数的十进制表示中1出现的次数。
例如，输入12，1～12这些整数中包含1 的数字有1、10、11和12，1一共出现了5次。

示例 1：
输入：n = 12
输出：5

示例 2：
输入：n = 13
输出：6
"""
"""
思路：将当前位记为cur，将当前位后面的称为低位，记为 low ；将当前位前面的称为高位，记为 high 。将 10**i 称为 位因子 ，记为 digit 。
如果cur==0，我们计算当前位cur为1出现的次数，显然我们的出现出现次数只能是cur*digit。例如2304，求十位出现1的次数，因为十位为0，且
当前位必须为1，所以我们的高位只能取00-22，十位为1，个位为0-9的情况，也就是23*10，即high*digit；如果cur==1，例如2314，高位取00-22，
个位取0-9，为23*10，高位取23，cur为1，低位取0-4，也就是low+1，总共就是high*digit+low+1；如果cur>1，例如2334，高位取00-23，
cur取1，低位0-9，总数为(23+1)*10，即(high+1)*digit。
"""


class Solution:
    @staticmethod
    def countDigitOne(n: int) -> int:
        digit, res = 1, 0
        high, cur, low = n // 10, n % 10, 0
        while high != 0 or cur != 0:
            if cur == 0:
                res += high * digit
            elif cur == 1:
                res += high * digit + low + 1
            else:
                res += (high + 1) * digit
            low += cur * digit
            cur = high % 10
            high //= 10
            digit *= 10
        return res
