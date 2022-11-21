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
思路：对于query来说，如果当前是大写字母，则必须匹配到pattern中的大写字母；如果当前是小写字母则能匹配就匹配，因为再下一次遇到
大写字母之前，如果可以匹配成功肯定可以消掉，否则的话下一次遇到大写字母就会return False。
"""


class Solution:
    @staticmethod
    def camelMatch(queries: List[str], pattern: str) -> List[bool]:
        def match(word):
            p = 0
            for letter in word:
                if letter.isupper():
                    if p < len(pattern) and pattern[p] == letter:
                        p += 1
                    else:
                        return False
                else:
                    if p < len(pattern) and pattern[p] == letter:
                        p += 1
            return p == len(pattern)

        res = []
        for query in queries:
            res.append(match(query))
        return res
