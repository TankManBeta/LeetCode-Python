# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2023/1/30 10:08
"""
from typing import List

"""
你有一个单词列表 words 和一个模式  pattern，你想知道 words 中的哪些单词与模式匹配。
如果存在字母的排列 p ，使得将模式中的每个字母 x 替换为 p(x) 之后，我们就得到了所需的单词，那么单词与模式是匹配的。
（回想一下，字母的排列是从字母到字母的双射：每个字母映射到另一个字母，没有两个字母映射到同一个字母。）
返回 words 中与给定模式匹配的单词列表。
你可以按任何顺序返回答案。

示例：
输入：words = ["abc","deq","mee","aqq","dkd","ccc"], pattern = "abb"
输出：["mee","aqq"]
解释：
"mee" 与模式匹配，因为存在排列 {a -> m, b -> e, ...}。
"ccc" 与模式不匹配，因为 {a -> c, b -> c, ...} 不是排列。
因为 a 和 b 映射到同一个字母。
"""
"""
思路：逐个判断 words 中的每个单词 word 是否与 pattern 匹配。
根据题意，我们需要构造从字母到字母的双射，即 word 的每个字母需要映射到 pattern 的对应字母，并且 pattern 的每个字母也需要映射到 
word 的对应字母。我们可以编写一个函数 match(word,pattern)，仅当 word 中相同字母映射到 pattern 中的相同字母时返回 true。我们
可以在遍历这两个字符串的同时，用一个哈希表记录 word 的每个字母 x 需要映射到 pattern 的哪个字母上，如果 x 已有映射，则需要检查
对应字母是否相同。
如果 match(word,pattern) 和 match(pattern,word) 均为 true，则表示 word 与 pattern 匹配。
"""


class Solution:
    @staticmethod
    def findAndReplacePattern(words: List[str], pattern: str) -> List[str]:
        def match(word: str, pattern: str) -> bool:
            mp = {}
            for x, y in zip(word, pattern):
                if x not in mp:
                    mp[x] = y
                elif mp[x] != y:  # word 中的同一字母必须映射到 pattern 中的同一字母上
                    return False
            return True

        return [word for word in words if match(word, pattern) and match(pattern, word)]
