# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2021/12/9 10:20
"""
"""
给定一个正整数 n ，输出外观数列的第 n 项。
「外观数列」是一个整数序列，从数字 1 开始，序列中的每一项都是对前一项的描述。
你可以将其视作是由递归公式定义的数字字符串序列：
countAndSay(1) = "1"
countAndSay(n) 是对 countAndSay(n-1) 的描述，然后转换成另一个数字字符串。
前五项如下：
1.     1
2.     11
3.     21
4.     1211
5.     111221

输入：n = 1
输出："1"
解释：这是一个基本样例。

输入：n = 4
输出："1211"
解释：
countAndSay(1) = "1"
countAndSay(2) = 读 "1" = 一 个 1 = "11"
countAndSay(3) = 读 "11" = 二 个 1 = "21"
countAndSay(4) = 读 "21" = 一 个 2 + 一 个 1 = "12" + "11" = "1211"
"""
"""
思路：每次计算上一次的ans_str中重复字符的个数即可
"""


class Solution(object):
    @staticmethod
    def count_and_say(n):
        """
        :type n: int
        :rtype: str
        """
        ans_str = "1"
        for i in range(1, n):
            new_ans_str = ""
            start = 0
            count = 1
            while start < len(ans_str):
                end = start+1
                if end == len(ans_str):
                    new_ans_str += str(count) + ans_str[start]

                    break
                if ans_str[start] == ans_str[end]:
                    count += 1
                    start += 1
                else:
                    new_ans_str += str(count) + ans_str[start]
                    start = end
                    count = 1
            ans_str = new_ans_str
            print(ans_str)
        return ans_str
