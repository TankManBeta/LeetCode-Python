# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2022/1/27 12:32
"""
"""
有效数字（按顺序）可以分成以下几个部分：
    一个 小数 或者 整数
    （可选）一个 'e' 或 'E' ，后面跟着一个 整数
小数（按顺序）可以分成以下几个部分：
    （可选）一个符号字符（'+' 或 '-'）
    下述格式之一：
    至少一位数字，后面跟着一个点 '.'
    至少一位数字，后面跟着一个点 '.' ，后面再跟着至少一位数字
    一个点 '.' ，后面跟着至少一位数字
整数（按顺序）可以分成以下几个部分：
    （可选）一个符号字符（'+' 或 '-'）
    至少一位数字
部分有效数字列举如下：
["2", "0089", "-0.1", "+3.14", "4.", "-.9", "2e10", "-90E3", "3e+7", "+6e-1", "53.5e93", "-123.456e789"]
部分无效数字列举如下：
["abc", "1a", "1e", "e3", "99e2.5", "--6", "-+3", "95a54e53"]
给你一个字符串 s ，如果 s 是一个 有效数字 ，请返回 true 。

输入：s = "0"
输出：true

输入：s = "e"
输出：false

输入：s = "."
输出：false

输入：s = ".1"
输出：true
"""
"""
思路：定义两个函数用于判断是否是整数或者小数，对于整数来说，首先判断正负号，然后判断是否是数字以及数字数量至少为1；对于小数来说，
首先判断正负号，然后判断小数点的个数，然后用小数点将数字分成前后两端，前后两端是否为整数即可。对于输入的字符串，首先把E换成e，
然后根据第一部分是否有.来选择用整数还是小数的判断。
"""


class Solution(object):
    @staticmethod
    def is_number(s):
        """
        :type s: str
        :rtype: bool
        """

        def is_int(s1):
            # + -
            if len(s1) == 0:
                return False
            if s1[0] in ['+', '-']:
                s1 = s1[1:]
            count1 = s1.count('+')
            count2 = s1.count('-')
            if count1 > 0 or count2 > 0:
                return False
            # at least one number
            count = 0
            for i in s1:
                if '0' <= i <= '9':
                    count += 1
                else:
                    return False
            return True if count > 0 else False

        def is_float(s2):
            if len(s2) == 0:
                return False
            # + -
            if s2[0] in ['+', '-']:
                s2 = s2[1:]
            count1 = s2.count('+')
            count2 = s2.count('-')
            if count1 > 0 or count2 > 0:
                return False
            # .
            parts = s2.split('.')
            if len(parts) > 2:
                return False
            else:
                if parts[0] == '':
                    count = 0
                    for i in parts[1]:
                        if '0' <= i <= '9':
                            count += 1
                        else:
                            return False
                    return True if count > 0 else False
                else:
                    if parts[1] == '':
                        count = 0
                        for i in parts[0]:
                            if '0' <= i <= '9':
                                count += 1
                            else:
                                return False
                        return True if count > 0 else False
                    else:
                        count1 = 0
                        count2 = 0
                        for i in parts[0]:
                            if '0' <= i <= '9':
                                count1 += 1
                            else:
                                return False
                        for i in parts[1]:
                            if '0' <= i <= '9':
                                count2 += 1
                            else:
                                return False
                        return True if count1 > 0 and count2 > 0 else False

        s = s.replace('E', 'e')
        count_e = s.count('e')
        if count_e == 0:
            if '.' in s:
                return is_float(s)
            else:
                return is_int(s)
        elif count_e == 1:
            new_parts = s.split('e')
            if '.' in new_parts[0]:
                return is_float(new_parts[0]) & is_int(new_parts[1])
            else:
                return is_int(new_parts[0]) & is_int(new_parts[1])
        else:
            return False


# class Solution(object):
#     def isNumber(self, s):
#         """
#         :type s: str
#         :rtype: bool
#         """
#
#         def is_int(s1):
#             # + -
#             if len(s1) == 0:
#                 return False
#             if s1[0] in ['+', '-']:
#                 s1 = s1[1:]
#             count1 = s1.count('+')
#             count2 = s1.count('-')
#             if count1 > 0 or count2 > 0:
#                 return False
#             # at least one number
#             count = 0
#             for i in s1:
#                 if '0' <= i <= '9':
#                     count += 1
#                 else:
#                     return False
#             return True if count > 0 else False
#
#         def is_float(s2):
#             if len(s2) == 0:
#                 return False
#             # + -
#             if s2[0] in ['+', '-']:
#                 s2 = s2[1:]
#             count1 = s2.count('+')
#             count2 = s2.count('-')
#             if count1 > 0 or count2 > 0:
#                 return False
#             # .
#             parts = s2.split('.')
#             if len(parts) > 2:
#                 return False
#             else:
#                 if parts[0] == '':
#                     return is_int(parts[1])
#                 else:
#                     if parts[1] == '':
#                         return is_int(parts[0])
#                     else:
#                         return is_int(parts[0]) & is_int(parts[1])
#
#         s = s.replace('E', 'e')
#         count_e = s.count('e')
#         if count_e == 0:
#             if '.' in s:
#                 return is_float(s)
#             else:
#                 return is_int(s)
#         elif count_e == 1:
#             new_parts = s.split('e')
#             if '.' in new_parts[0]:
#                 return is_float(new_parts[0]) & is_int(new_parts[1])
#             else:
#                 return is_int(new_parts[0]) & is_int(new_parts[1])
#         else:
#             return False
