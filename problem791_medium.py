# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2022/11/13 15:43
"""
from collections import Counter

"""
给定两个字符串 order 和 s 。order 的所有单词都是 唯一 的，并且以前按照一些自定义的顺序排序。
对 s 的字符进行置换，使其与排序的 order 相匹配。更具体地说，如果在 order 中的字符 x 出现字符 y 之前，那么在排列后的字符串中， 
x 也应该出现在 y 之前。
返回 满足这个性质的 s 的任意排列 。

示例 1:
输入: order = "cba", s = "abcd"
输出: "cbad"
解释: 
“a”、“b”、“c”是按顺序出现的，所以“a”、“b”、“c”的顺序应该是“c”、“b”、“a”。
因为“d”不是按顺序出现的，所以它可以在返回的字符串中的任何位置。“dcba”、“cdba”、“cbda”也是有效的输出。

示例 2:
输入: order = "cbafg", s = "abcd"
输出: "cbad"
"""
"""
思路：
（1）自定义排序，将order中第一次出现的记为1，第二次出现的记为2，没出现的默认记为0，然后用sorted排序
（2）计数排序，我们首先遍历字符串 s，使用数组或哈希表统计每个字符出现的次数。随后遍历字符串 order 中的每个字符 c，
如果其在 s 中出现了 k 次，就在答案的末尾添加 k 个 c，并将数组或哈希表中对应的次数置为 0。最后我们遍历一次哈希表，
对于所有次数 k 非 0 的键值对 (c, k)，在答案的末尾添加 k 个 c 即可。
"""


class Solution:
    @staticmethod
    def customSortString(order: str, s: str) -> str:
        # val = defaultdict(int)
        # for i, ch in enumerate(order):
        #     val[ch] = i + 1
        # return "".join(sorted(s, key=lambda ch: val[ch]))

        freq = Counter(s)
        ans = list()
        for ch in order:
            if ch in freq:
                ans.extend([ch] * freq[ch])
                freq[ch] = 0
        for (ch, k) in freq.items():
            if k > 0:
                ans.extend([ch] * k)
        return "".join(ans)


