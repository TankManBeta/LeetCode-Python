# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2023/9/13 14:18
"""
import collections

"""
给定一个非负整数数组 A，如果该数组每对相邻元素之和是一个完全平方数，则称这一数组为正方形数组。
返回 A 的正方形排列的数目。两个排列 A1 和 A2 不同的充要条件是存在某个索引 i，使得 A1[i] != A2[i]。 

示例 1：
输入：[1,17,8]
输出：2
解释：
[1,8,17] 和 [17,8,1] 都是有效的排列。

示例 2：
输入：[2,2,2]
输出：1
"""
"""
思路：构造一张图，包含所有的边 i 到 j ，如果满足 A[i]+A[j] 是一个完全平方数。我们的目标就是求这张图的所有哈密顿路径，即经过图中所有点仅
一次的路径。我们使用 count 记录对于每一种值还有多少个节点等待被访问，与一个变量 todo 记录还剩多少个节点等待被访问。对于每一个节点，我们可以
访问它的所有邻居节点（从数值的角度来看，从而大大减少复杂度）。
"""


class Solution(object):
    @staticmethod
    def numSquarefulPerms(A):
        N = len(A)
        count = collections.Counter(A)

        graph = {x: [] for x in count}
        for x in count:
            for y in count:
                if int((x+y)**.5 + 0.5) ** 2 == x+y:
                    graph[x].append(y)

        def dfs(x, todo):
            count[x] -= 1
            if todo == 0:
                ans = 1
            else:
                ans = 0
                for y in graph[x]:
                    if count[y]:
                        ans += dfs(y, todo - 1)
            count[x] += 1
            return ans

        return sum(dfs(x, len(A) - 1) for x in count)
