# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2022/12/6 17:15
"""
"""
给你一个字符串 word ，该字符串由数字和小写英文字母组成。
请你用空格替换每个不是数字的字符。例如，"a123bc34d8ef34" 将会变成 " 123  34 8  34" 。
注意，剩下的这些整数为（相邻彼此至少有一个空格隔开）："123"、"34"、"8" 和 "34" 。
返回对 word 完成替换后形成的 不同 整数的数目。
只有当两个整数的 不含前导零 的十进制表示不同， 才认为这两个整数也不同。

示例 1：
输入：word = "a123bc34d8ef34"
输出：3
解释：不同的整数有 "123"、"34" 和 "8" 。注意，"34" 只计数一次。

示例 2：
输入：word = "leet1234code234"
输出：2

示例 3：
输入：word = "a1b01c001"
输出：1
解释："1"、"01" 和 "001" 视为同一个整数的十进制表示，因为在比较十进制值时会忽略前导零的存在。
"""
"""
思路：
（1）直接将字母变成空格，然后按照空格分割，再看这些数字是否是唯一的即可
（2）双指针，左指针先找到数字开始的位置，然后右指针找到数字结束的位置，然后左指针判断是否有前导零，有的话就左指针一直++
"""


class Solution:
    @staticmethod
    def numDifferentIntegers(word: str) -> int:
        # temp_word = []
        # for i, letter in enumerate(word):
        #     if word[i].isalpha():
        #         temp_word.append(' ')
        #     else:
        #         temp_word.append(word[i])
        # new_word = ''.join(temp_word)
        # nums = new_word.split()
        # nums = set([int(num) for num in nums])
        # return len(nums)

        n = len(word)
        hash_set = set()
        i = 0
        while i < n:
            while i < n and 'a' <= word[i] <= 'z':
                i += 1
            j = i+1
            while j < n and '0' <= word[j] <= '9':
                j += 1
            if j <= n:
                while i < j and word[i] == '0':
                    i += 1
                hash_set.add(word[i:j])
            i = j + 1
        return len(hash_set)
