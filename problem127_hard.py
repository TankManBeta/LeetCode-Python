# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2022/3/3 11:01
"""
"""
字典 wordList 中从单词 beginWord 和 endWord 的 转换序列 是一个按下述规格形成的序列 beginWord -> s1 -> s2 -> ... -> sk：
    每一对相邻的单词只差一个字母。
    对于 1 <= i <= k 时，每个 si 都在 wordList 中。注意， beginWord 不需要在 wordList 中。
    sk == endWord
给你两个单词beginWord和endWord和一个字典wordList，返回从beginWord到endWord的最短转换序列中的单词数目。
如果不存在这样的转换序列，返回0。

输入：beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]
输出：5
解释：一个最短转换序列是 "hit" -> "hot" -> "dot" -> "dog" -> "cog", 返回它的长度 5。

输入：beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log"]
输出：0
解释：endWord "cog" 不在字典中，所以无法进行转换。
"""
"""
思路：
首先定义一个函数看两个单词能否转换，然后bfs，每次将能和当前转换的单词入队，如果恰好是endWord就返回当前bfs的层次+1，否则将
新入队的单词从后续wordList中删除。
"""


class Solution(object):
    @staticmethod
    def ladder_length(begin_word, end_word, word_list):
        """
        :type begin_word: str
        :type end_word: str
        :type word_list: List[str]
        :rtype: int
        """
        # 判断能否转换
        def is_exchangeable(word1, word2):
            count = 0
            word_len = len(word1)
            for index in range(word_len):
                if word1[index] != word2[index]:
                    count += 1
                    if count >= 2:
                        return False
            return count == 1

        if end_word not in word_list:
            return 0
        queue = list()
        queue.append(begin_word)
        # 防止begin_word已经在队列中
        if begin_word in word_list:
            word_list.remove(begin_word)
        steps = 1
        while queue:
            queue_len = len(queue)
            for i in range(queue_len):
                temp_word = queue.pop(0)
                # 用于在后续word_list中删除
                temp_list = []
                for word in word_list:
                    if is_exchangeable(temp_word, word):
                        if word == end_word:
                            return steps+1
                        temp_list.append(word)
                        queue.append(word)
                for word in temp_list:
                    word_list.remove(word)
            steps += 1
        return 0
