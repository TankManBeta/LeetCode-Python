# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2023/5/2 1:52
"""
import math
from typing import List

"""
给定三个整数 x 、 y 和 bound ，返回 值小于或等于 bound 的所有 强整数 组成的列表 。
如果某一整数可以表示为 xi + yj ，其中整数 i >= 0 且 j >= 0，那么我们认为该整数是一个 强整数 。
你可以按 任何顺序 返回答案。在你的回答中，每个值 最多 出现一次。 

示例 1：
输入：x = 2, y = 3, bound = 10
输出：[2,3,4,5,7,9,10]
解释： 
2 = 20 + 30
3 = 21 + 30
4 = 20 + 31
5 = 21 + 31
7 = 22 + 31
9 = 23 + 30
10 = 20 + 32

示例 2：
输入：x = 3, y = 5, bound = 15
输出：[2,4,6,8,10,14]
"""
"""
思路：直接枚举即可
"""


class Solution:
    @staticmethod
    def powerfulIntegers(x: int, y: int, bound: int) -> List[int]:
        # ans = set()
        # for i in range(21):
        #     for j in range(21):
        #         tmp = x**i + y**j
        #         if tmp <= bound:
        #             ans.add(tmp)
        # return list(ans)

        if bound == 0:
            return []
        ans = set()
        m = int(math.log(bound, x)) if x != 1 else 0
        n = int(math.log(bound, y)) if y != 1 else 0
        for i in range(m + 1):
            for j in range(n + 1):
                tmp = x ** i + y ** j
                if tmp <= bound:
                    ans.add(tmp)
        return list(ans)
