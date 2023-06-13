# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2023/6/12 21:00
"""
from typing import List

"""
给你一棵树，树上有 n 个节点，按从 0 到 n-1 编号。树以父节点数组的形式给出，其中 parent[i] 是节点 i 的父节点。树的根节点是编号为 0 的节点。
树节点的第 k 个祖先节点是从该节点到根节点路径上的第 k 个节点。
实现 TreeAncestor 类：
    TreeAncestor（int n， int[] parent） 对树和父数组中的节点数初始化对象。
    getKthAncestor(int node, int k) 返回节点 node 的第 k 个祖先节点。如果不存在这样的祖先节点，返回 -1 。

示例 1：
输入：
["TreeAncestor","getKthAncestor","getKthAncestor","getKthAncestor"]
[[7,[-1,0,0,1,1,2,2]],[3,1],[5,2],[6,3]]
输出：
[null,1,0,-1]
解释：
TreeAncestor treeAncestor = new TreeAncestor(7, [-1, 0, 0, 1, 1, 2, 2]);
treeAncestor.getKthAncestor(3, 1);  // 返回 1 ，它是 3 的父节点
treeAncestor.getKthAncestor(5, 2);  // 返回 0 ，它是 5 的祖父节点
treeAncestor.getKthAncestor(6, 3);  // 返回 -1 因为不存在满足要求的祖先节点
"""
"""
思路：我们定义 p[i][j] 表示节点 i 的第 2**j 个祖先节点，即 p[i][j] 表示节点 i 向上走 2**j  步的节点。那么我们可以得到状态转移
方程：p[i][j]=p[p[i][j−1]][j−1]即：要想找到节点 i 的第 2**j 个祖先节点，我们可以先找到节点 i 的第 2**(j−1) 个祖先节点，然后
再找到该节点的第 2**(j−1) 个祖先节点即可。所以，我们要找到每个节点的距离为 2**j 的祖先节点，直到达到树的最大高度。之后对于每次
查询，我们可以把 k 拆成二进制的表示形式，然后根据二进制中 1 的位置，累计向上查询，最终得到节点 node 的第 k 个祖先节点。
"""


class TreeAncestor:

    def __init__(self, n: int, parent: List[int]):
        self.p = [[-1] * 18 for _ in range(n)]
        for i, fa in enumerate(parent):
            self.p[i][0] = fa
        for i in range(n):
            for j in range(1, 18):
                if self.p[i][j - 1] == -1:
                    continue
                self.p[i][j] = self.p[self.p[i][j - 1]][j - 1]

    def getKthAncestor(self, node: int, k: int) -> int:
        for i in range(17, -1, -1):
            if k >> i & 1:
                node = self.p[node][i]
                if node == -1:
                    break
        return node


# Your TreeAncestor object will be instantiated and called as such:
# obj = TreeAncestor(n, parent)
# param_1 = obj.getKthAncestor(node,k)
