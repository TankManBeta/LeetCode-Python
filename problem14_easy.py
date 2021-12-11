# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2021/11/30 21:43
"""
"""
编写一个函数来查找字符串数组中的最长公共前缀。
如果不存在公共前缀，返回空字符串 ""。

输入：strs = ["flower","flow","flight"]
输出："fl"

输入：strs = ["dog","racecar","car"]
输出：""
解释：输入不存在公共前缀。
"""
"""
思路：
（1）先找前两个的最长前缀，然后再找这个最长前缀和剩下的字符串的最长前缀。
（2）纵向扫描
"""


class Solution(object):
    @staticmethod
    def get_prefix(s1, s2):
        min_len = len(s1) if len(s1) < len(s2) else len(s2)
        prefix = ''
        for i in range(0, min_len):
            if s1[i] != s2[i]:
                return prefix
            else:
                prefix += s1[i]
        return prefix

    @staticmethod
    def longest_common_prefix(str_list):
        """
        :type str_list: List[str]
        :rtype: str
        """
        list_len = len(str_list)
        if list_len == 1:
            return str_list[0]
        else:
            longest_prefix = Solution.get_prefix(str_list[0], str_list[1])
            for i in range(0, len(str_list)-2):
                if len(longest_prefix) == 0:
                    return ""
                else:
                    longest_prefix = Solution.get_prefix(longest_prefix, str_list[i+2])
            return longest_prefix
