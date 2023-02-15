# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2023/2/14 11:25
"""
from typing import List

"""
给你一份工作时间表 hours，上面记录着某一位员工每天的工作小时数。
我们认为当员工一天中的工作小时数大于 8 小时的时候，那么这一天就是「劳累的一天」。
所谓「表现良好的时间段」，意味在这段时间内，「劳累的天数」是严格 大于「不劳累的天数」。
请你返回「表现良好时间段」的最大长度。 

示例 1：
输入：hours = [9,9,6,0,6,6,9]
输出：3
解释：最长的表现良好时间段是 [9,9,6]。

示例 2：
输入：hours = [6,6,6]
输出：0
"""
"""
思路：前缀和+哈希表。如果hour>0，s++；否则，s--。如果当前s>0，则说明0-i时间段是一个表现良好的时间段，更新ans；否则的话我们查看
s-1是否在哈希表当中，如果在哈希表中，则说明j+1-i时间段是一个表现良好时间段，因为它把s从s-1变到了s，所以我们更新ans。如果s-1不在
哈希表中，就把它加入哈希表即可。
"""


class Solution:
    @staticmethod
    def longestWPI(hours: List[int]) -> int:
        ans = 0
        pos = {}
        s = 0
        for i, hour in enumerate(hours):
            s += 1 if hour > 8 else -1
            if s > 0:
                ans = i+1
            elif s-1 in pos:
                ans = max(ans, i - pos[s-1])
            if s not in pos:
                pos[s] = i
        return ans
