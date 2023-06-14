# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2023/6/14 23:13
"""
from typing import List

"""
输入数字 n，按顺序打印出从 1 到最大的 n 位十进制数。比如输入 3，则打印出 1、2、3 一直到最大的 3 位数 999。

示例 1:
输入: n = 1
输出: [1,2,3,4,5,6,7,8,9]
"""
"""
思路：直接输出即可
"""


class Solution:
    @staticmethod
    def printNumbers(n: int) -> List[int]:
        return [i for i in range(1, 10 ** n)]
