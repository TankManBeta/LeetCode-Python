# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2022/4/8 14:20
"""

"""
给你一个字符串表达式 s ，请你实现一个基本计算器来计算并返回它的值。
注意:不允许使用任何将字符串作为数学表达式计算的内置函数，比如 eval() 。

输入：s = "1 + 1"
输出：2

输入：s = " 2-1 + 2 "
输出：3

输入：s = "(1+(4+5+2)-3)+(6+8)"
输出：23
"""
"""
思路：两个栈，ops维护运算符，nums维护运算数，给各个运算符制定优先级，如果当前入栈的运算符优先级小于等于当前栈顶运算符的优先级，
nums弹两个数，ops弹一个运算符进行运算，否则入栈，重复操作即可
"""


class Solution(object):
    @staticmethod
    def calculate(s):
        """
        :type s: str
        :rtype: int
        """

        def calculate(operator, a, b):
            if operator == "+":
                return a + b
            if operator == "-":
                return a - b
            if operator == "*":
                return a * b
            if operator == "/":
                return a / b

        s = s.replace(" ", "")
        s = s.replace("(-", "(0-")
        s = s.replace("(+", "(0+")
        s = s + ")"
        prior = {
            "+": 0,
            "-": 0,
            "*": 1,
            "/": 1,
            "(": -1
        }
        if s[0] == "-":
            nums = [0]
        else:
            nums = []
        ops = ["("]
        n = len(s)
        i = 0
        while i < n:
            if s[i].isdigit():
                temp_i = i
                while temp_i < n and s[temp_i].isdigit():
                    temp_i += 1
                nums.append(int(s[i:temp_i]))
                i = temp_i
                continue
            else:
                if s[i] == "(":
                    ops.append(s[i])
                elif s[i] == ")":
                    while ops and ops[-1] != "(":
                        num1 = nums.pop()
                        num2 = nums.pop()
                        op = ops.pop()
                        nums.append(calculate(op, num2, num1))
                    ops.pop()
                else:
                    while ops and prior[s[i]] <= prior[ops[-1]]:
                        num1 = nums.pop()
                        num2 = nums.pop()
                        op = ops.pop()
                        nums.append(calculate(op, num2, num1))
                    ops.append(s[i])
            i += 1
        return nums[0]
