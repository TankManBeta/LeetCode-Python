# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2023/2/26 13:02
"""
from collections import Counter
from typing import List

"""
你将会得到一份单词表 words，一个字母表 letters （可能会有重复字母），以及每个字母对应的得分情况表 score。
请你帮忙计算玩家在单词拼写游戏中所能获得的「最高得分」：能够由 letters 里的字母拼写出的 任意 属于 words 单词子集中，分数最高的单词集合的得分。
单词拼写游戏的规则概述如下：
    玩家需要用字母表 letters 里的字母来拼写单词表 words 中的单词。
    可以只使用字母表 letters 中的部分字母，但是每个字母最多被使用一次。
    单词表 words 中每个单词只能计分（使用）一次。
    根据字母得分情况表score，字母 'a', 'b', 'c', ... , 'z' 对应的得分分别为 score[0], score[1], ..., score[25]。
    本场游戏的「得分」是指：玩家所拼写出的单词集合里包含的所有字母的得分之和。 

示例 1：
输入：words = ["dog","cat","dad","good"], letters = ["a","a","c","d","d","d","g","o","o"], score = [1,0,9,5,0,0,3,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,0,0,0,0]
输出：23
解释：
字母得分为  a=1, c=9, d=5, g=3, o=2
使用给定的字母表 letters，我们可以拼写单词 "dad" (5+1+5)和 "good" (3+2+2+5)，得分为 23 。
而单词 "dad" 和 "dog" 只能得到 21 分。

示例 2：
输入：words = ["xxxz","ax","bx","cx"], letters = ["z","a","b","c","x","x","x"], score = [4,4,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,5,0,10]
输出：27
解释：
字母得分为  a=4, b=4, c=4, x=5, z=10
使用给定的字母表 letters，我们可以组成单词 "ax" (4+5)， "bx" (4+5) 和 "cx" (4+5) ，总得分为 27 。
单词 "xxxz" 的得分仅为 25 。

示例 3：
输入：words = ["leetcode"], letters = ["l","e","t","c","o","d"], score = [0,0,1,1,1,0,0,0,0,0,0,1,0,0,1,0,0,0,0,1,0,0,0,0,0,0]
输出：0
解释：
字母 "e" 在字母表 letters 中只出现了一次，所以无法组成单词表 words 中的单词。
"""
"""
思路：我们注意到题目的数据范围不大，因此对于给定的单词表，我们可以使用二进制枚举的方法，枚举出所有的单词组合，然后判断每个单词
组合是否满足题目要求，如果满足则计算其得分，最后取得分最大的单词组合。
我们首先用哈希表或数组 cnt 记录字母表 letters 中每个字母出现的次数。
接下来，我们使用二进制枚举的方法，枚举出所有的单词组合。二进制的每一位表示单词表中的每一个单词是否被选中，如果第 i 位为 1，则
表示第 i 个单词被选中，否则表示第 i 个单词没有被选中。
然后我们统计当前单词组合中每个字母出现的次数，记录在哈希表或数组 cur 中。如果 cur 中的每个字母的出现次数都不大于 cnt 中的对应
字母的出现次数，则说明当前单词组合满足题目要求，我们计算当前单词组合的得分，取得分最大的单词组合。
"""


class Solution:
    @staticmethod
    def maxScoreWords(words: List[str], letters: List[str], score: List[int]) -> int:
        cnt = Counter(letters)
        n = len(words)
        ans = 0
        for i in range(1 << n):
            cur = Counter(''.join([words[j] for j in range(n) if i >> j & 1]))
            if all(v <= cnt[c] for c, v in cur.items()):
                t = sum(v * score[ord(c) - ord('a')] for c, v in cur.items())
                ans = max(ans, t)
        return ans
