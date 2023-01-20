# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2023/1/19 19:35
"""
"""
如果一个密码满足以下所有条件，我们称它是一个 强 密码：
    它有至少 8 个字符。
    至少包含 一个小写英文 字母。
    至少包含 一个大写英文 字母。
    至少包含 一个数字 。
    至少包含 一个特殊字符 。特殊字符为："!@#$%^&*()-+" 中的一个。
    它 不 包含 2 个连续相同的字符（比方说 "aab" 不符合该条件，但是 "aba" 符合该条件）。
给你一个字符串 password ，如果它是一个 强 密码，返回 true，否则返回 false 。

示例 1：
输入：password = "IloveLe3tcode!"
输出：true
解释：密码满足所有的要求，所以我们返回 true 。

示例 2：
输入：password = "Me+You--IsMyDream"
输出：false
解释：密码不包含数字，且包含 2 个连续相同的字符。所以我们返回 false 。

示例 3：
输入：password = "1aB!"
输出：false
解释：密码不符合长度要求。所以我们返回 false 。
"""
"""
思路：模拟，用一个数组，初始化为0、0、0、0、1，遇到大写、小写、数字、特殊字符就对应ans++，遇到连续的就对应ans--，然后看是否所有
的数都大于等于1即可
"""


class Solution:
    @staticmethod
    def strongPasswordCheckerII(password: str) -> bool:
        n = len(password)
        if n < 8:
            return False
        ans = [0, 0, 0, 0, 1]
        for i, letter in enumerate(password):
            if '0' <= letter <= '9':
                ans[0] += 1
            if 'a' <= letter <= 'z':
                ans[1] += 1
            if 'A' <= letter <= 'Z':
                ans[2] += 1
            if letter in "!@#$%^&*()-+":
                ans[3] += 1
            if i + 1 < n and letter == password[i + 1]:
                ans[4] -= 1
        return all([i >= 1 for i in ans])
