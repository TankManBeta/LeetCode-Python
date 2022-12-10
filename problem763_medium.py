# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2022/12/9 17:42
"""
from typing import List

"""
给你一个字符串 s 。我们要把这个字符串划分为尽可能多的片段，同一字母最多出现在一个片段中。
注意，划分结果需要满足：将所有划分结果按顺序连接，得到的字符串仍然是 s 。
返回一个表示每个字符串片段的长度的列表。

示例 1：
输入：s = "ababcbacadefegdehijhklij"
输出：[9,7,8]
解释：
划分结果为 "ababcbaca"、"defegde"、"hijhklij" 。
每个字母最多出现在一个片段中。
像 "ababcbacadefegde", "hijhklij" 这样的划分是错误的，因为划分的片段数较少。 

示例 2：
输入：s = "eccbbbbdec"
输出：[10]
"""
"""
思路：贪心，首先找到每一个字母出现的最后的位置，然后遍历s，对于每一个字母而言，更新end为当前字母能到达的最远位置和end之间的最大值，
当i==end时，说明当前子串遍历结束，start=end+1，生成下一个子串
"""


class Solution:
    @staticmethod
    def partitionLabels(s: str) -> List[int]:
        last = [0] * 26
        for i, letter in enumerate(s):
            last[ord(letter) - ord('a')] = i

        res = []
        start = end = 0
        for i, letter in enumerate(s):
            end = max(end, last[ord(letter) - ord('a')])
            if i == end:
                res.append(end - start + 1)
                start = end + 1
        return res
