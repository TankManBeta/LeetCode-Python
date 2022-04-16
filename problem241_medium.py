# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2022/4/15 20:32
"""
"""
给你一个由数字和运算符组成的字符串 expression ，按不同优先级组合数字和运算符，计算并返回所有可能组合的结果。
你可以 按任意顺序 返回答案。

输入：expression = "2-1-1"
输出：[0,2]
解释：
((2-1)-1) = 0 
(2-(1-1)) = 2

输入：expression = "2*3-4*5"
输出：[-34,-14,-10,-10,10]
解释：
(2*(3-(4*5))) = -34 
((2*3)-(4*5)) = -14 
((2*(3-4))*5) = -10 
(2*((3-4)*5)) = -10 
(((2*3)-4)*5) = 10
"""
"""
思路：以运算符作为分界进行分治，（1）分解：按运算符分成左右两部分，分别求解（2）解决：实现一个递归函数，输入算式，返回算式解
（3）合并：根据运算符合并左右两部分的解，得出最终解
"""


class Solution(object):
    def diffWaysToCompute(self, expression):
        """
        :type expression: str
        :rtype: List[int]
        """
        # 如果只有数字，直接返回
        if expression.isdigit():
            return [int(expression)]
        res = []
        for i, char in enumerate(expression):
            if char in ['+', '-', '*']:
                # 1.分解：遇到运算符，计算左右两侧的结果集
                # 2.解决：diffWaysToCompute 递归函数求出子问题的解
                left = self.diffWaysToCompute(expression[:i])
                right = self.diffWaysToCompute(expression[i+1:])
                # 3.合并：根据运算符合并子问题的解
                for l in left:
                    for r in right:
                        if char == '+':
                            res.append(l + r)
                        elif char == '-':
                            res.append(l - r)
                        else:
                            res.append(l * r)

        return res
