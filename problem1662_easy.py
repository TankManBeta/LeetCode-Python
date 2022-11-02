# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2022/11/1 10:08
"""
from typing import List

"""
给你两个字符串数组 word1 和 word2 。如果两个数组表示的字符串相同，返回 true ；否则，返回 false 。
数组表示的字符串 是由数组中的所有元素 按顺序 连接形成的字符串。

示例 1：
输入：word1 = ["ab", "c"], word2 = ["a", "bc"]
输出：true
解释：
word1 表示的字符串为 "ab" + "c" -> "abc"
word2 表示的字符串为 "a" + "bc" -> "abc"
两个字符串相同，返回 true

示例 2：
输入：word1 = ["a", "cb"], word2 = ["ab", "c"]
输出：false

示例 3：
输入：word1  = ["abc", "d", "defg"], word2 = ["abcddefg"]
输出：true
"""
"""
思路：
（1）拼接字符串，然后看两个字符串是否完全一样
（2）遍历数组，挨个比较字符。设置两个指针p1和p2分别表示遍历到了word1[p1]和word2[p2]，另外还需设置两个指针i和j，表示正在对比
word1[p1][i]和word2[p2][j]。如果 word1[p1][i]!=word2[p2][j]，则直接返回false。否则i+1，当 i=word1[p1].length 时，
表示对比到当前字符串末尾，需要将p1+1，i 赋值为 0。j 和 p2 同理。当 p1<word1.length 或者 p2<word2.length 不满足时，算法结束。
最终两个数组相等条件即为 p1=word1.length 并且 p2=word2.length
"""


class Solution:
    @staticmethod
    def arrayStringsAreEqual(word1: List[str], word2: List[str]) -> bool:
        # return ''.join(word1) == ''.join(word2)

        p1 = p2 = i = j = 0
        while p1 < len(word1) and p2 < len(word2):
            if word1[p1][i] != word2[p2][j]:
                return False
            else:
                i += 1
                j += 1
                if i == len(word1[p1]):
                    p1 += 1
                    i = 0
                if j == len(word2[p2]):
                    p2 += 1
                    j = 0
        return p1 == len(word1) and p2 == len(word2)
