# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2022/12/15 18:11
"""
from typing import List

"""
给定一个仅包含数字 0-9 的字符串 num 和一个目标值整数 target ，在 num 的数字之间添加 二元 运算符（不是一元）+、- 或 * ，
返回 所有 能够得到 target 的表达式。
注意，返回表达式中的操作数 不应该 包含前导零。

示例 1:
输入: num = "123", target = 6
输出: ["1+2+3", "1*2*3"] 
解释: “1*2*3” 和 “1+2+3” 的值都是6。

示例 2:
输入: num = "232", target = 8
输出: ["2*3+2", "2+3*2"]
解释: “2*3+2” 和 “2+3*2” 的值都是8。

示例 3:
输入: num = "3456237490", target = 9191
输出: []
解释: 表达式 “3456237490” 无法得到 9191 。
"""
"""
思路：设字符串 num 的长度为 nn，为构建表达式，我们可以往 num 中间的 n-1n−1 个空隙添加 + 号、 - 号或 * 号，或者不添加符号。
我们可以用「回溯法」来模拟这个过程。从左向右构建表达式，并实时计算表达式的结果。由于乘法运算优先级高于加法和减法运算，
我们还需要保存最后一个连乘串（如 2*3*4）的运算结果。
定义递归函数 backtrack(expr,i,res,mul)，其中：
    expr 为当前构建出的表达式；
    i 表示当前的枚举到了 num 的第 i 个数字；
    res 为当前表达式的计算结果；
    mul 为表达式最后一个连乘串的计算结果。
该递归函数分为两种情况：
    如果 i=n，说明表达式已经构造完成，若此时有 res=target，则找到了一个可行解，我们将 expr 放入答案数组中，递归结束；
    如果 i<n，需要枚举当前表达式末尾要添加的符号（+-*），以及该符号之后需要截取多少位数字。设该符号之后的数字为val，按符号分类讨论：
        若添加 + 号，则 res 增加 val，且 val 单独组成表达式最后一个连乘串；
        若添加 - 号，则 res 减少 val，且 −val 单独组成表达式最后一个连乘串；
        若添加 * 号，由于乘法运算优先级高于加法和减法运算，我们需要对 res 撤销之前 mul 的计算结果，并添加新的连乘结果 mul∗val，
        也就是将 res 减少 mul 并增加 mul∗val。
"""


class Solution:
    @staticmethod
    def addOperators(num: str, target: int) -> List[str]:
        n = len(num)
        ans = []

        def backtrack(expr: List[str], i: int, res: int, mul: int):
            if i == n:
                if res == target:
                    ans.append(''.join(expr))
                return
            signIndex = len(expr)
            if i > 0:
                expr.append('')  # 占位，下面填充符号
            val = 0
            for j in range(i, n):  # 枚举截取的数字长度（取多少位）
                if j > i and num[i] == '0':  # 数字可以是单个 0 但不能有前导零
                    break
                val = val * 10 + int(num[j])
                expr.append(num[j])
                if i == 0:  # 表达式开头不能添加符号
                    backtrack(expr, j + 1, val, val)
                else:  # 枚举符号
                    expr[signIndex] = '+'; backtrack(expr, j + 1, res + val, val)
                    expr[signIndex] = '-'; backtrack(expr, j + 1, res - val, -val)
                    expr[signIndex] = '*'; backtrack(expr, j + 1, res - mul + mul * val, mul * val)
            del expr[signIndex:]

        backtrack([], 0, 0, 0)
        return ans
