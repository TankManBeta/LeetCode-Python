# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2022/3/8 9:58
"""
"""
给你一个长桌子，桌子上盘子和蜡烛排成一列。
给你一个下标从0开始的字符串s，它只包含字符'*'和'|'，其中'*'表示一个盘子，'|'表示一支蜡烛 。
同时给你一个下标从 0 开始的二维整数数组 queries ，其中 queries[i] = [lefti, righti] 表示 子字符串 s[lefti...righti] 
（包含左右端点的字符）。对于每个查询，你需要找到 子字符串中 在 两支蜡烛之间 的盘子的 数目 。如果一个盘子在 子字符串中左边和右边
都 至少有一支蜡烛，那么这个盘子满足在 两支蜡烛之间 。
比方说，s = "||**||**|*" ，查询 [3, 8] ，表示的是子字符串 "*||**|" 。子字符串中在两支蜡烛之间的盘子数目为 2 ，
子字符串中右边两个盘子在它们左边和右边 都 至少有一支蜡烛。
请你返回一个整数数组 answer ，其中 answer[i] 是第 i 个查询的答案。

输入：s = "**|**|***|", queries = [[2,5],[5,9]]
输出：[2,3]
解释：
- queries[0] 有两个盘子在蜡烛之间。
- queries[1] 有三个盘子在蜡烛之间。

输入：s = "***|**|*****|**||**|*", queries = [[1,17],[4,5],[14,17],[5,11],[15,16]]
输出：[9,0,0,0,0]
解释：
- queries[0] 有 9 个盘子在蜡烛之间。
- 另一个查询没有盘子在蜡烛之间。
"""
"""
思路：三个数组，第一个数组记录左边最近的蜡烛的位置，第二个记录右边最近的蜡烛的位置，第三个记录左边的蜡烛数，对于query来说，找
左边界的最右边的蜡烛位置，就是开始查找区间的起点；找右边界的左边的蜡烛位置就是开始查找的终点，计算两个区间之间的蜡烛数目的差。
注意边界
"""


class Solution(object):
    @staticmethod
    def plates_between_candles(s, queries):
        """
        :type s: str
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        n = len(s)
        left_index = [-1] * n
        right_index = [-1] * n
        if s[0] == '|':
            left_index[0] = 0
        if s[n - 1] == '|':
            right_index[n - 1] = n - 1
        for i in range(1, n):
            if s[i] == '|':
                left_index[i] = i
            else:
                left_index[i] = left_index[i - 1]
        for i in range(n - 2, -1, -1):
            if s[i] == '|':
                right_index[i] = i
            else:
                right_index[i] = right_index[i + 1]

        candles = [0] * n
        for i in range(0, n):
            if s[i] == '|':
                candles[i] = candles[i - 1]
            else:
                candles[i] = candles[i - 1] + 1

        res = []
        for l, r in queries:
            left = right_index[l]
            right = left_index[r]
            if left >= r - 1 or right <= l + 1:
                res.append(0)
            else:
                res.append(candles[right] - candles[left])

        return res
