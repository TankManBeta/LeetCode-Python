# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2022/11/29 9:47
"""
"""
给你一个仅由字符 '0' 和 '1' 组成的字符串 s 。一步操作中，你可以将任一 '0' 变成 '1' ，或者将 '1' 变成 '0' 。
交替字符串 定义为：如果字符串中不存在相邻两个字符相等的情况，那么该字符串就是交替字符串。
例如，字符串 "010" 是交替字符串，而字符串 "0100" 不是。
返回使 s 变成 交替字符串 所需的 最少 操作数。

示例 1：
输入：s = "0100"
输出：1
解释：如果将最后一个字符变为 '1' ，s 就变成 "0101" ，即符合交替字符串定义。

示例 2：
输入：s = "10"
输出：0
解释：s 已经是交替字符串。

示例 3：
输入：s = "1111"
输出：2
解释：需要 2 步操作得到 "0101" 或 "1010" 。
"""
"""
思路：直接按照规则排列，然后看两种情况的最小值
"""


class Solution:
    @staticmethod
    def minOperations(s: str) -> int:
        s = list(s)
        n = len(s)
        i = 0
        count = 0
        while i < n - 1:
            if s[i] == s[i + 1]:
                if s[i] == '0':
                    s[i + 1] = '1'
                else:
                    s[i + 1] = '0'
                count += 1
            i += 1
        return min(count, n - count)
