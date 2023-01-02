# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2023/1/1 15:51
"""
from typing import List

"""
给你一个由若干括号和字母组成的字符串 s ，删除最小数量的无效括号，使得输入的字符串有效。
返回所有可能的结果。答案可以按 任意顺序 返回。

示例 1：
输入：s = "()())()"
输出：["(())()","()()()"]

示例 2：
输入：s = "(a)())()"
输出：["(a())()","(a)()()"]

示例 3：
输入：s = ")("
输出：[""]
"""
"""
思路：我们可以遍历一次输入字符串，统计「左括号」和「右括号」出现的次数。当遍历到「左括号」的时候：「左括号」数量加 1。当遍历到
「右括号」的时候：如果此时「左括号」的数量不为 0，因为「右括号」可以与之前遍历到的「左括号」匹配，此时「左括号」出现的次数 −1；
如果此时「左括号」的数量为 0，「右括号」数量加 1。这样的计数规则，得到的「左括号」和「右括号」的数量就是各自最少应该删除的数量。
首先我们利用括号匹配的规则求出该字符串 s 中最少需要去掉的左括号的数目 lremove 和右括号的数目 rremove，然后我们尝试在原字符串 s 
中去掉 lremove 个左括号和 rremove 个右括号，然后检测剩余的字符串是否合法匹配，如果合法匹配则我们则认为该字符串为可能的结果，
我们利用回溯算法来尝试搜索所有可能的去除括号的方案。剪枝技巧来增加搜索的效率：我们从字符串中每去掉一个括号，则更新 lremove 或者 
rremove，当我们发现剩余未尝试的字符串的长度小于 lremove+rremove 时，则停止本次搜索。当 lremove 和 rremove 同时为 0 时，则我们
检测当前的字符串是否合法匹配，如果合法匹配则我们将其记录下来。去重的办法：（1）哈希表去重。（2）如果遇到连续相同的括号我们只需要
搜索一次即可，比如当前遇到的字符串为 "(((())"，去掉前四个左括号中的任意一个，生成的字符串是一样的，均为 "((())"，因此我们在尝试
搜索时，只需去掉一个左括号进行下一轮搜索，不需要将前四个左括号都尝试一遍。
"""


class Solution:
    @staticmethod
    def removeInvalidParentheses(s: str) -> List[str]:
        res = []
        left, right = 0, 0
        for c in s:
            if c == '(':
                left += 1
            elif c == ')':
                if left == 0:
                    right += 1
                else:
                    left -= 1

        def isValid(string):
            cnt = 0
            for letter in string:
                if letter == '(':
                    cnt += 1
                elif letter == ')':
                    cnt -= 1
                    if cnt < 0:
                        return False
            return cnt == 0

        def helper(string, start, l_remove, r_remove):
            if l_remove == 0 and r_remove == 0:
                if isValid(string):
                    res.append(string)
                return
            for i in range(start, len(string)):
                if i > start and string[i] == string[i - 1]:
                    continue
                # 如果剩余的字符无法满足去掉的数量要求，直接返回
                if l_remove + r_remove > len(string) - i:
                    break
                # 尝试去掉一个左括号
                if l_remove > 0 and string[i] == '(':
                    helper(string[:i] + string[i + 1:], i, l_remove - 1, r_remove)
                # 尝试去掉一个右括号
                if r_remove > 0 and string[i] == ')':
                    helper(string[:i] + string[i + 1:], i, l_remove, r_remove - 1)
                # 统计当前字符串中已有的括号数量

        helper(s, 0, left, right)
        return res
