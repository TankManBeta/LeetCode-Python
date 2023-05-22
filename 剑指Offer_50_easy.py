# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2023/5/20 14:44
"""
"""
在字符串 s 中找出第一个只出现一次的字符。如果没有，返回一个单空格。 s 只包含小写字母。

示例 1:
输入：s = "abaccdeff"
输出：'b'

示例 2:
输入：s = "" 
输出：' '
"""
"""
思路：
（1）哈希表计数，遍历两次字符串s，第一次统计，第二次选择计数为1的第一个字符
（2）哈希表记录位置，第一次出现记成i，第二次出现记成-1
"""


class Solution:
    @staticmethod
    def firstUniqChar(s: str) -> str:
        # frequency = Counter(s)
        # for i, ch in enumerate(s):
        #     if frequency[ch] == 1:
        #         return ch
        # return ' '

        position = dict()
        n = len(s)
        for i, ch in enumerate(s):
            if ch in position:
                position[ch] = -1
            else:
                position[ch] = i
        first = n
        for pos in position.values():
            if pos != -1 and pos < first:
                first = pos
        return ' ' if first == n else s[first]
