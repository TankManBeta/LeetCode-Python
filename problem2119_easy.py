# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2022/11/28 18:34
"""
"""
反转 一个整数意味着倒置它的所有位。
例如，反转 2021 得到 1202 。反转 12300 得到 321 ，不保留前导零 。
给你一个整数 num ，反转 num 得到 reversed1 ，接着反转 reversed1 得到 reversed2 。
如果 reversed2 等于 num ，返回 true ；否则，返回 false 。

示例 1：
输入：num = 526
输出：true
解释：反转 num 得到 625 ，接着反转 625 得到 526 ，等于 num 。

示例 2：
输入：num = 1800
输出：false
解释：反转 num 得到 81 ，接着反转 81 得到 18 ，不等于 num 。 

示例 3：
输入：num = 0
输出：true
解释：反转 num 得到 0 ，接着反转 0 得到 0 ，等于 num 。
"""
"""
思路：
（1）直接按照题意反转两次
（2）如果末尾有0，那么反转后位数肯定会变少，所以只需判断是否末尾有0即可（0除外）
"""


class Solution:
    @staticmethod
    def isSameAfterReversals(num: int) -> bool:
        # return num == 0 or num % 10 != 0

        num1 = int(str(num)[::-1])
        num2 = int(str(num1)[::-1])
        return num == num2
