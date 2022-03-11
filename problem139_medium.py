# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2022/3/10 10:31
"""
"""
给你一个字符串 s 和一个字符串列表 wordDict 作为字典。请你判断是否可以利用字典中出现的单词拼接出 s 。
注意：不要求字典中出现的单词全部都使用，并且字典中的单词可以重复使用。

输入: s = "leetcode", wordDict = ["leet", "code"]
输出: true
解释: 返回 true 因为 "leetcode" 可以由 "leet" 和 "code" 拼接成。

输入: s = "applepenapple", wordDict = ["apple", "pen"]
输出: true
解释: 返回 true 因为 "applepenapple" 可以由 "apple" "pen" "apple" 拼接成。
     注意，你可以重复使用字典中的单词。

输入: s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
输出: false
"""
"""
思路：
（1）dp，dp[i]表示前i个能否被被表示，遍历i+1到n，如果dp[i]为True并且s[i:j]在wordDict里，说明可以
（2）回溯，初始化当前字符串是否可以被分割 res=False，res=backtrack(s[i,⋯,n−1]) or res
"""


class Solution(object):
    @staticmethod
    def word_break(s, word_dict):
        """
        :type s: str
        :type word_dict: List[str]
        :rtype: bool
        """
        n = len(s)
        dp = [False]*(n+1)
        dp[0] = True
        for i in range(n):
            for j in range(i+1,n+1):
                if dp[i] and (s[i:j] in word_dict):
                    dp[j] = True
        return dp[-1]

        # import functools
        # @functools.lru_cache(None)
        # def back_track(s):
        #     if(not s):
        #         return True
        #     res=False
        #     for i in range(1,len(s)+1):
        #         if(s[:i] in wordDict):
        #             res=back_track(s[i:]) or res
        #     return res
        # return back_track(s)
