# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2022/3/10 11:28
"""
"""
给定一个字符串s和一个字符串字典wordDict，在字符串s中增加空格来构建一个句子，使得句子中所有的单词都在词典中。
以任意顺序返回所有这些可能的句子。
注意：词典中的同一个单词可能在分段中被重复使用多次。

输入:s = "catsanddog", wordDict = ["cat","cats","and","sand","dog"]
输出:["cats and dog","cat sand dog"]

输入:s = "pineapplepenapple", wordDict = ["apple","pen","applepen","pine","pineapple"]
输出:["pine apple pen apple","pineapple pen apple","pine applepen apple"]
解释: 注意你可以重复使用字典中的单词。

输入:s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]
输出:[]
"""
"""
思路：dfs，先用139的判断是否有解
"""


class Solution(object):
    @staticmethod
    def word_break(s, word_dict):
        """
        :type s: str
        :type word_dict: List[str]
        :rtype: List[str]
        """
        n = len(s)
        dp = [False] * (n + 1)
        dp[0] = True
        for i in range(n):
            for j in range(i + 1, n + 1):
                if dp[i] and (s[i:j] in word_dict):
                    dp[j] = True

        set_dict = set(word_dict)
        combination = list()
        combinations = list()

        def dfs(index):
            if index == n:
                combinations.append(' '.join(combination))
                return
            for i in range(index, n):
                if s[index:i + 1] in set_dict:
                    combination.append(s[index:i + 1])
                    dfs(i + 1)
                    combination.pop()

        if dp[-1]:
            dfs(0)
        return combinations

        # res = []
        # memo = [1] * (len(s)+1)
        # wordDict = set(wordDict)

        # def dfs(wordDict,temp,pos):
        #     num = len(res)                  # 回溯前先记下答案中有多少个元素
        #     if pos == len(s):
        #         res.append(" ".join(temp))
        #         return
        #     for i in range(pos,len(s)+1):
        #         if memo[i] and s[pos:i] in wordDict: # 添加备忘录的判断条件
        #             temp.append(s[pos:i])
        #             dfs(wordDict,temp,i)
        #             temp.pop()
        #     # 答案中的元素没有增加，说明s[pos:]不能分割，修改备忘录
        #     memo[pos] = 1 if len(res) > num else 0

        # dfs(wordDict,[],0)
        # return res
