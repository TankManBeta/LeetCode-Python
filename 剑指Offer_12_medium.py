# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2023/5/29 10:05
"""
from typing import List

"""
给定一个 m x n 二维字符网格 board 和一个字符串单词 word 。如果 word 存在于网格中，返回 true ；否则，返回 false 。
单词必须按照字母顺序，通过相邻的单元格内的字母构成，其中“相邻”单元格是那些水平相邻或垂直相邻的单元格。同一个单元格内的字母不允许被重复使用。
例如，在下面的 3×4 的矩阵中包含单词 "ABCCED"（单词中的字母已标出）。

示例 1：
输入：board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
输出：true

示例 2：
输入：board = [["a","b"],["c","d"]], word = "abcd"
输出：false
"""
"""
思路：回溯
（1）使用标记来标记是否已经访问过。
（2）不使用标记，直接在原数组上进行修改，注意返回时要修改上一步的状态。
"""


class Solution:
    @staticmethod
    def exist(board: List[List[str]], word: str) -> bool:
        # directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        # def check(i: int, j: int, k: int) -> bool:
        #     if board[i][j] != word[k]:
        #         return False
        #     if k == len(word) - 1:
        #         return True

        #     visited.add((i, j))
        #     result = False
        #     for di, dj in directions:
        #         newi, newj = i + di, j + dj
        #         if 0 <= newi < len(board) and 0 <= newj < len(board[0]):
        #             if (newi, newj) not in visited:
        #                 if check(newi, newj, k + 1):
        #                     result = True
        #                     break

        #     visited.remove((i, j))
        #     return result

        # h, w = len(board), len(board[0])
        # visited = set()
        # for i in range(h):
        #     for j in range(w):
        #         if check(i, j, 0):
        #             return True

        # return False

        def dfs(i, j, k):
            if not 0 <= i < len(board) or not 0 <= j < len(board[0]) or board[i][j] != word[k]:
                return False
            if k == len(word) - 1:
                return True
            board[i][j] = ''
            res = dfs(i + 1, j, k + 1) or dfs(i - 1, j, k + 1) or dfs(i, j + 1, k + 1) or dfs(i, j - 1, k + 1)
            board[i][j] = word[k]
            return res

        for i in range(len(board)):
            for j in range(len(board[0])):
                if dfs(i, j, 0):
                    return True
        return False
