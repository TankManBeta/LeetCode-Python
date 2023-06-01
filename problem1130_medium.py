# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2023/5/31 11:34
"""
from typing import List

"""
给你一个正整数数组 arr，考虑所有满足以下条件的二叉树：
    每个节点都有 0 个或是 2 个子节点。
    数组 arr 中的值与树的中序遍历中每个叶节点的值一一对应。
    每个非叶节点的值等于其左子树和右子树中叶节点的最大值的乘积。
在所有这样的二叉树中，返回每个非叶节点的值的最小可能总和。这个和的值是一个 32 位整数。
如果一个节点有 0 个子节点，那么该节点为叶节点。 

示例 1：
输入：arr = [6,2,4]
输出：32
解释：有两种可能的树，第一种的非叶节点的总和为 36 ，第二种非叶节点的总和为 32 。 

示例 2：
输入：arr = [4,11]
输出：44
"""
"""
思路：
（1）递归。函数 dfs(i,j) 的计算过程如下：如果 i=j，说明数组 arr[i..j] 中只有一个元素，没有非叶节点，因此 dfs(i,j)=0。否则，
我们枚举 k∈[i,j−1]，将数组 arr 划分为两个子数组 arr[i⋯k] 和 arr[k+1⋯j]，对于每个 k，我们递归计算 dfs(i,k) 和 dfs(k+1,j)，
其中 dfs(i,k) 表示数组 arr 中下标范围 [i,k] 内的所有非叶节点的值的最小可能总和，而 dfs(k+1,j) 表示数组 arr 中下标范围 [k+1,j] 
内的所有非叶节点的值的最小可能总和，那么 dfs(i,j)=min i≤k<j {dfs(i,k)+dfs(k+1,j)+max i≤t≤k {arr[t]}max k<t≤j {arr[t]}}。
上述递归过程中，我们可以使用记忆化搜索的方法，避免重复计算。另外，我们还可以使用数组 g 记录数组 arr 中下标范围 [i,j] 内的所有
叶节点的最大值
（2）动态规划，定义 f[i][j] 表示数组 arr 中下标范围 [i,j] 内的所有非叶节点的值的最小可能总和，而 g[i][j] 表示数组 arr 中
下标范围 [i,j] 内的所有叶节点的最大值。
"""


class Solution:
    @staticmethod
    def mctFromLeafValues(arr: List[int]) -> int:
        # @cache
        # def dfs(i: int, j: int) -> int:
        #     if i == j:
        #         return 0
        #     return min(dfs(i, k) + dfs(k + 1, j) + g[i][k] * g[k + 1][j] for k in range(i, j))

        # n = len(arr)
        # g = [[0] * n for _ in range(n)]
        # for i in range(n - 1, -1, -1):
        #     g[i][i] = arr[i]
        #     for j in range(i + 1, n):
        #         g[i][j] = max(g[i][j - 1], arr[j])
        # return dfs(0, n - 1)

        n = len(arr)
        f = [[0] * n for _ in range(n)]
        g = [[0] * n for _ in range(n)]
        for i in range(n - 1, -1, -1):
            g[i][i] = arr[i]
            for j in range(i + 1, n):
                g[i][j] = max(g[i][j - 1], arr[j])
                f[i][j] = min(f[i][k] + f[k + 1][j] + g[i][k] * g[k + 1][j] for k in range(i, j))
        return f[0][n - 1]
