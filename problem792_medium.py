# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2022/11/17 18:53
"""
from bisect import bisect_right
from collections import defaultdict
from typing import List

"""
给定字符串 s 和字符串数组 words, 返回  words[i] 中是s的子序列的单词个数 。
字符串的 子序列 是从原始字符串中生成的新字符串，可以从中删去一些字符(可以是none)，而不改变其余字符的相对顺序。
例如， “ace” 是 “abcde” 的子序列。

示例 1:
输入: s = "abcde", words = ["a","bb","acd","ace"]
输出: 3
解释: 有三个是 s 的子序列的单词: "a", "acd", "ace"。

示例2:
输入: s = "dsahjpjauf", words = ["ahjpjau","ja","ahbwzgqnuk","tnmlanowax"]
输出: 2
"""
"""
思路：
（1）枚举子串，超时
（2）我们可以先用数组或哈希表 d 存放字符串 ss 每个字符的下标，即 d[c] 为 ss 中所有字符 c 的下标组成的数组。
然后我们遍历 words 中的每个单词 w，我们通过二分查找的方法，判断 w 是否为 s 的子序列，是则答案加 1。判断逻辑如下：
    定义指针 i 表示当前指向字符串 s 的第 i 个字符，初始化为 −1。
    遍历字符串 w 中的每个字符 cc，在 d[c] 中二分查找第一个大于 i 的位置 j，如果不存在，则说明 w 不是 s 的子序列，直接跳出循环；
    否则，将 i 更新为 d[c][j]，继续遍历下一个字符。
    如果遍历完 w 中的所有字符，说明 w 是 s 的子序列。
（3）我们可以使用多指针，开始将每一个单词的第一个字母记下，遍历s中的每一个字母，如果有word当前指向的字符是s当前遍历的字符，就
把该word的指针移动到下一位，直到s遍历结束。
"""


class Solution:
    @staticmethod
    def numMatchingSubSequence(s: str, words: List[str]) -> int:
        # n = len(s)
        # res = set()
        # count = 0
        # for i in range(1<<n):
        #     temp = []
        #     for j in range(n):
        #         if (1<<j) & i:
        #             temp.append(s[j])
        #     res.add(''.join(temp))
        # for word in words:
        #     if word in res:
        #         count += 1
        # return count

        # pos = defaultdict(list)
        # for i, c in enumerate(s):
        #     pos[c].append(i)
        # ans = len(words)
        # for w in words:
        #     if len(w) > len(s):
        #         ans -= 1
        #         continue
        #     p = -1
        #     for c in w:
        #         ps = pos[c]
        #         j = bisect_right(ps, p)
        #         if j == len(ps):
        #             ans -= 1
        #             break
        #         p = ps[j]
        # return ans

        p = defaultdict(list)
        for i, word in enumerate(words):
            p[word[0]].append((i, 0))
        ans = 0
        for c in s:
            q = p[c]
            p[c] = []
            for i, j in q:
                j += 1
                if j == len(words[i]):
                    ans += 1
                else:
                    p[words[i][j]].append((i, j))
        return ans
