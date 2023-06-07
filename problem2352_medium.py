# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2023/6/6 21:01
"""
from collections import Counter
from typing import List

"""
给你一个下标从 0 开始、大小为 n x n 的整数矩阵 grid ，返回满足 Ri 行和 Cj 列相等的行列对 (Ri, Cj) 的数目。
如果行和列以相同的顺序包含相同的元素（即相等的数组），则认为二者是相等的。

示例 1：
输入：grid = [[3,2,1],[1,7,6],[2,7,7]]
输出：1
解释：存在一对相等行列对：
- (第 2 行，第 1 列)：[2,7,7]

示例 2：
输入：grid = [[3,1,2,2],[1,4,4,5],[2,4,2,2],[2,4,2,2]]
输出：3
解释：存在三对相等行列对：
- (第 0 行，第 0 列)：[3,1,2,2]
- (第 2 行, 第 2 列)：[2,4,2,2]
- (第 3 行, 第 2 列)：[2,4,2,2]
"""
"""
思路：
（1）把每一列存到grid1里，然后遍历看grid[i]和grid[j]是否一样，一样就ans++。
（2）首先将矩阵的行放入哈希表中统计次数，哈希表的键可以是将行拼接后的字符串，也可以用各语言内置的数据结构，然后分别统计每一列
相等的行有多少，求和即可。
"""


class Solution:
    @staticmethod
    def equalPairs(grid: List[List[int]]) -> int:
        # n = len(grid)
        # grid1 = []
        # for j in range(n):
        #     tmp = []
        #     for i in range(n):
        #         tmp.append(grid[i][j])
        #     grid1.append(tmp)
        # ans = 0
        # for i in range(n):
        #     for j in range(n):
        #         if grid[i] == grid1[j]:
        #             ans += 1
        # return ans

        res, n = 0, len(grid)
        cnt = Counter(tuple(row) for row in grid)
        res = 0
        for j in range(n):
            res += cnt[tuple([grid[i][j] for i in range(n)])]
        return res
