# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2023/7/24 7:41
"""
"""
 给你一个字符串 jewels 代表石头中宝石的类型，另有一个字符串 stones 代表你拥有的石头。 stones 中每个字符代表了一种你拥有的石头
的类型，你想知道你拥有的石头中有多少是宝石。
字母区分大小写，因此 "a" 和 "A" 是不同类型的石头。

示例 1：
输入：jewels = "aA", stones = "aAAbbbb"
输出：3

示例 2：
输入：jewels = "z", stones = "ZZ"
输出：0
"""
"""
思路：模拟即可
"""


class Solution:
    @staticmethod
    def numJewelsInStones(jewels: str, stones: str) -> int:
        ans = 0
        for stone in stones:
            if stone in jewels:
                ans += 1
        return ans
