# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2022/2/7 13:53
"""
"""
如果字符串中不含有任何 'aaa'，'bbb' 或 'ccc' 这样的字符串作为子串，那么该字符串就是一个「快乐字符串」。
给你三个整数 a，b ，c，请你返回 任意一个 满足下列全部条件的字符串 s：
    s 是一个尽可能长的快乐字符串。
    s 中 最多 有a 个字母 'a'、b 个字母 'b'、c 个字母 'c' 。
    s 中只含有 'a'、'b' 、'c' 三种字母。
如果不存在这样的字符串 s ，请返回一个空字符串 ""。

输入：a = 1, b = 1, c = 7
输出："ccaccbcc"
解释："ccbccacc" 也是一种正确答案。

输入：a = 2, b = 2, c = 1
输出："aabbc"

输入：a = 7, b = 1, c = 0
输出："aabaa"
解释：这是该测试用例的唯一正确答案。
"""
"""
思路：每次给list按照数量排序，首先判断res[-1]和res[-2]和剩余数量最多的字符是否相等，如果不等，则继续；如果相等，说明出现了
类似"aaa"情况，就需要用剩余数量第二多的字符补充。
"""


class Solution(object):
    @staticmethod
    def longest_diverse_string(a, b, c):
        """
        :type a: int
        :type b: int
        :type c: int
        :rtype: str
        """
        res = ""
        num_list = [['a', a], ['b', b], ['c', c]]

        while True:
            num_list = sorted(num_list, key=lambda x: x[1], reverse=True)
            if len(res) >= 2 and res[-1] == num_list[0][0] and res[-2] == num_list[0][0]:
                if num_list[1][1] != 0:
                    num_list[0], num_list[1] = num_list[1], num_list[0]
                else:
                    break
            if num_list[0][1] == 0:
                break
            elif num_list[0][1] >= 1:
                res += num_list[0][0]
                num_list[0][1] -= 1

        return res
