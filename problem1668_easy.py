# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2022/11/3 15:20
"""
"""
给你一个字符串 sequence ，如果字符串 word 连续重复 k 次形成的字符串是 sequence 的一个子字符串，那么单词 word 的 重复值为 k 。
单词 word 的 最大重复值 是单词 word 在 sequence 中最大的重复值。如果 word 不是 sequence 的子串，那么重复值 k 为 0 。
给你一个字符串 sequence 和 word ，请你返回 最大重复值 k 。

示例 1：
输入：sequence = "ababc", word = "ab"
输出：2
解释："abab" 是 "ababc" 的子字符串。

示例 2：
输入：sequence = "ababc", word = "ba"
输出：1
解释："ba" 是 "ababc" 的子字符串，但 "baba" 不是 "ababc" 的子字符串。

示例 3：
输入：sequence = "ababc", word = "ac"
输出：0
解释："ac" 不是 "ababc" 的子字符串。
"""
"""
思路：
（1）首先计算sequence里最多能由几个word组成，然后从大到小看word*k是否在sequence中，如果存在就return
（2）把sequence中每个位置作为结束，然后依次遍历sequence和word，挨个比较，如果合法的话f[i] = f[i-len(word)]+1
"""


class Solution:
    @staticmethod
    def maxRepeating(sequence: str, word: str) -> int:
        # n1 = len(sequence)
        # n2 = len(word)
        # max_k = int(n1 / n2)
        # for i in range(max_k, -1, -1):
        #     if word * i in sequence:
        #         return i

        m, n = len(sequence), len(word)
        res = [0] * m
        for i in range(n-1, m):
            flag = True
            for j in range(n):
                if word[j] != sequence[i-n+j+1]:
                    flag = False
                    break
            if flag:
                res[i] = (0 if i == n-1 else res[i-n]) + 1
        return max(res)
