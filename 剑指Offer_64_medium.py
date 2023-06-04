# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2023/6/3 10:43
"""
"""
求 1+2+...+n ，要求不能使用乘除法、for、while、if、else、switch、case等关键字及条件判断语句（A?B:C）。

示例 1：
输入: n = 3
输出: 6

示例 2：
输入: n = 9
输出: 45
"""
"""
思路：
（1）本题需要实现 “当 n=1 时终止递归” 的需求，可通过短路效应实现。n > 1 && sumNums(n - 1) // 当 n = 1 时 n > 1 不成立 ，
此时 “短路” ，终止后续递归
（2）python的 and 操作如果最后结果为真，返回最后一个表达式的值，or 操作如果结果为真，返回第一个结果为真的表达式的值
"""


# class Solution:
#     def __init__(self):
#         self.res = 0
#     def sumNums(self, n: int) -> int:
#         n > 1 and self.sumNums(n - 1)
#         self.res += n
#         return self.res

class Solution:
    def sumNums(self, n: int) -> int:
        return n and (n + self.sumNums(n - 1))
