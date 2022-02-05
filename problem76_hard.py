# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2022/2/5 15:09
"""
"""
给你一个字符串s、一个字符串t。返回s中涵盖t所有字符的最小子串。如果 s 中不存在涵盖 t 所有字符的子串，则返回空字符串 "" 。
注意：
    对于 t 中重复字符，我们寻找的子字符串中该字符数量必须不少于 t 中该字符数量。
    如果 s 中存在这样的子串，我们保证它是唯一的答案。

输入：s = "ADOBECODEBANC", t = "ABC"
输出："BANC"

输入：s = "a", t = "a"
输出："a"

输入: s = "a", t = "aa"
输出: ""
解释: t 中两个字符 'a' 均应包含在 s 的子串中，
因此没有符合条件的子字符串，返回空字符串。
"""
"""
思路：滑动窗口，先right++，直到窗口中包含的各字符数量之和符合t字符串的长度，然后left++进行优化，如果当前字符不在dict_t中，
left++，否则判断dict_s中的该字符计数是否大于dict_t中字符的计数，如果大于说明还可以继续减少，否则说明不可以减少，already--
"""


class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        size_t = len(t)
        size_s = len(s)
        dict_t = {}
        dict_s = {}
        for char in t:
            dict_t[char] = dict_t.get(char, 0) + 1

        left, right = 0, 0
        already = 0
        start, end = 0, 10 ** 5
        while right < size_s:
            # 首先必须满足条件
            while already != size_t:
                if s[right] in dict_t:
                    if dict_s.get(s[right], 0) < dict_t[s[right]]:
                        already += 1
                dict_s[s[right]] = dict_s.get(s[right], 0) + 1
                right += 1
                if right >= size_s:
                    break
            # 进行优化
            while already == size_t:
                # 当前字符不在t中
                if s[left] not in dict_t:
                    left += 1
                else:
                    # 不可继续优化
                    if dict_s[s[left]] <= dict_t[s[left]]:
                        already -= 1
                        # 更新结果
                        if (right - left) < (end - start):
                            start = left
                            end = right
                    dict_s[s[left]] = dict_s.get(s[left]) - 1
                    left += 1
        return s[start:end] if end != 10 ** 5 else ""
