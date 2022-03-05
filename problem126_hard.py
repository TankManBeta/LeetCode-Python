# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2022/3/4 9:49
"""
from collections import defaultdict

"""
按字典wordList完成从单词beginWord到单词endWord转化，一个表示此过程的转换序列是形式上像beginWord->s1->s2->...->sk这样的单词序
列，并满足：
    每对相邻的单词之间仅有单个字母不同。
    转换过程中的每个单词 si（1 <= i <= k）必须是字典 wordList 中的单词。注意，beginWord 不必是字典 wordList 中的单词。
    sk == endWord
给你两个单词 beginWord 和 endWord ，以及一个字典 wordList 。请你找出并返回所有从 beginWord 到 endWord 的 最短转换序列，
如果不存在这样的转换序列，返回一个空列表。每个序列都应该以单词列表 [beginWord, s1, s2, ..., sk] 的形式返回。

输入：beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]
输出：[["hit","hot","dot","dog","cog"],["hit","hot","lot","log","cog"]]
解释：存在 2 种最短的转换序列：
"hit" -> "hot" -> "dot" -> "dog" -> "cog"
"hit" -> "hot" -> "lot" -> "log" -> "cog"

输入：beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log"]
输出：[]
解释：endWord "cog" 不在字典 wordList 中，所以不存在符合要求的转换序列。
"""
"""
思路：用bfs+dfs，bfs用来找每个level可能的单词，dfs用于输出路径，对于每一层的word，如果它的下一个单词可能是endWord，它的下个单
词的候选集就是[endWord]，此时不能返回，因为它同层的其他单词也可能下一个单词是endWord，就这样我们记录下来同层所有单词的所有候选
集，记为temp_lists，如果endWord在temp_lists中，那么说明在这次就结束了，更新记录层次的字典即可；否则就继续下一层，将下层可能节
点入队，同时在候选集中删除，同时更新记录层次的字典
"""


class Solution(object):
    def find_ladders(self, begin_word, end_word, word_list):
        """
        :type begin_word: str
        :type end_word: str
        :type word_list: List[str]
        :rtype: List[List[str]]
        """

        def is_changeable(word1, word2):
            count = 0
            word_len = len(word1)
            for index in range(word_len):
                if word1[index] != word2[index]:
                    count += 1
                    if count > 1:
                        return False
            return count == 1

        # 特殊情况
        if end_word not in word_list:
            return []
        # 记录前驱用于dfs
        level_dict = defaultdict(list)
        level = 0
        level_dict[0].append(begin_word)
        if begin_word in word_list:
            word_list.remove(begin_word)
        queue = [begin_word]
        while queue:
            level += 1
            temp_len = len(queue)
            # 记录每个level所有单词的下个单词的可能结果
            temp_lists = []
            # 对于同level的单词，如果下个单词是endWord，那么下个单词的集合只有endWord
            for i in range(temp_len):
                temp_list = []
                temp_word = queue.pop(0)
                for word in word_list:
                    if is_changeable(temp_word, word):
                        if word == end_word:
                            temp_list = [word]
                            break
                        else:
                            temp_list.append(word)
                # 加入大集合中，因为还有同level的其他单词下个单词也可能是endWord
                temp_lists.append(temp_list[:])
            # # 查看同level所有单词的下个单词的结果
            # if [endWord] in temp_lists:
            #     level_dict[level].append(endWord)
            #     break
            # else:
            #     all_words = []
            #     for temp1 in temp_lists:
            #         all_words += temp1
            #     all_words = set(all_words)
            #     all_words = list(all_words)
            #     for word in all_words:
            #         queue.append(word)
            #         wordList.remove(word)
            #         level_dict[level].append(word)
            all_words = []
            for temp1 in temp_lists:
                all_words += temp1
            all_words = set(all_words)
            all_words = list(all_words)
            if end_word in all_words:
                level_dict[level] = [end_word]
                break
            else:
                for word in all_words:
                    queue.append(word)
                    word_list.remove(word)
                    level_dict[level].append(word)
        # 最后结果到不了endWord，直接返回[]
        if level_dict[max(level_dict.keys())] != [end_word]:
            return []

        self.res_dict = level_dict
        combination = list()
        combinations = list()

        def dfs(start, end):
            if start == end:
                combinations.append(combination[:])
            for word in self.res_dict[start]:
                if not combination:
                    combination.append(word)
                    dfs(start + 1, end)
                    combination.pop()
                else:
                    if is_changeable(word, combination[-1]):
                        combination.append(word)
                        dfs(start + 1, end)
                        combination.pop()

        dfs(0, max(self.res_dict.keys()) + 1)
        return combinations
