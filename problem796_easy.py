# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2022/4/7 9:48
"""
"""
给定两个字符串, s 和 goal。如果在若干次旋转操作之后，s 能变成 goal ，那么返回 true 。
s 的 旋转操作 就是将 s 最左边的字符移动到最右边。 
例如, 若 s = 'abcde'，在旋转一次之后结果就是'bcdea' 。

输入: s = "abcde", goal = "cdeab"
输出: true

输入: s = "abcde", goal = "abced"
输出: false
"""
"""
思路：模拟
（1）每次将首个字符串放到最后面看新的字符串是否是goal
（2）将s复制到s的末尾，然后找子串
"""


class Solution(object):
    @staticmethod
    def rotateString(s, goal):
        """
        :type s: str
        :type goal: str
        :rtype: bool
        """
        # for i in range(len(s)):
        #     s = s[1:] + s[0]
        #     if s == goal:
        #         return True
        # return False

        return True if len(s) == len(goal) and (s + s).find(goal) != -1 else False
