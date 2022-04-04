# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2022/4/3 13:41
"""
"""
给你一个排序后的字符列表 letters ，列表中只包含小写英文字母。
另给出一个目标字母 target，请你寻找在这一有序列表里比目标字母大的最小字母。
在比较时，字母是依序循环出现的。举个例子：
    如果目标字母 target = 'z' 并且字符列表为 letters = ['a', 'b']，则答案返回 'a'

输入: letters = ["c", "f", "j"]，target = "a"
输出: "c"

输入: letters = ["c","f","j"], target = "c"
输出: "f"

输入: letters = ["c","f","j"], target = "d"
输出: "f"
"""
"""
思路：直接遍历即可
"""


class Solution(object):
    @staticmethod
    def nextGreatestLetter(letters, target):
        """
        :type letters: List[str]
        :type target: str
        :rtype: str
        """
        for letter in letters:
            if letter > target:
                return letter
        return letters[0]
