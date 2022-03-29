# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2022/3/28 11:13
"""
"""
给定两个字符串 s 和 t ，判断它们是否是同构的。
如果 s 中的字符可以按某种映射关系替换得到 t ，那么这两个字符串是同构的。
每个出现的字符都应当映射到另一个字符，同时不改变字符的顺序。
不同字符不能映射到同一个字符上，相同字符只能映射到同一个字符上，字符可以映射到自己本身。

输入：s = "egg", t = "add"
输出：true

输入：s = "foo", t = "bar"
输出：false

输入：s = "paper", t = "title"
输出：true
"""
"""
思路：两个哈希表记录映射关系，有冲突就return False
"""


class Solution(object):
    @staticmethod
    def isIsomorphic(s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        m = len(s)
        map_dict1 = {}
        map_dict2 = {}
        for i in range(m):
            a = map_dict1.get(s[i], "")
            b = map_dict2.get(t[i], "")
            if not a and not b:
                map_dict1[s[i]] = t[i]
                map_dict2[t[i]] = s[i]
            else:
                if a != t[i] or b != s[i]:
                    return False
        return True
