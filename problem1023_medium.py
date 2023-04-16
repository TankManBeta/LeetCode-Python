# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2022/11/20 17:58
"""
from typing import List

"""
如果我们可以将小写字母插入模式串 pattern 得到待查询项 query，那么待查询项与给定模式串匹配。
（我们可以在任何位置插入每个字符，也可以插入 0 个字符。）
给定待查询列表 queries，和模式串 pattern，返回由布尔值组成的答案列表 answer。
只有在待查项 queries[i] 与模式串 pattern 匹配时， answer[i] 才为 true，否则为 false。

示例 1：
输入：queries = ["FooBar","FooBarTest","FootBall","FrameBuffer","ForceFeedBack"], pattern = "FB"
输出：[true,false,true,true,false]
示例：
"FooBar" 可以这样生成："F" + "oo" + "B" + "ar"。
"FootBall" 可以这样生成："F" + "oot" + "B" + "all".
"FrameBuffer" 可以这样生成："F" + "rame" + "B" + "uffer".

示例 2：
输入：queries = ["FooBar","FooBarTest","FootBall","FrameBuffer","ForceFeedBack"], pattern = "FoBa"
输出：[true,false,true,false,false]
解释：
"FooBar" 可以这样生成："Fo" + "o" + "Ba" + "r".
"FootBall" 可以这样生成："Fo" + "ot" + "Ba" + "ll".

示例 3：
输出：queries = ["FooBar","FooBarTest","FootBall","FrameBuffer","ForceFeedBack"], pattern = "FoBaT"
输入：[false,true,false,false,false]
解释： 
"FooBarTest" 可以这样生成："Fo" + "o" + "Ba" + "r" + "T" + "est".
"""
"""
思路：
（1）匹配pattern，看最后pattern是否能到末尾。对于query来说，如果当前是大写字母，则必须匹配到pattern中的大写字母；如果当前是
小写字母则能匹配就匹配，因为再下一次遇到大写字母之前，如果可以匹配成功肯定可以消掉，否则的话下一次遇到大写字母就会return False。
（2）匹配query，看最后query能否到末尾。如果指针 i 和 j 指向的字符不同，并且 s[i] 为小写字母，则指针 i 循环向后移动一位。如果
指针 i 已经到达字符串 s 的末尾，或者指针 i 和 j 指向的字符不同，则返回 false。否则，指针 i 和 j 同时向后移动一位。当指针 j 
到达字符串 t 的末尾时，我们需要判断字符串 s 中剩余的字符是否都为小写字母，若是则返回 true，否则返回 false。
"""


class Solution:
    @staticmethod
    def camelMatch(queries: List[str], pattern: str) -> List[bool]:
        # n = len(pattern)
        #
        # def match(word):
        #     p = 0
        #     for letter in word:
        #         if letter.isupper():
        #             if p < n and pattern[p] == letter:
        #                 p += 1
        #             else:
        #                 return False
        #         else:
        #             if p < n and pattern[p] == letter:
        #                 p += 1
        #     return p == n
        #
        # res = []
        # for query in queries:
        #     res.append(match(query))
        # return res

        def check(s, t):
            m, n = len(s), len(t)
            i = j = 0
            while j < n:
                while i < m and s[i] != t[j] and s[i].islower():
                    i += 1
                if i == m or s[i] != t[j]:
                    return False
                i, j = i + 1, j + 1
            while i < m and s[i].islower():
                i += 1
            return i == m

        return [check(q, pattern) for q in queries]
