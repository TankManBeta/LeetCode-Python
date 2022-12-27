# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2022/12/26 13:33
"""
"""
给你一个字符串 s ，返回 s 中 同构子字符串 的数目。由于答案可能很大，只需返回对 109 + 7 取余 后的结果。
同构字符串 的定义为：如果一个字符串中的所有字符都相同，那么该字符串就是同构字符串。
子字符串 是字符串中的一个连续字符序列。

示例 1：
输入：s = "abbcccaa"
输出：13
解释：同构子字符串如下所列：
"a"   出现 3 次。
"aa"  出现 1 次。
"b"   出现 2 次。
"bb"  出现 1 次。
"c"   出现 3 次。
"cc"  出现 2 次。
"ccc" 出现 1 次。
3 + 1 + 2 + 1 + 3 + 2 + 1 = 13

示例 2：
输入：s = "xy"
输出：2
解释：同构子字符串是 "x" 和 "y" 。

示例 3：
输入：s = "zzzzz"
输出：15
"""
"""
思路：
（1）枚举所有的可能，超时。
（2）双指针，找第一个不相同的字符，[i:j-1]中的都是同构字符串，该区间内的同构子字符串个数为(1+cnt)×cnt/2，将其累加到答案中即可。
"""


class Solution:
    @staticmethod
    def countHomogenous(s: str) -> int:
        # counter = defaultdict(int)
        # n = len(s)
        # for i in range(n):
        #     j = i
        #     while j < n:
        #         if s[j] == s[i]:
        #             counter[s[i:j+1]] += 1
        #             j += 1
        #         else:
        #             break
        # res = [count for _, count in counter.items()]
        # return sum(res)

        mod = 10**9 + 7
        i, n = 0, len(s)
        ans = 0
        while i < n:
            j = i
            while j < n and s[j] == s[i]:
                j += 1
            cnt = j - i
            ans += (1 + cnt) * cnt // 2
            ans %= mod
            i = j
        return ans
