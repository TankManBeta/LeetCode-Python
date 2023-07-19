# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2023/7/17 11:14
"""
"""
给定两个字符串形式的非负整数 num1 和num2 ，计算它们的和并同样以字符串形式返回。
你不能使用任何內建的用于处理大整数的库（比如 BigInteger）， 也不能直接将输入的字符串转换为整数形式。 

示例 1：
输入：num1 = "11", num2 = "123"
输出："134"

示例 2：
输入：num1 = "456", num2 = "77"
输出："533"

示例 3：
输入：num1 = "0", num2 = "0"
输出："0"
"""
"""
思路：模拟即可。carry表示进位，然后每次计算total和，然后计算当前位的数字和新的进位。
"""


class Solution:
    @staticmethod
    def addStrings(num1: str, num2: str) -> str:
        # n1 = len(num1)
        # n2 = len(num2)
        # n = max(n1, n2)
        # num1 = (n-n1) * '0' + num1
        # num2 = (n-n2) * '0' + num2
        # res = []
        # carry = 0
        # for i in range(n-1, -1, -1):
        #     tmp = int(num1[i]) + int(num2[i]) + carry
        #     carry = tmp // 10
        #     res.append(str(tmp % 10))
        # return ''.join(res[::-1]) if not carry else '1'+''.join(res[::-1])

        i, j = len(num1) - 1, len(num2) - 1
        ans = []
        c = 0
        while i >= 0 or j >= 0 or c:
            a = 0 if i < 0 else int(num1[i])
            b = 0 if j < 0 else int(num2[j])
            c, v = divmod(a + b + c, 10)
            ans.append(str(v))
            i, j = i - 1, j - 1
        return "".join(ans[::-1])
