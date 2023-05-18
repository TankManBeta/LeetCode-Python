# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2023/5/17 11:18
"""
"""
请实现 copyRandomList 函数，复制一个复杂链表。在复杂链表中，每个节点除了有一个 next 指针指向下一个节点，还有一个 random 指针
指向链表中的任意节点或者 null。

示例 1：
输入：head = [[7,null],[13,0],[11,4],[10,2],[1,0]]
输出：[[7,null],[13,0],[11,4],[10,2],[1,0]]

示例 2：
输入：head = [[1,1],[2,1]]
输出：[[1,1],[2,1]]

示例 3：
输入：head = [[3,null],[3,0],[3,null]]
输出：[[3,null],[3,0],[3,null]]

示例 4：
输入：head = []
输出：[]
解释：给定的链表为空（空指针），因此返回 null。
"""
"""
思路：
（1）本题的主要难点在于如何将random域指向对应的节点，因为在顺序遍历链表的时候，每次新建一个node的时候，该node的random域指向的
节点可能还没有被新建。于是想到可以用一个哈希表记录，然后等所有节点都建好之后再遍历原链表一次给random域赋值。
（2）先在遍历每个节点的时候在它后面新建一个node，然后再进行拆分。
"""


# Definition for a Node.
class Node:
    def __init__(self, x: int, next: "Node" = None, random: "Node" = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    @staticmethod
    def copyRandomList(head: "Node") -> "Node":
        # if not head:
        #     return
        # mapping = {}
        # cur = head
        # while cur:
        #     tmp = Node(cur.val)
        #     mapping[cur] = tmp
        #     cur = cur.next
        # cur = head
        # while cur:
        #     mapping[cur].next = mapping.get(cur.next)
        #     mapping[cur].random = mapping.get(cur.random)
        #     cur = cur.next
        # return mapping[head]

        if not head:
            return
        cur = head
        while cur:
            tmp = Node(cur.val)
            tmp.next = cur.next
            cur.next = tmp
            cur = tmp.next
        cur = head
        while cur:
            if cur.random:
                cur.next.random = cur.random.next
            cur = cur.next.next
        cur = res = head.next
        pre = head
        while cur.next:
            pre.next = pre.next.next
            cur.next = cur.next.next
            pre = pre.next
            cur = cur.next
        pre.next = None
        return res
