# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2023/5/25 10:52
"""
"""
给定一个数字，我们按照如下规则把它翻译为字符串：0 翻译成 “a” ，1 翻译成 “b”，……，11 翻译成 “l”，……，25 翻译成 “z”。
一个数字可能有多个翻译。请编程实现一个函数，用来计算一个数字有多少种不同的翻译方法。

示例 1:
输入: 12258
输出: 5
解释: 12258有5种不同的翻译，分别是"bccfi", "bwfi", "bczi", "mcfi"和"mzi"
"""
"""
思路：dp，可以看成有条件的青蛙跳台阶，如果最后两位的范围在10-25之间，则dp[i] = dp[i-1]+dp[i-2]；否则就是dp[i-1]
"""


class Solution:
    @staticmethod
    def translateNum(num: int) -> int:
        s = str(num)
        n = len(s)
        if n <= 1:
            return 1
        dp = [0] * (n + 1)
        dp[0] = 1
        dp[1] = 1
        for i in range(2, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2] if 10 <= int(s[i - 2:i]) <= 25 else dp[i - 1]
        return dp[n]
