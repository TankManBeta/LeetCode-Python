# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2022/12/12 10:00
"""
from collections import defaultdict

"""
一个字符串的 美丽值 定义为：出现频率最高字符与出现频率最低字符的出现次数之差。
比方说，"abaacc" 的美丽值为 3 - 1 = 2 。
给你一个字符串 s ，请你返回它所有子字符串的 美丽值 之和。

示例 1：
输入：s = "aabcb"
输出：5
解释：美丽值不为零的字符串包括 ["aab","aabc","aabcb","abcb","bcb"] ，每一个字符串的美丽值都为 1 。

示例 2：
输入：s = "aabcbaa"
输出：17
"""
"""
思路：直接遍历所有子串，对每一个字串进行count，然后ans+=max_count-min_count
"""


class Solution:
    @staticmethod
    def beautySum(s: str) -> int:
        n = len(s)
        i = 0
        res = 0
        while i < n:
            count = defaultdict(int)
            j = i
            while j < n:
                count[s[j]] += 1
                values = sorted(count.values())
                max_count, min_count = values[-1], values[0]
                res += (max_count - min_count)
                j += 1
            i += 1
        return res
