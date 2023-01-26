# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2023/1/24 17:56
"""
"""
给定一个正整数 n，返回 连续正整数满足所有数字之和为 n 的组数 。 

示例 1:
输入: n = 5
输出: 2
解释: 5 = 2 + 3，共有两组连续整数([5],[2,3])求和后为 5。

示例 2:
输入: n = 9
输出: 3
解释: 9 = 4 + 5 = 2 + 3 + 4

示例 3:
输入: n = 15
输出: 4
解释: 15 = 8 + 7 = 4 + 5 + 6 = 1 + 2 + 3 + 4 + 5
"""
"""
思路：如果 k 是奇数，则当 n 可以被 k 整除时，正整数 n 可以表示成 k 个连续正整数之和；如果 k 是偶数，则当 n 不可以被 k 整除且 
2n 可以被 k 整除时，正整数 n 可以表示成 k 个连续正整数之和。
"""


class Solution:
    @staticmethod
    def consecutiveNumbersSum(n: int) -> int:
        def isKConsecutive(n: int, k: int) -> bool:
            if k % 2:
                return n % k == 0
            return n % k and 2 * n % k == 0

        ans = 0
        k = 1
        while k * (k + 1) <= n * 2:
            if isKConsecutive(n, k):
                ans += 1
            k += 1
        return ans
