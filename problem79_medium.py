# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2022/2/7 13:49
"""
"""
给定一个 m x n 二维字符网格 board 和一个字符串单词 word 。如果 word 存在于网格中，返回 true ；否则，返回 false 。
单词必须按照字母顺序，通过相邻的单元格内的字母构成，其中“相邻”单元格是那些水平相邻或垂直相邻的单元格。
同一个单元格内的字母不允许被重复使用。

输入：board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
输出：true

输入：board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE"
输出：true

输入：board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB"
输出：false
"""
"""
思路：dfs，同时维护一个visited数组
"""


class Solution(object):
    @staticmethod
    def exist(board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        m = len(board)
        n = len(board[0])
        word_len = len(word)
        visited = [[0 for _ in range(n)] for _ in range(m)]

        def dfs(x, y, k):
            if word[k] != board[x][y]:
                return False
            if k == word_len - 1:
                return True
            visited[x][y] = 1
            for new_x, new_y in ((x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)):
                if 0 <= new_x <= m - 1 and 0 <= new_y <= n - 1:
                    if visited[new_x][new_y] == 0:
                        if dfs(new_x, new_y, k + 1):
                            return True
            visited[x][y] = 0

        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    if dfs(i, j, 0):
                        return True
        return False
