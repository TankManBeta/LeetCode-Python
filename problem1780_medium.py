# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2022/12/9 9:47
"""
"""
给你一个整数 n ，如果你可以将 n 表示成若干个不同的三的幂之和，请你返回 true ，否则请返回 false 。
对于一个整数 y ，如果存在整数 x 满足 y == 3x ，我们称这个整数 y 是三的幂。

示例 1：
输入：n = 12
输出：true
解释：12 = 31 + 32

示例 2：
输入：n = 91
输出：true
解释：91 = 30 + 32 + 34

示例 3：
输入：n = 21
输出：false
"""
"""
思路：
（1）数组子集枚举，然后看是否有那个数字，复杂度太高
（2）转化为3进制的余数只能有0或1
"""


class Solution:
    @staticmethod
    def checkPowersOfThree(n: int) -> bool:
        # m = 15
        # for i in range(1, 1<<15):
        #     num = 0
        #     for j in range(15):
        #         if (1<<j) & i:
        #             num += 3**j
        #     if num == n:
        #         return True
        # return False

        while n > 0:
            if n % 3 == 2:
                return False
            n //= 3
        return True
