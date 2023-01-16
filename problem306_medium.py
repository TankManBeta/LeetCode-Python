# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2023/1/15 14:53
"""
"""
累加数 是一个字符串，组成它的数字可以形成累加序列。
一个有效的 累加序列 必须 至少 包含 3 个数。除了最开始的两个数以外，序列中的每个后续数字必须是它之前两个数字之和。
给你一个只包含数字 '0'-'9' 的字符串，编写一个算法来判断给定输入是否是 累加数 。如果是，返回 true ；否则，返回 false 。
说明：累加序列里的数，除数字 0 之外，不会 以 0 开头，所以不会出现 1, 2, 03 或者 1, 02, 3 的情况。

示例 1：
输入："112358"
输出：true 
解释：累加序列为: 1, 1, 2, 3, 5, 8 。1 + 1 = 2, 1 + 2 = 3, 2 + 3 = 5, 3 + 5 = 8

示例 2：
输入："199100199"
输出：true 
解释：累加序列为: 1, 99, 100, 199。1 + 99 = 100, 99 + 100 = 199
"""
"""
思路：一个累加序列，当它的第一个数字和第二个数字以及总长度确定后，这整个累加序列也就确定了。根据这个性质，我们可以穷举累加序列的
第一个数字和第二个数字的所有可能性，对每个可能性，进行一次合法性的判断。当出现一次合法的累加序列后，即可返回true。当所有可能性
都遍历完仍无法找到一个合法的累加序列时，返回 false。
"""


class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        n = len(num)
        for secondStart in range(1, n - 1):
            if num[0] == '0' and secondStart != 1:
                break
            for secondEnd in range(secondStart, n - 1):
                if num[secondStart] == '0' and secondStart != secondEnd:
                    break
                if self.valid(secondStart, secondEnd, num):
                    return True
        return False

    def valid(self, secondStart: int, secondEnd: int, num: str) -> bool:
        n = len(num)
        firstStart, firstEnd = 0, secondStart - 1
        while secondEnd <= n - 1:
            third = self.stringAdd(num, firstStart, firstEnd, secondStart, secondEnd)
            thirdStart = secondEnd + 1
            thirdEnd = secondEnd + len(third)
            if thirdEnd >= n or num[thirdStart:thirdEnd + 1] != third:
                break
            if thirdEnd == n - 1:
                return True
            firstStart, firstEnd = secondStart, secondEnd
            secondStart, secondEnd = thirdStart, thirdEnd
        return False

    @staticmethod
    def stringAdd(s: str, firstStart: int, firstEnd: int, secondStart: int, secondEnd: int) -> str:
        third = []
        carry, cur = 0, 0
        while firstEnd >= firstStart or secondEnd >= secondStart or carry != 0:
            cur = carry
            if firstEnd >= firstStart:
                cur += ord(s[firstEnd]) - ord('0')
                firstEnd -= 1
            if secondEnd >= secondStart:
                cur += ord(s[secondEnd]) - ord('0')
                secondEnd -= 1
            carry = cur // 10
            cur %= 10
            third.append(chr(cur + ord('0')))
        return ''.join(third[::-1])
