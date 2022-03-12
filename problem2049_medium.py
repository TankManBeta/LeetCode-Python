# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2022/3/11 10:41
"""
"""
给你一棵根节点为 0 的 二叉树 ，它总共有 n 个节点，节点编号为 0 到 n - 1 。
同时给你一个下标从 0 开始的整数数组 parents 表示这棵树，其中 parents[i] 是节点 i 的父节点。
由于节点 0 是根，所以 parents[0] == -1 。
一个子树的 大小 为这个子树内节点的数目。每个节点都有一个与之关联的 分数 。
求出某个节点分数的方法是，将这个节点和与它相连的边全部删除，剩余部分是若干个非空子树，这个节点的分数为所有这些子树大小的乘积 。
请你返回有 最高得分 节点的 数目 。

输入：parents = [-1,2,0,2,0]
输出：3
解释：
- 节点 0 的分数为：3 * 1 = 3
- 节点 1 的分数为：4 = 4
- 节点 2 的分数为：1 * 1 * 2 = 2
- 节点 3 的分数为：4 = 4
- 节点 4 的分数为：4 = 4
最高得分为 4 ，有三个节点得分为 4 （分别是节点 1，3 和 4 ）。

输入：parents = [-1,2,0]
输出：2
解释：
- 节点 0 的分数为：2 = 2
- 节点 1 的分数为：2 = 2
- 节点 2 的分数为：1 * 1 = 1
最高分数为 2 ，有两个节点分数为 2 （分别为节点 0 和 1 ）。
"""
"""
思路：拆变之后分为三个树，左子树，右子树，剩余节点组成的树，统计左右子树的节点数即可
"""


class Solution(object):
    def __init__(self):
        self.ans = 0
        self.max_score = 0

    def count_highest_score_codes(self, parents):
        """
        :type parents: List[int]
        :rtype: int
        """
        n = len(parents)
        children = [[] for _ in range(n)]
        for node, p in enumerate(parents):
            if p != -1:
                children[p].append(node)

        def dfs(root):
            score = 1
            size = n - 1
            for child in children[root]:
                sz = dfs(child)
                score *= sz
                size -= sz
            if root != 0:
                score *= size
            if score == self.max_score:
                self.ans += 1
            elif score > self.max_score:
                self.max_score, self.ans = score, 1
            return n - size

        dfs(0)
        return self.ans
