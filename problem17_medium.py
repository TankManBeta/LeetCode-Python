# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2021/12/1 14:29
"""
"""
给定一个仅包含数字 2-9 的字符串，返回所有它能表示的字母组合。答案可以按 任意顺序 返回。

输入：digits = "23"
输出：["ad","ae","af","bd","be","bf","cd","ce","cf"]

输入：digits = ""
输出：[]

输入：digits = "2"
输出：["a","b","c"]
"""
"""
思路：
回溯法，每次取电话号码的一位数字，从哈希表中获得该数字对应的所有可能的字母，并将其中的一个字母插入到已有的字母排列后面，
然后继续处理电话号码的后一位数字，直到处理完电话号码中的所有数字，即得到一个完整的字母排列。
然后进行回退操作，遍历其余的字母排列。
"""


class Solution:
    @staticmethod
    def letter_combinations(digits):
        if not digits:
            return list()
        reflection_dict = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }
        def backtrack(index):
            # 返回条件
            if index == len(digits):
                # 返回一个结果
                combinations.append("".join(combination))
            else:
                # 取数字
                digit = digits[index]
                for letter in reflection_dict[digit]:
                    # 将这个数字对应的一个字母放进去
                    combination.append(letter)
                    # 处理下一个字母
                    backtrack(index + 1)
                    # 将存入的数字取出
                    combination.pop()
        combination = list()
        combinations = list()
        backtrack(0)
        return combinations
