# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2023/4/29 22:26
"""
from collections import Counter

"""
给你一个下标从 0 开始的字符串 word ，字符串只包含小写英文字母。你需要选择 一个 下标并 删除 下标处的字符，使得 word 中剩余每个字母出现 频率 相同。
如果删除一个字母后，word 中剩余所有字母的出现频率都相同，那么返回 true ，否则返回 false 。
注意：
    字母 x 的 频率 是这个字母在字符串中出现的次数。
    你 必须 恰好删除一个字母，不能一个字母都不删除。

示例 1：
输入：word = "abcc"
输出：true
解释：选择下标 3 并删除该字母，word 变成 "abc" 且每个字母出现频率都为 1 。

示例 2：
输入：word = "aazz"
输出：false
解释：我们必须删除一个字母，所以要么 "a" 的频率变为 1 且 "z" 的频率为 2 ，要么两个字母频率反过来。所以不可能让剩余所有字母出现频率相同。
"""
"""
思路：先统计每个字符的数量，然后将其中某个字符数量-1，看剩下的字符的数目是否相同即可。
"""


class Solution:
    @staticmethod
    def equalFrequency(word: str) -> bool:
        cnt = Counter(word)
        for c in cnt.keys():
            cnt[c] -= 1
            if len(set(v for v in cnt.values() if v)) == 1:
                return True
            cnt[c] += 1
        return False
