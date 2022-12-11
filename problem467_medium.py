# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2022/12/10 14:47
"""
from collections import defaultdict

"""
把字符串 s 看作 "abcdefghijklmnopqrstuvwxyz" 的无限环绕字符串，所以 s 看起来是这样的：
"...zabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcd...." 。
现在给定另一个字符串 p 。返回 s 中 不同 的 p 的 非空子串 的数量 。 

示例 1：
输入：p = "a"
输出：1
解释：字符串 s 中只有 p 的一个 "a" 子字符。

示例 2：
输入：p = "cac"
输出：2
解释：字符串 s 中只有 p 的两个子串 ("a", "c") 。

示例 3：
输入：p = "zab"
输出：6
解释：在字符串 s 中有 p 的六个子串 ("z", "a", "b", "za", "ab", "zab") 。
"""
"""
思路：可以定义 dp[α] 表示 p 中以字符 α 结尾且在 s 中的子串的最长长度，知道了最长长度，也就知道了不同的子串的个数。
我们可以在遍历 p 时，维护连续递增的子串长度 k。具体来说，遍历到 p[i] 时，如果 p[i] 是 p[i−1] 在字母表中的下一个字母，
则将 k 加一，否则将 k 置为 1，表示重新开始计算连续递增的子串长度。然后，用 k 更新 dp[p[i]] 的最大值。遍历结束后，
p 中以字符 c 结尾且在 s 中的子串有 dp[c] 个。例如dp['d']=3 表示子串 "bcd"、"cd" 和 "d"。
"""


class Solution:
    @staticmethod
    def findSubstringInWrapRoundString(p: str) -> int:
        dp = defaultdict(int)
        k = 0
        for i, ch in enumerate(p):
            if i > 0 and (ord(ch) - ord(p[i - 1])) % 26 == 1:  # 字符之差为 1 或 -25
                k += 1
            else:
                k = 1
            dp[ch] = max(dp[ch], k)
        return sum(dp.values())
