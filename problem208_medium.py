# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2022/3/30 10:37
"""
"""
Trie（发音类似 "try"）或者说 前缀树 是一种树形数据结构，用于高效地存储和检索字符串数据集中的键。
这一数据结构有相当多的应用情景，例如自动补完和拼写检查。
请你实现 Trie 类：
    Trie() 初始化前缀树对象。
    void insert(String word) 向前缀树中插入字符串 word 。
    boolean search(String word) 如果字符串 word 在前缀树中，返回 true（即，在检索之前已经插入）；否则，返回 false 。
    boolean startsWith(String prefix) 如果之前已经插入的字符串 word 的前缀之一为 prefix ，返回 true ；否则，返回 false 。

输入
["Trie", "insert", "search", "search", "startsWith", "insert", "search"]
[[], ["apple"], ["apple"], ["app"], ["app"], ["app"], ["app"]]
输出
[null, null, true, false, true, null, true]

解释
Trie trie = new Trie();
trie.insert("apple");
trie.search("apple");   // 返回 True
trie.search("app");     // 返回 False
trie.startsWith("app"); // 返回 True
trie.insert("app");
trie.search("app");     // 返回 True
"""
"""
思路：
（1）官解思路是对每一个字符建一个长度为26的数组，并且有一个isEnd标识是否一个单词已经结束，然后对每个字符判断，如果是None就新建
Trie节点，否则就指向那个字符的Trie节点
（2）针对本题来说，用一个set+dict记录更好，有需要开叉再开叉
"""


# class Trie(object):

#     def __init__(self):
#         self.children = [None]*26
#         self.isEnd = False

#     def searchPrefix(self, prefix):
#         node = self
#         for ch in prefix:
#             ch = ord(ch) - ord("a")
#             if not node.children[ch]:
#                 return None
#             node = node.children[ch]
#         return node

#     def insert(self, word):
#         """
#         :type word: str
#         :rtype: None
#         """
#         node = self
#         for char in word:
#             index = ord(char)-ord('a')
#             if not node.children[index]:
#                 node.children[index] = Trie()
#             node = node.children[index]
#         node.isEnd = True

#     def search(self, word):
#         """
#         :type word: str
#         :rtype: bool
#         """
#         node = self.searchPrefix(word)
#         return node is not None and node.isEnd

#     def startsWith(self, prefix):
#         """
#         :type prefix: str
#         :rtype: bool
#         """
#         return self.searchPrefix(prefix) is not None

class Trie(object):

    def __init__(self):
        self.words = set()
        self.treeDict = {}

    def insert(self, word):
        """
        :type word: str
        :rtype: None
        """
        self.words.add(word)
        curDict = self.treeDict
        for each in word:
            if each in curDict:
                curDict = curDict[each]
            else:
                curDict[each] = {}
                curDict = curDict[each]

    def search(self, word):
        """
        :type word: str
        :rtype: bool
        """
        if word in self.words:
            return True
        else:
            return False

    def startsWith(self, prefix):
        """
        :type prefix: str
        :rtype: bool
        """
        curDict = self.treeDict
        for each in prefix:
            if each in curDict:
                curDict = curDict[each]
            else:
                return False
        return True

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
