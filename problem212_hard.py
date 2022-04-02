# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2022/4/1 11:40
"""
from collections import defaultdict

"""
给定一个 m x n 二维字符网格 board 和一个单词（字符串）列表 words， 返回所有二维网格上的单词 。
单词必须按照字母顺序，通过 相邻的单元格 内的字母构成，其中“相邻”单元格是那些水平相邻或垂直相邻的单元格。
同一个单元格内的字母在一个单词中不允许被重复使用。

输入：board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]], words = ["oath","pea","eat","rain"]
输出：["eat","oath"]

输入：board = [["a","b"],["c","d"]], words = ["abcb"]
输出：[]
"""
"""
思路：
（1）直接dfs，超时，考虑优化，统计字符出现次数，不合法的扔掉，仍然超时
（2）字典树+dfs
"""


# class Trie:
#     def __init__(self):
#         self.child = [None for _ in range(26)]
#         self.is_word = False

#     def insert(self, word):
#         rt = self
#         for c in word:
#             ID = ord(c) - ord('a')
#             if rt.child[ID] == None:
#                 rt.child[ID] = Trie()
#             rt = rt.child[ID]
#         rt.is_word = True

class Trie:
    def __init__(self):
        self.children = defaultdict(Trie)
        self.word = ""

    def insert(self, word):
        cur = self
        for c in word:
            cur = cur.children[c]
        cur.is_word = True
        cur.word = word


class Solution(object):
    @staticmethod
    def findWords(board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        # 直接dfs超时
        # m = len(board)
        # n = len(board[0])
        # visited = [[False for _ in range(n)] for _ in range(m)]
        # cnts = Counter()
        # for i in range(m):
        #     for j in range(n):
        #         cnts[board[i][j]] += 1

        # options = []
        # for word in words:
        #     cur = Counter(word)
        #     can_exisits = True
        #     for c in cur:
        #         if cnts[c] < cur[c]:
        #             can_exisits = False
        #             break
        #     if can_exisits:
        #         options.append(word)

        # combination = list()
        # combinations = list()

        # def dfs(row, col):
        #     if len(combination)>10:
        #         return
        #     temp_string = ''.join(combination)
        #     if temp_string in options:
        #         combinations.append(temp_string)
        #         options.remove(temp_string)
        #     for idx, idy in [(0,1), (0,-1), (1,0), (-1,0)]:
        #         new_row, new_col = row+idx, col+idy
        #         if new_row<0 or new_row>=m or new_col<0 or new_col>=n:
        #             continue
        #         if visited[new_row][new_col]:
        #             continue
        #         visited[new_row][new_col] = True
        #         combination.append(board[new_row][new_col])
        #         dfs(new_row, new_col)
        #         visited[new_row][new_col] = False
        #         combination.pop()

        # for i in range(m):
        #     for j in range(n):
        #         visited[i][j] = True
        #         combination.append(board[i][j])
        #         dfs(i, j)
        #         visited[i][j]=False
        #         combination.pop()

        # return combinations

        # 字典树超时
        # def backtrace(trie, r, c):
        #     ID = ord(board[r][c]) - ord('a')
        #     if trie.child[ID] == None:
        #         return
        #     path.append(board[r][c])
        #     visited[r][c] = True
        #     child_trie = trie.child[ID]
        #     if child_trie.is_word == True:
        #         res_set.add(''.join(path))
        #     for nr, nc in [(r-1, c), (r+1,c), (r,c-1), (r,c+1)]:
        #         if 0 <= nr < Row and 0 <= nc < Col and visited[nr][nc] == False:
        #             backtrace(child_trie, nr, nc)
        #     path.pop()
        #     visited[r][c] = False

        # Row = len(board)
        # Col = len(board[0])
        # T = Trie()
        # for word in words:
        #     T.insert(word)
        # res_set = set()
        # path = list()
        # visited = [[False for _ in range(Col)] for _ in range(Row)]
        # for r in range(Row):
        #     for c in range(Col):
        #         backtrace(T, r, c)
        # return list(res_set)

        trie = Trie()
        for word in words:
            trie.insert(word)

        def dfs(now, i1, j1):
            if board[i1][j1] not in now.children:
                return
            ch = board[i1][j1]
            now = now.children[ch]
            if now.word != "":
                ans.add(now.word)
            board[i1][j1] = "#"
            for i2, j2 in [(i1 + 1, j1), (i1 - 1, j1), (i1, j1 + 1), (i1, j1 - 1)]:
                if 0 <= i2 < m and 0 <= j2 < n:
                    dfs(now, i2, j2)
            board[i1][j1] = ch

        ans = set()
        m, n = len(board), len(board[0])
        for i in range(m):
            for j in range(n):
                dfs(trie, i, j)
        return list(ans)
