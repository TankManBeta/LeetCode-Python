# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2021/12/26 18:48
"""
"""
给出第一个词first和第二个词second，考虑在某些文本text中可能以 "first second third" 形式出现的情况，
其中 second 紧随 first 出现，third 紧随 second 出现。
对于每种这样的情况，将第三个词 "third" 添加到答案中，并返回答案。

输入：text = "alice is a good girl she is a good student", first = "a", second = "good"
输出：["girl","student"]

输入：text = "we will we will rock you", first = "we", second = "will"
输出：["we","rock"]
"""
"""
思路：遍历即可
"""


class Solution(object):
    @staticmethod
    def find_occurrences(text, first, second):
        """
        :type text: str
        :type first: str
        :type second: str
        :rtype: List[str]
        """
        words_list = text.split(' ')
        text_len = len(words_list)
        res_list = []
        i = 0
        while i+2 < text_len:
            if words_list[i] == first and words_list[i+1] == second:
                res_list.append(words_list[i+2])
            i += 1
        return res_list
