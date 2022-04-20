# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2022/4/19 12:41
"""
"""
给你一个字符串 s 和一个字符 c ，且 c 是 s 中出现过的字符。
返回一个整数数组 answer ，其中 answer.length == s.length 且 answer[i] 是 s 中从下标 i 到离它 最近 的字符 c 的 距离 。
两个下标 i 和 j 之间的 距离 为 abs(i - j) ，其中 abs 是绝对值函数。

输入：s = "loveleetcode", c = "e"
输出：[3,2,1,0,1,0,0,1,2,2,1,0]
解释：字符 'e' 出现在下标 3、5、6 和 11 处（下标从 0 开始计数）。
距下标 0 最近的 'e' 出现在下标 3 ，所以距离为 abs(0 - 3) = 3 。
距下标 1 最近的 'e' 出现在下标 3 ，所以距离为 abs(1 - 3) = 2 。
对于下标 4 ，出现在下标 3 和下标 5 处的 'e' 都离它最近，但距离是一样的 abs(4 - 3) == abs(4 - 5) = 1 。
距下标 8 最近的 'e' 出现在下标 6 ，所以距离为 abs(8 - 6) = 2 。

输入：s = "aaab", c = "b"
输出：[3,2,1,0]
"""
"""
思路：两边遍历，第一遍遍历获取当前位置左边第一个给定字符的位置，第二遍遍历获取当前位置右边第一个给定字符的位置
"""


class Solution(object):
    @staticmethod
    def shortestToChar(s, c):
        """
        :type s: str
        :type c: str
        :rtype: List[int]
        """
        n = len(s)
        ans = [0] * n

        index1 = -n
        for i in range(n):
            if s[i] == c:
                index1 = i
            else:
                ans[i] = i - index1

        index2 = 2 * n
        for i in range(n - 1, -1, -1):
            if s[i] == c:
                index2 = i
            else:
                ans[i] = min(ans[i], index2 - i)

        return ans
