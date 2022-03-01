# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2021/10/28 18:37
"""
"""
将一个给定字符串s根据给定的行数numRows，以从上往下、从左到右进行Z字形排列。

输入：s = "PAYPALISHIRING", numRows = 3
输出："PAHNAPLSIIGYIR"

输入：s = "PAYPALISHIRING", numRows = 4
输出："PINALSIGYAHRPI"
解释：
P     I    N
A   L S  I G
Y A   H R
P     I

输入：s = "A", numRows = 1
输出："A"
"""
"""
思路：
（1）先算出填满一个周期要几个数字，每次取计算出的数量的子串，将子串的前num_rows个正常按顺序存放，计算剩下的每个字符该在的行数，
将字符加到对应行数即可
（2）有个题解很好，用了个flag，太妙了，mark一下
"""


class Solution(object):
    @staticmethod
    def convert(s, num_rows):
        """
        :type s: str
        :type num_rows: int
        :rtype: str
        """
        amount = num_rows * 2 - 2
        string_list = ["" for _ in range(num_rows)]
        if num_rows == 1:
            return s
        for i in range(0, len(s), amount):
            substring = s[i: i+amount]
            for index, value in enumerate(substring[0:num_rows]):
                string_list[index] += value
            for index, value in enumerate(substring[num_rows:]):
                string_list[num_rows - 2 - index] += value
        final_str = "".join(string_list)
        return final_str


# class Solution:
#     def convert(self, s: str, numRows: int) -> str:
#         if numRows < 2: return s
#         res = ["" for _ in range(numRows)]
#         i, flag = 0, -1
#         for c in s:
#             res[i] += c
#             if i == 0 or i == numRows - 1: flag = -flag
#             i += flag
#         return "".join(res)
