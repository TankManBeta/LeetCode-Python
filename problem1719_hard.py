# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2023/2/7 23:51
"""
from collections import defaultdict
from sys import maxsize
from typing import List

"""
给你一个数组 pairs ，其中 pairs[i] = [xi, yi] ，并且满足：
    pairs 中没有重复元素
    xi < yi
令 ways 为满足下面条件的有根树的方案数：
    树所包含的所有节点值都在 pairs 中。
    一个数对 [xi, yi] 出现在 pairs 中 当且仅当 xi 是 yi 的祖先或者 yi 是 xi 的祖先。
    注意：构造出来的树不一定是二叉树。
两棵树被视为不同的方案当存在至少一个节点在两棵树中有不同的父节点。
请你返回：
    如果 ways == 0 ，返回 0 。
    如果 ways == 1 ，返回 1 。
    如果 ways > 1 ，返回 2 。
一棵 有根树 指的是只有一个根节点的树，所有边都是从根往外的方向。
我们称从根到一个节点路径上的任意一个节点（除去节点本身）都是该节点的 祖先 。根节点没有祖先。

示例 1：
输入：pairs = [[1,2],[2,3]]
输出：1
解释：如上图所示，有且只有一个符合规定的有根树。

示例 2：
输入：pairs = [[1,2],[2,3],[1,3]]
输出：2
解释：有多个符合规定的有根树，其中三个如上图所示。

示例 3：
输入：pairs = [[1,2],[2,3],[2,4],[1,5]]
输出：0
解释：没有符合规定的有根树。
"""
"""
思路：首先我们需要找到根节点 root，通过上述结论，我们找到满足 degree[root]=n−1 的节点，如果不存在根节点，则认为其不能构成
合法的树，返回 0。
我们需要利用上述的结论检测是构建的树是否合法，遍历每个节点 nodei，找到 nodei 的祖先 parenti，检测集合 adj[nodei] 是否为 
adj[parenti] 的子集。可以利用 degree[nodei]≤degree[parenti] 找到所有属于 nodei 的祖先节点，然后依次检测是否满足 adj[nodei]
∈adj[parenti]，如果不满足要求，则认为构建的树为非法，返回 0。
实际检测过程中不必检测节点 nodei 的所有祖先节点，只需要检测节点 nodei 的父节点是否满足子集包含的要求即可。根据上述推论找到节点 
x 满足 degree[x] 最小且 degree[x]≥degree[nodei]，则此时找到的节点为节点 nodei 的父亲节点，此时只需检测父亲节点是否满足上述要求即可。
设 nodei 的父节点为 parent，若满足 degree[nodei]=degree[parent] 则树的构造方式可以有多个，返回 2。
"""


class Solution:
    def checkWays(self, pairs: List[List[int]]) -> int:
        adj = defaultdict(set)
        for x, y in pairs:
            adj[x].add(y)
            adj[y].add(x)

        # 检测是否存在根节点
        root = next((node for node, neighbours in adj.items() if len(neighbours) == len(adj) - 1), -1)
        if root == -1:
            return 0

        ans = 1
        for node, neighbours in adj.items():
            if node == root:
                continue

            currDegree = len(neighbours)
            parent = -1
            parentDegree = maxsize
            # 根据 degree 的大小找到 node 的父节点 parent
            for neighbour in neighbours:
                if currDegree <= len(adj[neighbour]) < parentDegree:
                    parent = neighbour
                    parentDegree = len(adj[neighbour])
            # 检测 neighbours 是否为 adj[parent] 的子集
            if parent == -1 or any(neighbour != parent and neighbour not in adj[parent] for neighbour in neighbours):
                return 0

            if parentDegree == currDegree:
                ans = 2
        return ans
