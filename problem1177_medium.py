# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2023/6/15 0:30
"""
from typing import List

"""
给你一个字符串 s，请你对 s 的子串进行检测。
每次检测，待检子串都可以表示为 queries[i] = [left, right, k]。我们可以 重新排列 子串 s[left], ..., s[right]，并从中选择 最多 
k 项替换成任何小写英文字母。 
如果在上述检测过程中，子串可以变成回文形式的字符串，那么检测结果为 true，否则结果为 false。
返回答案数组 answer[]，其中 answer[i] 是第 i 个待检子串 queries[i] 的检测结果。
注意：在替换时，子串中的每个字母都必须作为 独立的 项进行计数，也就是说，如果 s[left..right] = "aaa" 且 k = 2，我们只能替换
其中的两个字母。（另外，任何检测都不会修改原始字符串 s，可以认为每次检测都是独立的）

示例：
输入：s = "abcda", queries = [[3,3,0],[1,2,0],[0,3,1],[0,3,2],[0,4,1]]
输出：[true,false,false,true,true]
解释：
queries[0] : 子串 = "d"，回文。
queries[1] : 子串 = "bc"，不是回文。
queries[2] : 子串 = "abcd"，只替换 1 个字符是变不成回文串的。
queries[3] : 子串 = "abcd"，可以变成回文的 "abba"。 也可以变成 "baab"，先重新排序变成 "bacd"，然后把 "cd" 替换为 "ab"。
queries[4] : 子串 = "abcda"，可以变成回文的 "abcba"。
"""
"""
思路：我们先考虑一个子串能否在经过最多 k 次替换后变成回文串，显然，我们需要统计子串中每个字符出现的次数，这可以通过前缀和来实现。
对于出现偶数次的字符，我们不需要进行替换，对于出现奇数次的字符，我们需要进行替换，替换的次数为 ⌊x//2⌋，其中 x 为出现奇数次的字符
的个数。如果 ⌊x//2⌋≤k，那么这个子串就可以变成回文串。因此，我们定义一个前缀和数组 ss，其中 ss[i][j] 表示字符串 s 的前 i 个字符中，
字符 j 出现的次数。那么对于一个子串 s[l..r]，我们可以通过 ss[r+1][j]−ss[l][j] 得到子串中字符 j 出现的次数。我们遍历所有的查询，
对于每个查询 [l,r,k]，我们统计子串 s[l..r] 中出现奇数次的字符的个数 x，如果 ⌊x//2⌋≤k，那么这个子串就可以变成回文串。
"""


class Solution:
    @staticmethod
    def canMakePaliQueries(s: str, queries: List[List[int]]) -> List[bool]:
        n = len(s)
        ss = [[0] * 26 for _ in range(n + 1)]
        for i, c in enumerate(s, 1):
            ss[i] = ss[i - 1][:]
            ss[i][ord(c) - ord("a")] += 1
        ans = []
        for l, r, k in queries:
            cnt = sum((ss[r + 1][j] - ss[l][j]) & 1 for j in range(26))
            ans.append(cnt // 2 <= k)
        return ans
