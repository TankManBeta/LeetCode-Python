# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2023/6/8 22:08
"""
"""
你是一位施工队的工长，根据设计师的要求准备为一套设计风格独特的房子进行室内装修。
房子的客厅大小为 n x m，为保持极简的风格，需要使用尽可能少的 正方形 瓷砖来铺盖地面。
假设正方形瓷砖的规格不限，边长都是整数。
请你帮设计师计算一下，最少需要用到多少块方形瓷砖？

示例 1：
输入：n = 2, m = 3
输出：3
解释：3 块地砖就可以铺满卧室。
     2 块 1x1 地砖
     1 块 2x2 地砖

示例 2：
输入：n = 5, m = 8
输出：5

示例 3：
输入：n = 11, m = 13
输出：6
"""
"""
思路：我们可以按位置进行递归回溯，过程中我们用一个变量 t 记录当前使用的瓷砖数。
    如果 j=m，即第 i 行已经被完全填充，则递归到下一行，即 (i+1,0)。
    如果 i=n，则表示所有位置都已经被填充，我们更新答案并返回。
    如果当前位置 (i,j) 已经被填充，则直接递归到下一个位置 (i,j+1)。
    否则，我们枚举当前位置 (i,j) 可以填充的最大正方形的边长 w，并将当前位置 (i,j) 到 (i+w−1,j+w−1) 的位置全部填充，然后递归到
    下一个位置 (i,j+w)。在回溯时，我们需要将当前位置 (i,j) 到 (i+w−1,j+w−1) 的位置全部清空。
由于每个位置只有两种状态：填充或者未填充，因此我们可以使用一个整数来表示当前位置的状态。我们使用一个长度为 n 的整数数组 filled，
其中 filled[i] 表示第 i 行的状态。如果 filled[i] 的第 j 位为 1，则表示第 i 行第 j 列已经被填充，否则表示未填充。
"""


class Solution:
    @staticmethod
    def tilingRectangle(n: int, m: int) -> int:
        def dfs(i: int, j: int, t: int):
            nonlocal ans
            if j == m:
                i += 1
                j = 0
            if i == n:
                ans = t
                return
            if filled[i] >> j & 1:
                dfs(i, j + 1, t)
            elif t + 1 < ans:
                r = c = 0
                for k in range(i, n):
                    if filled[k] >> j & 1:
                        break
                    r += 1
                for k in range(j, m):
                    if filled[i] >> k & 1:
                        break
                    c += 1
                mx = r if r < c else c
                for w in range(1, mx + 1):
                    for k in range(w):
                        filled[i + w - 1] |= 1 << (j + k)
                        filled[i + k] |= 1 << (j + w - 1)
                    dfs(i, j + w, t + 1)
                for x in range(i, i + mx):
                    for y in range(j, j + mx):
                        filled[x] ^= 1 << y

        ans = n * m
        filled = [0] * n
        dfs(0, 0, 0)
        return ans
