# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2023/4/16 13:30
"""
from collections import defaultdict
from typing import List

"""
有 n 个花园，按从 1 到 n 标记。另有数组 paths ，其中 paths[i] = [xi, yi] 描述了花园 xi 到花园 yi 的双向路径。在每个花园中，
你打算种下四种花之一。另外，所有花园 最多 有 3 条路径可以进入或离开。你需要为每个花园选择一种花，使得通过路径相连的任何两个花园
中的花的种类互不相同。以数组形式返回 任一 可行的方案作为答案 answer，其中 answer[i] 为在第 (i+1) 个花园中种植的花的种类。
花的种类用  1、2、3、4 表示。保证存在答案。 

示例 1：
输入：n = 3, paths = [[1,2],[2,3],[3,1]]
输出：[1,2,3]
解释：
花园 1 和 2 花的种类不同。
花园 2 和 3 花的种类不同。
花园 3 和 1 花的种类不同。
因此，[1,2,3] 是一个满足题意的答案。其他满足题意的答案有 [1,2,4]、[1,4,2] 和 [3,2,1]

示例 2：
输入：n = 4, paths = [[1,2],[3,4]]
输出：[1,2,1,2]

示例 3：
输入：n = 4, paths = [[1,2],[2,3],[3,4],[4,1],[1,3],[2,4]]
输出：[1,2,3,4]
"""
"""
思路：我们先根据数组 paths 构建图 g，其中 g[x] 表示与花园 x 相邻的花园列表。接下来，对于每个花园 x，我们先找出与 x 相邻的花园 
y，并将 y 花园中种植的花的种类标记为已使用。然后我们从花的种类 1 开始枚举，直到找到一个未被使用的花的种类 c，将 c 标记为 x 花园
中种植的花的种类，然后继续枚举下一个花园。
"""


class Solution:
    @staticmethod
    def gardenNoAdj(n: int, paths: List[List[int]]) -> List[int]:
        g = defaultdict(list)
        for x, y in paths:
            x, y = x - 1, y - 1
            g[x].append(y)
            g[y].append(x)
        ans = [0] * n
        for x in range(n):
            used = {ans[y] for y in g[x]}
            for c in range(1, 5):
                if c not in used:
                    ans[x] = c
                    break
        return ans
