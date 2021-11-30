# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2021/10/29 11:11
"""
"""
给你一个整数x，如果x是一个回文整数，返回true；否则，返回false 。
回文数是指正序（从左向右）和倒序（从右向左）读都是一样的整数。例如，121 是回文，而 123 不是。
"""
"""
思路：
（1）将整数转化成字符串，再逆序，比较两个字符串是否相等。
（2）本质上和（1）的思路相同，转化成字符串，head从前往后，tail从后往前比较每一字符，直到相遇。
"""


class Solution(object):
    @staticmethod
    def is_palindrome(x):
        """
        :type x: int
        :rtype: bool
        """
        s1 = str(x)
        s2 = s1[::-1]
        return s1 == s2


# class Solution(object):
#     def isPalindrome(self, x):
#         """
#         :type x: int
#         :rtype: bool
#         """
#         s1 = str(x)
#         head = 0
#         tail = len(s1) - 1
#         while head <= tail:
#             if s1[head] != s1[tail]:
#                 return False
#             else:
#                 head += 1
#                 tail -= 1
#         return True
