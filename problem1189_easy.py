# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2022/2/13 10:20
"""
"""
给你一个字符串 text，你需要使用 text 中的字母来拼凑尽可能多的单词 "balloon"（气球）。
字符串 text 中的每个字母最多只能被使用一次。请你返回最多可以拼凑出多少个单词 "balloon"。

输入：text = "nlaebolko"
输出：1

输入：text = "loonbalxballpoon"
输出：2

输入：text = "leetcode"
输出：0
"""
"""
思路：直接统计计数即可
"""


class Solution(object):
    @staticmethod
    def max_number_of_balloons(text):
        """
        :type text: str
        :rtype: int
        """
        ans = [0]*5
        for char in text:
            if char == 'a':
                ans[0] += 1
            elif char == 'b':
                ans[1] += 1
            elif char == 'l':
                ans[2] += 1
            elif char == 'o':
                ans[3] += 1
            elif char == 'n':
                ans[4] += 1
        return min(ans[0], ans[1], ans[2]/2, ans[3]/2, ans[4])
