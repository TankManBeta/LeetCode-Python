# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2022/11/11 10:32
"""
"""
给你一个偶数长度的字符串 s 。将其拆分成长度相同的两半，前一半为 a ，后一半为 b 。
两个字符串 相似 的前提是它们都含有相同数目的元音（'a'，'e'，'i'，'o'，'u'，'A'，'E'，'I'，'O'，'U'）。
注意，s 可能同时含有大写和小写字母。
如果 a 和 b 相似，返回 true ；否则，返回 false 。

示例 1：
输入：s = "book"
输出：true
解释：a = "bo" 且 b = "ok" 。a 中有 1 个元音，b 也有 1 个元音。所以，a 和 b 相似。

示例 2：
输入：s = "textbook"
输出：false
解释：a = "text" 且 b = "book" 。a 中有 1 个元音，b 中有 2 个元音。因此，a 和 b 不相似。
注意，元音 o 在 b 中出现两次，记为 2 个。
"""
"""
思路：遍历计数即可
"""


class Solution:
    @staticmethod
    def halvesAreAlike(s: str) -> bool:
        n = len(s)
        count1, count2 = 0, 0
        option = ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U')
        for letter in s[0:n // 2]:
            if letter in option:
                count1 += 1
        for letter in s[n // 2:]:
            if letter in option:
                count2 += 1
        return count1 == count2
