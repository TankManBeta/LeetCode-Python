# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2022/11/5 15:04
"""
"""
给你两个正整数 num1 和 num2 ，找出满足下述条件的整数 x ：
    x 的置位数和 num2 相同，且
    x XOR num1 的值 最小
    注意 XOR 是按位异或运算。
返回整数 x 。题目保证，对于生成的测试用例， x 是 唯一确定 的。
整数的 置位数 是其二进制表示中 1 的数目。
"""
"""
思路：因为x的置位数和num2相同，所以要将这些1合理分配，又因为要异或和最小，所以优先把1放在num1有1的地方。所以思路很清晰，统计num1
和num2中1的个数记为k1和k2，如果num1中的1大于num2中的1，就把num1中最低的k1-k2个1变为0；否则就把k1-k2个0变为1
"""


class Solution:
    @staticmethod
    def minimizeXor(num1: int, num2: int) -> int:
        c1 = num1.bit_count()
        c2 = num2.bit_count()
        while c2 < c1:
            num1 &= num1 - 1  # 最低的 1 变成 0
            c2 += 1
        while c2 > c1:
            num1 |= num1 + 1  # 最低的 0 变成 1
            c2 -= 1
        return num1
