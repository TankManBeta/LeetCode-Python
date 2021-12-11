# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2021/12/2 19:59
"""
"""
给你单链表的头节点 head ，请你反转链表，并返回反转后的链表。

输入：head = [1,2,3,4,5]
输出：[5,4,3,2,1]

输入：head = [1,2]
输出：[2,1]

输入：head = []
输出：[]
"""
"""
思路：头插法
"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    @staticmethod
    def reverse_list(head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None:
            return None
        if head.next is None:
            return head
        new_head1 = ListNode(-1)
        while head:
            temp = head.next
            head.next = new_head1.next
            new_head1.next = head
            head = temp
        return new_head1.next
