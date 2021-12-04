# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2021/12/2 14:47
"""
"""
数字 n 代表生成括号的对数，请你设计一个函数，用于能够生成所有可能的并且 有效的 括号组合。

输入：n = 3
输出：["((()))","(()())","(())()","()(())","()()()"]

输入：n = 1
输出：["()"]
"""
"""
思路：
（1）最初的思路：直接用递归穷举，然后判断合法性
（2）看完题解改进思路：如果左右括号数量相等，下一个只能是左括号；
如果左有括号数量不等，若左括号数量不为0，下一个左右括号都可，否则只能是右括号
"""


class Solution(object):
    @staticmethod
    def generate_parenthesis(n):
        """
        :type n: int
        :rtype: List[str]
        """
        combination = list()
        combinations = list()

        def traceback(left, right):
            if left == 0 and right == 0:
                combinations.append(''.join(combination))
                return
            else:
                if left == right:
                    combination.append('(')
                    traceback(left-1, right)
                    combination.pop()
                else:
                    if left > 0:
                        combination.append('(')
                        traceback(left-1, right)
                        combination.pop()
                    combination.append(')')
                    traceback(left, right-1)
                    combination.pop()
        traceback(n, n)
        return combinations
