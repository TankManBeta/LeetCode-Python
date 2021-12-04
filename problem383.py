# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2021/12/4 18:48
"""
"""
为了不在赎金信中暴露字迹，从杂志上搜索各个需要的字母，组成单词来表达意思。
给你一个赎金信 (ransomNote) 字符串和一个杂志(magazine)字符串，判断 ransomNote 能不能由 magazines 里面的字符构成。
如果可以构成，返回 true ；否则返回 false 。
magazine 中的每个字符只能在 ransomNote 中使用一次。

输入：ransomNote = "a", magazine = "b"
输出：false

输入：ransomNote = "aa", magazine = "ab"
输出：false

输入：ransomNote = "aa", magazine = "aab"
输出：true
"""
"""
思路：字典存magazine中字母的个数，ransomNote中如果存在magazine中没有的key，直接返回False，否则用一次magazine中的值减一，
值如果变为-1直接返回False，否则继续
"""


class Solution(object):
    @staticmethod
    def can_construct(ransom_note, magazine):
        """
        :type ransom_note: str
        :type magazine: str
        :rtype: bool
        """
        magazine_dict = {}
        for i in magazine:
            magazine_dict[i] = magazine_dict.get(i, 0) + 1
        for j in ransom_note:
            if j not in magazine_dict.keys():
                return False
            else:
                magazine_dict[j] = magazine_dict[j] - 1
                if magazine_dict[j] == -1:
                    return False
        return True
