# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2023/1/29 15:40
"""
"""
给你一个字符串 s ，每 两个 连续竖线 '|' 为 一对 。换言之，第一个和第二个 '|' 为一对，第三个和第四个 '|' 为一对，以此类推。
请你返回 不在 竖线对之间，s 中 '*' 的数目。
注意，每个竖线 '|' 都会 恰好 属于一个对。

示例 1：
输入：s = "l|*e*et|c**o|*de|"
输出：2
解释：不在竖线对之间的字符加粗加斜体后，得到字符串："l|*e*et|c**o|*de|" 。
第一和第二条竖线 '|' 之间的字符不计入答案。
同时，第三条和第四条竖线 '|' 之间的字符也不计入答案。
不在竖线对之间总共有 2 个星号，所以我们返回 2 。

示例 2：
输入：s = "iamprogrammer"
输出：0
解释：在这个例子中，s 中没有星号。所以返回 0 。

示例 3：
输入：s = "yo|uar|e**|b|e***au|tifu|l"
输出：5
解释：需要考虑的字符加粗加斜体后："yo|uar|e**|b|e***au|tifu|l" 。不在竖线对之间总共有 5 个星号。所以我们返回 5 。
"""
"""
思路：
（1）统计所有的'*'，然后统计两个'|'之间的'*'，然后两个结果相减
（2）定义一个整型变量 ok，表示遇到 * 时是否能计数，初始时 ok=1，表示可以计数。遍历字符串 s，如果遇到 *，则根据 ok 的值决定是否
计数，如果遇到 |，则 ok 的值取反。最后返回计数的结果。
"""


class Solution:
    @staticmethod
    def countAsterisks(s: str) -> int:
        # n = len(s)
        # left, right = 0, 0
        # ans_all = 0
        # for letter in s:
        #     if letter == '*':
        #         ans_all += 1
        # ans_sub = 0
        # while left<n and right<n:
        #     while left<n and s[left] != '|':
        #         left += 1
        #     right = left+1
        #     while right<n and s[right] != '|':
        #         if s[right] == '*':
        #            ans_sub += 1
        #         right += 1
        #     left = right + 1
        # return ans_all - ans_sub

        ans, ok = 0, 1
        for c in s:
            if c == "*":
                ans += ok
            elif c == "|":
                ok ^= 1
        return ans
