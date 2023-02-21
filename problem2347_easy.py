# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2023/2/20 11:12
"""
from collections import Counter
from typing import List

"""
给你一个整数数组 ranks 和一个字符数组 suit 。你有 5 张扑克牌，第 i 张牌大小为 ranks[i] ，花色为 suits[i] 。
下述是从好到坏你可能持有的 手牌类型 ：
    "Flush"：同花，五张相同花色的扑克牌。
    "Three of a Kind"：三条，有 3 张大小相同的扑克牌。
    "Pair"：对子，两张大小一样的扑克牌。
    "High Card"：高牌，五张大小互不相同的扑克牌。
请你返回一个字符串，表示给定的 5 张牌中，你能组成的 最好手牌类型 。
注意：返回的字符串 大小写 需与题目描述相同。

示例 1：
输入：ranks = [13,2,3,1,9], suits = ["a","a","a","a","a"]
输出："Flush"
解释：5 张扑克牌的花色相同，所以返回 "Flush" 。

示例 2：
输入：ranks = [4,4,2,4,4], suits = ["d","a","a","b","c"]
输出："Three of a Kind"
解释：第一、二和四张牌组成三张相同大小的扑克牌，所以得到 "Three of a Kind" 。
注意我们也可以得到 "Pair" ，但是 "Three of a Kind" 是更好的手牌类型。
有其他的 3 张牌也可以组成 "Three of a Kind" 手牌类型。

示例 3：
输入：ranks = [10,10,2,12,9], suits = ["a","b","c","a","d"]
输出："Pair"
解释：第一和第二张牌大小相同，所以得到 "Pair" 。
我们无法得到 "Flush" 或者 "Three of a Kind" 。
"""
"""
思路：直接统计花色和点数出现的次数。先看花色，如果全一样就是同花；再看每个点数出现的次数，按照次数分别是三条、对子和高牌
"""


class Solution:
    @staticmethod
    def bestHand(ranks: List[int], suits: List[str]) -> str:
        card_t = Counter(suits)
        card_p = Counter(ranks)
        if 5 in card_t.values():
            return "Flush"
        if 3 in card_p.values() or 4 in card_p.values():
            return "Three of a Kind"
        elif 2 in card_p.values():
            return "Pair"
        else:
            return "High Card"
