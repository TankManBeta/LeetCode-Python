# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2022/12/23 12:35
"""
from typing import List

"""
存在一种仅支持 4 种操作和 1 个变量 X 的编程语言：
    ++X 和 X++ 使变量 X 的值 加 1
    --X 和 X-- 使变量 X 的值 减 1
最初，X 的值是 0
给你一个字符串数组 operations ，这是由操作组成的一个列表，返回执行所有操作后， X 的 最终值 。

示例 1：
输入：operations = ["--X","X++","X++"]
输出：1
解释：操作按下述步骤执行：
最初，X = 0
--X：X 减 1 ，X =  0 - 1 = -1
X++：X 加 1 ，X = -1 + 1 =  0
X++：X 加 1 ，X =  0 + 1 =  1

示例 2：
输入：operations = ["++X","++X","X++"]
输出：3
解释：操作按下述步骤执行： 
最初，X = 0
++X：X 加 1 ，X = 0 + 1 = 1
++X：X 加 1 ，X = 1 + 1 = 2
X++：X 加 1 ，X = 2 + 1 = 3

示例 3：
输入：operations = ["X++","++X","--X","X--"]
输出：0
解释：操作按下述步骤执行：
最初，X = 0
X++：X 加 1 ，X = 0 + 1 = 1
++X：X 加 1 ，X = 1 + 1 = 2
--X：X 减 1 ，X = 2 - 1 = 1
X--：X 减 1 ，X = 1 - 1 = 0
"""
"""
思路：按要求模拟即可
"""


class Solution:
    @staticmethod
    def finalValueAfterOperations(operations: List[str]) -> int:
        res = 0
        for operation in operations:
            if '+' in operation:
                res += 1
            else:
                res -= 1
        return res
