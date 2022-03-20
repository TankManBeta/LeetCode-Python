# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2022/3/19 12:18
"""
"""
给你两个版本号 version1 和 version2 ，请你比较它们。
版本号由一个或多个修订号组成，各修订号由一个 '.' 连接。每个修订号由 多位数字 组成，可能包含 前导零 。
每个版本号至少包含一个字符。修订号从左到右编号，下标从 0 开始，最左边的修订号下标为 0 ，下一个修订号下标为 1 ，以此类推。
例如，2.5.33 和 0.1 都是有效的版本号。
比较版本号时，请按从左到右的顺序依次比较它们的修订号。比较修订号时，只需比较 忽略任何前导零后的整数值 。
也就是说，修订号 1 和修订号 001 相等 。如果版本号没有指定某个下标处的修订号，则该修订号视为 0 。
例如，版本 1.0 小于版本 1.1 ，因为它们下标为 0 的修订号相同，而下标为 1 的修订号分别为 0 和 1 ，0 < 1 。
返回规则如下：
    如果 version1 > version2 返回 1，
    如果 version1 < version2 返回 -1，
    除此之外返回 0。

输入：version1 = "1.01", version2 = "1.001"
输出：0
解释：忽略前导零，"01" 和 "001" 都表示相同的整数 "1"

输入：version1 = "1.0", version2 = "1.0.0"
输出：0
解释：version1 没有指定下标为 2 的修订号，即视为 "0"

输入：version1 = "0.1", version2 = "1.1"
输出：-1
解释：version1 中下标为 0 的修订号是 "0"，version2 中下标为 0 的修订号是 "1" 。0 < 1，所以 version1 < version2
"""
"""
思路：先通过'.'分割字符串，然后在短的那个后面补0，让两个数组一样长，然后依次比较每一个数的大小
"""


class Solution(object):
    @staticmethod
    def compareVersion(version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        # a = version1.split('.')
        # b = version2.split('.')
        # len_a, len_b = len(a), len(b)
        # if len_a > len_b:
        #     for i in range(0, len_a-len_b):
        #         b.append('0')
        # else:
        #     for i in range(0, len_b-len_a):
        #         a.append('0')
        # for i in range(len(a)):
        #     if int(a[i]) > int(b[i]):
        #         return 1
        #     if int(a[i]) < int(b[i]):
        #         return -1
        # return 0

        n, m = len(version1), len(version2)
        i, j = 0, 0
        while i < n or j < m:
            x = 0
            while i < n and version1[i] != '.':
                x = x * 10 + ord(version1[i]) - ord('0')
                i += 1
            i += 1
            y = 0
            while j < m and version2[j] != '.':
                y = y * 10 + ord(version2[j]) - ord('0')
                j += 1
            j += 1
            if x != y:
                return 1 if x > y else -1
        return 0
