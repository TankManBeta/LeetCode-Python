# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2022/12/13 17:13
"""
"""
全字母句 指包含英语字母表中每个字母至少一次的句子。
给你一个仅由小写英文字母组成的字符串 sentence ，请你判断 sentence 是否为 全字母句 。
如果是，返回 true ；否则，返回 false 。

示例 1：
输入：sentence = "thequickbrownfoxjumpsoverthelazydog"
输出：true
解释：sentence 包含英语字母表中每个字母至少一次。

示例 2：
输入：sentence = "leetcode"
输出：false
"""
"""
思路：
（1）使用长度为26的数组，出现就把对应的值改为1，最后判断和是否为26即可
（2）位运算，出现就或上2^i，然后看结果是否等于(1 << 26) - 1
"""


class Solution:
    @staticmethod
    def checkIfPangram(sentence: str) -> bool:
        # res = [0]*26
        # for letter in sentence:
        #     res[ord(letter)-ord('a')] = 1
        # return sum(res) == 26

        state = 0
        for c in sentence:
            state |= 1 << (ord(c) - ord('a'))
        return state == (1 << 26) - 1
