# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2022/3/15 10:03
"""
"""
根据 逆波兰表示法，求表达式的值。
有效的算符包括 +、-、*、/ 。每个运算对象可以是整数，也可以是另一个逆波兰表达式。
注意 两个整数之间的除法只保留整数部分。
可以保证给定的逆波兰表达式总是有效的。换句话说，表达式总会得出有效数值且不存在除数为 0 的情况。

输入：tokens = ["2","1","+","3","*"]
输出：9
解释：该算式转化为常见的中缀算术表达式为：((2 + 1) * 3) = 9

输入：tokens = ["4","13","5","/","+"]
输出：6
解释：该算式转化为常见的中缀算术表达式为：(4 + (13 / 5)) = 6

输入：tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
输出：22
解释：该算式转化为常见的中缀算术表达式为：
  ((10 * (6 / ((9 + 3) * -11))) + 17) + 5
= ((10 * (6 / (12 * -11))) + 17) + 5
= ((10 * (6 / -132)) + 17) + 5
= ((10 * 0) + 17) + 5
= (0 + 17) + 5
= 17 + 5
= 22
"""
"""
思路：遇到运算符就从栈里弹两个计算，再将结果进栈即可，注意：python负数是下取整
"""


class Solution(object):
    @staticmethod
    def eval_rpn(tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        import math
        stack = []
        for token in tokens:
            if token == '+':
                a = stack.pop()
                b = stack.pop()
                c = a + b
                stack.append(c)
            elif token == '-':
                a = stack.pop()
                b = stack.pop()
                c = b - a
                stack.append(c)
            elif token == '*':
                a = stack.pop()
                b = stack.pop()
                c = a * b
                stack.append(c)
            elif token == '/':
                a = stack.pop()
                b = stack.pop()
                if (a < 0 < b) or (a > 0 > b):
                    c = math.ceil(float(b) / a)
                else:
                    c = b / a
                c = int(c)
                stack.append(c)
            else:
                stack.append(int(token))
        return stack[-1]
