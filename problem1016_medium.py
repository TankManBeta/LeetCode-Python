# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2023/5/11 10:10
"""
"""
给定一个二进制字符串 s 和一个正整数 n，如果对于 [1, n] 范围内的每个整数，其二进制表示都是 s 的 子字符串 ，就返回 true，否则返回 false 。
子字符串 是字符串中连续的字符序列。

示例 1：
输入：s = "0110", n = 3
输出：true

示例 2：
输入：s = "0110", n = 4
输出：false
"""
"""
思路：直接暴力把每个数变成二进制，然后看字符是否在s中。那么为什么不会超时呢？
举例说明。如果 n=7，单看闭区间 [4,7]，有 4 个互不相同的整数，它们的二进制长度均为 3。如果要让字符串 s 包含这 4 个数，s 中至少
要有 4 个长为 3 的互不相同的子串。考虑到这些子串可以有重叠部分，设 s 的长度为 m，则应满足 m≥3+(4−1)=6，否则直接返回 false。
（想象一个长为 3 的滑动窗口在 s 中滑动，至少要得到 4 个子串。）随着 n 的变大，m 的长度也应当随之变大。本题 m 至多为 1000，而 
n 却高达 10^9。可以预见，当 n 较大时，可以直接返回 false。如何精确地判断呢？
考虑到 n+1 不一定是 2 的幂，分两组讨论。
设 n 的二进制长度为 k+1，那么：
    区间 [2^k,n] 内的二进制数的长度均为 k+1，这有 n−2^k+1 个，所以应满足 m≥k+1+(n−2^k+1−1)=n−2^k+k+1。
    区间 [2^(k−1),2^k−1] 内的二进制数的长度均为 k，这有 2^k−1个，所以应满足 m≥k+(2^(k−1)−1)=2^(k−1)+k−1。
    注意，当 n=1 时，k=0，此时区间 [2^(k−1),2^k−1] 不存在。直接特判这种情况，返回 s 是否包含 1。
由于 m≤1000，根据上式，如果 n≥2014，可以直接返回 false。但不推荐这样写，根据 n 和 m 的值来判断更准确。
"""


class Solution:
    @staticmethod
    def queryString(s: str, n: int) -> bool:
        for i in range(1, n + 1):
            if bin(i)[2:] not in s:
                return False
        return True
