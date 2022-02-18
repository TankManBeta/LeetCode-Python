# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2022/2/18 11:04
"""
"""
有一个无向的星型图，由 n 个编号从 1 到 n 的节点组成。星型图有一个 中心 节点，并且恰有n - 1条边将中心节点与其他每个节点连接起来。
给你一个二维整数数组edges，其中edges[i] = [ui, vi]表示在节点ui和vi之间存在一条边。请你找出并返回edges所表示星型图的中心节点。

输入：edges = [[1,2],[2,3],[4,2]]
输出：2
解释：如上图所示，节点 2 与其他每个节点都相连，所以节点 2 是中心节点。

输入：edges = [[1,2],[5,1],[1,3],[1,4]]
输出：1
"""
"""
思路：找前两个edge中出现次数多的顶点即可
"""


class Solution(object):
    @staticmethod
    def find_center(edges):
        """
        :type edges: List[List[int]]
        :rtype: int
        """
        res_dict = {}
        res_dict[edges[0][0]] = res_dict.get(edges[0][0], 0)+1
        res_dict[edges[0][1]] = res_dict.get(edges[0][1], 0)+1
        res_dict[edges[1][0]] = res_dict.get(edges[1][0], 0)+1
        res_dict[edges[1][1]] = res_dict.get(edges[1][1], 0)+1
        return edges[1][0] if res_dict[edges[1][0]] == 2 else edges[1][1]
