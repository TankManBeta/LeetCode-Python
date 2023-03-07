# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2023/3/6 9:39
"""
"""
给你一个字符串 s ，它仅包含字符 'a' 和 'b'​。你可以删除 s 中任意数目的字符，使得 s 平衡 。当不存在下标对 (i,j) 满足 i < j ，
且 s[i] = 'b' 的同时 s[j]= 'a' ，此时认为 s 是平衡的。
请你返回使 s 平衡 的 最少 删除次数。

示例 1：
输入：s = "aababbab"
输出：2
解释：你可以选择以下任意一种方案：
下标从 0 开始，删除第 2 和第 6 个字符（"aababbab" -> "aaabbb"），
下标从 0 开始，删除第 3 和第 6 个字符（"aababbab" -> "aabbbb"）。

示例 2：
输入：s = "bbaaaaabb"
输出：2
解释：唯一的最优解是删除最前面两个字符。
"""
"""
思路：
（1）动态规划1。要想删除的字符最少，那么就是剩下的最多。假设当前字符是'a'，那么它只能跟在上一个'a'后面；如果当前字符是'b'，那么
它可以跟在上一个'a'和上一个'b'中较长的那一个后面。
（2）动态规划2.我们定义 f[i] 表示前 i 个字符中，删除最少的字符数，使得字符串平衡。初始时 f[0]=0。答案为 f[n]。我们遍历字符串 
s，维护变量 b，表示当前遍历到的位置之前的字符中，字符 b 的个数。
    如果当前字符为 'b'，此时不影响前 i 个字符的平衡性，因此 f[i]=f[i−1]，然后我们更新 b←b+1。
    如果当前字符为 'a'，此时我们可以选择删除当前字符，那么有 f[i]=f[i−1]+1；也可以选择删除之前的字符 b，那么有 f[i]=b。因此
    我们取两者的最小值，即 f[i]=min(f[i−1]+1,b)。
（3）模拟。对于当前位置i来说，我们需要删除的是它前面所有的b和后面所有的a，所以统计即可。
"""


class Solution:
    @staticmethod
    def minimumDeletions(s: str) -> int:
        # a, b, n = 0, 0, len(s)
        # for i in range(n):
        #     if s[i] == 'a':
        #         a += 1
        #     else:
        #         b = max(a, b) + 1
        # return n - max(a, b)

        # ans = b = 0
        # for c in s:
        #     if c == 'b':
        #         b += 1
        #     else:
        #         ans = min(ans + 1, b)
        # return ans

        lb, ra = 0, s.count('a')
        res = ra
        for c in s:
            if c == 'a':
                ra -= 1
            else:
                lb += 1
            res = min(res, lb + ra)
        return res
