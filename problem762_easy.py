# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2022/4/5 12:13
"""
"""
给你两个整数 left 和 right ，在闭区间 [left, right] 范围内，统计并返回 计算置位位数为质数 的整数个数。
计算置位位数 就是二进制表示中 1 的个数。
例如， 21 的二进制表示 10101 有 3 个计算置位。

输入：left = 6, right = 10
输出：4
解释：
6 -> 110 (2 个计算置位，2 是质数)
7 -> 111 (3 个计算置位，3 是质数)
9 -> 1001 (2 个计算置位，2 是质数)
10-> 1010 (2 个计算置位，2 是质数)
共计 4 个计算置位为质数的数字。

输入：left = 10, right = 15
输出：5
解释：
10 -> 1010 (2 个计算置位, 2 是质数)
11 -> 1011 (3 个计算置位, 3 是质数)
12 -> 1100 (2 个计算置位, 2 是质数)
13 -> 1101 (3 个计算置位, 3 是质数)
14 -> 1110 (3 个计算置位, 3 是质数)
15 -> 1111 (4 个计算置位, 4 不是质数)
共计 5 个计算置位为质数的数字。
"""
"""
思路：
（1）计算1的数量并判断是否为素数
（2）计算1的数量并打表
（3）计算1的数量左移并与上665772
"""


class Solution(object):
    @staticmethod
    def countPrimeSetBits(left, right):
        """
        :type left: int
        :type right: int
        :rtype: int
        """

        # def isPrime(x):
        #     if x == 1:
        #         return False
        #     for i in range(2, x):
        #         if x % i == 0:
        #             return False
        #     return True
        #
        # ans = 0
        # for num in range(left, right + 1):
        #     count = 0
        #     while num != 0:
        #         count += 1
        #         num &= num - 1
        #     if isPrime(count):
        #         ans += 1
        # return ans

        # primes = [2,3,5,7,11,13,17,19]
        # ans = 0
        # for num in range(left, right+1):
        #     count = 0
        #     while num != 0:
        #         count += 1
        #         num &= num-1
        #     if count in primes:
        #         ans += 1
        # return ans

        ans = 0
        for num in range(left, right + 1):
            count = 0
            while num != 0:
                count += 1
                num &= num - 1
            if (1 << count) & 665772 != 0:
                ans += 1
        return ans
