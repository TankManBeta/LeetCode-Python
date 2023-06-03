# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2023/6/2 10:08
"""
from typing import List

"""
给你一个下标从 0 开始的字符串数组 words 以及一个二维整数数组 queries 。
每个查询 queries[i] = [li, ri] 会要求我们统计在 words 中下标在 li 到 ri 范围内（包含 这两个值）并且以元音开头和结尾的字符串的数目。
返回一个整数数组，其中数组的第 i 个元素对应第 i 个查询的答案。
注意：元音字母是 'a'、'e'、'i'、'o' 和 'u' 。 

示例 1：
输入：words = ["aba","bcb","ece","aa","e"], queries = [[0,2],[1,4],[1,1]]
输出：[2,3,0]
解释：以元音开头和结尾的字符串是 "aba"、"ece"、"aa" 和 "e" 。
查询 [0,2] 结果为 2（字符串 "aba" 和 "ece"）。
查询 [1,4] 结果为 3（字符串 "ece"、"aa"、"e"）。
查询 [1,1] 结果为 0 。
返回结果 [2,3,0] 。

示例 2：
输入：words = ["a","e","i"], queries = [[0,2],[0,1],[2,2]]
输出：[3,2,1]
解释：每个字符串都满足这一条件，所以返回 [3,2,1] 。
"""
"""
思路：前缀和，s[i] 表示数组 words 的前 i 个字符串中以元音开头和结尾的字符串的数目。初始时 s[0]=0。接下来，我们遍历数组 words，
如果当前字符串以元音开头和结尾，那么 s[i+1]=s[i]+1，否则 s[i+1]=s[i]。最后，我们遍历每个查询 (l,r)，那么当前查询的答案就是 
s[r+1]−s[l]。
"""


class Solution:
    @staticmethod
    def vowelStrings(words: List[str], queries: List[List[int]]) -> List[int]:
        pre = [0]
        for word in words:
            if word[0] in ['a', 'e', 'i', 'o', 'u'] and word[-1] in ['a', 'e', 'i', 'o', 'u']:
                pre.append(pre[-1] + 1)
            else:
                pre.append(pre[-1])
        ans = []
        for l, r in queries:
            ans.append(pre[r + 1] - pre[l])
        return ans
