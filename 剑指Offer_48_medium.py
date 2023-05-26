# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2023/5/25 10:12
"""
"""
请从字符串中找出一个最长的不包含重复字符的子字符串，计算该最长子字符串的长度。

示例 1:
输入: "abcabcbb"
输出: 3 
解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。

示例 2:
输入: "bbbbb"
输出: 1
解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。

示例 3:
输入: "pwwkew"
输出: 3
解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
     请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。
"""
"""
思路：
（1）双指针，初始i，j分别为0，1，然后一直移动右指针，直到s[j]在s[i:j]中出现过，移动过程中注意维护最大值；然后移动左指针直到
第一个重复字符的位置，此时i再加1就是下轮i的起始位置。
（2）dp，设动态规划列表 dp ，dp[j] 代表以字符 s[j] 为结尾的 “最长不重复子字符串” 的长度。转移方程： 固定右边界 j ，设字符 s[j] 
左边距离最近的相同字符为 s[i] ，即 s[i]=s[j] 。当 i<0 ，即 s[j] 左边无相同字符，则 dp[j]=dp[j−1]+1 ；当 dp[j−1]<j−i ，说明字符 
s[i] 在子字符串 dp[j−1] 区间之外 ，则 dp[j]=dp[j−1]+1 ；当 dp[j−1]≥j−i ，说明字符 s[i] 在子字符串 dp[j−1] 区间之中 ，则 dp[j] 
的左边界由 s[i] 决定，即 dp[j]=j−i ；最后返回max(dp) ，即全局的 “最长不重复子字符串” 的长度。实现的时候我们可以用一个哈希表记录
每个字符上次出现的位置。
"""


class Solution:
    @staticmethod
    def lengthOfLongestSubstring(s: str) -> int:
        # n = len(s)
        # if n <= 1:
        #     return n
        # i, j = 0, 1
        # ans = 0
        # while j < n:
        #     while j < n and s[j] not in s[i:j]:
        #         ans = max(ans, j-i+1)
        #         j += 1
        #     while s[i] not in s[i:j+1]:
        #         i += 1
        #     i += 1
        # return ans

        dic = {}
        res = tmp = 0
        for j in range(len(s)):
            i = dic.get(s[j], -1)  # 获取索引 i
            dic[s[j]] = j  # 更新哈希表
            tmp = tmp + 1 if tmp < j - i else j - i  # dp[j - 1] -> dp[j]
            res = max(res, tmp)  # max(dp[j - 1], dp[j])
        return res
