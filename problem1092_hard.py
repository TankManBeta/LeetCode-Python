# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2023/3/29 11:20
"""
"""
给出两个字符串 str1 和 str2，返回同时以 str1 和 str2 作为子序列的最短字符串。如果答案不止一个，则可以返回满足条件的任意一个答案。
（如果从字符串 T 中删除一些字符（也可能不删除，并且选出的这些字符可以位于 T 中的 任意位置），可以得到字符串 S，那么 S 就是 T 的子序列）

示例：
输入：str1 = "abac", str2 = "cab"
输出："cabac"
解释：
str1 = "abac" 是 "cabac" 的一个子串，因为我们可以删去 "cabac" 的第一个 "c"得到 "abac"。 
str2 = "cab" 是 "cabac" 的一个子串，因为我们可以删去 "cabac" 末尾的 "ac" 得到 "cab"。
最终我们给出的答案是满足上述属性的最短字符串。
"""
"""
思路：我们先用动态规划求出两个字符串的最长公共子序列，然后根据最长公共子序列构造出最短公共超序列。我们用双指针 i 和 j 分别指向
字符串 str1 和 str2 的末尾，然后从后往前遍历，每次比较 str1[i] 和 str2[j] 的值：
如果 str1[i]=str2[j]，则将 str1[i] 或 str2[j] 中的任意一个字符加入到答案序列，然后 i 和 j 同时减 1；
如果 str1[i]!=str2[j]，则将 f[i][j] 与 f[i−1][j] 和 f[i][j−1] 中的最大值进行比较：
    如果 f[i][j]=f[i−1][j]，则将 str1[i] 加入到答案序列，然后 i 减 1；
    如果 f[i][j]=f[i][j−1]，则将 str2[j] 加入到答案序列，然后 j 减 1。
重复上述操作，直到 i=0 或 j=0，然后将剩余的字符串加入到答案序列即可。
最后我们将答案序列反转，即可得到最终的答案。
"""


class Solution:
    @staticmethod
    def shortestCommonSupersequence(str1: str, str2: str) -> str:
        m, n = len(str1), len(str2)
        f = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if str1[i - 1] == str2[j - 1]:
                    f[i][j] = f[i - 1][j - 1] + 1
                else:
                    f[i][j] = max(f[i - 1][j], f[i][j - 1])
        ans = []
        i, j = m, n
        while i or j:
            if i == 0:
                j -= 1
                ans.append(str2[j])
            elif j == 0:
                i -= 1
                ans.append(str1[i])
            else:
                if f[i][j] == f[i - 1][j]:
                    i -= 1
                    ans.append(str1[i])
                elif f[i][j] == f[i][j - 1]:
                    j -= 1
                    ans.append(str2[j])
                else:
                    i, j = i - 1, j - 1
                    ans.append(str1[i])
        return ''.join(ans[::-1])
