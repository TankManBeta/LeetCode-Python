# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2022/4/9 12:05
"""
"""
给你一个字符串表达式 s ，请你实现一个基本计算器来计算并返回它的值。
整数除法仅保留整数部分。
你可以假设给定的表达式总是有效的。所有中间结果将在 [-231, 231 - 1] 的范围内。
注意：不允许使用任何将字符串作为数学表达式计算的内置函数，比如 eval() 。

输入：s = "3+2*2"
输出：7

输入：s = " 3/2 "
输出：1

输入：s = " 3+5 / 2 "
输出：5
"""
"""
思路：同224
"""


class Solution(object):
    @staticmethod
    def calculate(s):
        """
        :type s: str
        :rtype: int
        """

        def cal(operator, a, b):
            if operator == "+":
                return a + b
            if operator == "-":
                return a - b
            if operator == "*":
                return a * b
            if operator == "/":
                return a // b

        priority = {
            "+": 0,
            "-": 0,
            "*": 1,
            "/": 1,
            "#": -1
        }
        ops = ["#"]
        nums = []
        s = s.replace(" ", "")
        s = s + "#"
        n = len(s)
        i = 0
        while i < n:
            if s[i].isdigit():
                temp_i = i
                while s[temp_i].isdigit():
                    temp_i += 1
                nums.append(int(s[i:temp_i]))
                i = temp_i
                continue
            else:
                if s[i] == "#":
                    while ops and ops[-1] != "#":
                        num1 = nums.pop()
                        num2 = nums.pop()
                        op = ops.pop()
                        nums.append(cal(op, num2, num1))
                    ops.pop()
                else:
                    while ops and priority[s[i]] <= priority[ops[-1]]:
                        num1 = nums.pop()
                        num2 = nums.pop()
                        op = ops.pop()
                        nums.append(cal(op, num2, num1))
                    ops.append(s[i])
            i += 1
        return nums[0]
