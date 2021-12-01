# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2021/12/1 17:32
"""
"""
给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串 s ，判断字符串是否有效。
有效字符串需满足：
左括号必须用相同类型的右括号闭合。
左括号必须以正确的顺序闭合。

输入：s = "()"
输出：true

输入：s = "()[]{}"
输出：true

输入：s = "(]"
输出：false

输入：s = "([)]"
输出：false

输入：s = "{[]}"
输出：true
"""
"""
思路：
用栈，首先先用字典对每个符号编号，每次读一个字符，如果栈为空，进栈；
否则进行匹配，和为5并且是左右的组合就匹配成功，出栈，否则进栈。
"""


class Solution(object):
    @staticmethod
    def is_valid(s):
        """
        :type s: str
        :rtype: bool
        """
        reflection_dict = {
            '(': 0,
            ')': 5,
            '[': 1,
            ']': 4,
            '{': 2,
            '}': 3
        }
        save_list = []
        for i in range(0, len(s)):
            if len(save_list) == 0:
                save_list.append(s[i])
            else:
                if reflection_dict[s[i]] + reflection_dict[save_list[-1]] == 5 and \
                        reflection_dict[s[i]] > reflection_dict[save_list[-1]]:
                    del save_list[-1]
                else:
                    save_list.append(s[i])
        if len(save_list) == 0:
            return True
        else:
            return False
