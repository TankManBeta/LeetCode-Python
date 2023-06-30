# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2023/6/29 20:32
"""
from typing import List

"""
给你一个 2 行 n 列的二进制数组：
    矩阵是一个二进制矩阵，这意味着矩阵中的每个元素不是 0 就是 1。
    第 0 行的元素之和为 upper。
    第 1 行的元素之和为 lower。
    第 i 列（从 0 开始编号）的元素之和为 colsum[i]，colsum 是一个长度为 n 的整数数组。
你需要利用 upper，lower 和 colsum 来重构这个矩阵，并以二维整数数组的形式返回它。
如果有多个不同的答案，那么任意一个都可以通过本题。
如果不存在符合要求的答案，就请返回一个空的二维数组。 

示例 1：
输入：upper = 2, lower = 1, colsum = [1,1,1]
输出：[[1,1,0],[0,0,1]]
解释：[[1,0,1],[0,1,0]] 和 [[0,1,1],[1,0,0]] 也是正确答案。

示例 2：
输入：upper = 2, lower = 3, colsum = [2,2,1,1]
输出：[]

示例 3：
输入：upper = 5, lower = 5, colsum = [2,1,2,0,1,0,1,2,0,1]
输出：[[1,1,1,0,1,0,0,1,0,0],[1,0,1,0,0,0,1,1,0,1]]
"""
"""
思路：我们先创建一个答案数组 ans，其中 ans[0] 和 ans[1] 分别表示矩阵的第一行和第二行。接下来，从左到右遍历数组 colsum，对于
当前遍历到的元素 colsum[j]，我们有以下几种情况：如果 colsum[j]=2，那么我们将 ans[0][j] 和 ans[1][j] 都置为 1。此时 upper 和 
lower 都减去 1。如果 colsum[j]=1，那么我们将 ans[0][j] 或 ans[1][j] 置为 1。如果 upper>lower，那么我们优先将 ans[0][j] 置为 
1，否则我们优先将 ans[1][j] 置为 1。此时 upper 或 lower 减去 1。如果 colsum[j]=0，那么我们将 ans[0][j] 和 ans[1][j] 都置为 
0。如果 upper<0 或 lower<0，那么说明无法构造出满足要求的矩阵，我们返回一个空数组。遍历结束，如果 upper 和 lower 都为 0，那么
我们返回 ans，否则我们返回一个空数组。
"""


class Solution:
    @staticmethod
    def reconstructMatrix(upper: int, lower: int, colsum: List[int]) -> List[List[int]]:
        n = len(colsum)
        ans = [[0] * n for _ in range(2)]
        for j, v in enumerate(colsum):
            if v == 2:
                ans[0][j] = ans[1][j] = 1
                upper, lower = upper - 1, lower - 1
            if v == 1:
                if upper > lower:
                    upper -= 1
                    ans[0][j] = 1
                else:
                    lower -= 1
                    ans[1][j] = 1
            if upper < 0 or lower < 0:
                return []
        return ans if lower == upper == 0 else []
