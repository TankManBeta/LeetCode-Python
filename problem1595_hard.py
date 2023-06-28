# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2023/6/20 21:43
"""
from cmath import inf
from typing import List

"""
给你两组点，其中第一组中有 size1 个点，第二组中有 size2 个点，且 size1 >= size2 。
任意两点间的连接成本 cost 由大小为 size1 x size2 矩阵给出，其中 cost[i][j] 是第一组中的点 i 和第二组中的点 j 的连接成本。
如果两个组中的每个点都与另一组中的一个或多个点连接，则称这两组点是连通的。换言之，第一组中的每个点必须至少与第二组中的一个点连接，
且第二组中的每个点必须至少与第一组中的一个点连接。
返回连通两组点所需的最小成本。

示例 1：
输入：cost = [[15, 96], [36, 2]]
输出：17
解释：连通两组点的最佳方法是：
1--A
2--B
总成本为 17 。

示例 2：
输入：cost = [[1, 3, 5], [4, 1, 1], [1, 5, 3]]
输出：4
解释：连通两组点的最佳方法是：
1--A
2--B
2--C
3--A
最小成本为 4 。
请注意，虽然有多个点连接到第一组中的点 2 和第二组中的点 A ，但由于题目并不限制连接点的数目，所以只需要关心最低总成本。

示例 3：
输入：cost = [[2, 5, 1], [3, 4, 7], [8, 1, 2], [6, 2, 4], [3, 8, 8]]
输出：10
"""
"""
思路：我们记第一组的点数为 m，第二组的点数为 n。由于 1≤n≤m≤12，因此，我们可以用一个整数来表示第二组中点的状态，即二进制表示的
一个长度为 n 的整数，其中第 k 位为 1 表示第二组中的第 k 个点与第一组中的点连通，为 0 表示不连通。
接下来，我们定义 f[i][j] 表示第一组中的前 i 个点已经全部连通，且第二组中的点的状态为 j 时的最小成本。初始时 f[0][0]=0，其余值
均为正无穷大。答案即为 f[m][2**n−1]。考虑 f[i][j]，其中 i≥1。我们可以枚举第二组中的每个点 k，如果点 k 与第一组中的第 i 个点连通，
那么我们可以分以下两种情况讨论：
    如果点 k 只与第一组中的第 i 个点连通，那么 f[i][j] 可以从 f[i][j⊕2**k]（第二组中的第k个不与其他联通） 或者 f[i−1][j⊕2**k]
    （第二组第k个和第一组第i-1个都不与其他联通）转移而来，其中 ⊕ 表示异或运算；
    如果点 k 与第一组中的第 i 个点以及其他点都连通，那么 f[i][j] 可以从 f[i−1][j] 转移而来。
在上述两种情况中，我们需要选择转移值最小的那个，即有：f[i][j]= k∈{0,1,⋯,n−1}min{f[i][j⊕2**k],f[i−1][j⊕2**k],f[i−1][j]}+cost[i−1][k]
最后，我们返回 f[m][2**n−1] 即可。
"""


class Solution:
    @staticmethod
    def connectTwoGroups(cost: List[List[int]]) -> int:
        m, n = len(cost), len(cost[0])
        f = [[inf] * (1 << n) for _ in range(m + 1)]
        f[0][0] = 0
        for i in range(1, m + 1):
            for j in range(1 << n):
                for k in range(n):
                    if (j >> k & 1) == 0:
                        continue
                    c = cost[i - 1][k]
                    x = min(f[i][j ^ (1 << k)], f[i - 1][j], f[i - 1][j ^ (1 << k)]) + c
                    f[i][j] = min(f[i][j], x)
        return f[m][-1]