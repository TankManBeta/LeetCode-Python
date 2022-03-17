# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2022/3/16 10:08
"""
"""
请你设计一个用于存储字符串计数的数据结构，并能够返回计数最小和最大的字符串。
实现 AllOne 类：
    AllOne() 初始化数据结构的对象。
    inc(String key) 字符串 key 的计数增加 1 。如果数据结构中尚不存在 key ，那么插入计数为 1 的 key 。
    dec(String key) 字符串 key 的计数减少 1 。如果 key 的计数在减少后为 0 ，那么需要将这个 key 从数据结构中删除。
    测试用例保证：在减少计数前，key 存在于数据结构中。
    get_max_key() 返回任意一个计数最大的字符串。如果没有元素存在，返回一个空字符串 "" 。
    get_min_key() 返回任意一个计数最小的字符串。如果没有元素存在，返回一个空字符串 "" 。

输入
["AllOne", "inc", "inc", "get_max_key", "get_min_key", "inc", "get_max_key", "get_min_key"]
[[], ["hello"], ["hello"], [], [], ["leet"], [], []]
输出
[null, null, null, "hello", "hello", null, "hello", "leet"]

解释
AllOne allOne = new AllOne();
allOne.inc("hello");
allOne.inc("hello");
allOne.get_max_key(); // 返回 "hello"
allOne.get_min_key(); // 返回 "hello"
allOne.inc("leet");
allOne.get_max_key(); // 返回 "hello"
allOne.get_min_key(); // 返回 "leet"
"""
"""
思路：同LRU那一题，双向链表+哈希表，哈希表的count值单调递增
"""


class Node:
    def __init__(self, key="", count=0):
        self.prev = None
        self.next = None
        self.keys = {key}
        self.count = count

    def insert(self, node):
        node.prev = self
        node.next = self.next
        node.prev.next = node
        node.next.prev = node
        return node

    def remove(self):
        self.prev.next = self.next
        self.next.prev = self.prev


class AllOne(object):

    def __init__(self):
        self.root = Node()
        self.root.prev = self.root
        self.root.next = self.root
        self.nodes = {}

    def inc(self, key):
        """
        :type key: str
        :rtype: None
        """
        if key not in self.nodes:
            if self.root.next is self.root or self.root.next.count > 1:
                self.nodes[key] = self.root.insert(Node(key, 1))
            else:
                self.root.next.keys.add(key)
                self.nodes[key] = self.root.next
        else:
            cur = self.nodes[key]
            nxt = cur.next
            if nxt is self.root or nxt.count > cur.count + 1:
                self.nodes[key] = cur.insert(Node(key, cur.count + 1))
            else:
                nxt.keys.add(key)
                self.nodes[key] = nxt
            cur.keys.remove(key)
            if len(cur.keys) == 0:
                cur.remove()

    def dec(self, key):
        """
        :type key: str
        :rtype: None
        """
        cur = self.nodes[key]
        if cur.count == 1:
            del self.nodes[key]
        else:
            pre = cur.prev
            if pre is self.root or pre.count < cur.count - 1:
                self.nodes[key] = cur.prev.insert(Node(key, cur.count - 1))
            else:
                pre.keys.add(key)
                self.nodes[key] = pre
        cur.keys.remove(key)
        if len(cur.keys) == 0:
            cur.remove()

    def get_max_key(self):
        """
        :rtype: str
        """
        return next(iter(self.root.prev.keys)) if self.root.prev is not self.root else ""

    def get_min_key(self):
        """
        :rtype: str
        """
        return next(iter(self.root.next.keys)) if self.root.next is not self.root else ""

# Your AllOne object will be instantiated and called as such:
# obj = AllOne()
# obj.inc(key)
# obj.dec(key)
# param_3 = obj.get_max_key()
# param_4 = obj.get_min_key()
