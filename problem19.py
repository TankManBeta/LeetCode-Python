# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2021/12/1 16:43
"""
"""
给你一个链表，删除链表的倒数第 n 个结点，并且返回链表的头结点。

输入：head = [1,2,3,4,5], n = 2
输出：[1,2,3,5]

输入：head = [1], n = 1
输出：[]

输入：head = [1,2], n = 1
输出：[1]
"""
"""
思路：
快慢指针，快指针先走n步，然后同时走，快指针到头，删除慢指针对应的节点即可。注意一些特殊情况。
"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    @staticmethod
    def remove_nth_from_end(head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        if head.next is None:
            return None
        fast_node = ListNode()
        fast_node.next = head
        slow_node = ListNode()
        slow_node.next = head
        aux_node = ListNode()
        aux_node.next = fast_node.next
        for i in range(0, n):
            fast_node.next = aux_node.next.next
            aux_node.next = fast_node.next
        aux_node_fast = ListNode()
        aux_node_fast.next = head
        aux_node_slow = ListNode()
        aux_node_slow.next = head
        while fast_node.next is not None:
            aux_node_fast.next = fast_node.next
            aux_node_slow.next = slow_node.next
            fast_node.next = aux_node_fast.next.next
            slow_node.next = aux_node_slow.next.next
        if slow_node.next == head:
            head = slow_node.next.next
        else:
            aux_node_slow.next.next = slow_node.next.next
        return head



